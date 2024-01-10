import requests

### TEST 3 ###
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)
print(response.status_code)
print("--------------------")
print(response.json())