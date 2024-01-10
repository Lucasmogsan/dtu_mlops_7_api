import requests

### TEST 2 ###
# Other response attributes
response=requests.get("https://api.github.com/repos/SkafteNicki/dtu_mlops")
print(response.status_code)
print("--------------------")
print(response.headers)
print("--------------------")
print(response.content)
print("--------------------")
print(response.json())