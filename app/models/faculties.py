from sqlalchemy import Table, Column, String, Integer
from app.config.db import Base

class Faculties(Base):
    __tablename__ = 'faculties'
    id = Column(Integer,primary_key=True)
    name = Column(String(255))
    