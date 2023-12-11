import requests
import json

url = "https://api.tomorrow.io/v4/weather/realtime?location=princeton&units=metric&apikey=Juan77wTtNdrtSKHER9FTPKPXVzn6xvN"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
response_json=json.loads(response)
print(type(response_json))
print(response_json['data'])

print(response.text)