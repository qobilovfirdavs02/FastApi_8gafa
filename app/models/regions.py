from sqlalchemy import Table, Column, String, Integer
from app.config.db import Base

class Regions(Base):
    __tablename__ = 'regions'
    id = Column(Integer,primary_key=True)
    name = Column(String(255))
    