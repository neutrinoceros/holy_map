#!/usr/bin/env python3
import pathlib
import pandas as pd

datadir = pathlib.Path(__file__).parent.resolve() / "data"
dataurl = r"https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-O2uILc5idASTrYexoOqK_elcSmK1f266aDtfsU5Rd9FoWAXrbH8z4kuouNvkk5LtHMCziL50BEYX/pubhtml#"
names = ("ALMA", "IR-Bands")

if __name__ == "__main__":
    raw_data = pd.read_html(dataurl, encoding="utf-8", index_col=1, header=0)
    data = {name: df.drop(["1"], 1) for name, df in zip(names, raw_data)}

    for name, df in data.items():
        file = datadir / f"{name}.csv"
        print(f"Writing {file}")
        df.to_csv(file)
