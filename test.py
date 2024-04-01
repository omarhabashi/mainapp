
from final_product import Datapoint_Extraction,Data_Processor
import pytest
from api_storer import api_key
import os
import pandas as pd

api_key=api_key

def Datapoint_instance():
    return Datapoint_Extraction(api_key)

def Dataprocessor_instance():
    return Data_Processor()

def test_location_finder(Datapoint_instance):
    assert Datapoint_instance.location_finder('London')='352409'

def test_forecast_finder(Datapoint_instance):
    locations=["London","Manchester"]
    df=Datapoint_instance.forcast_finder(locations)
    assert isinstance(df,pd.DataFrame)

def test_csv_saver(DataPoint_instance):
    df=pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
    file_name="test.csv"
    DataPoint_instance.csv_saver(df,file_name)
    assert os.path.isfile(file_name)
    os.remove(file_name)


def test_column_deleter(Dataprocessor_instance):
    csv_filename="test.csv"
    column_name="B"
    df=Dataprocessor_instance.column_deleter(csv_filename,column_name)
    assert isinstance(df,pd.DataFrame)
    assert column_name not in df.columns

def test_weather_mapper(Dataprocessor_instance):
    input_directory="input.csv"
    output_directory="output.csv"
    csv_filename="input.csv"
    new_filename="output.csv"
    df=Dataprocessor_instance.weather_mapper(input_directory,output_directory,csv_filename,new_filename)
    assert isinstance(df,pd.DataFrame)
    assert os.path.isfile(os.path.join(output_directory,new_filename))

