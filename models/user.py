from pydantic import BaseModel

class User(BaseModel):
    user_name:str
    password:str
    email:str