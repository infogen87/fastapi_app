from fastapi import APIRouter, HTTPException, status
from schemas import todo as todo_schema
from crud.todo import todo_crud

todo_router = APIRouter(prefix="/todos", tags=["todos"])


@todo_router.get("/", status_code=status.HTTP_200_OK)
def get_all_todos():
    all_todos = todo_crud.get_all_todos()
    return all_todos


@todo_router.get("/{id}", response_model=todo_schema.Todo, status_code=status.HTTP_200_OK)
def get_a_todo(id: str):
    todo = todo_crud.get_a_todo(id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo

@todo_router.post("/", response_model=todo_schema.TodoCreate, status_code=status.HTTP_201_CREATED)
def make_a_todo(todo: todo_schema.TodoCreate):
    return todo_crud.create_todo(todo)


@todo_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_a_todos(id: str, todo_data: todo_schema.TodoUpdate):
    updated_todo = todo_crud.update_todo(id, todo_data)
    if not updated_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return updated_todo


@todo_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_a_todos(id: str):
    return todo_crud.delete_todo(id)