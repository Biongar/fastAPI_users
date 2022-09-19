from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from .schemas import ReadUserSchema, CreateUserSchema, UpdateUserSchema
from .managers import UserManager
from src.depends import get_user_manager, get_current_user

router = APIRouter()

@router.get('/users/', response_model=List[ReadUserSchema])
async def get_users(users: UserManager = Depends(get_user_manager), current_user = Depends(get_current_user)):
    if not current_user.is_superuser or not current_user.is_admin:
        raise HTTPException(detail='Отказано в доступе.', status_code=status.HTTP_403_FORBIDDEN)
    return await users.get_all()

@router.get('/users/{id}', response_model=ReadUserSchema)
async def get_user(id: int, users: UserManager = Depends(get_user_manager), current_user = Depends(get_current_user)):
    if not current_user.is_superuser or not current_user.is_admin:
        raise HTTPException(detail='Отказано в доступе.', status_code=status.HTTP_403_FORBIDDEN)
    
    user = await users.get_by_id(id)
    if user.username != current_user.username and (not current_user.is_superuser or not current_user.is_admin):
        raise HTTPException(detail='Отказано в доступе.', status_code=status.HTTP_403_FORBIDDEN)
    
    return await users.get_by_id(id)

@router.post('/users/', response_model=ReadUserSchema)
async def create_user(instance: CreateUserSchema, users: UserManager = Depends(get_user_manager)):
    return await users.create(instance)

@router.patch('/users/{id}', response_model=ReadUserSchema)
async def update_user(id: int, 
                      instance: UpdateUserSchema, 
                      users: UserManager = Depends(get_user_manager), 
                      current_user = Depends(get_current_user)):
    
    user = await users.get_by_id(id)
    if user.username != current_user.username and (not current_user.is_superuser or not current_user.is_admin):
        raise HTTPException(detail='Отказано в доступе.', status_code=status.HTTP_403_FORBIDDEN)
    return await users.update(id, instance)

@router.delete('/users/{id}')
async def delete_user(id: int, users: UserManager = Depends(get_user_manager), current_user = Depends(get_current_user)):
    user = await users.get_by_id(id)
    if user.username != current_user.username and (not current_user.is_superuser or not current_user.is_admin):
        raise HTTPException(detail='Отказано в доступе.', status_code=status.HTTP_403_FORBIDDEN)
    return await users.delete(id)
    
