from fastapi import FastAPI
from http import HTTPStatus
import re

app = FastAPI()

@app.get("/text_model/")
def contains_email(data: str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    response = {
        "input": data,
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "is_email": re.fullmatch(regex, data) is not None
    }
    return response


# Tested with
# curl -X 'GET' 'http://localhost:8000/text_model/?data=hello@gmail.com' -H 'accept: application/json'
