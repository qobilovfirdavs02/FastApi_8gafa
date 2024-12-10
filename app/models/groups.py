from sqlalchemy import Table, Column, String, Integer
from app.config.db import Base

class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer,primary_key=True)
    name = Column(String(255))
    