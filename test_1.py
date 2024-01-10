import requests


### TEST 1 ###
# Test GET request and status codes
def get_status_code(url):
    response = requests.get(url)

    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 403:
        print('Forbidden.')
    elif response.status_code == 404:
        print('Not Found.')
    else:
        print('Something else happened.')

    return response.status_code

print(get_status_code("https://api.github.com/this-api-should-not-exist"))
print(get_status_code('https://api.github.com'))
print(get_status_code("https://api.github.com/repos/SkafteNicki/dtu_mlops"))