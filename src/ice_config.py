"""
ice_config.py
--------------------------------------------------------------------
Configuration file for visualization parameters used across the
Astro Ice Analysis repository. This allows centralized control of
aesthetic and scientific display options.
--------------------------------------------------------------------
"""

import numpy as np
import matplotlib.cm as cm

# ===============================================================
# GENERAL PLOT SETTINGS
# ===============================================================

PLOT_SETTINGS = {
    # === Color palette ===
    # Automatically generate N colors from a chosen colormap
    "COLORMAP": cm.viridis,      # You can change to cm.plasma, cm.inferno, etc.
    "NUM_COLORS": 10,            # Default number of colors (auto-adjusted if needed)

    # === Axis labels ===
    "XLABEL": "Wavenumber (cm$^{-1}$)",
    "YLABEL": "Absorbance",

    # === Axis limits ===
    # Set to None for automatic scaling
    "XLIM": (2145, 2130),        # Example zoom range
    "YLIM": (0.15, 0.35),

    # === Vertical reference lines ===
    # Wavenumbers (cm^-1) where vertical dashed lines should be drawn
    "REFERENCE_LINES": [21],  # SO₂, SO₃, etc.
    "REFERENCE_COLOR": "gray",
    "REFERENCE_STYLE": "--",
    "REFERENCE_ALPHA": 0.6,
}

# ===============================================================
# PHYSICAL CONVERSION SETTINGS
# ===============================================================

CONVERSION_SETTINGS = {
    "CONVERT_TO_COLUMN_DENSITY": True,   # If True, convert integrated area to N (cm^-2)
    "CONVERT_TO_MONOLAYERS": True,       # If True, also express result in ML
    "BAND_STRENGTH": 1.1e-17,            # CO stretch band at 2139 cm⁻¹
    "MONOLAYER_EQUIVALENCE": 1e15,       # molecules cm^-2 per monolayer
    "SAVE_INTEGRATION_PLOTS": True,  # Save each integration figure instead of showing
    "INTEGRATION_PLOTS_DIR": "results/integrations/",  # Folder for saving plots

}
