from pydantic import BaseModel
# from bson import ObjectId
from datetime import date

class Task(BaseModel):
    task_title:str
    task_description:str
    status:str
    due_date:date
    user:str