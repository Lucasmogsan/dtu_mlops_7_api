from http import HTTPStatus
from fastapi import FastAPI
from enum import Enum

# Create the app object
app = FastAPI()

# For the root path, return a dictionary with a message and status code
@app.get("/")
def root():
    """ Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
    }
    return response

### STEP 1 ###
# Add a path parameter to the path /items/{item_id}
@app.get("/items/{item_id}")
def read_item(item_id: int):    # Path parameters, item_id is required and must be an integer
    return {"item_id": item_id}

# TEST WITH: http://localhost:8000/items/1



### STEP 2 ###
# Add a path parameter to the path /restric_items/{item_id}
class ItemEnum(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/restric_items/{item_id}")
def read_item(item_id: ItemEnum):   # item_id is required and can only be one of the three values in ItemEnum
    return {"item_id": item_id}

# TEST WITH: http://localhost:8000/restric_items/alexnet



### STEP 3 ###
# Add query parameters to the path /query_items
@app.get("/query_items")
def read_item(item_id: int):
    return {"item_id": item_id}

# TEST WITH: http://localhost:8000/query_items?item_id=1