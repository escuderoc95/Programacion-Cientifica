# Algorithms Directory

## Overview

This directory contains scripts for analyzing and preprocessing the data from the DAB converter simulation. These scripts perform various tasks such as statistical analysis, data normalization, and plotting results. Below is a detailed description of each script and the algorithms they use.

## Files

### `analysis.py`

This script performs the following tasks:

1. **Load Data**:
   - Reads the simulation data from a text file.

2. **Initial Data Analysis**:
   - Displays the first few rows of the data.

3. **Statistical Analysis**:
   - Calculates and displays basic statistics for the filtered data within a specific time range.

4. **Data Visualization**:
   - Creates and saves various plots including time series, area charts, and line charts.

5. **Save Results**:
   - Compiles all the results into a PDF report.

#### Algorithms and Functions

- **Loading Data**:
  ```python
  df = pd.read_csv(data_file, delimiter='\t', names=['Time', 'I_LK', 'VHigh', 'Vlow', 'VLK'])

#### initial Data Analysis:
- head_data = df.head()

#### Statistical Analysis:
- filtered_data = df[(df['Time'] >= 0.0060) & (df['Time'] <= 0.0080)]
statistics = filtered_data.describe()

#### Data Visualization:
- plt.plot(df['Time'], df['Vlow'])
- plt.fill_between(df['Time'], df['I_LK'])
- df[['Time', 'VHigh', 'Vlow', 'I_LK']].plot(x='Time')

## Preprocessing data 

This script performs the following tasks:

1. Load Data:
- Reads the simulation data from a text file.

2. Initial Data Analysis:
- Calculates mean, standard deviation, coefficient of variation, interquartile range, and skewness of Vlow.

3. Normalization:
- Normalizes the data using MinMaxScaler.

4. Statistical Analysis on Normalized Data:
- Filters the normalized data within a specific time range and calculates statistics.

5. Linear Regression Analysis:
- Splits the data into training and testing sets, trains a linear regression model, and evaluates its performance.