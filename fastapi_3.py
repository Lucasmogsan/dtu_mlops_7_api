from fastapi import FastAPI
from http import HTTPStatus

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

# Add database
database = {'username': [ ], 'password': [ ]}

@app.post("/login/")
def login(username: str, password: str):
    username_db = database['username']
    password_db = database['password']
    if username not in username_db and password not in password_db:
        with open('database.csv', "a") as file:
            file.write(f"{username}, {password} \n")
        username_db.append(username)
        password_db.append(password)
    return "login saved"

# Tested with http://localhost:8000/docs

# # OR:
# curl -X 'POST' \
#   'http://localhost:8000/login/?username=lucas&password=123abc' \
#   -H 'accept: application/json' \
#   -d ''
