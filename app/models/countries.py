from sqlalchemy import Table, Column, String, Integer
from app.config.db import Base

class Countries(Base):
    __tablename__ = 'countries'
    id = Column(Integer,primary_key=True)
    name = Column(String(255))
    