import string

from DataBase.models import User, Image
from DataBase.db import Session
from DataBase.db import engine


def get_user(ip_address: string) -> User:
    session = Session()
    find_user = session.query(User).filter(User.ip_address == ip_address).first()
    session.close()
    return find_user


def create_user(ip_address: string) -> User:
    session = Session()
    new_user = User(ip_address=ip_address)
    session.add(new_user)
    session.commit()
    session.close()
    return new_user


def create_image(user: User, path_file: string, description: string) -> Image:
    session = Session()
    new_image = Image(path_image=path_file, description=description, user=user)
    session.add(new_image)
    session.commit()
    session.close()
    return new_image


def get_image_by_name(file_name: string) -> Image:
    session = Session()
    found_image = session.query(Image).filter(Image.path_image == file_name).first()
    session.close()
    return found_image


def get_images_by_user(user: User):
    session = Session()
    images = session.query(Image).filter(Image.user_id == user.id)
    session.close()
    return images
