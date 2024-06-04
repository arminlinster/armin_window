import requests
from requests import JSONDecodeError
from pprint import pprint

def download_json()->dict[any]:
    aqi_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        response = requests.get(aqi_url)
    except Exception:
        raise Exception("連線失敗")
    else:
        #print(type(request))
        #print(request.text)
        #print(len(request.text))
        if response.status_code == 200:
            try:
                all_data:dict[any] = response.json()
                #pprint(all_data)
                #print(len(all_data))
                return all_data
            except JSONDecodeError:
                raise Exception("JSON error - format error !!!")
                
            #pprint(all_data)
        else:
            raise Exception('status is not 200')  

def main():
    try:
        all_data:dict[any] = download_json()
        pprint(all_data['records'])
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()