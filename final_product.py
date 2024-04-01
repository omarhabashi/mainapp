import requests
import pandas as pd
import os
from api_storer import api_key

class Datapoint_Extraction:
    """class to extract weather forecast data from the met office Datapoint Api"""

    def __init__(self, api_key):
        """initiates Datapoint with provided API key.
        Parameters:api_key for accessing met office datapoint API"""
        self.api_key = api_key
        self.url = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/"

    def location_finder(self, location):
        """find the location id according to location string with datapoint API
        parameters:location as a string
        returns:the location ID
        Raises:value error if location not found """
        url = f"http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key={self.api_key}"
        response = requests.get(url)
        locations = response.json()["Locations"]["Location"]
        for loc in locations:
            if loc["name"] == location:
                print("Location ID:", loc["id"])
                return loc["id"]
        raise ValueError("location not found")

    def forcast_finder(self, locations):
        """Finds the weather forecast of given locations
        Parameters:List of strings of locations for which to retrieve the forecast
        Returns: pandas.Dataframe for stated location containing the weather forecast """


        forecast_data = []
        for location in locations:
            location_id = self.location_finder(location)
            url = f"{self.url}{location_id}?res=3hourly&key={self.api_key}"
            response = requests.get(url)
            forecast = response.json()['SiteRep']['DV']['Location']
            for period in forecast['Period']:
                for rep in period['Rep']:
                    forecast_data.append((location, period['value'], rep['D'], rep['F'], rep['G'], rep['H'], rep['Pp'],
                                          rep['T'], rep['V'], rep['W'], rep['U'], rep['$'], rep['S'],))
        columns = ['location', 'Date', 'Wind direction', 'Feels like temp', 'Wind Gust', 'Screen relative humidity',
                       'Precipitation probability', 'Temperature', 'Visibility', 'Weather type', 'Max UV index', '$',
                       'Wind speed']
        df = pd.DataFrame(forecast_data, columns=columns)
        return df


    def csv_saver(self , forecast_df, filename):
        """saves forecast data dataframe to a CSV file
        Parameters:forecast_df;dataframe containing forecast data.
        filename(str):name of the file to save CSV file as """
        base_directory = r'C:\Users\User\OneDrive\Desktop\data1'
        file_path = os.path.join(base_directory, filename)
        forecast_df.to_csv(file_path, sep=',', index=False, encoding='utf-8')

class Data_Processor:
    """Class which processes forecast data from CSV files
    attributes:Weather mapping dictionary required to convert numerical codes to strings"""
    # api_key = '25c264c6-4457-4668-b25c-607f37b87e95'
    WEATHER_MAPPING = {
        "NA": "Not available",
        -1: "Trace rain",
        0: "Clear",
        1: "Clear",
        2: "Partly cloudy",
        3: "Partly cloudy",
        4: "Not used",
        5: "Low visibility",
        6: "Low visibility",
        7: "Cloudy",
        8: "Cloudy",
        9: "Light rain",
        10: "Light rain",
        11: "Light rain",
        12: "Light rain",
        13: "Heavy rain",
        14: "Heavy rain",
        15: "Heavy rain",
        16: "Sleet",
        17: "Sleet",
        18: "Sleet",
        19: "Hail",
        20: "Hail",
        21: "Hail",
        "22": "Light snow",
        23: "Light snow",
        24: "Light snow",
        25: "Heavy snow",
        26: "Heavy snow",
        27: "Heavy snow",
        28: "Thunder",
        29: "Thunder",
        30: "Thunder"}


    @staticmethod
    def column_deleter(csv_filename, column_name):
        """Deletes a specific column from a CSV file to process column name
        Parameters:
            csv_filename:name of csv to process
            column_name:name of column name to delete in the dataframe
        Returns:
              pandas.Dataframe or none
        """
        file_path = os.path.join(r'C:\Users\User\OneDrive\Desktop\data1', csv_filename)
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if column_name in df.columns:
                df.drop(column_name, axis=1, inplace=True)
                print(f"column name {column_name} deleted successfully in Dataframe")
                print(df)

                new_csv_filename = f"modified_{csv_filename}"
                new_file_path = os.path.join(r'C:\Users\User\OneDrive\Desktop\data1', new_csv_filename)
                df.to_csv(new_file_path, index=False)
                print(f"modified Dataframe saved as {new_csv_filename}to the same file path ")

                return df
            else:
                print(f"column name '{column_name} not found in Dataframe")
                return None
        else:
            print("file not found")
            return None

    @staticmethod
    def weather_mapper(input_directory, output_directory, csv_filename, new_filename):
        """Maps 'Weather Type column to descriptive strings in a csv file and saves to modified dataframe
        Parameters:
            Input directory(str):Directory to upload csv file from
            Output directory(str):The directory to save the modified CSV file
            csv_filename(str):The name of the input csv file
            new_filename(str):The name use for the modified CSV file
        Returns:
              pandas.Dataframe which has replace values in weather type column and uploaded to output directory site
        """
        input_filepath = os.path.join(input_directory, csv_filename)
        output_filepath = os.path.join(output_directory, new_filename)

        if os.path.exists(input_filepath):
            df = pd.read_csv(input_filepath)
            df['Weather type'] = df['Weather type'].replace(WEATHER_MAPPING)
            print("Weather Type column")
            print(df['Weather type'])

            df.to_csv(output_filepath, index=False)
            print(f"Modified dataframe saved as '{new_filename}' to '{output_filepath}'")
            return df
        else:
            print(f"input file from {input_filepath} not found ")


input_directory = r'C:\Users\User\OneDrive\Desktop\data1'
output_directory = r'C:\Users\User\OneDrive\Desktop\data1'



#Initiating datapoint_extraction class
data1 = Datapoint_Extraction(api_key)
#creation of variable to be used in forcast finder function
places = ['London', 'Plymouth']
#Assigning variable for forcast_df
forcast_df=data1.forcast_finder(places)
print(forcast_df)
#using location_finder to retrieve id of 'london
data1.location_finder('London')
#saving the dataframe of london and plymouth forecast data
data1.csv_saver(forcast_df,"LONDON_AND_PLYMOUTH.csv")
#inititating the use of Dataprocessor and applying data mapper function to convert columns
#data2=Data_Processor.data_mapper('forcast_df')
#deleting column from csv file correspondong to london and plymouth data
forecast_tryout=data2=Data_Processor.column_deleter(' LONDON_AND_PLYMOUTH.csv','$')
#mapping new values in csv file according to WEATHER_MAPPING dictionary
mapper_tryout=Data_Processor.weather_mapper(input_directory,output_directory,'modified_LONDON_AND_PLYMOUTH.csv','Mapped_L2P.csv')
