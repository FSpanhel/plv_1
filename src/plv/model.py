from __future__ import annotations

import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AutoReg
from plv.data import max_inflation


class CrisisDummy:
    def __init__(self, start: str = "2020", end: str = max_inflation):
        "The Dummy is 1 if the index is between *start* and *end*."
        self.start = start
        self.end = end
    def get(self, lb: str = '1996-01-01', ub: str = '2049-12-01') -> pd.Series:
        "*lb* and *ub* determine the start and end of the index of the returned value"
        dummy = pd.Series(0, index=pd.date_range(start=lb, end=ub, freq='MS'))
        dummy.loc[self.start:self.end] = 1
        return dummy


class AR1:
    def __init__(
            self,
        ):
        self.lags = [1]
        self.dummy = None
        self._set_exog_to_None()
        self.auto_reg = None
        self.res = None
        self.params = None
        self.mean = None

    '''
    def __str__(self) -> str:
        if self.dummy is None:
            return f"AR({self.lags})"
        else:
            return f"AR({self.lags})
    '''

    def _set_exog_to_None(self):
        self._exog = None
        self.exog = None
        self.exog_oos = None
        self._exog_oos = None

    def _get_params(self):
        params = self.res._params
        res = {"constant": params[0], "a": params[1]}
        if len(params) == 3:
            res["dummy"] = params[2]
        return res

    '''
        def _get_mean(self, start: str, end: str):
            "Mean without dummy"
            mean_ar = self.params["constant"] / (1 - self.params["a"])
            if self.dummy is None:
                offset = 0
            else:
                offset = self.params["dummy"]
            return mean_ar + self.dummy.get(start, end) * offset
    '''
    
    def get_mean(self, start: str, end: str):
        "Mean without dummy"
        if abs(self.params["a"]) >= 1:
            return pd.Series(np.nan, pd.date_range(start=start, end=end, freq='MS'))
        denom = (1 - self.params["a"])
        if self.dummy is None:
            nom = pd.Series(
                self.params["constant"],
                index=pd.date_range(start=start, end=end, freq='MS')
            )
        else:  # E[Y_t|D] = (c+ E[D|D])/(1-a)
            nom = (
                self.params["constant"]
                + self.params["dummy"] * self.dummy.get(start, end)
            )
        return nom / denom

    def fit(self, ts: pd.Series, dummy: None | CrisisDummy = None):
        self.ts = ts
        self.dummy = dummy
        if self.dummy is None:
            self._set_exog_to_None()
        else:
            self.exog = dummy.get(ts.index[0], ts.index[-1])
            self._exog = self.exog.to_numpy()
        self.auto_reg = AutoReg(
            ts.to_numpy(), lags=self.lags, seasonal=False, exog=self._exog,
        )
        self.res = self.auto_reg.fit()
        self.params = self._get_params()
        # self.mean = self._get_mean()

    def oos_forecast(
        self, forecast_horizon: int = 1, forecast_date: str = None
    ) -> pd.Series:
        if self.res is None:
            raise ValueError("Call `fit` before.")

        if self.dummy is not None:
            self.exog_oos = self.dummy.get(
                lb=self.ts.index[-1] + pd.DateOffset(months=1),
                ub=self.ts.index[-1] + pd.DateOffset(months=forecast_horizon)
            )
            self._exog_oos = self.exog_oos.to_numpy()

        # import pdb; pdb.set_trace()

        if forecast_date:
            index = pd.date_range(self.ts.index[0], forecast_date, freq="MS")
            end = len(index)
        else:
            end = len(self.ts) + forecast_horizon - 1

        forecast_values = self.res.predict(
            start=0,
            end=end,
            # dynamic=True leads strange results    
            dynamic=False,
            exog=self._exog,
            exog_oos=self._exog_oos,
        )

        index = pd.date_range(
            start=self.ts.index[0], periods=len(forecast_values), freq='MS'
        )
        forecast = pd.Series(forecast_values, index=index)
        return forecast
    
    def get_is_and_oos_forecast(
            self, forecast_horizon: int = 1
        ) -> dict[str, pd.Series]:
        forecast = self.oos_forecast(forecast_horizon)
        dc = {}
        dc["is"] = forecast.loc[:self.ts.index[-1]]
        dc["oos"] = forecast.loc[self.ts.index[-1] + pd.DateOffset(months=1):]
        return dc
