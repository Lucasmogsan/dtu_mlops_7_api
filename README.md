# API

## Requesting API data

1. Using python requests to call the API
See `test_1.py` to `test_5.py`

See [this page](https://realpython.com/python-requests/) for more information about requests.


2. Test with curl from commandline

```bash
curl -X GET "https://api.github.com"
curl -X GET -I "https://api.github.com" # if you want the status code
```

See [this page](https://gist.github.com/subfuzion/08c5d85437d5d4f00e58) for more.


## Creating APIs

See `main.py`

Launch with:
```bash
uvicorn --reload --port 8000 fastapi_1:app
```

Use [doc](http://localhost:8000/docs) and [redoc](http://localhost:8000/redoc) to test application with a simple UI.