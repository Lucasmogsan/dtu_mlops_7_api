from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Add a path parameter to the path /items/{item_id}
@app.get("/items/{item_id}")
def read_item(item_id: int):    # Path parameters, item_id is required and must be an integer
    return {"item_id": item_id}