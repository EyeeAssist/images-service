from PIL import Image
from fastapi import FastAPI, UploadFile
from io import BytesIO
from service.image_service import process_image

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/caption")
async def generate_caption(file: UploadFile):
    try:
        image_data = await file.read()
        image_pil = Image.open(BytesIO(image_data))
        result = process_image(image_pil.convert("RGB"))
        return {"message": result}
    except print(0):
        pass
