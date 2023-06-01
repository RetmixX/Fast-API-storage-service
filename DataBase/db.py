from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from helper import connection_url


engine = create_engine(connection_url)

Base = declarative_base()
Session = sessionmaker(bind=engine, expire_on_commit=False)
