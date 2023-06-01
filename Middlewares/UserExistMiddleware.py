from fastapi import Request
from DataBase.OperationOnModels import get_user, create_user
from starlette.middleware.base import BaseHTTPMiddleware


class UserExistMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        address_client = request.client.host
        if get_user(address_client) is None:
            create_user(address_client)

        return await call_next(request)
