from fastapi import APIRouter
from schemas import users as user_schema
from crud.users import user_crud


user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/")
def get_all_users():
    all_users = user_crud.get_all_users()
    return all_users


@user_router.get("/{id}")
def get_a_user(id: str):
    return user_crud.get_user(id)
   


@user_router.post("/")
def create_a_user(user: user_schema.UserCreate):
    return user_crud.create_user(user)



@user_router.put("/{id}")
def update_a_user(id: str, user_data: user_schema.UserUpdate):
    return user_crud.update_user(id, user_data)


@user_router.delete("/{id}")
def delete_a_user(id: str):
    return user_crud.delete_user(id)

