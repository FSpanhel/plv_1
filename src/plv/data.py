import datetime as dt

import pandas as pd

corona_begin = "2020-01-01"
max_inflation = "2023-02-01"

def load_verbraucherpreisindex(
    filter_columns: None | list[str] = ["vpi", "inflation"],
    start_date: None | dt.date = dt.date(1996, 1, 1)
):
    vpi = pd.read_csv(
        "data/verbraucherpreisindex.csv",
        delimiter=";", decimal=",", na_values="."
    ).convert_dtypes()

    # set dt as index
    month_mapping = dict(zip(
        vpi["2_Auspraegung_Label"].drop_duplicates().tolist(),
        range(1, 12 +1)
    ))

    _df = pd.DataFrame({
        "year": vpi["Zeit"],
        "month": vpi["2_Auspraegung_Label"].map(month_mapping),
        "day": 1
    })
    dt = pd.to_datetime(_df)
    dt = pd.DatetimeIndex(dt, freq="MS")
    vpi = vpi.set_index(dt)

    # compute inflation
    vpi["vpi"] = vpi["PREIS1__Verbraucherpreisindex__2020=100"].copy()
    vpi["inflation"] = (
        (vpi["vpi"] - vpi["vpi"].shift(12)) / vpi["vpi"].shift(12) * 100
    )
    vpi["monthly_Inflation"] = (
        (vpi["vpi"] - vpi["vpi"].shift(1)) / vpi["vpi"].shift(1) * 100
    )

    # filter columns
    if filter_columns:
        vpi = vpi[filter_columns].copy()

    # filter date
    if start_date:
        _slice = slice(start_date.strftime("%Y-%m-%d"), None)
        vpi = vpi.loc[_slice, :].copy()

    return vpi.squeeze()
