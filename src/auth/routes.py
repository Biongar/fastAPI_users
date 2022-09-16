from fastapi import APIRouter, HTTPException, Depends, status

from src.account.security import verify_password
from src.depends import get_user_manager
from src.account.managers import UserManager

from .schemas import Token, Login
from .security import create_access_token

router = APIRouter()


@router.post('/', response_model=Token)
async def login(login: Login, users: UserManager = Depends(get_user_manager)):
    user = await users.get_by_username(login.username)

    if not verify_password(login.password, user.password):
        raise HTTPException(detail='Введен неверный пароль.', status_code=status.HTTP_401_UNAUTHORIZED)
    
    return Token(
        access_token=create_access_token({'sub': user.username}),
        token_type='Bearer'
    )