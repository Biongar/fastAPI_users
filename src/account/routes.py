from datetime import datetime
from typing import List

from fastapi import APIRouter, status, HTTPException, Depends
from starlette.responses import Response

from .schemas import ReadUserSchema, CreateUserSchema, UpdateUserSchema
from .managers import UserManager
from .depends import get_user_manager

router = APIRouter()

@router.get('/users/', response_model=List[ReadUserSchema])
async def get_users(users: UserManager = Depends(get_user_manager)):
    return await users.get_all()

@router.get('/users/{id}', response_model=ReadUserSchema)
async def get_user(id: int, users: UserManager = Depends(get_user_manager)):
    return await users.get_by_id(id)

@router.post('/users/', response_model=ReadUserSchema)
async def create_user(instance: CreateUserSchema, users: UserManager = Depends(get_user_manager)):
    return await users.create(instance)

@router.patch('/users/{id}', response_model=ReadUserSchema)
async def update_user(id: int, instance: UpdateUserSchema, users: UserManager = Depends(get_user_manager)):
    return await users.update(id, instance)

@router.delete('/users/{id}')
async def delete_user(id: int, users: UserManager = Depends(get_user_manager)):
    return await users.delete(id)
    
