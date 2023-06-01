from pydantic import BaseModel


class GenerateImageDTO(BaseModel):
    text: str
