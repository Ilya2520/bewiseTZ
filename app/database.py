from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://myuser:mypassword@postgres:5432/mydb"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = SessionLocal()


class QuestionRequest(BaseModel):
    questions_num: int


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, unique=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)


Base.metadata.create_all(bind=engine)
