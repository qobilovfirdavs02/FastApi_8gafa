from pydantic import BaseModel
from datetime import date as Date
from typing import List
from pydantic import BaseModel

class StudentCreateUpdateSchema(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    tel: str
    nation_id: int
    gender: int
    birthday:Date
    country_id: int
    region_id: int
    city_id:int
    adress: str
    current_region_id: int
    current_city_id:int
    current_adress: str
    faculty_id:int
    department_id:int
    group_id:int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class StudentSchema(StudentCreateUpdateSchema):
    id: int | None = None
        
class ListStudentResponse(BaseModel):
    status: str
    results: int
    students: List[StudentSchema]
    