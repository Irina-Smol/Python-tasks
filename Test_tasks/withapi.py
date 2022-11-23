import requests
from apikey import API_TOKEN

params = {'apikey': API_TOKEN, 'file': '0.jpeg'}
response = requests.get('https://api.ocr.space/parse/imageurl', params=params)
print(response.status_code)
print(response.json())
print(response.headers)