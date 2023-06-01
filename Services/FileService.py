import string
import uuid
from DataBase.OperationOnModels import create_image, get_user, get_image_by_name
from fastapi.responses import JSONResponse
from fastapi import HTTPException

from fastapi import UploadFile


class FileService:
    def save_upload_file(self, file: UploadFile, ip_user: string) -> JSONResponse:
        filename = file.filename
        new_filename = f"{str(uuid.uuid4())}.{filename[filename.find('.') + 1:]}"
        file_location = f"storage/{new_filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        image_object = create_image(get_user(ip_user), new_filename, 'Self save file')
        return JSONResponse(content={
            "id": image_object.id,
            "path": image_object.path_image,
            "description": image_object.description
        }, status_code=201)

    def file_download(self, file_name: string) -> string:
        found_image = get_image_by_name(file_name)
        if found_image is None:
            raise HTTPException(status_code=404, detail="Image not found")

        return f"storage/{found_image.path_image}"
