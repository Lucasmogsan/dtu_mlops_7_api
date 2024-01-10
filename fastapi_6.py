from fastapi import UploadFile, File
from http import HTTPStatus
from fastapi import FastAPI

app = FastAPI()

@app.post("/cv_model/")
async def cv_model(data: UploadFile = File(...)):
    with open('fastapi_6_output.jpg', 'wb') as image:
        content = await data.read()
        image.write(content)
        image.close()

    response = {
        "input": data,
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
    }
    return response


# Tested with:

# curl -X 'POST' \
#   'http://localhost:8000/cv_model/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'data=@test_4.png;type=image/png'