from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from ..data import URL


engine = create_engine(URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
