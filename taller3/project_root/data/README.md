# Data Directory

## Summary

This directory contains the raw simulation data for the DAB converter analysis project. The data is essential for performing statistical analysis, normalization, visualization, and regression modeling as part of the project.

## Files

### `simulacion_VLVHresistencia110.txt`

This text file contains the raw simulation data for the DAB converter. The data is tab-delimited and includes the following columns:

- **Time**: Time in seconds (s)
- **I_LK**: Leakage current in amperes (A)
- **VHigh**: High voltage side voltage in volts (V)
- **Vlow**: Low voltage side voltage in volts (V)
- **VLK**: Leakage voltage in volts (V)

## Data Description

The simulation data captures the behavior of the DAB converter over a period of 10 milliseconds (ms). The primary focus is on analyzing the transfer of energy from the low voltage side (V_L) to the high voltage side (V_H), considering the phase shift between voltages and currents.

### Columns

1. **Time**: This column records the simulation time in seconds.
2. **I_LK**: This column records the leakage current in amperes.
3. **VHigh**: This column records the voltage on the high voltage side in volts.
4. **Vlow**: This column records the voltage on the low voltage side in volts.
5. **VLK**: This column records the leakage voltage in volts.

## How to Use the Data

### Loading the Data

To load the data into a pandas DataFrame for analysis, use the following code:

```python
import pandas as pd
import os

data_file = os.path.join(os.path.dirname(__file__), 'simulacion_VLVHresistencia110.txt')
df = pd.read_csv(data_file, delimiter='\t', names=['Time', 'I_LK', 'VHigh', 'Vlow', 'VLK'])
