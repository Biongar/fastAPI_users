from databases import Database

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config.settings import DATABASE

DATABASE_URL = f"postgresql://{DATABASE['USER']}:{DATABASE['PASSWORD']}@{DATABASE['HOST']}/{DATABASE['NAME']}"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
database = Database(DATABASE_URL)