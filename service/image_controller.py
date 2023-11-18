from fastapi import APIRouter, UploadFile, Depends
from PIL import Image
from io import BytesIO
from service.image_service import process_image
from auth.auth_service import api_key_auth
from googletrans import Translator

router = APIRouter()

translator = Translator()


@router.post("/caption", dependencies=[Depends(api_key_auth)])
async def generate_caption(file: UploadFile):
    try:
        image_data = await file.read()
        image_pil = Image.open(BytesIO(image_data))
        result = process_image(image_pil.convert("RGB"))
        translated = translator.translate(result, dest='es')
        return {"message": translated[0].text}
    except print(0):
        pass
