def taskEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "task_title": item["task_title"],
        "task_description": item["task_description"],
        "status" : item['status'],
        "due_date":item['due_date'],
        "user":str(item['user'])
    }