from fastapi.encoders import jsonable_encoder
from schemas.users import UserCreate, UserUpdate
from database import user_collection
from serializers.users import user_serializer, serialize_users
from bson.objectid import ObjectId

class UserCrud:
    @staticmethod
    def get_all_users():
        users = user_collection.find()
        return serialize_users(users)
    


    @staticmethod
    def get_user(user_id: str):
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(user)


    @staticmethod
    def create_user(user_data: UserCreate):
        user_data = jsonable_encoder(user_data)
        user_document_data = user_collection.insert_one(user_data)
        user_id = user_document_data.inserted_id
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(user)



    @staticmethod
    def update_user(user_id: str, user_data: UserUpdate):
        update_data = jsonable_encoder(user_data, exclude_unset=True)
        user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data}) 
        updated_todo = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(updated_todo)



    @staticmethod
    def delete_user(user_id):
        user_collection.delete_one({"_id": ObjectId(user_id)})
        return "successfully deleted"
       
  


user_crud = UserCrud()