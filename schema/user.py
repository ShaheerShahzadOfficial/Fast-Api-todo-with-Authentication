def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "user_name": item["user_name"],
        "email": item["email"],
    }



