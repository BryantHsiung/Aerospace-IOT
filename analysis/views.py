from django.shortcuts import render
from .scraper import scraper 
from django.http import JsonResponse
from .pandas import load_data, perform_analysis 
import csv
import pandas as pd
import plotly.express as px


# Create your views here.

def temperature(request):
    return render(request, "temperature.html")

def temperature_analysis(request):
    # Read data from the CSV file
    csv_file_path = 'temperature_data.csv'
    data = []

    # with open(csv_file_path, mode='r') as file:
    #     csv_reader = csv.reader(file)
    #     header = next(csv_reader)  # Read the header row

    #     for row in csv_reader:
    #         data.append(dict(zip(header, row)))
    df = load_data(csv_file_path)

    # Create graphs
    df["datatime"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour", "Minute", "Second"]])
    fig = px.line(df, x = "datatime", y = "Temperature", title = "Temperature vs. Time")
    fig.write_image("temperature_plot.jpeg")

    fig2 = px.line(df, x = "datatime", y = "Humidity", title = "Humidity vs. Time")
    fig2.write_image("humidity_plot.jpeg")
    

    analysis = perform_analysis(df)
    analysis_html = analysis.to_html()

    # print(data[0])

    # Pass the data to the template
    return render(request, "temperature_analysis.html", {'data': df, "analysis_html" : analysis_html})