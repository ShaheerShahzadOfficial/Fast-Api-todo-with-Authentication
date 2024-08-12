from fastapi import FastAPI
from routes.user import userRouter
from routes.token import taskRouter

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}

app.include_router(userRouter,prefix='/user')
app.include_router(taskRouter,prefix='/task')