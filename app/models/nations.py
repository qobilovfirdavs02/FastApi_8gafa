from app.config.db import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Nations(Base):
    __tablename__ = 'nations'
    id = Column(Integer,primary_key=True)
    name = Column(String(255), nullable=False)
