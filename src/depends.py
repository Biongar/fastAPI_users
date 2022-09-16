from fastapi import Depends, HTTPException, status

from config.database.db import database
from src.account.managers import UserManager
from src.auth.security import JWTBearer, decode_access_token

def get_user_manager():
    return UserManager(database)

async def get_current_user(users = Depends(get_user_manager), token = Depends(JWTBearer())):
    cred_exception = HTTPException(detail='Credential are not valid.', status_code=status.HTTP_401_UNAUTHORIZED)
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    username = payload.get('sub')
    if username is None:
        raise cred_exception
    user = await users.get_by_username(username)
    if user is None:
        return cred_exception
    return user