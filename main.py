from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from schemas import Todo as Todoschema,TodoCreate, TodoUpdate

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

#dependency for db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message":"Welcome to Todo Project!"}

#create new Todo
@app.post("/todos", response_model = Todoschema)
def create_Todo(Todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = models.Todo(**Todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

#display all Todo
@app.get("/todos", response_model = list[Todoschema])
def get_Todo(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

#get Todo by id
@app.get("/todos/{todo_id}", response_model = Todoschema)
def get_Todo_id(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

#update Todo
@app.put("/todos/{todo_id}",response_model = Todoschema)
def update_todo(todo_id:int, updated: TodoUpdate, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key,value in updated.dict().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

#delete Todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message":"data deleted succesfully"}
