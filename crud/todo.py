from fastapi.encoders import jsonable_encoder
from schemas.todo import TodoCreate, TodoUpdate
from database import todo_collection
from serializers.todo import todo_serializer, serialize_todos
from bson.objectid import ObjectId


class TodoCrud:
    @staticmethod
    def get_all_todos():
        todos = todo_collection.find()
        return serialize_todos(todos)
        


    @staticmethod
    def get_a_todo(todo_id: str):
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return todo_serializer(todo)


    @staticmethod
    def create_todo(todo_data: TodoCreate):
        todo_data = jsonable_encoder(todo_data)
        todo_document_data = todo_collection.insert_one(todo_data)
        todo_id = todo_document_data.inserted_id
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return todo_serializer(todo)


    @staticmethod
    def update_todo(todo_id: str, todo_data: TodoUpdate):
        update_data = jsonable_encoder(todo_data, exclude_unset=True)
        todo_collection.update_one({"_id": ObjectId(todo_id)}, {"$set": update_data}) 
        updated_todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return todo_serializer(updated_todo)


    @staticmethod
    def delete_todo(todo_id):
        todo_collection.delete_one({"_id": ObjectId(todo_id)})
        return "successfully deleted"




todo_crud = TodoCrud()