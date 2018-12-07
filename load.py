from pathlib import Path
import pandas as pd

datadir = Path(__file__).parent.resolve() / "data"
def filepath(name:str) -> Path:
    return datadir / f"Holy Map - {name}.csv"
def csvdat(name:str) -> pd.DataFrame:
    return pd.read_csv(filepath(name), index_col=0)

data = {key: csvdat(key) for key in {'ALMA', 'IR bands'}}

if __name__ == "__main__":
    for name, df in data.items():
        print(name)
        print('-' * len(name))
        print(df)
        print()

    print(data["ALMA"].T["Band 1"])
    print(type(data["ALMA"].T["Band 1"]["lambda min"]))
