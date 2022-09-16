from datetime import datetime, timedelta
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer

from jose import jwt

from config.settings import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({'exp': datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

def decode_access_token(token: str):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except jwt.JWSError:
        return None
    return decoded_jwt


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        
    async def __call__(self, request: Request):
        credentials = await super(JWTBearer, self).__call__(request)
        exc = HTTPException(detail='Неверный токен.', status_code=status.HTTP_403_FORBIDDEN)
        if credentials:
            token = decode_access_token(credentials.credentials)
            if token is None:
                raise exc
            return credentials.credentials
        else:
            raise exc