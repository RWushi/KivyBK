from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


load_dotenv()
SERVER_URL = os.getenv("SERVER_URL")
DB_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DB_URL)
session = async_sessionmaker(engine)
