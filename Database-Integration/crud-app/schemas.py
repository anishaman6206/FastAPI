from pydantic import BaseModel, EmailStr


class EmployeeBase(BaseModel): # common fields for create and update
    name: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int # already inheriting name and email from EmployeeBase

    class Config:
        orm_mode = True  # to work with ORM objects directly
        # allow pydantic to read data directly from orm objects
        # convert orm object to json serializable dict
        # used to display the data in the response model