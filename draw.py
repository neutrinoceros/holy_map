#!/usr/bin/env python3
from collections import namedtuple
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
YLIM = (0, 1)

def draw_span(ax, xmin:float, xmax:float, y:float=0.8, epsy:float=0.02, name:str="") -> None:
    # arrow
    ax.annotate("", xytext=(xmin, y), xy=(xmax, y), arrowprops=dict(arrowstyle="<|-|>", color="black"))
    # associated name
    if name:
        ax.annotate(f"   {name}", xytext=(xmin, y+epsy), xy=(xmax, y+epsy))

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

    # add visible spectrum
    xblue = 0.4
    xred  = 0.8
    xv = np.linspace(xblue, xred, 1000)
    yv = np.linspace(*YLIM, 2)
    xg, yg = np.meshgrid(xv, yv)
    ax.pcolormesh(xg, yg, xg, cmap="gist_rainbow_r", zorder=0, alpha=0.5)

    # over plot basic domains
    Domain = namedtuple("Domain", "name xmin xmax yoffset")
    domains = [
        Domain("infrared", 0.75, 300, 0.8),
        Domain("submillimeter", 1e2, 1e3, 0.7),
        Domain("millimeter", 1e3, 1e4, 0.7),
    ]
    for d in domains:
        draw_span(ax, xmin=d.xmin, xmax=d.xmax, y=d.yoffset, name=d.name)
    xredest = max([d.xmax for d in domains])

    # to update
    ax.set_xlim(min(xblue, 0.8*10**powlims[0]), max(1.2*10**powlims[1], xredest))
    ax.set_ylim(*YLIM)
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
    import argparse
    aparser = argparse.ArgumentParser()
    aparser.add_argument("-i", "--interactive", action="store_true", default=False)
    args = aparser.parse_args()

    fig = main()

    if args.interactive:
        plt.ion()
        plt.show()
        plt.ioff()
        input("<Enter> to quit and save    ")
    fig.savefig("output.pdf")
