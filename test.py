from final_product import Data_Processor
from final_product import Datapoint_Extraction
import pytest
from api_storer import api_key
import os
class Test_De:
    def test_location_finder(self):
        extractor = Datapoint_Extraction(api_key)
        location_id = extractor.location_finder('London')
        assert location_id == '352409'

    def test_forcast_finder(self):
        extractor = Datapoint_Extraction(api_key)
        forecast_data = extractor.forcast_finder(['London', 'Manchester'])
        assert len(forecast_data) > 0
        assert 'location' in forecast_data.columns
        assert 'Date' in forecast_data.columns

class Test_DP:
    class Test_DP:
        def test_column_deleter:
            temp_dir=tmpdir.mkdir("test_data")
            csv_filename="test_data.csv"
            csv_filepath=os.path.join(temp_dir,csv_filename)
            test_data={
                "A":[1,2,3],
                "B":[4,5,6],
                "C":[7,8,9]
            }
            df=pd.Dataframe(test_data)
            df.to_csv(csv_filepath,index=False)
            deleted_df=col



def test_weather_mapper:
        processor = Data_Processor
        processor.weather_mapper(r'C:\Users\User\OneDrive\Desktop\data1',
                                    r'C:\Users\User\OneDrive\Desktop\data1',
                                    'LONDON_AND_NEWCASTLE.csv',
                                    'modified.csv')


