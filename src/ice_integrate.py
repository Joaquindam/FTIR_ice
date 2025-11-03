"""
ice_integrate.py
--------------------------------------------------------------------
Integration utilities for infrared spectra.

Provides numerical integration of spectral features (absorption or
emission lines) over a selected wavenumber range, correcting for the
local baseline to yield a physically meaningful area.

Includes optional visualization of the integrated region.
--------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
import os


def integrate_band(
    x, y,
    x_min, x_max,
    correct_baseline=True,
    ax=None,
    show_plot=False,
    save_plot=False,
    save_path=None,
    filename=None
):
    """
    Integrate a spectral feature between x_min and x_max.

    If `show_plot` is True, display the integrated region.
    If `save_plot` is True, save the figure to `save_path` (requires filename).
    """

    x = np.asarray(x)
    y = np.asarray(y)

    # Handle inverted IR axis
    if x[0] > x[-1]:
        mask = (x <= x_min) & (x >= x_max)
    else:
        mask = (x >= x_min) & (x <= x_max)

    if np.sum(mask) < 3:
        raise ValueError(
            f"Integration region [{x_min}, {x_max}] outside data range "
            f"({x.min():.1f}–{x.max():.1f}) or too narrow."
        )

    x_region = x[mask]
    y_region = y[mask]

    # Fit baseline
    if correct_baseline:
        slope = (y_region[-1] - y_region[0]) / (x_region[-1] - x_region[0])
        intercept = y_region[0] - slope * x_region[0]
        baseline = slope * x_region + intercept
        y_corrected = y_region - baseline
    else:
        baseline = np.zeros_like(y_region)
        y_corrected = y_region

    # Integrate
    if x_region[0] > x_region[-1]:
        area = simpson(y_corrected[::-1], x_region[::-1])
    else:
        area = simpson(y_corrected, x_region)

    # Visualization
    if show_plot or save_plot:
        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(x, y, "k-", lw=1.2)
            ax.invert_xaxis()
        ax.plot(x_region, baseline, "r--", lw=1.2, label="Baseline")
        ax.fill_between(x_region, y_region, baseline, color="tab:blue", alpha=0.3, label="Integrated Area")
        ax.legend(frameon=False)
        ax.set_xlim(max(x_min, x_max), min(x_min, x_max))
        ax.set_ylim(0, max(y_region)*1.5)
        ax.set_xlabel("Wavenumber (cm$^{-1}$)")
        ax.set_ylabel("Absorbance")
        plt.tight_layout()

        if save_plot and save_path is not None and filename is not None:
            os.makedirs(save_path, exist_ok=True)
            full_path = os.path.join(save_path, filename)
            plt.savefig(full_path, dpi=300)
            plt.close()
            print(f" Saved integration plot: {full_path}")
        elif show_plot:
            plt.show()

    return area, baseline, mask

def area_to_column_density(area, band_strength, in_monolayers=False):
    """
    Convert integrated absorbance area to column density or monolayers.

    Parameters
    ----------
    area : float
        Integrated band area (cm^-1 * absorbance)
    band_strength : float
        Band strength in cm/molecule
    in_monolayers : bool, optional
        If True, return result in monolayers instead of cm^-2.

    Returns
    -------
    N : float
        Column density [molec/cm^2] or monolayers (ML)
    """

    N_cm2 = 2.303 * area / band_strength  # convert to column density
    if in_monolayers:
        return N_cm2 / 1e15
    else:
        return N_cm2


