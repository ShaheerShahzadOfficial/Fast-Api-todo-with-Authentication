from fastapi import APIRouter
from models.user import User
from config.db import userCollection
import jwt
import bcrypt
from schema.user import userEntity

userRouter = APIRouter()


@userRouter.post("/register")
async def register(user: User):
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    user.password = hashed_password

    userCollection.insert_one(dict(user))
    return {"message": "User Registration Successfull"}


@userRouter.post("/login")
async def login(user: User):
    try:
        user_data = userCollection.find_one({"email": user.email})

        if not user_data:
            return {"message": "user not found"}

        if not bcrypt.checkpw(user.password.encode("utf-8"), user_data["password"]):
            return {"message": "Invalid Credential"}
        print(str(user_data))
        payload = {"id": str(user_data["_id"]), "email": user_data["email"]}

        header = {"alg": "HS256", "typ": "JWT"}

        secret = "Ravipass"
        encoded_jwt = jwt.encode(payload, secret, algorithm="HS256", headers=header)

        return {"message": "Login Successful", "token": encoded_jwt, "user": userEntity(user_data)}
    except Exception as e:
        print("======== > ", e,'============>' )
