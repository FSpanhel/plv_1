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

# %% [markdown]
# # Load

# %%
data = load_verbraucherpreisindex(filter_columns=None)
data = data[data["inflation"].notna()].copy()

# %% [markdown]
# # Plot

# %%
import matplotlib.pyplot as plt

# %%
plt.plot(data.index, data["inflation"])

# %% [markdown]
# # Investigate PACF

# %%
filter_ = slice("1995", "2020")

# %%
data.loc[filter_]

# %%
y = data.loc[filter_, "inflation"]

# %%
from statsmodels.tsa.stattools import pacf
import statsmodels.api as sm
import matplotlib.pyplot as plt
y
sm.graphics.tsa.plot_pacf(y, lags=40, method="ywm")
plt.show()
p = pacf(y)
pd.Series(p, index=range(1, len(p) +1 ))
