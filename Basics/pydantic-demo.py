from fastapi import FastAPI
# basemodel is a core component of the Pydantic library used for data validation and settings management in Python.
# using pydantic we can define data models with type annotations, and Pydantic will handle the validation and serialization of data automatically.
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

app = FastAPI()

# Define a route that returns a User model instance as JSON, 
# response_model parameter is used to specify the model that should be used for the response.
@app.get("/user", response_model=User)
def get_user():
    return User(id=1, name="Ani")

# To run the app, use the command: uvicorn pydantic-demo:app --reload. Here, uvicorn is the ASGI server, 'pydantic-demo' is the filename (without .py), and 'app' is the FastAPI instance.
