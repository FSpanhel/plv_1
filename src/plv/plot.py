import pandas as pd
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import statsmodels.api as sm
import ipywidgets
from ipywidgets import interact
import matplotlib.gridspec as gridspec
from statsmodels.tsa.arima_process import arma_generate_sample
from scipy.stats import norm
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import MultipleLocator

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


def plot_inflation(inflation: pd.Series, figsize=(16, 4)):
    plot_ts(
        data=inflation,
        title=(
            "Inflationsrate: Prozentuale Veränderung des Verbraucherpreisindex"
            " zum Vorjahresmonat. Quelle: https://www.destatis.de/"
        ),
        size=figsize
    )
    plt.axvline(
        x=pd.Timestamp(corona_begin), color='y', linestyle='--', label='Corona Beginn'
    )
    plt.legend()
    # https://www-genesis.destatis.de/genesis/online?sequenz=tabelleErgebnis&selectionname=61111-0002&startjahr=1996#abreadcrumb

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
            dummy: None | CrisisDummy = None,
            forecast_horizon: int = 750,
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

        widget["mean"] = ipywidgets.Dropdown(
            options={'Ja': True, 'Nein': False},
            value=False,
            description='Erwartungswert des AR(1) Modells',
        )

        if self.dummy is not None:
            widget["dummy"] = ipywidgets.Dropdown(
                options={'AR(1)': False, 'AR(1) mit Krisen Dummy': True},
                value=False,
                description='Modell:',
            )
            @interact(
                Jahr=widget["year"], Monat=widget["month"], dummy=widget["dummy"],
                plot_mean=widget["mean"]
            )
            def update(Jahr: int, Monat: int, dummy: bool, plot_mean: bool):
                self.update_plot(line, fig, Jahr, Monat, dummy, plot_mean)
            
        else:
            @interact(
                Jahr=widget["year"], Monat=widget["month"], plot_mean=widget["mean"]
            )
            def update(Jahr: int, Monat: int, plot_mean: bool):
                dummy = False
                self.update_plot(line, fig, Jahr, Monat, dummy, plot_mean)

    def update_plot(
            self, line, fig, Jahr: int, Monat: int, dummy: bool, plot_mean: bool
        ):
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


class InteractiveForecastPlotNew:
    def get_data(self, forecast_origin, dummy=False) -> dict:
        data = {}
        data["in_sample"] = self.y.loc[:forecast_origin].copy()  # this is ts
        data["out_of_sample"] = self.y.loc[:forecast_origin].copy() 
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
        
        if False:
            data["in_sample_forecast"] = data["forecast"].loc[
                :data["in_sample"].index[-1]
            ]
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
            dummy: None | CrisisDummy = None,
            forecast_horizon: int = 750,
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

        widget["mean"] = ipywidgets.Dropdown(
            options={'Ja': True, 'Nein': False},
            value=False,
            description='Erwartungswert des AR(1) Modells',
        )

        if self.dummy is not None:
            widget["dummy"] = ipywidgets.Dropdown(
                options={'AR(1)': False, 'AR(1) mit Krisen Dummy': True},
                value=False,
                description='Modell:',
            )
            @interact(
                Jahr=widget["year"], Monat=widget["month"], dummy=widget["dummy"],
                plot_mean=widget["mean"]
            )
            def update(Jahr: int, Monat: int, dummy: bool, plot_mean: bool):
                self.update_plot(line, fig, Jahr, Monat, dummy, plot_mean)
            
        else:
            @interact(
                Jahr=widget["year"], Monat=widget["month"], plot_mean=widget["mean"]
            )
            def update(Jahr: int, Monat: int, plot_mean: bool):
                dummy = False
                self.update_plot(line, fig, Jahr, Monat, dummy, plot_mean)

    def update_plot(
            self, line, fig, Jahr: int, Monat: int, dummy: bool, plot_mean: bool
        ):
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



class SimAR:
        
    def setup_ax(self, figsize):
        fig  = plt.figure(figsize=figsize)
        ax = {}
        if not self.plot_mean_var:
            ax["y"] = plt.subplot()
        
        # Create 2x2 sub plots
        else:
            gs = gridspec.GridSpec(2, 3, width_ratios=[4, 1, 1])
            

            ax["y"] = plt.subplot(gs[:, :2]) # row 1, span all columns
            ax["mean"] = plt.subplot(gs[0, 2]) # row 0, col 0
            ax["var"] = plt.subplot(gs[1, 2]) # row 0, col 1

            if False:
                ax["y"] = plt.subplot(2, 2, (1, 2))
                ax["mean"] = plt.subplot(2, 2, 3)  
                ax["var"] = plt.subplot(2, 2, 4)
            plt.subplots_adjust(hspace=0.5)
        # fig.suptitle('rrr')
        # ax.set_ylim(*ylim)
        fig.subplots_adjust(
            left=0.05, 
            # right=0.9, 
            top=0.95, 
            # bottom=0.1
        )
        return fig, ax

    def plot(self, figsize=(12,6), plot_mean_var: bool = False):
        self.figsize = figsize
        self.plot_mean_var = plot_mean_var

        fig, ax = self.setup_ax(figsize=self.figsize)

        widget = {}
        widget["c"] = ipywidgets.FloatSlider(
            value=0,
            min=0,
            max=4,
            step=0.5,
            description='c'
        )
        widget["a"] = ipywidgets.FloatSlider(
            value=0,
            min=-1.1,
            max=1.1,
            step=0.1,
            description='a'
        )
        widget["r"] = ipywidgets.IntSlider(value=1, min=1, max=1001, step=50)
        widget["n"] = ipywidgets.IntSlider(min=100, max=1000, step=100)

        @interact(c=widget["c"], a=widget["a"], r=widget["r"], n=widget["n"])
        def update(c, a, r, n):
            self.update_plot(fig, ax, c, a, r, n)

    def update_plot(
        self, fig, ax, c: float, a: float, r: int, n: int
    ):
        y = arma_generate_sample([1, -a], [1], (n, r))

        # add intercept
        exponents = np.arange(0, n)
        power_series = c * np.power(a, exponents)
        intercept = power_series.cumsum().reshape(n, 1)

        y = y + intercept
        
        # cannot use line["realization"].set_data(y) if y is a matrix
        ax["y"].clear()
        ax["y"].plot(y, alpha=0.5)
        ax["y"].set_xlabel('t')
        ax["y"].set_ylabel('Realisierung')
        ax["y"].set_title(f'{n} Realisierungen eines AR(1) Prozesses')

        if self.plot_mean_var:
            mean = y.mean(axis=1) # .round(2)
            var = y.var(axis=1) # .round(2)
            ax["mean"].clear()
            ax["mean"].plot(mean)
            ax["mean"].set_ylim(y.min(), y.max())
            ax["mean"].set_title("Mittelwert")
            ax["mean"].set_xlabel("t")
            
            ax["var"].clear()
            ax["var"].plot(var)
            ax["var"].set_ylim(y.min(), max(y.max(), var.max()))
            ax["var"].set_title("Varianz")
            ax["var"].set_xlabel("t")
            # import pdb; pdb.set_trace()

        fig.canvas.draw_idle()

class SimARSimple:
    # Like SimAR but without c
        
    def setup_ax(self, figsize):
        fig  = plt.figure(figsize=figsize)
        ax = {}
        if not self.plot_mean_var:
            ax["y"] = plt.subplot()
        
        # Create 2x2 sub plots
        else:
            gs = gridspec.GridSpec(2, 3, width_ratios=[4, 1, 1])
            

            ax["y"] = plt.subplot(gs[:, :2]) # row 1, span all columns
            ax["mean"] = plt.subplot(gs[0, 2]) # row 0, col 0
            ax["var"] = plt.subplot(gs[1, 2]) # row 0, col 1

            if False:
                ax["y"] = plt.subplot(2, 2, (1, 2))
                ax["mean"] = plt.subplot(2, 2, 3)  
                ax["var"] = plt.subplot(2, 2, 4)
            plt.subplots_adjust(hspace=0.5)
        # fig.suptitle('rrr')
        # ax.set_ylim(*ylim)
        fig.subplots_adjust(
            left=0.05, 
            # right=0.9, 
            top=0.95, 
            # bottom=0.1
        )
        return fig, ax

    def plot(self, figsize=(12,6), plot_mean_var: bool = False):
        self.figsize = figsize
        self.plot_mean_var = plot_mean_var

        fig, ax = self.setup_ax(figsize=self.figsize)

        widget = {}
        widget["c"] = ipywidgets.FloatSlider(
            value=0,
            min=0,
            max=4,
            step=0.5,
            description='c'
        )
        widget["a"] = ipywidgets.FloatSlider(
            value=0,
            min=-1.1,
            max=1.1,
            step=0.1,
            description='a'
        )
        widget["n"] = ipywidgets.IntSlider(min=100, max=1000, step=100, description="T")
        widget["r"] = ipywidgets.IntSlider(
            value=1, min=1, max=1001, step=50, description="R"
        )

        @interact(a=widget["a"], n=widget["n"], r=widget["r"])
        def update(a, n, r):
            c = 0
            self.update_plot(fig, ax, c, a, r, n)

    def update_plot(
        self, fig, ax, c: float, a: float, r: int, n: int
    ):
        y = arma_generate_sample([1, -a], [1], (n, r))

        # add intercept
        exponents = np.arange(0, n)
        power_series = c * np.power(a, exponents)
        intercept = power_series.cumsum().reshape(n, 1)

        y = y + intercept
        
        # cannot use line["realization"].set_data(y) if y is a matrix
        ax["y"].clear()
        ax["y"].plot(y, alpha=0.5)
        ax["y"].set_xlabel('t')
        ax["y"].set_ylabel('Realisierung')
        ax["y"].set_title(
            f'{r} Realisierungen eines AR(1) Prozesses mit c = 0 und {n} Beobachtungen'
        )

        if self.plot_mean_var:
            mean = y.mean(axis=1) # .round(2)
            var = y.var(axis=1) # .round(2)
            ax["mean"].clear()
            ax["mean"].plot(mean)
            ax["mean"].set_ylim(y.min(), y.max())
            ax["mean"].set_title("Mittelwert")
            ax["mean"].set_xlabel("t")
            
            ax["var"].clear()
            ax["var"].plot(var)
            ax["var"].set_ylim(y.min(), max(y.max(), var.max()))
            ax["var"].set_title("Varianz")
            ax["var"].set_xlabel("t")
            # import pdb; pdb.set_trace()

        fig.canvas.draw_idle()


class DataVsProcess:

    def get_data(self):
        a = 0.5
        mu = 8
        n = 10
        self.n = n
        r = 4
        self.r = r

        # times series
        x = range(1, n + 1)
        # add burnin because Y_0 is not drawn from the stationary distribution
        y = arma_generate_sample(
            [1, -a], [1], (n, r), scale=np.sqrt((1-a**2)), burnin=1000
        )
        y = y + mu

        # normal density
        sigma = 1
        alpha = 0.001
        quantile = norm.ppf([alpha, 1-alpha], loc=mu, scale=sigma)
        x_norm = np.linspace(*quantile, 100)
        y_norm = norm.pdf(x_norm, mu, sigma)
        
        data = {
            "x": x,
            "y": y,
            "quantile": quantile,
            "x_norm": x_norm,
            "y_norm": y_norm
        }
        
        return data
        
    def setup_ax(self, ax, xlim, ylim):
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_xlabel("t")
        ax.set_ylabel("Realisierungen")
        ax.set_title("10 Beobachtungen einer Zeitreihe")
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        # ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.grid(True, axis='x', linestyle='--', which='major')
        ax.xaxis.set_major_locator(plt.MultipleLocator(1))
        # return fig, ax
        
    def plot(self, figsize=(12, 6)):
        data = self.get_data()
        fig, ax = plt.subplots(figsize=figsize)
        fig.subplots_adjust(
            left=0.05, 
            # right=0.9, 
            top=0.95, 
            # bottom=0.1
        )
        # fig, ax = self.setup_ax(figsize, xlim=[0, self.n+1], ylim=data["quantile"])

        line = {}
        color = {0: '#bcbd22', 1: '#17becf', 2: '#1f77b4', 3: '#ff7f0e'}
            
        button = ipywidgets.ToggleButtons(
            options=[
                'Daten', 'Zufallsvariablen', 'Mögliche Daten',
                'Mögliche Trajektorien', 'Daten Trajektorie'
            ],
            description=' ',  # If string is empty "button" is displayed
            disabled=False,
            button_style='info', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='',
        #     icon='check'
        )

        
        @interact(button=button)
        def update(button):
            #ax.clear()
            if button in ["Daten", "Daten Trajektorie"]:
                ax.clear()
            
            self.setup_ax(ax, xlim=[0, self.n+1], ylim=data["quantile"])
            line[0],  = ax.plot(
                data["x"], data["y"][:, 0], linestyle="", marker="x", color=color[0]
            )
            # print(button)

            if button == "Zufallsvariablen":
                for t in range(self.n):
                    if t == 0:
                        ax.plot(
                            data["y_norm"] + t + 1, data["x_norm"], color='gray',
                             linestyle='--', label='N(0, 1)'
                        )
                    else:
                        ax.plot(
                            data["y_norm"] + t + 1, data["x_norm"], color='gray',
                            linestyle='--')
                ax.legend(loc='upper left') 
            elif button == "Mögliche Daten":
                for t in range(self.r):
                    line[t],  = ax.plot(
                        data["x"], data["y"][:, t], linestyle="", marker="x",
                         color=color[t])               
            elif button == "Mögliche Trajektorien":
                for t in range(self.r):
                    line[t],  = ax.plot(data["x"], data["y"][:, t], linestyle="--",
                                        marker="x", color=color[t])
            elif button == "Daten Trajektorie":
                line[0],  = ax.plot(data["x"], data["y"][:, 0], linestyle="--",
                    marker="x", color=color[0])
                
            fig.canvas.draw_idle()
            return
