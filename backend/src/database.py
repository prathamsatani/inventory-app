from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 1. Define the Declarative Base
class Base(DeclarativeBase):
    pass

# 2. Setup your database engine and session (standard boilerplate)
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/inventory-app"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
