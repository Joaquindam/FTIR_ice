import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np
from src.ice_config import PLOT_SETTINGS

def plot_ir(x, y, ax=None, label="IR spectrum", index=0, total=1):
    """
    Plot an infrared (FTIR) spectrum with optional axis limits and reference lines.
    If multiple spectra are plotted, color is automatically assigned from a colormap.
    """

    # --- Create figure if not provided ---
    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 4))

    # --- Handle color palette ---
    cmap = PLOT_SETTINGS["COLORMAP"]
    num_colors = max(PLOT_SETTINGS["NUM_COLORS"], total)
    color = cmap(index / (num_colors - 1)) if total > 1 else "k"

    # --- Plot the spectrum ---
    ax.plot(x, y, color=color, lw=1.5, label=label)

    # --- Axis labels ---
    ax.set_xlabel(PLOT_SETTINGS["XLABEL"])
    ax.set_ylabel(PLOT_SETTINGS["YLABEL"])

    # --- Axis limits ---
    if PLOT_SETTINGS["XLIM"] is not None:
        ax.set_xlim(PLOT_SETTINGS["XLIM"])
    if PLOT_SETTINGS["YLIM"] is not None:
        ax.set_ylim(PLOT_SETTINGS["YLIM"])

    # --- Reference lines ---
    for nu in PLOT_SETTINGS["REFERENCE_LINES"]:
        ax.axvline(
            x=nu,
            color=PLOT_SETTINGS["REFERENCE_COLOR"],
            linestyle=PLOT_SETTINGS["REFERENCE_STYLE"],
            alpha=PLOT_SETTINGS["REFERENCE_ALPHA"],
            lw=1,
        )

    # --- Legend ---
    ax.legend(frameon=False, fontsize=8, loc="best")

    # --- Invert X axis (for IR spectra) ---
    return ax

def plot_qms(time, data, headers, masses, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    for m in masses:
        m_str = f"{m:.2f}"
        # Buscar columna que contenga el valor m/z solicitado
        for i, h in enumerate(headers):
            if m_str in h:
                ax.plot(time / 60.0, data[:, i], label=f"m/z {h}")
                break
    ax.set_xlabel("Elapsed time (min)")
    ax.set_ylabel("QMS Signal (A)")
    ax.legend(frameon=False)
    return ax
