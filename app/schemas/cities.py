from datetime import datetime
from typing import List
from pydantic import BaseModel


class CityCreateUpdateSchema(BaseModel):
    name: str
    population: int
    region: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class CitySchema(CityCreateUpdateSchema):
    id: int | None = None
        
class ListCityResponse(BaseModel):
    status: str
    results: int
    