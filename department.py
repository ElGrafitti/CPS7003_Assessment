from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = "Department"
    DepartmentID = Column(Integer, primary_key=True, autoincrement=True)
    DepartmentName = Column(String, unique=True, nullable=False)
