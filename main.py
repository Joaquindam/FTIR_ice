"""
main.py
--------------------------------------------------------------------
Astro Ice Analysis — Infrared Spectral Visualization Tool

This script visualizes one or multiple infrared (FTIR) spectra from
astrochemical ice experiments. If the input path corresponds to a
single file, only that spectrum is plotted. If the path corresponds
to a directory, all spectra inside are plotted together for comparison.

Developed for the Astrophysical & Planetary Ices Laboratory
--------------------------------------------------------------------
Author: Joaquín Delgado Amar
Affiliation: [Centro de Astrobiología (CAB), CSIC-INTA, Spain]
Date: 2025-11-03
--------------------------------------------------------------------
"""

import os
import matplotlib.pyplot as plt
from src.ice_io import read_ir
from src.ice_plots import plot_ir
from src.ice_integrate import integrate_band, area_to_column_density
from src.ice_config import CONVERSION_SETTINGS as conv


# ===============================================================
#  CONFIGURATION SECTION
# ===============================================================

CONFIG = {
    # === Input path (file OR directory) ===
    # Provide either a file (e.g. "...\\spectrum.dpt")
    # or a folder (e.g. "...\\IR_data\\")
    "IR_PATH": r"C:\Users\Usuario\Documents\CAB\20251023_CO_irr_TPD/20251023_CO_irr_TPD_IR",

    # === Output options ===
    "SAVE_FIGURE": True,                    # Save instead of showing
    "OUTPUT_FILE": "infrared_overlay.png",   # Output filename

    # === Plot aesthetics ===
    "TITLE": "Infrared Spectra (FTIR)",
    "FIGSIZE": (7, 4),
    "LINE_WIDTH": 1.2,

    "INTEGRATION_RANGE": (2145, 2130),      # cm^-1
    "INTEGRATE_BANDS": True,
    "SHOW_INTEGRATION_PLOT": False,
    "SAVE_INTEGRATION_PLOTS": True,
    "INTEGRATION_PLOTS_DIR": "results",


}


# ===============================================================
#  MAIN FUNCTION
# ===============================================================

def main(cfg: dict):
    """
    Visualize one or multiple infrared (FTIR) spectra depending on the input path.
    """

    path = cfg["IR_PATH"]

    # --- Determine whether path is a file or directory ---
    if os.path.isfile(path):
        spectra_files = [path]
        print(f"📄 Single file detected: {os.path.basename(path)}")

    elif os.path.isdir(path):
        # Accept common IR file extensions
        spectra_files = [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.lower().endswith((".dpt", ".asc", ".txt"))
        ]
        print(f"Directory detected: found {len(spectra_files)} spectra in {path}")
    else:
        raise FileNotFoundError(f"❌ Invalid path: {path}")

    if not spectra_files:
        print("Error: No valid IR files found in the specified path.")
        return

    # --- Create figure ---
    fig, ax = plt.subplots(figsize=cfg["FIGSIZE"])
    ax.set_title(cfg["TITLE"])

   # --- Plot each spectrum ---
    for i, fpath in enumerate(spectra_files):
        try:
            x, y = read_ir(fpath)
            label = os.path.splitext(os.path.basename(fpath))[0]
            plot_ir(x, y, ax=ax, label=label, index=i, total=len(spectra_files))
        except Exception as e:
            print(f"Error reading {fpath}: {e}")


    # --- Formatting ---
    for line in ax.lines:
        line.set_linewidth(cfg["LINE_WIDTH"])

    plt.tight_layout()

    # --- Output ---
    if cfg["SAVE_FIGURE"]:
        plt.savefig(cfg["OUTPUT_FILE"], dpi=300)
        print(f" Figure saved as '{cfg['OUTPUT_FILE']}'")
    else:
        plt.show()

    if cfg.get("INTEGRATE_BANDS", False):
        x1, x2 = cfg["INTEGRATION_RANGE"]
        print(f"\n Integrating spectral feature between {x1} and {x2} cm⁻¹")

        for fpath in spectra_files:
            try:
                x, y = read_ir(fpath)
                area, baseline, mask = integrate_band(
                    x, y, x1, x2,
                    correct_baseline=True,
                    show_plot=cfg.get("SHOW_INTEGRATION_PLOT", False),
                    save_plot=cfg.get("SAVE_INTEGRATION_PLOTS", False),
                    save_path=cfg.get("INTEGRATION_PLOTS_DIR", "results/integrations/"),
                    filename=os.path.basename(fpath).replace(".dpt", "_integration.png")
                )
                print(f"  • {os.path.basename(fpath)}: area = {area:.6f}")

            except Exception as e:
                print(f" Error integrating {fpath}: {e}")

# ===============================================================
#  EXECUTION ENTRY POINT
# ===============================================================

if __name__ == "__main__":
    main(CONFIG)
