import requests

url = 'https://api.nationalize.io/?name=michael'
response = requests.get(url)
result = response.json()
print(result['country'][0]['country_id'])