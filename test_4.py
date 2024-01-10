import requests

### TEST 4 ###
response = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
# print(response.json()) # This will fail
print(response.status_code)
print("--------------------")
print(response.content)

with open(r'test_4_img.png','wb') as f:
    f.write(response.content)