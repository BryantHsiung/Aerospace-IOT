# scraper.py
import requests
from bs4 import BeautifulSoup
import re
import datetime
import csv 
import time
import os

def scraper():
    URL = "http://172.20.10.2/" # From Pico 

    # Open a CSV file in write mode 
    # mode = a to keep writing when we restart the code
    with open("temperature_data.csv", mode = "a", newline = "") as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # We only want to write the header when we create the file
        is_empty = os.stat("temperature_data.csv").st_size == 0
        if is_empty:
            # Write header
            writer.writerow(["Internal", "Temperature", "Humidity", 
                         "Year", "Month", "Day", "Hour", "Minute", "Second"])
        
        while True: # We will have to manually stop the loop
            page = requests.get(URL)
            soup = BeautifulSoup(page.text, "html.parser")

            ptags = soup.find_all("p")

            internal_temp_pattern = r'Internal Temperature is ([\d.]+) C'
            temperature_pattern = r'Temperature: (\d+) C'
            humidity_pattern = r"Humidity: (\d+) %"
            epoch_pattern = r'Epoch Time in Seconds: (\d+)'

            internal_temp_match = re.search(internal_temp_pattern, str(ptags))
            temperature_match = re.search(temperature_pattern, str(ptags))
            humidity_match = re.search(humidity_pattern, str(ptags))
            epoch_match = re.search(epoch_pattern, str(ptags))

            internal_temp = internal_temp_match.group(1) if internal_temp_match else None
            temperature = temperature_match.group(1) if temperature_match else None
            humidity = humidity_match.group(1) if humidity_match else None
            epoch = epoch_match.group(1) if epoch_match else None

            dt_object = datetime.datetime.utcfromtimestamp(int(epoch))

            year = dt_object.year
            month = dt_object.month
            day = dt_object.day
            hour = dt_object.hour
            minute = dt_object.minute
            second = dt_object.second

            # Write data to the CSV file
            writer.writerow([internal_temp, temperature, humidity, year,
                             month, day, hour, minute, second])

            # Print data for demonstration
            print("Internal:", internal_temp)
            print("Temperature:", temperature)
            print("Humidity:", humidity)
            print("Year:", year, "Month:", month, "Day:", day)
            print("Hour:", hour, "Minute:", minute, "Second:", second)
            print("===")

            time.sleep(1)

# Call the function
# scraper()