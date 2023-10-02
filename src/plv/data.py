import pandas as pd

def load_verbraucherpreisindex(filter_columns: None | list[str] = ["vpi", "inflation"]):
    vpi = pd.read_csv(
        "data/verbraucherpreisindex.csv",
        delimiter=";", decimal=",", na_values="."
    ).convert_dtypes()

    # assign dt
    month_mapping = dict(zip(
        vpi["2_Auspraegung_Label"].drop_duplicates().tolist(),
        range(1, 12 +1)
    ))

    _df = pd.DataFrame({
        "year": vpi["Zeit"],
        "month": vpi["2_Auspraegung_Label"].map(month_mapping),
        "day": 1
    })
    vpi["dt"] = pd.to_datetime(_df)

    # compute inflation
    vpi["vpi"] = vpi["PREIS1__Verbraucherpreisindex__2020=100"].copy()
    vpi["inflation"] = (
        (vpi["vpi"] - vpi["vpi"].shift(12)) / vpi["vpi"].shift(12) * 100
    )
    vpi["monthly_Inflation"] = (
        (vpi["vpi"] - vpi["vpi"].shift(1)) / vpi["vpi"].shift(1) * 100
    )

    # set index
    vpi = vpi.set_index("dt")

    # filter columns
    if filter_columns:
        vpi = vpi[filter_columns].copy()

    return vpi
