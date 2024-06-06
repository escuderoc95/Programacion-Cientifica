# Analysis and Simulation Data of a DAB Converter in Psim

## Overview

This project involves analyzing and simulating data from a Dual Active Bridge (DAB) converter using Psim. The DAB converter is a type of power converter commonly used for efficient energy transfer between two DC voltage sources. The focus of this simulation is on the transfer of energy from the low voltage side (V_L) to the high voltage side (V_H).

<div align="center">
  <img src="/taller3/project_root/results/figures/DAB.png" alt="convertidor"/>
</div>

<div align="center"> DAB converter and parameters  </div> 
<br>

## Objective

The objective of this simulation is to study the behavior and efficiency of the DAB converter under specific operating conditions, focusing on the phase shift. By analyzing the currents and voltages, we aim to better understand the converter performance, identify possible inefficiencies, and explore potential improvements.





## Parameters and Data Collected

- **Currents and Voltages**: The dataset includes various electrical parameters such as currents and voltages within the circuit.
- **Energy Transfer**: The primary objective is to analyze the energy transfer from V_L to V_H.
- **Phase Shift**: The analysis also considers the phase shift between the voltages and currents to understand its impact on the converter's performance.
- **Simulation Time**: The data was collected over a simulation period of 10 milliseconds (ms).

## Project Structure

<div align="center">
  <img src="/taller3/project_root/results/figures/lista-archivos.png" alt="convertidor"/>
</div>

<div align="center"> Project Structure  </div> 
<br>

## How to Run the Project

### Prerequisites

Ensure you have the necessary Python packages installed. You can install them using pip:

```sh
pip install pandas matplotlib fpdf scikit-learn

```
## Preprocessing Script
The preprocessing script loads the data, performs initial statistical analysis, normalizes the data, filters it within a specific time range, and performs a linear regression analysis.

## Analysis script 
Creates various plots and saves them, along with statistical analysis results, to a PDF file.

To run the analysis script:

- Open analysis.py in your preferred IDE or text editor.

- Execute the script. In PyCharm, you can press Shift + F10 or use the run button.

## Output results

After running the scripts, you should obtain the following outputs:

Figures: Saved in the results/figures/ directory.

- Area_chart.png
- Line_chart.png
- Time_series_plot.png
- Normalized_time_series_plot.png
- PDF Report: Saved as analysis_results.pdf in the results/ directory.

The PDF report includes:

- The first few rows of the DataFrame.
- Statistics of the filtered data.
- Plots of the time series, area chart, and line chart.
- Preprocessing results, including statistical analysis and data normalization.
- Results of the linear regression analysis.
