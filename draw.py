import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.lines as mpllines
from scipy import constants

# style
plt.style.use("seaborn")
sns.set(style="ticks")
LINECOLOR = sns.color_palette("Blues")[-1]

# def
def mum2GHz(arr_mum:np.ndarray) -> np.ndarray:
    return(constants.c / arr_mum * 1e-3)

# data
# change me
from load import data
# ====================

almadat = data["ALMA"].T
sensitivity = [0.5 + 0.03*(-1)**n for n, _ in enumerate(almadat)] #fake

fig, ax = plt.subplots()

for xkey, color, marker in zip(
        ["lambda min", "lambda max"],
        reversed(sns.color_palette("Blues")),
        ['o', '>']
):
    ax.scatter(
        x=data["ALMA"][xkey],
        #y=Y0*np.ones(data["ALMA"].shape[0]) + SGN*yoffset,
        y=sensitivity,
        color=color,
        marker=marker,
        zorder=2
    )

for n, band in enumerate(almadat):
    wl = [almadat[band]["lambda min"], almadat[band]["lambda max"]]
    ax.plot(
        wl,
        sensitivity[n]*np.ones(2),
        color=LINECOLOR,
        zorder=1
    )
    ax.annotate(s=band, xy=[wl[0], sensitivity[n]+0.02], fontsize=8)

ax.set_xlim(
    0.8*min(data["ALMA"]["lambda min"]),
    1.2*max(data["ALMA"]["lambda max"])
)
ax.set_ylim(0, 1)
ax.set_xlabel(r"$\lambda$ [µm]")

# secondary x axis for frequencies
axb = ax.twiny()
axb.set_xlim(mum2GHz(np.array(ax.get_xlim())))
axb.set_xlabel(r"$\nu$ [GHz]")

# scaling
for a in (ax, axb):
    a.set_xscale("log")

# save
fig.savefig("output.pdf")
