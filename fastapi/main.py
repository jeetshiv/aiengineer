from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel):
    id:int
    name:str
    description:str

    
todos=[]

@app.get("/")
def Show_Todos():
    return todos

@app.post("/")
def create_todo(todo: ToDo):
    todos.append(todo)
    return {"message": "todo created successfully"}

@app.put('/{todo_id}')
def update_todo(todo_id:int,updated_todo:ToDo):
    for i,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[i]=updated_todo
            return {"message":"your todo updated"}
    return {"message":"failed todo update"}

@app.delete('/{todo_id}')
def delete_todo(todo_id:int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message":"todo deleted successfully"}
