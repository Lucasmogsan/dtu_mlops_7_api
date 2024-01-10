from http import HTTPStatus
from fastapi import FastAPI
from enum import Enum

# Create the app object
app = FastAPI()


@app.get("/")
def root():
    """ Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
    }
    return response

@app.get("/query_items")
def read_item(item_id: int):
    return {"item_id": item_id}

# Tested with: http://localhost/query_items?item_id=1
