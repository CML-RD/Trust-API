from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
DATABASE_CALL = "DATABASE:///DATABASE_NAME.DB"


engine = create_engine(DATABASE_CALL)
Base.metadata.create_all(engine)
