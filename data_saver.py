from final_product import Datapoint_Extraction
from final_product import Data_Processor
from api_storer import api_key
import pandas as pd
import os

data_extractor=Datapoint_Extraction(api_key)
data_extractor_2=Data_Processor
places=['London','Birmingham']
input_directory=r'C:\Users\User\OneDrive\Desktop\data1'
output_directory=r'C:\Users\User\OneDrive\Desktop\data1'
WEATHER_MAPPING ={
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

raw_data=data_extractor.forcast_finder(places)


print(raw_data)
#raw_data_saver=data_extractor.csv_saver(raw_data,'London_Birmingham.csv')

rd_cd=data_extractor_2.column_deleter('London_Birmingham.csv','$')
md_dm=data_extractor_2.weather_mapper(input_directory,output_directory,'modified_London_Birmingham.csv','M_L_B.csv')
