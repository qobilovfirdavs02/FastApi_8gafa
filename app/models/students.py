from app.config.db import Base
from sqlalchemy import Table, Column, String, Integer,ForeignKey,Date
from sqlalchemy.orm import relationship
from app.models import *

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer,primary_key=True)
    first_name = Column(String(255))
    middle_name = Column(String(255))
    last_name = Column(String(255))
    tel = Column(String(255))
    nation_id = Column(Integer, ForeignKey('nations.id'), nullable=False)
    gender = Column(Integer,comment='if 1 male, 0 female')
    birthday = Column(Date)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    region_id = Column(Integer, ForeignKey('regions.id'), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    adress = Column(String(255))
    current_region_id = Column(Integer, ForeignKey('regions.id'), nullable=False) 
    current_city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    current_adress = Column(String(255))
    faculty_id = Column(Integer, ForeignKey('faculties.id'), nullable=False)   
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False) 
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False) 
    