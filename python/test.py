import requests

url = 'https://api.agify.io/?name=sohee'
data = requests.get(url).json()
print(data)
print(data['name'])