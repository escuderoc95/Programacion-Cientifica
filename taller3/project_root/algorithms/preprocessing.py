import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Path to the text file
data_file = os.path.join(os.path.dirname(__file__), '../data/simulacion_VLVHresistencia110.txt')

def load_and_process_data(file_path):
    """
    Load and process the data from the given file path.

    This function reads the data from a text file, performs initial statistical analysis,
    normalizes the data, filters it within a specific time range, and performs a linear
    regression analysis.

    Args:
        file_path (str): Path to the text file containing the data.

    Returns:
        tuple: A tuple containing the following elements:
            - DataFrame with the original data.
            - Dictionary with preprocessing results.
            - DataFrame with normalized data.
            - Dictionary with normalized data results.
            - Dictionary with regression results.
    """
    df = pd.read_csv(file_path, delimiter='\t', names=['Time', 'I_LK', 'VHigh', 'Vlow', 'VLK'])

    # Calculate the necessary statistics
    vlow_mean = df['Vlow'].mean()
    vlow_std = df['Vlow'].std()
    vlow_cv = vlow_std / vlow_mean
    vlow_iqr = df['Vlow'].quantile(0.75) - df['Vlow'].quantile(0.25)
    vlow_skewness = df['Vlow'].skew()

    preprocessing_results = {
        'vlow_mean': vlow_mean,
        'vlow_std': vlow_std,
        'vlow_cv': vlow_cv,
        'vlow_iqr': vlow_iqr,
        'vlow_skewness': vlow_skewness,
        'cv_interpretation': 'Vlow is highly separable.' if vlow_cv < 0.1 else
                             'Vlow is moderately separable.' if vlow_cv < 0.2 else
                             'Vlow is poorly separable.',
        'iqr_skewness_interpretation': 'Vlow is moderately separable.' if vlow_iqr > 0 and abs(vlow_skewness) < 1 else
                                       'Vlow is poorly separable.' if vlow_iqr > 0 and abs(vlow_skewness) >= 1 else
                                       'Insufficient variability to assess separability.'
    }

    # Normalize the data
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(df[['Time', 'I_LK', 'VHigh', 'Vlow', 'VLK']])
    normalized_data = pd.DataFrame(normalized_data, columns=['Time', 'I_LK', 'VHigh', 'Vlow', 'VLK'])

    # Filter normalized data within a specific time range
    filtered_normalized_data = normalized_data[(normalized_data['Time'] >= 0.0060) & (normalized_data['Time'] <= 0.0080)]
    normalized_statistics = filtered_normalized_data.describe()

    # Separability analysis using normalized data
    normalized_vlow_mean = normalized_data['Vlow'].mean()
    normalized_vlow_std = normalized_data['Vlow'].std()
    normalized_vlow_cv = normalized_vlow_std / normalized_vlow_mean

    normalized_results = {
        'filtered_statistics': normalized_statistics,
        'vlow_mean': normalized_vlow_mean,
        'vlow_std': normalized_vlow_std,
        'vlow_cv': normalized_vlow_cv,
        'cv_interpretation': 'Vlow is highly separable.' if normalized_vlow_cv < 0.1 else
                             'Vlow is moderately separable.' if normalized_vlow_cv < 0.2 else
                             'Vlow is poorly separable.'
    }

    # Normalize for new analysis
    df[['Time', 'I_LK', 'VHigh', 'VLK']] = scaler.fit_transform(df[['Time', 'I_LK', 'VHigh', 'VLK']])

    # Split data into training and testing sets
    X = df[['VHigh', 'VLK']]  # Independent variables
    y = df['Vlow']  # Dependent variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the linear regression model
    regression_model = LinearRegression()
    regression_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = regression_model.predict(X_test)

    # Calculate mean squared error (MSE) and coefficient of determination (R^2)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    regression_results = {
        'mse': mse,
        'r2': r2
    }

    return df, preprocessing_results, normalized_data, normalized_results, regression_results

if __name__ == "__main__":
    df, preprocessing_results, normalized_data, normalized_results, regression_results = load_and_process_data(data_file)
    print("Data loaded and processed successfully.")
    print(f"Mean of Vlow: {preprocessing_results['vlow_mean']}")
    print(f"Standard deviation of Vlow: {preprocessing_results['vlow_std']}")
    print(f"Coefficient of variation of Vlow: {preprocessing_results['vlow_cv']}")
    print(preprocessing_results['cv_interpretation'])
    print(f"Interquartile Range (IQR) of Vlow: {preprocessing_results['vlow_iqr']}")
    print(f"Skewness of Vlow: {preprocessing_results['vlow_skewness']}")
    print(preprocessing_results['iqr_skewness_interpretation'])
    print("Normalized Data - Statistics of filtered data:")
    print(normalized_results['filtered_statistics'])
    print("Quantitative separability analysis of normalized data:")
    print(f"Mean of Vlow: {normalized_results['vlow_mean']}")
    print(f"Standard deviation of Vlow: {normalized_results['vlow_std']}")
    print(f"Coefficient of variation of Vlow: {normalized_results['vlow_cv']}")
    print(normalized_results['cv_interpretation'])
    print("Linear Regression Results:")
    print(f"Mean Squared Error (MSE): {regression_results['mse']}")
    print(f"Coefficient of Determination (R^2): {regression_results['r2']}")



