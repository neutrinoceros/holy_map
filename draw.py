import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.lines as mpllines
from scipy import constants

from load import load_sheet

# style
plt.style.use("seaborn")
sns.set(style="ticks")

# def
def mum2GHz(arr_mum:np.ndarray) -> np.ndarray:
    return(constants.c / arr_mum * 1e-3)

# main data struct
datasets = {
    'ALMA': sns.color_palette("Reds"),
    'IR-Bands': sns.color_palette("Blues"),
}


def main():
    fig, ax = plt.subplots()
    powlims = [0, 3]
    for sheetname, palette in datasets.items():
        ds = load_sheet(sheetname).T
        lc = palette[-1]
        offsets = [0.5 + 0.03*(-1)**n for n, _ in enumerate(ds)]

        for xkey, color, marker in zip(
                ["lambda min", "lambda max"],
                reversed(palette),
                ['o', '>']
        ):
            ax.scatter(
                x=ds.T[xkey],
                y=offsets,
                color=color,
                marker=marker,
                zorder=2
            )

        for n, band in enumerate(ds):
            wl = [ds[band]["lambda min"], ds[band]["lambda max"]]
            ax.plot(wl, offsets[n]*np.ones(2), color=lc, zorder=1)
            ax.annotate(s=band, xy=[wl[0], offsets[n]+0.02], fontsize=8)

        powlims[0] = min(powlims[0], np.log10(min(ds.T["lambda min"])))
        powlims[1] = max(powlims[1], np.log10(max(ds.T["lambda max"])))

    # to update
    ax.set_xlim(0.8*10**powlims[0], 1.2*10**powlims[1])
    ax.set_ylim(0, 1)
    ax.set_xlabel(r"$\lambda$ [µm]")

    # secondary x axis for frequencies
    axb = ax.twiny()
    axb.set_xlim(mum2GHz(np.array(ax.get_xlim())))
    axb.set_xlabel(r"$\nu$ [GHz]")

    # scaling
    for a in (ax, axb):
        a.set_xscale("log")

    return fig


# script
if __name__ == '__main__':
    fig = main()
    fig.savefig("output.pdf")
