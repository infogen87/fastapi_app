from fastapi import FastAPI
from routes import todo, users



app = FastAPI()


app.include_router(users.user_router)
app.include_router(todo.todo_router)


@app.get("/")
def home():
    return {"message": "app works"}
