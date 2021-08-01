import requests

url = 'https://api.agify.io/?name=sohee'
response = requests.get(url)
result = response.json()
print(result)
print(type(result))
print(result['age'])


import requests

names = ['tak', 'tony', 'eric', 'musk']

for name in names:
    url = f'https://api.agify.io/?name={name}'
    response = requests.get(url)
    result = response.json()
    print(result)
    print(result['age'])

