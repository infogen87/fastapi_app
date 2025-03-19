from fastapi import APIRouter, HTTPException, status
from schemas import users as user_schema
from crud.users import user_crud


user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/", status_code=status.HTTP_200_OK)
def get_all_users():
    all_users = user_crud.get_all_users()
    return all_users


@user_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_a_user(id: str):
    user = user_crud.get_user(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    return user
   


@user_router.post("/", status_code=status.HTTP_201_CREATED)
def create_a_user(user: user_schema.UserCreate):
    return user_crud.create_user(user)



@user_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_a_user(id: str, user_data: user_schema.UserUpdate):
    updated_user = user_crud.update_user(id, user_data)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    return updated_user


@user_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_a_user(id: str):
    return user_crud.delete_user(id)

