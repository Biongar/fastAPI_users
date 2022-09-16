from datetime import datetime

from fastapi import HTTPException, status
from starlette.responses import Response

from config.database.db import database
from src.managers import BaseManager
from .models import UserModel
from .security import hash_password
from .schemas import CreateUserSchema, UpdateUserSchema


users_table = UserModel.__table__


class UserManager(BaseManager):
    async def get_all(self):
        query = users_table.select()
        return await database.fetch_all(query)
    
    async def get_by_id(self, id):
        query = users_table.select().where(users_table.c.id==id)
        user = await database.fetch_one(query)
        if not user:
            raise HTTPException(detail='Пользователь не найден.', status_code=status.HTTP_404_NOT_FOUND)
        
        return user
    
    async def create(self, instance: CreateUserSchema):
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
        return user
    
    async def update(self, id: int, instance: UpdateUserSchema):
    
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
    
    async def delete(self, id: int):
        query = users_table.select().where(users_table.c.id==id)
        if not await database.fetch_one(query):
            raise HTTPException(detail='Пользователь не найден.', status_code=status.HTTP_404_NOT_FOUND)
        
        query = users_table.delete().where(users_table.c.id==id)
        await database.execute(query)
        
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        
