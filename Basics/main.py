from fastapi import FastAPI

# Create FastAPI instance, which is the main entry point for the application
app = FastAPI()

# Define a route for the root URL ("/"), which responds to GET requests, 
# returning a simple JSON message, (retrieved when accessing the root URL)
@app.get("/") # get: retrieval of data from the server to the client
def home():
    return {"message": "Hello, FastAPI!"}
# when user will route to the root URL,function home will be executed and they will receive a JSON response with the message "Hello, FastAPI!".

# To run the app, use the command: uvicorn main:app --reload. Here, uvicorn is the ASGI server, 'main' is the filename (without .py), and 'app' is the FastAPI instance.
# The --reload flag enables auto-reloading of the server on code changes, useful during development.