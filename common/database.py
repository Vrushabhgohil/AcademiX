from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()


class Student(Base):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    date_birth = Column(DateTime, nullable=False) 
    date_join = Column(DateTime, default=datetime.datetime.now, nullable=False) 
    is_active = Column(Boolean, default=True, nullable=False)


class Tutor(Base):
    __tablename__ = 'Tutor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    resume = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    experience = Column(Integer, nullable=False)
    expected_salary = Column(Integer, nullable=False)
    secret_code = Column(String, nullable=False)
    join_date = Column(DateTime, default=datetime.datetime.now, nullable=False) 
    is_approved = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)


engine = create_engine('sqlite:///academiX.db')

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

print("Database and table created successfully!")
