from pydantic import BaseModel

class TodoBase(BaseModel):
    name:str
    description:str
    status:str

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    name: str
    description: str

class Todo(TodoBase):
    id:int

    class Config:
        orm_mode=True
