from fastapi import FastAPI
from auth.auth_controller import router as AuthRouter
from service.image_controller import router as ImageRouter


app = FastAPI()

app.include_router(AuthRouter)
app.include_router(ImageRouter)


@app.get("/")
async def root():
    return {"message": "Hello World"}
