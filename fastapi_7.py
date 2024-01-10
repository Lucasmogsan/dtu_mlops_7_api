from fastapi import UploadFile, File
from http import HTTPStatus
from fastapi import FastAPI
import cv2
from fastapi.responses import FileResponse

app = FastAPI()

@app.post("/cv_model/")
async def cv_model(data: UploadFile = File(...), h: int = 28, w: int = 28):
    
    with open('fastapi_7_input.jpg', 'wb') as image:
        content = await data.read()
        image.write(content)
        image.close()
    
    img = cv2.imread("fastapi_7_input.jpg")
    res = cv2.resize(img, (h, w))
    cv2.imwrite("fastapi_7_output.jpg", res)

    response = {
        "input": data,
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "FileResponse_output": FileResponse("fastapi_7_output.jpg")
    }
    return response


# Tested with:

# curl -X 'POST' \
#   'http://localhost:8000/cv_model/?h=28&w=28' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'data=@test_4.png;type=image/png'
