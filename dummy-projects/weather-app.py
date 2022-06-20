import requests, json
from pprint import pprint
API_KEY = "baab46c0cc3e0d2c177b6f2c892cf93d"
CITY = input("Entre your city Name")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL).json()
pprint(response)
