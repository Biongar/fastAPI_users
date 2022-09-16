from dotenv import dotenv_values

env = dotenv_values('.env')

HOST = '127.0.0.1'
PORT = 8000
PROJECT_NAME = 'fapi_project'

DATABASE = {
    'NAME': env['NAME'],
    'HOST': env['HOST'],
    'USER': env['USER'],
    'PASSWORD': env['PASSWORD'],
}

SECRET_KEY = env['SECRET_KEY']
ALGORITHM = env['ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = 30