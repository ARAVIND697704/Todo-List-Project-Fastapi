from sqlalchemy import Integer,Column,String, Boolean
from database import Base

class Todo(Base):
    __tablename__="Todos"
    id=Column(Integer, primary_key = True)
    name=Column(String(50), nullable = False)
    description=Column(String(200))
    status = Column(String(20), nullable = True, default = "Incomplete")