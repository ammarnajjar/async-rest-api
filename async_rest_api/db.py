import os

from databases import Database
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.sql import func


# default to a local sqlite db
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./db.sqlite3')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

notes = Table(
    'notes',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('text', String(50)),
    Column('completed', Boolean),
    Column('created_date', DateTime, default=func.now(), nullable=False),
)

database = Database(DATABASE_URL)
