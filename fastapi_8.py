from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import torch
from PIL import Image
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File
from http import HTTPStatus
import re
from fastapi.responses import FileResponse


model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

gen_kwargs = {"max_length": 16, "num_beams": 8, "num_return_sequences": 1}
def predict_step(image_paths):
    images = []
    for image_path in image_paths:
        i_image = Image.open(image_path)
        if i_image.mode != "RGB":
            i_image = i_image.convert(mode="RGB")

        images.append(i_image)
    pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    output_ids = model.generate(pixel_values, **gen_kwargs)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds




app = FastAPI()

@app.post("/predict/")
async def cv_model(data: UploadFile = File(...)):
    
    with open('fastapi_8_input.jpg', 'wb') as image:
        content = await data.read()
        image.write(content)
        image.close()
    
    image_paths = ["fastapi_8_input.jpg"]
    preds = predict_step(image_paths)

    response = {
        "input": data,
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "output": preds
    }
    return response

# Tested with:
# curl -X 'POST' \
#   'http://localhost:8000/predict/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'data=@dragon-on-the-rock.jpg;type=image/jpeg'