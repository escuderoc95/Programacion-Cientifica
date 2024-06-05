import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
from preprocessing import load_and_process_data  # Import the preprocessing function

# Path to the text file
data_file = os.path.join(os.path.dirname(__file__), '../data/simulacion_VLVHresistencia110.txt')

# Load and process data
df, preprocessing_results, normalized_data, normalized_results, regression_results = load_and_process_data(data_file)

# Perform basic analysis (show first rows of DataFrame)
head_data = df.head()

# Filter data in a specific time range
filtered_data = df[(df['Time'] >= 0.0060) & (df['Time'] <= 0.0080)]

# Statistical description for each column
statistics = filtered_data.describe()

# Results/figures directory if it doesn't exist
results_dir = os.path.join(os.path.dirname(__file__), '../results')
figures_dir = os.path.join(results_dir, 'figures')
os.makedirs(figures_dir, exist_ok=True)

# Save figures in the figures directory

# Time series plot
plt.figure()
plt.plot(df['Time'], df['Vlow'])
plt.xlabel('Time [s]')
plt.ylabel('Vlow [V]')
plt.title('Time Series: Time vs Vlow')
time_series_plot = os.path.join(figures_dir, 'time_series_plot.png')
plt.savefig(time_series_plot)
plt.close()

# Area chart
plt.figure()
plt.fill_between(df['Time'], df['I_LK'])
plt.title('Area Chart')
plt.xlabel('Time [s]')
plt.ylabel('I_LK [A]')
plt.legend(['I_LK [A]'])
area_chart = os.path.join(figures_dir, 'area_chart.png')
plt.savefig(area_chart)
plt.close()

# Line chart
plt.figure()
df[['Time', 'VHigh', 'Vlow', 'I_LK']].plot(x='Time', title='Line Chart')
line_chart = os.path.join(figures_dir, 'line_chart.png')
plt.savefig(line_chart)
plt.close()

# Time series plot with normalized data
plt.figure()
plt.plot(normalized_data['Time'], normalized_data['Vlow'])
plt.xlabel('Time')
plt.ylabel('Vlow')
plt.title('Time Series: Time vs Vlow (Normalized)')
normalized_time_series_plot = os.path.join(figures_dir, 'normalized_time_series_plot.png')
plt.savefig(normalized_time_series_plot)
plt.close()

class PDF(FPDF):
    """
    PDF class to create a report with analysis results.

    This class extends FPDF to create a custom PDF with headers, footers,
    chapter titles, and bodies of text.
    """

    def header(self):
        """Set the header of the PDF."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Simulation Analysis Results', 0, 1, 'C')

    def footer(self):
        """Set the footer of the PDF."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        """Add a chapter title to the PDF.

        Args:
            title (str): The title of the chapter.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        """Add a body of text to the PDF.

        Args:
            body (str): The body text to add.
        """
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create the PDF
pdf = PDF()
pdf.add_page()

# Add title and description
pdf.chapter_title('Show data first 5 lines')
pdf.chapter_body(head_data.to_string(index=False))

# Statistics of filtered data to the PDF
pdf.chapter_title('Statistics of Filtered Data')
pdf.chapter_body(statistics.to_string())

# Preprocessing results to the PDF
pdf.chapter_title('Preprocessing Results')
preprocessing_text = (f"Mean of Vlow: {preprocessing_results['vlow_mean']}\n"
                      f"Standard deviation of Vlow: {preprocessing_results['vlow_std']}\n"
                      f"Coefficient of variation of Vlow: {preprocessing_results['vlow_cv']}\n"
                      f"{preprocessing_results['cv_interpretation']}\n"
                      f"Interquartile Range (IQR) of Vlow: {preprocessing_results['vlow_iqr']}\n"
                      f"Skewness of Vlow: {preprocessing_results['vlow_skewness']}\n"
                      f"{preprocessing_results['iqr_skewness_interpretation']}")
pdf.chapter_body(preprocessing_text)

# Normalized data results to the PDF
pdf.chapter_title('Normalized Data - Statistics of Filtered Data')
pdf.chapter_body(normalized_results['filtered_statistics'].to_string())

pdf.chapter_title('Quantitative Separability Analysis of Normalized Data')
normalized_text = (f"Mean of Vlow: {normalized_results['vlow_mean']}\n"
                   f"Standard deviation of Vlow: {normalized_results['vlow_std']}\n"
                   f"Coefficient of variation of Vlow: {normalized_results['vlow_cv']}\n"
                   f"{normalized_results['cv_interpretation']}")
pdf.chapter_body(normalized_text)

# linear regression results to the PDF
pdf.chapter_title('Linear Regression Results')
regression_text = (f"Mean Squared Error (MSE): {regression_results['mse']}\n"
                   f"Coefficient of Determination (R^2): {regression_results['r2']}")
pdf.chapter_body(regression_text)

# PDF in the results directory
pdf_output = os.path.join(results_dir, 'analysis_results.pdf')
pdf.output(pdf_output)

print(f'Results saved to {pdf_output}')

