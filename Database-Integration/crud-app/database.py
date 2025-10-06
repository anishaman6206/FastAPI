from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" 


# eastablish connection with database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # works for multi threading
)

# each session will be created when we need to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# autocommit = False -> we have to commit the changes to the database by ourselves
# autoflush = False -> we have to flush the changes by ourselves

# creates a base class for our models to inherit from, linking the python classes to the database tables
Base = declarative_base()