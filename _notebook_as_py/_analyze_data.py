# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

from plv.data import load_verbraucherpreisindex
from plv.plot import plot_ts

# %% [markdown]
# # Load

# %%
data = load_verbraucherpreisindex(filter_columns=None)
data = data[data["inflation"].notna()].copy()

# %% [markdown]
# # Plot

# %%
# plot_ts(data["inflation"])

# %%
import matplotlib.pyplot as plt

# %%
plt.plot(data.index, data["inflation"])

# %%
data["inflation"].tail(20)

# %% [markdown]
# # Investigate PACF

# %%
filter_ = slice("1995", "2020")

# %%
data.loc[filter_]

# %%
y = data.loc[filter_, "inflation"]

# %%
from statsmodels.tsa.stattools import pacf, acf
import statsmodels.api as sm
import matplotlib.pyplot as plt
y
sm.graphics.tsa.plot_pacf(y, lags=40, method="ywm")
plt.show()
p = pacf(y)
pd.Series(p, index=range(1, len(p) +1 ))

# %% [markdown]
# # ACF

# %%
sm.graphics.tsa.plot_acf(y, lags=40)
plt.show()
p = acf(y)
pd.Series(p, index=range(1, len(p) +1 ))

# %% [markdown]
# # Seasonality

# %%
import statsmodels.api as sm
def plot_seasonality(data: pd.Series, freq="MS"):
    "Seasonality plot of data"
    # this is necessary because otherwise sm.graphics.tsa.month_plot(y) throws an error
    # Turn the dtype Float64 of y into float64 
    index = pd.DatetimeIndex(data.index, freq=freq)
    y = pd.Series(index=index, data=data.to_numpy().astype(float))
    fig = sm.graphics.tsa.month_plot(y)
    return fig


# %%
plot_seasonality(data.loc[slice(None, "2020"), "inflation"])

# %%
data.index

# %%
import statsmodels.api as sm

y = pd.Series(index=data.index, data=data["inflation"].to_numpy().astype(float))
y = y.loc[slice(None, "2020")]
fig = sm.graphics.tsa.month_plot(y)
type(fig)

# %% [markdown]
# ## Example with seasonality

# %%
dta = sm.datasets.elnino.load_pandas().data
dta['YEAR'] = dta.YEAR.astype(int).astype(str)
dta = dta.set_index('YEAR').T.unstack()
dates = pd.to_datetime(list(map(lambda x: '-'.join(x) + '-1',
                                dta.index.values)))
dta.index = pd.DatetimeIndex(dates, freq='MS')
fig = sm.graphics.tsa.month_plot(dta)

# %% [markdown]
# # Zusammenhang Prozess und Daten

# %%
import matplotlib.pyplot as plt

# Sample data for four observations
top_data = [1, 2, 3, 4]
bottom_data = [5]

# Create a figure with two subplots (one on top, one on bottom)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))  # Adjust figsize as needed

# Plot the top subplot with four observations
ax1.plot(range(4), top_data, marker='o', linestyle='-')
ax1.set_title('Top Figure')
ax1.set_ylabel('Observations')

# Plot the bottom subplot with one observation
ax2.plot(0, bottom_data[0], marker='o', markersize=10, color='red')
ax2.set_title('Bottom Figure')
ax2.set_ylabel('Observation')

# Add an arrow connecting the first observation in the top subplot
arrowprops = dict(arrowstyle='->', connectionstyle='arc3,rad=1', lw=2, color='blue')
ax1.annotate('', xy=(0, top_data[0]), xytext=(0, bottom_data[0]), arrowprops=arrowprops)

# Adjust spacing between subplots
plt.subplots_adjust(hspace=0.5)

# Show the plot
plt.show()

# %% [markdown]
# # AR Simulation

# %% [markdown]
# ## Using statsmodels -> cannot set initial value

# %%
from statsmodels.tsa.arima_process import ArmaProcess, arma_generate_sample
import matplotlib.pyplot as plt

plt.plot(arma_generate_sample([1, -1], [1], 1000000))

# %%
n = int(1e4)
n = 10
r = 2
plt.plot(arma_generate_sample([1, -0.9], [1], (n, r)));

# %% [markdown]
# ## Manual

# %%
a = 0.9
exponents = np.arange(n)
a_vector = np.power(a, exponents)

mean = 0  # Mean of the normal distribution
std_dev = 1  # Standard deviation of the normal distribution
num_samples = 100  # Number of random samples to generate

# Generate random numbers from a normal distribution
U = np.random.normal(mean, std_dev, (n, r))
res = a_vector @ U


# %%
a_vector.T.shape

# %%
res.shape

# %%

# %%
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.tsa.arima.model import ARIMA

# %%
dta = sm.datasets.sunspots.load_pandas().data
dta.index = pd.Index(sm.tsa.datetools.dates_from_range("1700", "2008"))
dta.index.freq = dta.index.inferred_freq
del dta["YEAR"]

# %% [markdown]
# # Widgets

# %%
import ipywidgets as widgets
from IPython.display import display

# Variable to be changed
my_variable = 0

# Create a slider widget
slider = widgets.FloatSlider(
    value=my_variable,
    min=0.0,
    max=100.0,
    step=1.0,
    description='Change My Variable:',
)

# Function to update the variable
def update_variable(change):
    my_variable = change.new
    print(f"Updated My Variable: {my_variable}")
    return my_variable

# Link the slider to the update function
slider.observe(update_variable, names='value')

# Display the slider
display(slider)


# %%
slider.observe?

# %%
my_variable

# %% [markdown]
# ## interactive widgets
# https://hub.ovh2.mybinder.org/user/jupyter-widgets-tutorial-8dpcylxk/lab/tree/notebooks/01.Introduction/01.00-introduction.ipynb

# %%
slider = widgets.FloatSlider(
    value=7.5,
    min=5.0,
    max=10.0,
    step=0.1,
    description='Input:',
)

b = widgets.FloatSlider(
    value=7.5,
    min=5.0,
    max=10.0,
    step=0.1,
    description='Input:',
)

slider

# %%
square = slider.value * slider.value

def handle_change(change):
    global square
    square = change.new
    
slider.observe(handle_change, 'value')

# %%
square


# %% [markdown]
# ## interact

# %%
def f(x):
    print(x)
    
import ipywidgets as ipw

widgets.interact(f, x=(0, 100));

# %% [markdown]
# ### interact with a plot
# https://hub.ovh2.mybinder.org/user/jupyter-widgets-tutorial-8dpcylxk/lab/tree/notebooks/02.Widget_overview/01.Interact/01.00-Using-Interact.ipynb

# %%
# not optimal because figure is redrawn every time
import matplotlib.pyplot as plt
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def f(m, b):
    fig = plt.figure()
    plt.clf()
    plt.grid()
    x = np.linspace(-10, 10, num=1000)
    plt.plot(x, m * x + b)
    plt.ylim(-5, 5)
    plt.show()

interact(f, m=(-2.0, 2.0), b=(-3, 3, 0.5))

# %%
interact?

# %% [markdown]
# ### mpl interactinons -> does not work

# %%
%matplotlib ipympl

from mpl_interactions import ipyplot as iplt

fig, ax = plt.subplots()
ax.grid()
ax.set_ylim(-30,30)

# Define function in a way you can re-use in calculations
def f(x, m, b):
    return m * x + b

x = np.linspace(-10, 10, num=1000)
ctrls = iplt.plot(x, f, m=(-2,2), b=(-3, 3, 10))

# %%
import mpl_interactions.ipyplot as iplt
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi, 100)
tau = np.linspace(0.5, 10, 100)

def f1(x, tau, beta):
    return np.sin(x * tau) * x * beta
def f2(x, tau, beta):
    return np.sin(x * beta) * x * tau


fig, ax = plt.subplots()
controls = iplt.plot(x, f1, tau=tau, beta=(1, 10, 100), label="f1")
iplt.plot(x, f2, controls=controls, label="f2")
_ = plt.legend()
plt.show()
