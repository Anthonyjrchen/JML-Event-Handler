from sqlalchemy import Column, Integer, String, Date, Boolean, Identity, BLOB
from database import Base

class User(Base):
    __tablename__ = "users"
    username = Column(String, unique=True, index = True)
    user_id = Column(Integer, primary_key = True, index = True)
    hashed_password = Column(String)
    gender = Column(String)
    lawyer = Column(Boolean)
    