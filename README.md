# FTIR-Ice

**FTIR-Ice** is a Python toolkit for analyzing *infrared (FTIR)* spectra of astrophysical ices.  
It provides routines to read, visualize and integrate spectral features,  
and to convert them into physical quantities such as column densities or monolayers.

---

## Features

- Read and plot single or multiple FTIR spectra (`.asc`, `.dpt`, `.txt`)
- Automatic color palette and reference wavenumber markers
- Integration of spectral bands with local baseline correction
- Conversion of integrated areas into  
  - Column densities (molecules cm⁻²)  
  - Monolayers (ML)
- Optional automatic saving of plots and integration figures

---

## Project Structure

    ftir_ice/
    ├── main.py # Main entry point
    ├── src/
    │ ├── ice_io.py # Read FTIR data files
    │ ├── ice_plots.py # Plotting utilities
    │ ├── ice_integrate.py # Band integration + visualization
    │ └── ice_config.py # Global configuration (limits, colors, bands…)
    ├── results/ # (Optional) Output folder for plots
    ├── requirements.txt
    └── README.md

---

## Installation

1. **Clone the repository**
   
   git clone https://github.com/joaquindam/ftir_ice.git
   cd ftir_ice

2. **(Optional) Create a virtual environment**

    python -m venv venv
    source venv/bin/activate   # macOS / Linux
    venv\Scripts\activate      # Windows

3. **Install dependencies**

    pip install -r requirements.txt

---

## Usage

Edit the configuration block at the top of **`main.py`** to define:

- The path to a single FTIR spectrum file or to a folder containing multiple spectra.
- Whether to **display** the plots interactively or **save** them to disk.
- The **integration range** for the absorption band of interest.
- Whether to **convert** the integrated area to column density or monolayers.

Then, adjust **`src/ice_config.py`** to specify:

- Plot axis limits and reference (vertical) lines.
- Band strength values (`A`, in cm·molecule⁻¹) for the molecular species.
- Conversion factors to monolayers, if applicable.

Then run:

    python main.py

---

## Example Configuration

    CONFIG = {
        "IR_PATH": r"C:\\Users\\Usuario\\Documents\\CAB\\20251023_CO_irr_TPD\\20251023_CO_irr_TPD_IR",
        "SAVE_FIGURE": True,
        "OUTPUT_FILE": "infrared_overlay.png",
        "INTEGRATE_BANDS": True,
        "INTEGRATION_RANGE": (2155, 2130),
        "SHOW_INTEGRATION_PLOT": False,
        "SAVE_INTEGRATION_PLOTS": True,
        "INTEGRATION_PLOTS_DIR": "results/integrations/",
    }

---

## Example output

    Integrating spectral feature between 2155 and 2130 cm⁻¹
        • 20251023_145309_ventana_co_dep_10min_irr_15min: area = 0.00235, N = 4.92e14 molec cm⁻² (0.49 ML)
    Saved integration plot: results/integrations/20251023_145309_integration.png

---

## Author

    Joaquín Delgado Amar
    Centro de Astrobiología (CAB), CSIC-INTA, Spain

---

## License

This project is distributed under the MIT License.
