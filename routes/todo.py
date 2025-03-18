from fastapi import APIRouter
from schemas import todo as todo_schema
from crud.todo import todo_crud

todo_router = APIRouter(prefix="/todos", tags=["todos"])


@todo_router.get("/")
def get_all_todos():
    all_todos = todo_crud.get_all_todos()
    return all_todos


@todo_router.get("/{id}", response_model=todo_schema.Todo)
def get_a_todo(id: str):
    return todo_crud.get_a_todo(id)


@todo_router.post("/", response_model=todo_schema.TodoCreate)
def make_a_todo(todo: todo_schema.TodoCreate):
    return todo_crud.create_todo(todo)


@todo_router.put("/{id}")
def update_a_todos(id: str, todo_data: todo_schema.TodoUpdate):
    return todo_crud.update_todo(id, todo_data)


@todo_router.delete("/{id}")
def delete_a_todos(id: str):
    return todo_crud.delete_todo(id)