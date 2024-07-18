import requests
from requests import Response

def dload_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    try:
        res:Response = requests.get(url)
    except Exception:
        raise("連線失敗")
    else:
        all_datas:dict[any] = res.json()
        return all_datas
#====
try:
    all_datas:dict[any] = dload_json()
except Exception as error:
    print(error)
print("11111111111111111111111")
print(all_datas)
print("22222222222222222222222")
#====
from pydantic import BaseModel, RootModel, Field

class Info(BaseModel):
    sna:str
    sarea:str
    mday:str
    ar:str
    act:str
    updateTime:str
    total:int
    rent_bikes:int = Field(alias="available_rent_bikes")
    lat:float = Field(alias="latitude")
    lng:float = Field(alias="longitude")
    retuen_bikes:int = Field(alias="available_return_bikes")

class ubike_Data(RootModel):
    root:list[Info]
ubike_data:ubike_Data = ubike_Data.model_validate(all_datas)
mydata = ubike_data.model_dump()

#====
import math
for dat in mydata:
    if abs(dat['lat'] - 25.115000) < 0.00350 and abs(dat['lng'] - 121.537500) < 0.00350:
        print(dat['lat'] - 25.115000)
        print(dat['lng'] - 121.537500) 
        print(dat['lat'])
        print(dat['lng']) 
        print(dat['sna'])
        print(dat['sarea'])
        print(dat['ar'])
        print(dat['act'])
        print(dat['rent_bikes'])
        print(dat['retuen_bikes'])
    #print(dat.lng)
#====