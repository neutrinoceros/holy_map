### Goal

Draw a gigantic vizualization compiling data from spectral bands used in ppds observations.

### data location

[Google Sheet data](https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-O2uILc5idASTrYexoOqK_elcSmK1f266aDtfsU5Rd9FoWAXrbH8z4kuouNvkk5LtHMCziL50BEYX/pubhtml)

### Content

- `update.py` lets you update the data files (sheet names have to be written manually)
- `load.py` is a demo of how we load the data back into `pandas`
- `draw.py` main script, draws the image file `output.pdf`

### Used tools

`Google sheet` as a way to store shared data easily convertible to `.csv`

Python3:
- `pandas` : retreive data sheets as `.csv` files
- `matplotlib` + `seaborn` : graphics plotting


