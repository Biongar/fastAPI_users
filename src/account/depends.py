from .managers import UserManager
from config.database.db import database

def get_user_manager():
    return UserManager(database)