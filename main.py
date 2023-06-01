from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import FileResponse, JSONResponse
from Middlewares.UserExistMiddleware import UserExistMiddleware
from DataBase.db import Base, engine
from Services.FileService import FileService
from Services.UserService import UserService
from DTO.GenerateImageDTO import GenerateImageDTO

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(UserExistMiddleware)

file_service = FileService()
user_service = UserService()


@app.get("/")
def hello_controller(request: Request):
    return {"message": request.client.host}


@app.post("/file")
def upload_file(file: UploadFile, request: Request):
    return file_service.save_upload_file(file, request.client.host)


@app.get("/my-collections")
def get_my_collection_files(request: Request):
    return JSONResponse(content=user_service.get_all_my_files(request.client.host))


@app.post("/generate-image")
def generate_image_ai(data: GenerateImageDTO, request: Request):
    return user_service.generate_image(request.client.host, data)


@app.get("/download/{file_name}", response_class=FileResponse)
def download_file(file_name):
    return file_service.file_download(file_name)
