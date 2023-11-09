from fastapi import APIRouter, UploadFile, Depends
from PIL import Image
from io import BytesIO
from service.image_service import process_image
from auth.auth_service import api_key_auth

router = APIRouter()


@router.post("/caption", dependencies=[Depends(api_key_auth)])
async def generate_caption(file: UploadFile):
    try:
        image_data = await file.read()
        image_pil = Image.open(BytesIO(image_data))
        result = process_image(image_pil.convert("RGB"))
        return {"message": result}
    except print(0):
        pass
