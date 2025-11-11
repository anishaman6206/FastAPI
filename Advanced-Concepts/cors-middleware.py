from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# cors = cross-origin resource sharing
# it allows your backend to specify which frontends are allowed to make requests and what kind of requests are allowed
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ # which domains are allowed to make requests
        "https://my-frontend.com", "http://localhost:3000"
    ],
    allow_credentials=True, # allow cookies and authentication headers
    allow_methods=['GET', 'PUT', 'POST', 'DELETE'],  # which HTTP methods are allowed
    allow_headers=['*'],  # which headers are allowed
)

# what is middleware?
# middleware is a function that runs before and/or after each request
# it can modify the request or response, or perform some action like logging, authentication, etc.
# CORS middleware specifically handles cross-origin requests by adding the appropriate headers to the response
# this ensures that only allowed frontends can access the backend resources
# CORS is a security feature implemented by browsers to prevent malicious websites from making unauthorized requests to your backend

