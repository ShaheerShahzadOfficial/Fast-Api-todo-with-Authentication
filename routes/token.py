from fastapi import APIRouter, Depends
from models.task import Task
from config.db import taskCollection
from schema.task import taskEntity
from middleware.auth import JWTBearer, decodeJWT
from datetime import date
from bson import ObjectId

taskRouter = APIRouter()


@taskRouter.post("/createTask")
async def create_task(task: Task, dependencies: JWTBearer = Depends(JWTBearer())):
    token = decodeJWT(dependencies)["id"]
    if not token:
        return {"Token not found"}
    task.user = token
    format_string = "%Y-%m-%d"
    task.due_date = date.strftime(task.due_date, format_string)
    print(task)
    taskCollection.insert_one(dict(task))
    return {"message": "Task Created Successfully"}


@taskRouter.get("/getTasks")
async def get_tasks(dependencies: JWTBearer = Depends(JWTBearer())):
    token = decodeJWT(dependencies)["id"]
    tasks: list[Task] = taskCollection.find({"user": token})
    print("len(tasks)", tasks)
    allTasks = []
    for task in tasks:
        allTasks.append(taskEntity(task))

    return {"task": allTasks}


@taskRouter.put("/update/{id}")
async def update(id: str, task: Task):
    format_string = "%Y-%m-%d"
    task.due_date = date.strftime(task.due_date, format_string)
    taskCollection.update_one({"_id": ObjectId(id)}, {"$set": dict(task)})
    return {"message": "Task Updated Successfully"}


@taskRouter.delete("/delete/{id}")
async def delete(id: str):
    taskCollection.delete_one({"_id": ObjectId(id)})
    return {"message": "Task deleted Successfully"}
