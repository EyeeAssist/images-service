from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.auth_controller import router as AuthRouter
from service.image_controller import router as ImageRouter


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AuthRouter)
app.include_router(ImageRouter)


@app.get("/")
async def root():
    return {"message": "Hello World"}
