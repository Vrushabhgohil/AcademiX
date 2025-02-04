from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from common.extension import db

Base = declarative_base()
class Student(db.Model):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    date_birth = Column(DateTime, nullable=False)
    date_join = Column(DateTime, default=datetime.datetime.now, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

class Tutor(db.Model):
    __tablename__ = 'Tutor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    resume = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    experience = Column(Integer, nullable=False)
    expected_salary = Column(Integer, nullable=False)
    secret_code = Column(String, nullable=False)
    join_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modify_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    is_approved = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

# SQLite Database Connection
DATABASE_URL = "sqlite:///academiX.db"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Create Tables
Base.metadata.create_all(engine)

print("Database and tables created successfully!")
