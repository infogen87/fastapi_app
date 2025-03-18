


def user_serializer(user) -> dict:
    return {
        "id": str(user.get("_id")),
        "username": user.get("username"),
        "email": user.get("email"),
        "age": user.get("age"),
        "created_at": user.get("created_at")
    }


def serialize_users(users) -> list:
    return [user_serializer(user) for user in users]