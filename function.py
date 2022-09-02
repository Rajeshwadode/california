from artifacts import CONFIG 
import json
import pickle
import numpy as np


class california():
    
    def __init__(self,longitude, latitude,housing_median_age, total_rooms, total_bedrooms, population, households, median_income, ocean_proximity):
        self.longitude=longitude
        self.latitude=latitude
        self.housing_median_age=housing_median_age
        self.total_rooms=total_rooms
        self.total_bedrooms=total_bedrooms
        self.population=population
        self.households=households
        self.median_income=median_income
        self.ocean_proximity=ocean_proximity
        
        
        
    def model_load(self):
        
        with open(CONFIG.COLUMNS_FILE_PATH,"rb") as file:
            self.columns_dict=json.load(file)
            
        with open(CONFIG.MODEL_FILE_PATH,"rb") as file:
            self.model=pickle.load(file)
            
            
            
    def predict(self):
        self.model_load()
        
        
        array=np.zeros(len(self.columns_dict["columns"]))                          # columns is key for list of coulmns 
        array[0]=self.longitude
        array[1]=self.latitude
        array[2]=self.housing_median_age
        array[3]=self.total_rooms
        array[4]=self.total_bedrooms
        array[5]=self.population
        array[6]=self.households
        array[7]=self.median_income
        
        ocean_proximity_value='ocean_proximity_'+self.ocean_proximity
        index_value=self.columns_dict["columns"].index(ocean_proximity_value)
        array[index_value]=1
        
        print(array)
        
        result=self.model.predict([array])
        print(result[0])
        return result[0]

if __name__=="__main__":
    
    longitude=-122.23
    latitude=37.88	
    housing_median_age=41.0
    total_rooms=880.0	
    total_bedrooms=129.0
    population=322.0	
    households=126.0	
    median_income=8.3252	
    ocean_proximity="NEAR BAY"
    
    
    
    

    obj=california(longitude, latitude,housing_median_age, total_rooms, total_bedrooms, population, households, median_income, ocean_proximity)
    obj.predict()

