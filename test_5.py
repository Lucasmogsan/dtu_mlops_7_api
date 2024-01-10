import requests

### TEST 5 ###
pload = {'username':'Olivia','password':'123'}
response = requests.post('https://httpbin.org/post', data = pload)

print(response.status_code)
print("--------------------")
print(response.url)
print("--------------------")
print(response.text)
print("--------------------")
print(response.json())
print("--------------------")
print(response.content)
print("--------------------")
print(response.headers)