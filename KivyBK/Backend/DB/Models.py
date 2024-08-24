from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Numeric(precision=9, scale=6))
    longitude = Column(Numeric(precision=9, scale=6))
    photo_id = Column(String)
