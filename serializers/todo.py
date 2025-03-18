


def todo_serializer(todo) -> dict:
    return {
        "id": str(todo.get("_id")),
        "user_id": str(todo.get("id")),
        "title": todo.get("title"),
        "description": todo.get("description"),
        "is_completed": todo.get("is_completed")
    }



def serialize_todos(todos) -> list:
    return [todo_serializer(todo) for todo in todos]