"""sqlalchemy example"""

from datetime import datetime

from geo_ai_backend.database import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String)
    password = Column(String)
    role = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=True)
