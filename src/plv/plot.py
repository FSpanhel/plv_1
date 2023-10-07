import pandas as pd
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import statsmodels.api as sm
import ipywidgets
from ipywidgets import interact

from plv.model import AR1, CrisisDummy
from plv.data import corona_begin


def plot_ts(
    data: pd.Series,
    title: None | str = None,
    size: None | tuple[int, int] = (8, 4)
) -> None:
    "Plot a time series."
    if size:
        plt.figure(figsize=size)
    plt.plot(data.index, data)
    if title:
        plt.title(title)


def plot_seasonality(data: pd.Series, freq="MS") -> Figure:
    "Seasonality plot of data"
    # this is necessary because otherwise sm.graphics.tsa.month_plot(y) throws an error
    # Turn the dtype Float64 of y into float64 
    index = pd.DatetimeIndex(data.index, freq=freq)
    y = pd.Series(index=index, data=data.to_numpy().astype(float))
    fig = sm.graphics.tsa.month_plot(y)
    return fig


class InteractiveForecastPlot:
    def get_data(self, forecast_origin, dummy=False) -> dict:
        data = {}
        data["in_sample"] = self.y.loc[:forecast_origin].copy()  # this is ts
        # Fitting is very fast
        if not dummy:
            self.ar.fit(data["in_sample"])
        else:
            self.ar.fit(data["in_sample"], self.dummy)

        data["forecast"] = self.ar.oos_forecast(self.forecast_horizon)
        
        num = 2
        vertical = np.linspace(*self.ylim, num=num)
        data["forecast_origin"] = pd.Series(
            vertical, index=[data["in_sample"].index[-1]] * num
        )
        
        data["corona_start"] = pd.Series(
            vertical, index=[pd.Timestamp(corona_begin)] * num
        )
        
        data["in_sample_forecast"] = data["forecast"].loc[:data["in_sample"].index[-1]]
        data["oos_forecast"] = data["forecast"].loc[
        # Use data["in_sample"].index[-2] for a nicer plot
            data["in_sample"].index[-2] + pd.DateOffset(months=1):
        ]

        data["mean"] = self.ar.get_mean(
            data["forecast"].index[0].strftime("%Y-%m-%d"),
            data["forecast"].index[-1].strftime("%Y-%m-%d")
        )
        return data
    
    def setup_ax(self, figsize, ylim):
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_ylim(*ylim)
        ax.set_xlim(self.y.index[0], pd.Timestamp("2049-12-01"))
        # Add labels and a legend
        ax.set_xlabel('Jahre')
        ax.set_ylabel('Inflationsrate')
        ax.set_title('Vergleich von in-sample und out-of-sample Vorhersagen')
    
        return fig, ax
    
    def plot_initial_lines(self, ax, data) -> dict:
        line = {}

        # Plot
        line["in_sample"], = ax.plot(data["in_sample"].index, data["in_sample"],
                                     label="Daten", 
                                     marker="x", markersize=2,
                                     )
        # , linestyle="", marker="x")

        line["forecast_origin"],  = ax.plot(
            data["forecast_origin"].index, data["forecast_origin"],
            color="black", linestyle='-',
            label='In-sample Ende'
        )
        

        line["in_sample_forecast"], = ax.plot(
            data["in_sample_forecast"].index, data["in_sample_forecast"],
            color=(0, 1, 0), linestyle='-',
            label='In-sample Einschritt-Prognose'
        )

        line["oos_forecast"], = ax.plot(
            data["oos_forecast"].index, data["oos_forecast"], color='red',
            linestyle='--',
            label='Out-of-sample Mehrschritt-Prognose'
        )
        
        line["corona_start"],  = ax.plot(
            data["corona_start"].index, data["corona_start"],
            color="yellow", linestyle='--',
            label='Corona Start'
        )

        line["mean"], = ax.plot([], [], color='gray', linestyle='--',
                                label="Erwartungswert des AR(1) Modells")
        
        return line

    def __init__(
            self,
            ar: AR1,
            y: pd.Series,
            dummy: CrisisDummy,
            forecast_horizon: int,
            initial_forecast_origin = "2005",
            figsize = (12,6),
            ylim = (-3, 11)
            ):

        self.ar = ar
        self.y = y
        self.dummy = dummy
        self.forecast_horizon = forecast_horizon
        self.figsize = figsize
        self.ylim = ylim
        self.initial_forecast_origin = initial_forecast_origin
        
    def plot(self):

        # Compute data
        data = self.get_data(self.initial_forecast_origin, dummy=False)

        # set up figure
        fig, ax = self.setup_ax(figsize=self.figsize, ylim=self.ylim)
        
        # fig.canvas.footer_visible = False  # x/y not shown

        line = self.plot_initial_lines(ax, data)
        
        ax.legend(loc='upper left') # , bbox_to_anchor=(1, 0.5))

        # Ensure there is enough space on the right for the legend
        # plt.tight_layout()

        ax.grid(True, linewidth=0.5) 

        widget = {}
        # initial_year and initial_month
        try:
            initial_year, initial_month = self.initial_forecast_origin.split("-")
        except ValueError:
            initial_year, initial_month = self.initial_forecast_origin, "01"
        initial_year, initial_month = int(initial_year), int(initial_month)

        widget["year"] = ipywidgets.IntSlider(min=initial_year, max=2024, step=1)
        widget["month"] =  ipywidgets.IntSlider(min=initial_month, max=12*4, step=1)
        widget["dummy"] = ipywidgets.Dropdown(
            options={'AR(1)': False, 'AR(1) mit Krisen Dummy': True},
            value=False,
            description='Modell:',
        )

        widget["mean"] = ipywidgets.Dropdown(
            options={'Ja': True, 'Nein': False},
            value=False,
            description='Erwartungswert des AR(1) Modells',
        )

        @interact(
                Jahr=widget["year"], Monat=widget["month"], dummy=widget["dummy"],
                plot_mean=widget["mean"]
            )
        def update(Jahr: int, Monat: int, dummy: bool, plot_mean: bool):
            forecast_origin = (
                pd.Timestamp(f"{Jahr}-01-01")
                + pd.DateOffset(months=Monat-1)
            )
            data = self.get_data(forecast_origin, dummy)
            for key in line.keys():
                if key == "mean":
                    if not plot_mean:
                        continue
                line[key].set_data(data[key].index, data[key])
                # if (key == "in_sample_forecast") 
                # and (forecast_origin == pd.Timestamp("2020-01-01")):
                #    print(data[key].tail())
  
            # Request a widget redraw.
            fig.canvas.draw_idle()



# make a class? so that it plots faster?
def plot_is_oos_forecast(
        ar: AR1, forecast_horizon: int, oos_data: None | pd.Series = None,
        plot_mean: bool = False,
    ) -> Figure:
    ts = ar.ts.copy()
    forecast = ar.oos_forecast(forecast_horizon)
    forecast_is = forecast.loc[:ar.ts.index[-1]]
    forecast_oos = forecast.loc[ar.ts.index[-1] + pd.DateOffset(months=1):]

    if oos_data is not None:
        full = pd.concat([ts, oos_data])
    else:
        full = ts

    # Create the plot
    plt.figure(figsize=(12, 6))  # Optional: Set the figure size

    # Limit the y-axis between -1 and 1
    plt.ylim(-1, 9.5)

    plt.plot(full.index, full, color='blue', linestyle='-', label='Data')

    plt.axvline(x=ts.index[-1], color='yellow', linestyle='-', label='In-sample Ende')

    plt.plot(
        forecast_is.index, forecast_is, color='green', linestyle='-',
        label='In-sample one-step ahead forecast'
    )

    forecast_oos_ = pd.concat([forecast_is.tail(1), forecast_oos])

    plt.plot(
        forecast_oos_.index, forecast_oos_, color='red', linestyle='--',
        label='Out-of-sample multi-step ahead forecast'
    )

    if plot_mean:
        mean = ar.get_mean(
            forecast.index[0].strftime("%Y-%m-%d"),
            forecast.index[-1].strftime("%Y-%m-%d")
        )
        plt.plot(
            forecast.index, mean, color="gray", linestyle="--",
            label="Erwartungswert des AR(1) Modells"
        )

    # Add labels and a legend
    plt.xlabel('Jahre')
    plt.ylabel('Inflationsrate')
    plt.title('Vergleich von in-sample und out-of-sample Vorhersagen')

    plt.legend()

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Ensure there is enough space on the right for the legend
    # plt.tight_layout()

    # plt.grid(linewidth=0.2)

    # Show the plot
    plt.grid(True, linewidth=0.5) 

    return plt