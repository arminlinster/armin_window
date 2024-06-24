import requests

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    ip_data = response.json()
    return ip_data['ip']

public_ip = get_public_ip()
print(f"Public IP Address: {public_ip}")


def get_geolocation(api_key, ip_address):
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    payload = {
        "considerIp": "true",
        "wifiAccessPoints": []
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=payload, headers=headers)
    location_data = response.json()
    print(type(location_data))
    print(location_data)
    return location_data['location']

# 你的 Google Geolocation API 密钥
API_KEY = 'AIzaSyBRJYD0VQMu2nPv7iko9ZAYRE4JoWAwKfo'
# API_KEY = 'rU-EnmftHuIv9rFU_mQQxjLPVqg='

location = get_geolocation(API_KEY, public_ip)
latitude = location['lat']
longitude = location['lng']

print(f"Latitude: {latitude}, Longitude: {longitude}")

