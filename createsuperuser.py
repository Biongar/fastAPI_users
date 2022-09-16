import asyncio
from datetime import datetime

from config.database.db import database
from src.account.models import UserModel
from src.account.security import hash_password

users_table = UserModel.__table__

username = input('username: ')
password = hash_password(input('password: '))

async def create_super_user():
    await database.connect()   
    try: 
        superuser = {
            'username': username,
            'password': password,
            'is_active': True,
            'is_admin': True,
            'is_superuser': True,
            'date_created': datetime.utcnow(),
            'date_updated': datetime.utcnow()
        }
        query = users_table.insert().values(**superuser)

        await database.execute(query)
        
    finally:
        await database.disconnect()

if __name__ == '__main__':
    asyncio.run(create_super_user())