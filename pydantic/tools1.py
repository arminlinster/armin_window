import requests
from  requests import JSONDecodeError
from pydantic import BaseModel,RootModel,Field,field_validator

class Site(BaseModel):
    sna:str
    sarea:str
    mday:str
    ar:str
    act:str
    updateTime:str
    total:int
    rent_bikes:int 
    retuen_bikes:int
    lat:float = Field(alias="latitude")
    lng:float = Field(alias="longitude")


    @field_validator("lat",mode='before')
    @classmethod
    def abc(cls, value:str)->str:
        if value=="":
            return "0.0"
        else:
            return value
    @field_validator("lng",mode='before')
    @classmethod
    def ddd(cls, value:str)->str:
        if value=="":
            return "0.0"
        else:
            return value

class Records(RootModel):
    root:list[Site]

def download_json()->dict[any]:
    aqi_url ="https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    try:
        response = requests.get(aqi_url)
    except Exception:
        raise Exception("連線失敗")
    else:
        if response.status_code == 200:
            try:
                all_data:dict[any] = response.json()
                return all_data
            except JSONDecodeError:
                raise Exception("api_key為測試用,連線已至上限,請稍後再試")
        else:
            raise Exception("下載狀態碼不是200")
        
def get_data(all_data:dict[any]) -> list[dict]:
    records:Records = Records.model_validate(all_data['Records'])
    data:list[dict] = records.model_dump()
    return data