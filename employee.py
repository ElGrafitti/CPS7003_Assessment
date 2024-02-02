from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class Employee(Base):
    __tablename__ = "Employee"
    EmployeeID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, unique=True, nullable=False)
    LastName = Column(String, unique=True, nullable=False)
    Email = Column(String, unique=True, nullable=False)
    DOB = Column(String, unique=True, nullable=False)
    MobileNumber = Column(String, unique=True, nullable=False)
    Address = Column(String, unique=True, nullable=False)
    DepartmentID = Column(Integer, ForeignKey("Department.DepartmentID", ondelete="CASCADE"), nullable=False)
