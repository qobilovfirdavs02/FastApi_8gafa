from datetime import datetime
from typing import List
from pydantic import BaseModel


class NationCreateUpdateSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class NationSchema(NationCreateUpdateSchema):
    id: int | None = None
        
class ListNationResponse(BaseModel):
    status: str
    results: int
    