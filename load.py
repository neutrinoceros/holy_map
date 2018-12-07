from pathlib import Path
import pandas as pd

datadir = Path(__file__).parent.resolve() / "data"
def filepath(name:str) -> Path:
    return datadir / f"Holy Map - {name}.csv"
def load_sheet(name:str) -> pd.DataFrame:
    return pd.read_csv(
        filepath(name), index_col=0,
        dtype={"lambda min": float, "lambda max": float, "comment": str}
    )

data = {key: load_sheet(key) for key in {'ALMA', 'IR bands'}}

if __name__ == "__main__":
    for name, df in data.items():
        print(name)
        print('-' * len(name))
        print(df)
        print()

    print(data["ALMA"].T["Band 1"])
    print(type(data["ALMA"].T["Band 1"]["lambda min"]))
