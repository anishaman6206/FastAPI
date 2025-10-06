from pydantic import BaseModel, Field, StrictInt

class InputSchema(BaseModel):
    longitude: float = Field(..., description="Longitude of the location", example=-121.23)
    latitude: float = Field(..., description="Latitude of the location", example=37.88)
    housing_median_age: int = Field(..., gt=0, description="Median age of the houses in the area", example=35)
    total_rooms: StrictInt = Field(..., gt=0, description="Total number of rooms in the area", example=730)
    total_bedrooms: StrictInt = Field(..., gt=0, description="Total number of bedrooms in the area", example=600)
    population: int= Field(..., gt=0, description="Population of the area", example=350)
    households: StrictInt = Field(..., gt=0, description="Number of households in the area", example=250)
    median_income: float = Field(..., gt=0, description="Median income of the households in the area", example=7.42)


class OutputSchema(BaseModel):
    median_house_value: float = Field(..., description="Predicted median house value", example=250000.0)    


