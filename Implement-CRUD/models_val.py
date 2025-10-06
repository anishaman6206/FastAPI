from pydantic import BaseModel, Field, StrictInt
from typing import Optional


class Employee(BaseModel):
    id: int = Field(..., gt=0, title='Employee ID') # gt means greater than, ... means required field
    name: str = Field(..., min_length=3, max_length=30)
    department: str = Field(..., min_length=3, max_length=30)
    age: Optional[StrictInt] = Field(default=None, ge=21) # ge means greater than or equal to, StrictInt ensures that age must be an integer and not a float