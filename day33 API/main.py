import requests

responce=requests.get('https://api.sunrise-sunset.org/json?lat=16.529880&lng=74.602528&tzid=Asia/Kolkata')
responce.raise_for_status()
data=responce.json()
# print(data)
sunrise=data['results']['sunrise']
print(sunrise)