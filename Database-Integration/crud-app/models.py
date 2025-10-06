from sqlalchemy import Column, Integer, String
from .database import Base

# Base class for our models to inherit from, linking the python classes to the database tables
class Employee(Base):
    __tablename__ = "employees"  # name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # primary key column
    name = Column(String, index=True)  # name column
    email = Column(String, unique = True, index = True)  # email column
    