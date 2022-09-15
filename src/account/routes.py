from datetime import datetime
from typing import List

from fastapi import APIRouter, status, HTTPException
from starlette.responses import Response

from config.database.db import database
from .schemas import ReadUserSchema, CreateUserSchema, UpdateUserSchema
from .models import UserModel
from .security import hash_password

router = APIRouter()

users_table = UserModel.__table__

@router.get('/users/', response_model=List[ReadUserSchema])
async def get_users():
    query = users_table.select()
    return await database.fetch_all(query)

@router.get('/users/{id}')
async def get_user(id: int):
    query = users_table.select().where(users_table.c.id==id)
    return await database.fetch_one(query)

@router.post('/users/', response_model=ReadUserSchema)
async def create_user(instance: CreateUserSchema):
    query = users_table.select().where(users_table.c.username==instance.username)
    if await database.fetch_one(query):
        raise HTTPException(detail='Пользователь с таким ником уже существует.', status_code=status.HTTP_400_BAD_REQUEST)
    
    user = {
        'username': instance.username,
        'password': hash_password(instance.password),
        'is_active': True,
        'is_admin': False,
        'is_superuser': False,
        'date_created': datetime.utcnow(),
        'date_updated': datetime.utcnow()
    }
    
    query = users_table.insert().values(**user)
    user['id'] = await database.execute(query)
    user.pop('is_admin')
    user.pop('is_superuser')
    return user

@router.patch('/users/{id}', response_model=ReadUserSchema)
async def update_user(id: int, instance: UpdateUserSchema):
    
    query = users_table.select().where(users_table.c.id==id)
    if not await database.fetch_one(query):
        raise HTTPException(detail='Пользователя с таким id не существует.', status_code=status.HTTP_404_NOT_FOUND)
    
    query = users_table.select().where(users_table.c.username==instance.username)
    if await database.fetch_one(query):
        raise HTTPException(detail='Пользователь с таким ником уже существует.', status_code=status.HTTP_403_FORBIDDEN)
    
    user = {
        'username': instance.username,
        'date_updated': datetime.utcnow()
    }
    
    query = users_table.update().where(users_table.c.id==id).values(**user)
    await database.execute(query)
    
    query = users_table.select().where(users_table.c.id==id)
    return await database.fetch_one(query)

@router.delete('/users/{id}')
async def delete_user(id: int):
    query = users_table.select().where(users_table.c.id==id)
    if not await database.fetch_one(query):
        raise HTTPException(detail='Пользователь не найден.', status_code=status.HTTP_404_NOT_FOUND)
    
    query = users_table.delete().where(users_table.c.id==id)
    await database.execute(query)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
