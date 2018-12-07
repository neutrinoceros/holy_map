from pathlib import Path
import pandas as pd

from update import datadir, names

def load_sheet(name:str) -> pd.DataFrame:
    return pd.read_csv(
        datadir / f"{name}.csv",
        index_col=0,
        dtype={"lambda min": float, "lambda max": float, "comment": str}
    )

data = {name: load_sheet(name) for name in names}

if __name__ == "__main__":
    for name, df in data.items():
        print(name)
        print('-' * len(name))
        print(df)
        print()

    print(data["ALMA"].T["Band 1"])
    print(type(data["ALMA"].T["Band 1"]["lambda min"]))
