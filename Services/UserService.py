import string
from DataBase.OperationOnModels import create_image, get_user, get_images_by_user
from DTO.GenerateImageDTO import GenerateImageDTO
from fastapi import HTTPException
import requests
import uuid
import helper
from fastapi.responses import JSONResponse


class UserService:

    def get_all_my_files(self, ip_address: string):
        array_files = []

        images = get_images_by_user(get_user(ip_address))

        for image in images:
            array_files.append({
                "id": image.id,
                "filename": image.path_image,
                "description": image.description
            })

        return array_files

    def generate_image(self, ip_address: string, data: GenerateImageDTO):
        try:
            response = requests.post(helper.url, headers=helper.header, data=helper.get_body(data.text))
            if not response.status_code == 200:
                raise HTTPException(status_code=500, detail="External service not work, try later")

            url_json = response.json()
            url_image = url_json["output"][0]
            image = requests.get(url_image).content
            filename = f"{str(uuid.uuid4())}.png"
            with open(f"storage/{filename}", "wb+") as file:
                file.write(image)

            image_object = create_image(get_user(ip_address), filename, data.text)
            return JSONResponse(content={
                "id": image_object.id,
                "path": image_object.path_image,
                "description": image_object.description
            }, status_code=201)
        except:
            raise HTTPException(status_code=500, detail="External service not work, try later")
