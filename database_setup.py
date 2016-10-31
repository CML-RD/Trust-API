from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
DATABASE_CALL = "DATABASE:///DATABASE_NAME.DB"

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(30))
    address = Column(String(250))
    
class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    number = Column(String(6), nullable=False)
    currency = Column(String(3), nullable=False)
    user = relationship(User, backref='account')

engine = create_engine(DATABASE_CALL)
Base.metadata.create_all(engine)
