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
import matplotlib.dates as mdates

# Sample data with Timestamps
timestamps = pd.to_datetime(['2023-01-01', '2023-01-10'])
x_start, x_end = mdates.date2num(timestamps)

# Create a figure and axis
fig, ax = plt.subplots()

# Define the parameters of the rectangle
y = 0
width = x_end - x_start
height = 10
fill_color = 'blue'  # Change this to your desired fill color

# Create a Rectangle object and add it to the axis
rectangle = patches.Rectangle((x_start, y), width, height, linewidth=1, edgecolor='black', facecolor=fill_color)
ax.add_patch(rectangle)

# Set axis limits and display the plot
ax.set_xlim(min(timestamps) - pd.Timedelta(days=1), max(timestamps) + pd.Timedelta(days=1))
ax.set_ylim(0, 10)  # Adjust the y-axis limits as needed
plt.gca().set_aspect('auto')  # Set aspect ratio to 'auto' to allow for date-based x-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# %%
import matplotlib.pyplot as plt

plt.close("all")

# Create a simple plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
line, = plt.plot(x, y)

# Get the color of the line
line_color = line.get_color()

# Display the color
print(f"The color of the line is {line_color}")

# Show the plot
plt.show()

line_color

# %%
import numpy as np
import pandas as pd
import matplotlib.patches as patches

# Activate the widget based backend.
%matplotlib ipympl

date = pd.date_range("2010", "2024", freq="MS")
x = pd.Series(range(0, len(date)), index=date)

x_start, x_end = mdates.date2num(pd.to_datetime(["2022", "2023"]))
width = x_end - x_start
height = 10


fig, ax = plt.subplots()
ax.grid()
# ax.set_ylim(-5, 5)
# Initialize a plot object with y = x. We'll be modifying y below.
# This returns a list of `.Line2D` representing the plotted data. We grab the first one -- we only have 1 series.
line = ax.plot(x.index, x)

rectangle = patches.Rectangle((x_start, y), width, height, linewidth=1, edgecolor='black', facecolor="#50C878", label="ha")
ax.add_patch(rectangle)
ax.legend()
# rectangle = patches.Rectangle((pd.Timestamp("2016"), 0), 9.5, 10, linewidth=0, edgecolor='r', facecolor='red', alpha=0.2)
# ax.add_patch(rectangle)

# %% slideshow={"slide_type": "slide"}
import numpy as np
import matplotlib.patches as patches

# Activate the widget based backend.
%matplotlib ipympl

x = np.linspace(-10, 10, num=1000)
fig, ax = plt.subplots()
ax.grid()
ax.set_ylim(-5, 5)
# Initialize a plot object with y = x. We'll be modifying y below.
# This returns a list of `.Line2D` representing the plotted data. We grab the first one -- we only have 1 series.
line = ax.plot(x, x)[0]

rectangle = patches.Rectangle((1, 0), 9.5, 10, linewidth=0, edgecolor='r', facecolor='red', alpha=0.2)
ax.add_patch(rectangle)


# %% slideshow={"slide_type": "slide"}
@interact(m=(-2.0, 2.0), b=(-3, 3, 0.5))
def update_line(m=1, b=0.5):
    line.set_ydata(m * x + b)
    # Request a widget redraw.
    fig.canvas.draw_idle()
    
    import matplotlib.patches as patches


# %% slideshow={"slide_type": "slide"}
%matplotlib inline

import matplotlib.pyplot as plt
from ipywidgets import interact

# plt.close("all")
def plot_graph(n):
    plt.plot(range(n))
    plt.show()

plot_graph(10)

# %% slideshow={"slide_type": "slide"}
interact(plot_graph, n=(2,30))

# %% slideshow={"slide_type": "-"}
1

# %% slideshow={"slide_type": "slide"}
from scipy.stats import norm
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import MultipleLocator

class DataVsProcess:

    def get_data(self):
        a = 0.5
        mu = 8
        self.n = 10
        r = 4

        # times series
        x = range(1, n + 1)
        # add burnin because Y_0 is not drawn from the stationary distribution
        y = arma_generate_sample([1, -a], [1], (n, r), scale=np.sqrt((1-a**2)), burnin=1000)
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
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        # ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.grid(True, axis='x', linestyle='--', which='major')
        ax.xaxis.set_major_locator(plt.MultipleLocator(1))
        # return fig, ax
        
        
    def plot(self, figsize=(12, 6)):
        data = self.get_data()
        fig, ax = plt.subplots(figsize=figsize)
        # fig, ax = self.setup_ax(figsize, xlim=[0, self.n+1], ylim=data["quantile"])

        line = {}
        color = {0: '#bcbd22', 1: '#17becf', 2: '#1f77b4', 3: '#ff7f0e'}
            
        button = ipywidgets.ToggleButtons(
            options=['Daten', 'Zufallsvariablen', 'Mögliche Daten', 'Mögliche Trajektorien', 'Daten Trajektorie'],
            description=' ',
            disabled=False,
            button_style='info', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='',
            icon='check'
        )
        
        watcher = {}
        
        sim_data = ipywidgets.ToggleButton(
            value=False,
            description='Simuliere Daten',
            disabled=False,
            button_style='info', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Description',
            icon='check'
        )

        
        @interact(button=button, sim_data=sim_data)
        def update(button, sim_data):
            #ax.clear()
            # print(button)
            # print(sim_data)
            if button in ["Daten", "Daten Trajektorie"]:
                ax.clear()
            
            self.setup_ax(ax, xlim=[0, self.n+1], ylim=data["quantile"])

            # ax.set_ylim(*data["quantile"])
            # ax.set_xlim(0, self.n+1)
            line[0],  = ax.plot(data["x"], data["y"][:, 0], linestyle="", marker="x", color=color[0])
            # print(button)

            if button == "Zufallsvariablen":
                for t in range(n):
                    if t == 0:
                        ax.plot(data["y_norm"] + t + 1, data["x_norm"], color='gray', linestyle='--', label='N(0, 1)')
                    else:
                        ax.plot(data["y_norm"] + t + 1, data["x_norm"], color='gray', linestyle='--')
                ax.legend(loc='upper left') 
            elif button == "Mögliche Daten":
                for t in range(r):
                    line[t],  = ax.plot(data["x"], data["y"][:, t], linestyle="", marker="x", color=color[t])               
            elif button == "Mögliche Trajektorien":
                for t in range(r):
                    line[t],  = ax.plot(data["x"], data["y"][:, t], linestyle="--", marker="x", color=color[t])
            elif button == "Daten Trajektorie":
                line[0],  = ax.plot(data["x"], data["y"][:, 0], linestyle="--", marker="x", color=color[0])
                
            fig.canvas.draw_idle()
            return
        
    

# %%
a = DataVsProcess()
plt.close("all")
a.plot(figsize=(12, 6))

# %%
import ipywidgets
widget = ipywidgets.ToggleButtons(
    options=['Daten', 'Zufallsvariablen', 'Mögliche Daten', 'Mögliche Trajektorien', 'Daten Trajektorie'],
    description='A',
    disabled=False,
    button_style='info', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='A',
#     icon='check'
)

widget = ipywidgets.ToggleButton(
            value=False,
            description='Zeige Out-of-sample Daten',
            disabled=False,
            button_style='info', # 'success', 'info', 'warning', 'danger' or ''
            # tooltip='Description',
            # icon='check'
        )


widget = ipywidgets.Checkbox(
    value=False,
    description='Check me',
    disabled=False
)

from IPython.display import display

display(widget)

# %%
color

# %%
plt.close("all")
a = 0.5
mu = 8
n = 10
r = 4
y = arma_generate_sample([1, -a], [1], (n, r), scale=np.sqrt((1-a**2)), burnin=1000)
y = y + mu
x = range(1, n + 1)
print(y.shape)

from matplotlib.ticker import MaxNLocator
fig, ax = plt.subplots()

ax.plot(x, y, linestyle="", marker="x")

line = {}
color = {}
for t in range(r):
    line[t],  = ax.plot([], []) # , linestyle="", marker="x")
for t in range(r):
    line[t],  = ax.plot(x, y[:, t], linestyle="", marker="x")
    color[t] = line[t].get_color()
    # line[t].plot(x, y[:, t], linestyle="-", marker="x")
    
# ax.plot(x, y, linestyle="-", marker="x", alpha=0.8)
ax.set_xlim(0, n + 1)
ax.set_xlabel("t")
ax.set_ylabel("Realisierungen")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# %%
for t in range(r):
    line[t],  = ax.plot(x, y[:, t], linestyle="--", marker="x", color=line[t].get_color())

# %%
y.var(axis=1)

# %%
from scipy.stats import norm
sigma = 1
alpha = 0.001

# Compute the 1% quantile using the percent point function (ppf)
# The argument to ppf represents the desired percentile (1% in this case)
quantile = norm.ppf([alpha, 1-alpha], loc=mu, scale=sigma)
x_norm = np.linspace(*quantile, 100)
y_norm = norm.pdf(x_norm, mu, sigma)
quantile

# %%
ax.set_ylim(*quantile)
for t in x:
    ax.plot(y_norm + t, x_norm, color='gray', linestyle='--', label='N(0, 1)')

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

# %% [markdown]
# ## Using a plt

# %%

import ipywidgets
from ipywidgets import interact

class A:
    def __init__(self, figsize=(12,6)):
        self.figsize = figsize
    
    def setup_plt(self, figsize):
        plt.figure(figsize=figsize)
        plt.xlabel('t')
        plt.ylabel('Realisierung')
        plt.title(f'{n} Realisierungen eines AR(1) Prozesses')
        return plt

    def plot_initial_lines(self, plt) -> dict:
        line = {}
        # import pdb; pdb.set_trace()
        #line["realization"],  = 
        plt.plot([], [])
        return line

    def plot(self):

        plt = self.setup_plt(figsize=self.figsize)
        self.plot_initial_lines(plt)
        
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
        widget["r"] = ipywidgets.IntSlider(value=1, min=1, max=1000, step=50)
        widget["n"] = ipywidgets.IntSlider(min=100, max=1000, step=100)

        @interact(c=widget["c"], a=widget["a"], r=widget["r"], n=widget["n"])
        def update(c, a, r, n):
            self.update_plot(plt, c, a, r, n)

    def update_plot(
        self, plt, c: float, a: float, r: int, n: int
    ):
        y = arma_generate_sample([1, -a], [1], (n, r))

        # add intercept
        exponents = np.arange(0, n)
        power_series = c * np.power(a, exponents)
        intercept = power_series.cumsum().reshape(n, 1)

        y = y + intercept

        # cannot use line["realization"].set_data(y)
        plt.clf()
        plt.plot(y)

        # plt.canvas.draw_idle()


# %% [markdown]
# ## only y

# %%
import ipywidgets
from ipywidgets import interact

class A:
    def __init__(self, figsize=(12,6)):
        self.figsize = figsize
        
    def setup_ax(self, figsize):
        fig, ax = plt.subplots(figsize=figsize)
        # fig.suptitle('rrr')
        # ax.set_ylim(*ylim)
        fig.subplots_adjust(
            left=0.05, 
            # right=0.9, 
            top=0.95, 
            # bottom=0.1
        )
        ax.set_xlabel('t')
        ax.set_ylabel('Realisierung')
        ax.set_title(f'{n} Realisierungen eines AR(1) Prozesses')
        return fig, ax

    def plot(self):

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
        widget["r"] = ipywidgets.IntSlider(value=1, min=1, max=1000, step=50)
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
        ax.clear()
        ax.plot(y, alpha=0.5)
        ax.set_xlabel('t')
        ax.set_ylabel('Realisierung')
        ax.set_title(f'{n} Realisierungen eines AR(1) Prozesses')

        fig.canvas.draw_idle()


# %% [markdown]
# ## with mean and var

# %%
import matplotlib.gridspec as gridspec

class A:
    def __init__(self, figsize=(12,6), plot_mean_var: bool = False):
        self.figsize = figsize
        self.plot_mean_var = plot_mean_var
        
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

    def plot(self):

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

# %% slideshow={"slide_type": "slide"}
a = A(figsize=(12, 6))


# %% slideshow={"slide_type": "slide"} hide_input=false
from IPython.display import display, HTML
display(HTML("<style>.container { width:95% !important; }</style>"))

%matplotlib ipympl 
a = A(figsize=(14, 5), plot_mean_var=False)
a.plot()

# %%
a = A(figsize=(14, 5), plot_mean_var=True)

# %% slideshow={"slide_type": "slide"}
a.plot()

# %% slideshow={"slide_type": "slide"}
plt.subplot?

# %% slideshow={"slide_type": "slide"}
n = int(1e4)
n = 1000
r = 100
a = 1.01  # Common ratio of the geometric series  # larger > 1 not allowed because of overflow: <= 1.01
a = 1
c = 0
y = arma_generate_sample([1, -a], [1], (n, r))




# print("ha", c / (1-a))

# Generate the geometric series
if False:
    geometric_series = c * np.geomspace(first_term, first_term * a**(n-1), n)

    exponents = np.arange(0, n)  # For example, generates exponents from 0 to 5
    intercept = geometric_series.cumsum().reshape(n, 1)

# Generate the power series using numpy.power
exponents = np.arange(0, n)
power_series = c * np.power(a, exponents)
intercept = power_series.cumsum().reshape(n, 1)

y = y + intercept

# Create a figure
fig = plt.figure()

# Create subplots using plt.subplot()
if True:
    ax1 = plt.subplot(2, 2, (1, 2))  # 2 rows, 2 columns, subplot 1
    ax2 = plt.subplot(2, 2, 3)  
    ax3 = plt.subplot(2, 2, 4)
else:
    ax1 = plt.subplot(3, 3, (2, 1))  # 2 rows, 2 columns, subplot 1
    # ax2 = plt.subplot(2, 3, (1, 3))  
    # ax3 = plt.subplot(2, 3, (2, 3))
plt.subplots_adjust(hspace=0.5)
plt.subplots_adjust(
            left=0.05, 
            # right=0.9, 
            top=0.95, 
            # bottom=0.1
        )


# plt.rcParams['font.family'] = 'serif' 
ax1.plot(y, alpha=0.4);
ax1.set_title(f'{n} Realisierungen eines AR(1) Prozesses')

# %%
gs

# %% [markdown]
# ### three plots above each other

# %% slideshow={"slide_type": "slide"} code_folding=[]
if True:
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec

    # Create a figure with a 3x1 grid
    fig = plt.figure(figsize=(12, 6))
    gs = gridspec.GridSpec(3, 1, height_ratios=[3, 1, 1])

    # Create the larger plot at the top
    ax1 = plt.subplot(gs[0])
    ax1.plot(y, alpha=0.4);
    ax1.set_title('Larger Plot')

    # Create the middle plot
    ax2 = plt.subplot(gs[1])
    ax2.scatter([1, 2, 3, 4], [2, 4, 6, 8])
    ax2.set_title('Middle Plot')

    # Create the smaller plot at the bottom
    ax3 = plt.subplot(gs[2])
    ax3.bar(['A', 'B', 'C', 'D'], [10, 20, 15, 30])
    ax3.set_title('Smaller Plot')

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the figure with subplots
    plt.show()


# %% [markdown]
# ### two plots side by side

# %%
gridspec.GridSpec?

# %%
import numpy as np
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec

# Create 2x2 sub plots
gs = gridspec.GridSpec(2, 3, width_ratios=[4, 1, 1])

pl.figure(figsize=(12, 6))
ax = pl.subplot(gs[0, 2]) # row 0, col 0
pl.plot([0,1])

ax = pl.subplot(gs[1, 2]) # row 0, col 1
pl.plot([0,1])

ax = pl.subplot(gs[:, :2]) # row 1, span all columns
pl.plot([0,1])

# %% slideshow={"slide_type": "slide"}
mean = y.mean(axis=1) # .round(2)
var = y.var(axis=1) # .round(2)
ax2.plot(mean)
ax2.set_ylim(y.min(), y.max())
ax2.set_title("Mittelwert")
ax2.set_xlabel("t")

# %%
ax3.plot(var)
ax3.set_ylim(y.min(), max(y.max(), var.max()))
ax3.set_title("Varianz")
ax3.set_xlabel("t")

# %%
plt.plot(y.mean(axis=1), ylim=(-4, 4))

# %% [markdown]
# ## Manual -> obsolete

# %%
np.geomspace?

# %%
import numpy as np

# Define the first term, common ratio, and number of elements
first_term = 1  # First term of the series
a = 0.5  # Common ratio of the geometric series
n = 5  # Number of elements in the series

# Generate the geometric series
geometric_series = np.geomspace(first_term, first_term * a**(n-1), n)

# Print the resulting array
print(geometric_series)


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
# ### display slider

# %%
import ipywidgets as widgets
from IPython.display import display

# Create a float slider
slider = widgets.FloatSlider(
    value=0.0,
    min=0.0,
    max=100.0,
    step=0.1,
    description='Value:',
)

# Display the slider
display(slider)

# Define an event handler for slider changes
def on_slider_change(change):
    print(f"Slider value: {change['new']}")

slider.observe(on_slider_change, names='value')

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
# ### ipympl and plain matplotlib

# %%
# Activate the widget based backend.
%matplotlib ipympl

class H:
    def __init__(self):
        x = np.linspace(-10, 10, num=1000)
        fig, ax = plt.subplots()
        ax.grid()
        ax.set_ylim(-5, 5)
        # Initialize a plot object with y = x. We'll be modifying y below.
        # This returns a list of `.Line2D` representing the plotted data. We grab the first one -- we only have 1 series.
        line = ax.plot(x, x)[0]

        @interact(m=(-2.0, 2.0), b=(-3, 3, 0.5))
        def update_line(m=1, b=0.5):
            line.set_ydata(m * x + b)
            # Request a widget redraw.
            fig.canvas.draw_idle()
        
H()

# %%
# Activate the widget based backend.
%matplotlib ipympl

x = np.linspace(-10, 10, num=1000)
fig, ax = plt.subplots()
ax.grid()
ax.set_ylim(-5, 5)
# Initialize a plot object with y = x. We'll be modifying y below.
# This returns a list of `.Line2D` representing the plotted data. We grab the first one -- we only have 1 series.
line = ax.plot(x, x)[0]

@interact(m=(-2.0, 2.0), b=(-3, 3, 0.5))
def update_line(m=1, b=0.5):
    line.set_ydata(m * x + b)
    # Request a widget redraw.
    fig.canvas.draw_idle()


# %%
import matplotlib.pyplot as plt
import numpy as np

dates = pd.Series(
    range(0, n),
    index=pd.date_range("2016", periods=n, freq="MS")
)

# Create initial data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
    
x = dates.index
y = dates.to_numpy()

# Create the initial plot
fig, ax = plt.subplots()
line, = ax.plot(x, y, marker="x")

# Update the data and redraw the plot
new_y = dates.loc[:"2020"].to_numpy()
new_x = dates.loc[:"2020"].index
update_plot(new_x, new_y)

# Show the updated plot
plt.show()

# %%
line.set_data?

# %%
type(line)

# %%
# two lines
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the initial data
line1, = ax.plot(x, y1, label='Line 1', color='blue')
line2, = ax.plot(x, y2, label='Line 2', color='red')

# Set other plot properties
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Multiple Lines Example')

# Add a legend
ax.legend()

# Function to update the data of multiple lines
def update_lines():
    new_y1 = np.sin(x + 1)  # New data for Line 1
    new_y2 = np.cos(x + 1)  # New data for Line 2

    # Update the data of the lines using set_data
    line1.set_data(x, new_y1)
    line2.set_data(x, new_y2)

    # Redraw the canvas to reflect the changes
    fig.canvas.draw()

# Update the lines with new data
update_lines()

# Show the plot
plt.show()


# %% slideshow={"slide_type": "slide"}
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets

n = 100

dates = pd.Series(
    range(0, n),
    index=pd.date_range("2016", periods=n, freq="MS")
)

# Create initial data
    
x = dates.index
y = dates.to_numpy()

# Create the initial plot
fig, ax = plt.subplots()
line, = ax.plot(x, y, marker="x")
line2, = ax.plot(x, y - 5, marker="x", label="Orange")
ax.set_xlabel("hahah")
ax.legend()
ax.grid()

year_widget = widgets.IntSlider(min=2016, max=2024, step=2)


dummy_widget = widgets.Dropdown(
    options={'AR(1)': False, 'AR(1) mit Krisen Dummy': True},
    value=False,
    description='Modell:',
)

mean_widget = widgets.Dropdown(
    options={'Ja': True, 'Nein': False},
    value=False,
    description='Zeichne den Erwartungswert des AR(1) Modells',
)

max_year_widget = widgets.IntSlider(min=2016, max=2024, step=2)

# Function to update the plot data
@interact(Jahr=year_widget, Monat=(1, 12), Dummy=dummy_widget, plot_mean=mean_widget)
def update_plot(Jahr, Monat, Dummy, plot_mean):
    new_y = dates.loc[:f"{Jahr}-{Monat}"].to_numpy()
    new_x = dates.loc[:f"{Jahr}-{Monat}"].index
    if Dummy:
        new_y = new_y + 10
    line.set_data(new_x, new_y)
    line2.set_data(new_x, new_y -5)
    fig.canvas.draw()



# %%
# Activate the widget based backend.
%matplotlib ipympl

x = np.linspace(-10, 10, num=1000)
fig, ax = plt.subplots()
ax.grid()
ax.set_ylim(-5, 5)
# Initialize a plot object with y = x. We'll be modifying y below.
# This returns a list of `.Line2D` representing the plotted data. We grab the first one -- we only have 1 series.
line = ax.plot(x, x)[0]

@interact(m=(-2.0, 2.0), b=(-3, 3, 0.5))
def update_line(m=1, b=0.5):
    line.set_ydata(m * x + b)
    # Request a widget redraw.
    fig.canvas.draw_idle()


# %% [markdown]
# ### mpl interactions -> does only work with specific version
# Have to plot numerical values on the x-axis, no datetime

# %%
iplt.plot?

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
ctrls = iplt.plot(x, f, m=(-2,2), b=(-3, 3, 10), slider_formats="{:.4f}")


# %%

n = 100
import pandas as pd
dates = pd.Series(
    range(0, n),
    index=pd.date_range("2016", periods=n, freq="MS"))

x = dates.index.strftime("%Y.%m").astype(float)

def f(Jahr: int, Monat: int):
    date_end = f"{Jahr}.{Monat}"
    out = pd.Series(0, index=dates_index)
    return out.loc[:date_end]

def f(x, Jahr):
    return x * Jahr

year = widgets.IntSlider(
    value=2018,
    min=2016,
    max=2023,
    step=1,
    description='Jahr:',
    # disabled=False,
    # continuous_update=False,
    orientation='horizontal',
    # readout=True,
    # slider_color='black'
)

month = widgets.IntSlider(
    value=1,
    min=1,
    max=12,
    step=1,
    description='Monat:',
    # disabled=False,
    # continuous_update=False,
    orientation='horizontal',
    # readout=True,
    # slider_color='black'
)

ctrls = iplt.plot(
    x, f, 
    Jahr=(2016, 2022), 
    # Monat=(1, 12)
) # , slider_formats="{:.0f}")



# %% slideshow={"slide_type": "slide"}
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

# %% [markdown]
# ### categoricals https://mpl-interactions.readthedocs.io/en/stable/examples/usage.html#categoricals

# %%
import ipywidgets as widgets


def f(x, tau, beta, type_):
    if type_ == "sin":
        return np.sin(x * tau) * x**beta
    elif type_ == "cos":
        return np.cos(x * tau) * x**beta
    
tau = widgets.FloatText(value=7, step=0.1)

tau = widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    # disabled=False,
    # continuous_update=False,
    orientation='horizontal',
    # readout=True,
    # slider_color='black'
)

fig, ax = plt.subplots()
controls = iplt.plot(x, f, tau=tau, beta=(0.2, 1), type_={("sin", "cos")})

# %% [markdown]
# ### DatePicker

# %%
slider = widgets.DatePicker(
    description='Datum',  # Description shown next to the widget
    disabled=False,               # Set to True to disable the widget
    value=None                     # Set an initial date (optional)
)

# Display the slider
display(slider)

# Define an event handler for slider changes
def on_slider_change(change):
    print(f"Slider value: {change['new']}")

slider.observe(on_slider_change, names='value')

# %% [markdown]
# # Interactive Plot für die Anwendung

# %%
from IPython.display import display, HTML
# display(HTML("<style>.container { width:95% !important; }</style>"))

from plv.data import load_verbraucherpreisindex, max_inflation, corona_begin
from plv.plot import plot_ts, plot_seasonality, plot_is_oos_forecast

inflation = load_verbraucherpreisindex(filter_columns=["inflation"])

# %%
from plv.model import CrisisDummy, AR1
print(corona_begin)
print(max_inflation)
dummy = CrisisDummy(start=corona_begin, end=max_inflation)

# %%
ar = AR1()

# %%
# %debug

# %%
import pandas as pd
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import statsmodels.api as sm
import ipywidgets
from ipywidgets import interact

from plv.model import AR1, CrisisDummy

AR = AR1

import numpy as np

widgets = ipywidgets

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
        data["forecast_origin"] = pd.Series(vertical, index=[data["in_sample"].index[-1]] * num)
        
        data["corona_start"] = pd.Series(vertical, index=[pd.Timestamp(corona_begin)] * num)
        
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
                                     label="Daten", marker="x") # , markersize=4)
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
            ar: AR,
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
        widget["dummy"] = widgets.Dropdown(
            options={'AR(1)': False, 'AR(1) mit Krisen Dummy': True},
            value=False,
            description='Modell:',
        )

        widget["mean"] = widgets.Dropdown(
            options={'Ja': True, 'Nein': False},
            value=False,
            description='Erwartungswert des AR(1) Modells',
        )

        @interact(Jahr=widget["year"], Monat=widget["month"], dummy=widget["dummy"], plot_mean=widget["mean"])
        def update(Jahr: int, Monat: int, dummy: bool, plot_mean: bool):
            
            forecast_origin = f"{Jahr}-{Monat}"
            forecast_origin = pd.Timestamp(f"{Jahr}-01-01") + pd.DateOffset(months=Monat-1)
            data = self.get_data(forecast_origin, dummy)
            for key in line.keys():
                if key == "mean":
                    if not plot_mean:
                        # continue
                        line[key].set_data([], [])
                        continue
                line[key].set_data(data[key].index, data[key])
                # if (key == "in_sample_forecast") and (forecast_origin == pd.Timestamp("2020-01-01")):
                #    print(data[key].tail())
  
            # Request a widget redraw.
            fig.canvas.draw_idle()


# %% slideshow={"slide_type": "slide"}
%matplotlib ipympl
a = InteractiveForecastPlot(ar, inflation, dummy, 750, figsize=(13, 5.5), ylim=(-1, 8.5))
a.plot()

# %%
import ipywidgets as widgets
from ipywidgets import interact
from IPython.display import display

# Define a function that takes widget parameters as arguments
@interact(value=widgets.FloatSlider(value=0.5, min=0, max=1, step=0.1, description='Slider'))
def update_plot(value):
    # Replace this with your plot update logic based on the value
    print(f"Slider value selected: {value}")

# Optionally, create additional widgets
button = widgets.Button(description='Click Me')
checkbox = widgets.Checkbox(value=False, description='Checkbox')

# Create an HBox to arrange the widgets horizontally
hbox = widgets.HBox([button, checkbox])

# Display the HBox
display(hbox)



# %%
import ipywidgets as widgets
from IPython.display import display

# Create some widgets
button1 = widgets.Button(description='Button 1')
button2 = widgets.Button(description='Button 2')
slider = widgets.FloatSlider(value=0.5, min=0, max=1, step=0.1, description='Slider')

# Create a VBox to arrange the widgets vertically
vbox = widgets.HBox([button1, button2, slider])

# Display the VBox
# display(vbox)


# %% slideshow={"slide_type": "slide"}
%debug

# %%
a.get_data("2000").keys()

# %%
a.get_data("2020-01")["forecast_origin"]

# %%
a.get_data("2020-01", dummy=True)["in_sample"].tail()

# %%
a.get_data("2020-01", dummy=True)["in_sample_forecast"].tail()

# %%
a.get_data("2020-01")["oos_forecast"].head()

# %%
a.get_data("2020-01", dummy=True)["mean"].loc["2020-01":"2021"]

# %%
