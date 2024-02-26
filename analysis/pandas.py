import pandas as pd


# Create a DataFrame using the input CSV file
def load_data(csv):
    df = pd.read_csv(csv)
    return df 

def perform_analysis(df):
    # mean_temp = df["Temperature"].mean()
    # mean_humid = df["Humidity"].mean()
    # median_temp = df["Temperature"].median()
    # median_humid = df["Humidity"].median()

    # return {"Mean_Temp" : mean_temp, "Mean_Humidity" : mean_humid, 
    #         "Median_Temp" : median_temp, "Median_Humidity" : median_humid}
    analysis_result = df[["Internal", "Temperature", "Humidity"]].describe()
    return analysis_result