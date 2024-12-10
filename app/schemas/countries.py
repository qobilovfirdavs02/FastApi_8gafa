from datetime import datetime
from typing import List
from pydantic import BaseModel


class CountryCreateUpdateSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class CountrySchema(CountryCreateUpdateSchema):
    id: int | None = None
        
class ListCountryResponse(BaseModel):
    status: str
    results: int
    