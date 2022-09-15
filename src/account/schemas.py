from datetime import datetime

from pydantic import BaseModel, validator


class BaseUserSchema(BaseModel):
    username: str
    
    class Config:
        orm_mode = True
    

class UpdateUserSchema(BaseUserSchema):
    username: str

class ReadUserSchema(BaseUserSchema):
    id: int
    is_active: bool
    date_created: datetime
    date_updated: datetime
    

class CreateUserSchema(BaseUserSchema):
    password: str
    repeat_password: str
    
    @validator('repeat_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Пароли не совпадают')
        return v