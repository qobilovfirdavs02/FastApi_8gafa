from sqlalchemy import Table, Column, String, Integer
from app.config.db import Base

class Cities(Base):
    __tablename__ = 'cities'
    id = Column(Integer,primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    region = Column(String(255))