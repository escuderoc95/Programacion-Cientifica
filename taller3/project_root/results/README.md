# Results Directory

## Summary

This directory contains the output of the analysis and preprocessing scripts for the DAB converter simulation data. The results include statistical summaries, visualizations, and comprehensive PDF reports generated from the simulation data.


### figures/

This subdirectory contains various plots generated during the analysis. Each plot provides visual insights into different aspects of the simulation data.
**Time Series Plot (Vlow)**

This plot shows the voltage (Vlow) of the converter. The voltage fluctuates over time, with a general upward trend and periodic fluctuations. These fluctuations could be caused by factors such as changes in load or switching events in the converter.

**Area Chart (I_LK)**

This plot represents the current (I_LK) flowing through the inductor using an area chart. The area under the curve represents the total energy stored in the inductor. The current fluctuates over time, with periods of high and low current.

**Line Chart (VHigh)**

This plot shows the voltage (VHigh)of the converter. stabilizing the voltage at an average value of 36V.

The plots and the relationships between the variables, it appears that the data is separable to some extent. The time series plots of Vlow, I_LK, and VHigh each capture distinct aspects of the converter's behavior, and the relationships between these variables provide additional insights into the system dynamics.
However, it's important to note that the separability of the data may depend on the specific operating conditions and parameters of the DAB converter.

#### Files

- *area_chart.png*: An area chart showing the leakage current over time.
- *line_chart.png*: A line chart showing the high voltage, low voltage, and leakage current over time.
- *time_series_plot.png*: A time series plot showing the low voltage over time.
- *normalized_time_series_plot.png*: A time series plot showing the normalized low voltage over time.

### analysis_results.pdf

This PDF report compiles all the results from the analysis and preprocessing scripts. It includes:

- *Show data first 5 lines*: The first few rows of the DataFrame to provide a quick overview of the data structure.
- *Statistical Analysis*: Summary statistics for the filtered data within a specific time range.
- *Plots*: Visualizations including time series, area charts, and line charts.
- *Normalization Results*: Statistical summaries and plots of the normalized data.
- *Linear Regression Analysis*: Results of the regression model, including mean squared error (MSE) and coefficient of determination (R^2).

#### To analyze the results of separability where CV, IQR and Skewness are present, we explain as follows:

**Coefficient of variation (CV)**: A lower CV indicates a more clustered distribution and potentially higher separability, a CV below 0.1 is interpreted as “highly separable”, 0.1 to 0.2 as “moderately separable” and above 0.2 as “poorly separable”.

The CV value is approximately 0.098, lower than 0.1, indicating high separability. This suggests that the Vlow values are relatively stable with low relative variability compared to the mean.

**Interquartile range (IQR)**: represents the difference between the 75th and 25th percentiles of the data, indicating the dispersion of the median 50% of the data points. A non-zero IQR indicates some variability in the data, while a positive IQR indicates that there is variability in the middle 50% of the data.

**Skewness**: A skewness value close to 0 suggests a symmetric distribution, while a positive or negative skewness indicates a skewed distribution. A skewness value of approximately 0.793 indicates a distribution that is moderately skewed to the right. This means that there are more values at the lower end of the distribution and fewer at the upper end.

The Vlow variable demonstrates high consistency and stability, making it a good candidate for future analysis and possible control strategies in the simulation of the OBD converter. This provides a global understanding of the Vlow distribution.

#### The results of the MSE and R^2 are explained as follows: 

**Mean Squared Error (MSE)**:

The MSE obtained is 0.0015535278, which is a relatively low value. This indicates that the linear regression model performs well in terms of accuracy in predicting the value of "Vlow" from the independent variables ("Time", "I_LK", "VHigh", "VLK").

**Coefficient of Determination (R^2)**:

The R^2 obtained is 0.7097821756, which represents 71% of variance explained by the model. This means that 71% of the variations in "Vlow" can be explained by the independent variables. In general, an R^2 value greater than 0.5 is considered acceptable for a linear regression model.

Do the MSE and R^2 results suggest that the linear regression model has good predictive power and explains a significant amount of the variance in the target variable "Vlow". This indicates that the model may be useful for estimating the value of "Vlow" based on the values of the independent variables.
