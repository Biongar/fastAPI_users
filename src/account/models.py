from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from config.database.db import Base


class UserModel(Base):
    __tablename__ = 'account_user'
    
    id = Column(Integer, primary_key=True, unique=True)
    
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())
    date_updated = Column(DateTime, default=datetime.utcnow())
    