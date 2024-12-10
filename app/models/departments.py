from sqlalchemy import Table, Column, String, Integer
from app.config.db import Base

class Departments(Base):
    __tablename__ = 'departments'
    id = Column(Integer,primary_key=True)
    name = Column(String(255))
    