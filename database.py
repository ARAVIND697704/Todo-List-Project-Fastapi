from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

engine=create_engine(os.getenv("database_url"))
SessionLocal=sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base=declarative_base()