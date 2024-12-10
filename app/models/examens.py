from sqlalchemy import Table, Column, String, Integer
from app.config.db import Base

class Examen(Base):
    __tablename__ = 'examens'
    id = Column(Integer,primary_key=True)
    name = Column(String(255))