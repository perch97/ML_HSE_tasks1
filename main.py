from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import pandas as pd
import json
from preprocessing import preproces, fitted_model
from fastapi.responses import StreamingResponse
from io import StringIO
from models import Item, Items,Event, Item_predicted, Items_predicted


app = FastAPI()


class Item(BaseModel):
    name: str
    year: int
    selling_price: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: str 
    engine: str
    max_power: str
    torque: str
    seats: float



class Items(BaseModel):
    objects: List[Item]



@app.post("/predict_item")
def predict_item(item: Item) -> float:
    selling_price_model = pickle.load(open('','rb'))
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    name = input_dictionary['name']
    year = input_dictionary['year']
    selling_price = input_dictionary['selling_price']
    km_driven = input_dictionary['km_driven']
    fuel = input_dictionary['fuel']
    seller_type = input_dictionary['seller_type']
    transmission = input_dictionary['transmission']
    owner = input_dictionary['owner']
    mileage = input_dictionary['mileage']
    engine = input_dictionary['engine']
    max_power = input_dictionary['max_power']
    torque = input_dictionary['torque']
    seats = input_dictionary['seats']

    input_list = [name,year,selling_price,km_driven,fuel,selling_price,km_driven,fuel,seller_type,
                  transmission,owner,mileage,engine,max_power,torque,seats]
    
    predict = selling_price_model.predict([input_list])
    print(predict)
    return {'You can sell your car for {}'.format(predict)}
    
    


