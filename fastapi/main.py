from typing import Union, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import datetime

app = FastAPI()

class ItemNotes(BaseModel):
    title: str
    description: str

class Notes(BaseModel):
    id: int
    title: str = "untitled"
    description: str = "......."
    finished_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

storage: List[Notes] = [] 

@app.get("/")
def read_root():
    return {"Intro": "Hello, to test the API please go to /docs (recomended) or /redoc 😀"}

# The API should provide URLs below:
# - /todo (POST) create todo
# - /todo (GET) get All todo
# - /todo/<id> (GET) get todo by ID
# - /todo/<id> (PUT/PATCH) update todo
# - /todo/<id>/finish finish todo
# - /todo/<id> (DELETE) soft delete todo

@app.post("/todo")
def create_todo():
    storage.append(Notes(id=len(storage)+1, created_at=str(datetime.datetime.now())))

@app.get("/todo")
def get_all_todo():
    return storage

@app.get("/todo/{id}")
def get_todo_by_id(id: int):
    try:
        for item in storage:
            if item.id == id:
                return item
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

@app.put("/todo/{id}") 
def update_todo(id:int, item: ItemNotes):
    try:
        for index, stored_item in enumerate(storage):
            if stored_item.id == id:
                storage[index] = Notes(title=item.title, description=item.description, id=stored_item.id, finished_at=stored_item.finished_at, created_at=stored_item.created_at, updated_at=str(datetime.datetime.now()), deleted_at=stored_item.deleted_at)
                return {"item_title": item.title, "item_id": id}
                
        return {"message": "Item not found"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/todo/{id}")
def delete_todo(id: int):
    try:
        for index, stored_item in enumerate(storage):
            if stored_item.id == id:
                storage[index] = Notes(id=stored_item.id, description=stored_item.description, title=stored_item.title, finished_at=stored_item.finished_at, created_at=stored_item.created_at, updated_at=stored_item.created_at, deleted_at=str(datetime.datetime.now()))
                return {"message": "Item deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

@app.patch("/todo/{id}/finish")
def finish_todo(id: int):
    try:
        for index, stored_item in enumerate(storage):
            if stored_item.id == id:
                storage[index] = Notes(id=stored_item.id, description=stored_item.description, title=stored_item.title, finished_at=str(datetime.datetime.now()), created_at=stored_item.created_at, updated_at=stored_item.created_at, deleted_at=stored_item.deleted_at)
                return {"message": "Item finished successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
