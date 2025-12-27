# Nanofluid Automotive Radiator Heat Transfer Study

This repository contains the core data and analysis scripts for the research paper:

**"Enhancement of Heat Transfer in Automotive Radiators Using Al2O3-Water Nanofluids: Experimental and Numerical Analysis"**

*Journal of Dispersion Science and Technology*, 2023.  
[DOI: 10.1080/01932691.2023.1234567](https://doi.org/10.1080/01932691.2023.1234567)

## Project Summary

The study investigates the performance of Al2O3-water nanofluids as coolants in automotive radiators. Experiments were conducted to measure heat transfer enhancement and pressure drop across a range of nanoparticle concentrations (0.1–2.0 %) and flow rates (2–10 L/min). The data and scripts provided here allow other researchers to reproduce the key findings and build upon the work.

## Repository Structure

- `data/experimental_results.csv` – anonymized experimental measurements. Columns:
  - `TestID` – unique identifier for each test run
  - `BaseFluid` – base fluid (e.g., "Water", "EG‑30%")
  - `Nanoparticle` – nanoparticle type (e.g., "Al2O3", "TiO2")
  - `Concentration_percent` – nanoparticle concentration (weight %)
  - `FlowRate_L/min` – coolant flow rate (L · min⁻¹)
  - `InletTemp_C` – inlet temperature (°C)
  - `OutletTemp_C` – outlet temperature (°C)

- `scripts/plot_heat_transfer.py` – a Python script that loads the CSV file and defines a starter function `plot_effectiveness_vs_concentration(data_file)` for visualizing the effect of nanoparticle concentration on thermal effectiveness.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/shuchua39/nanofluid-radiator-reproducibility.git
   ```
2. Install the required Python packages (pandas, matplotlib).
3. Run the script, pointing it to the data file:
   ```bash
   cd scripts
   python plot_heat_transfer.py
   ```

## License

This work is made available under the [MIT License](LICENSE).