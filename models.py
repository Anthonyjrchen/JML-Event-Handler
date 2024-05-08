from sqlalchemy import Column, Integer, String, Date, Boolean, Identity, BLOB
from database import Base

class User(Base):
    __tablename__ = "users"
    username = Column(String, unique=True, index = True)
    user_id = Column(Integer, primary_key = True, index = True)
    hashed_password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    occupation = Column(Integer)
    