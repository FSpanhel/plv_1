import pandas as pd
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import statsmodels.api as sm

from plv.model import AR


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

def plot_is_oos_forecast(
        ar: AR, forecast_horizon: int, oos_data: None | pd.Series = None,
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

    plt.axvline(x=ts.index[-1], color='gray', linestyle='--', label='In-sample Ende')

    plt.plot(
        forecast_is.index, forecast_is, color='green', linestyle='-',
        label='In-sample one-step ahead forecast'
    )

    forecast_oos_ = pd.concat([forecast_is.tail(1), forecast_oos])

    plt.plot(
        forecast_oos_.index, forecast_oos_, color='red', linestyle='--',
        label='Out-of-sample multi-step ahead forecast'
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