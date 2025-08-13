from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1:{"name": "Ishant", "age": 20},
    2:{"name": "John", "age": 30}, 
    3:{"name": "Doe", "age": 25}
}

class user(BaseModel):
    name:str
    age:int

@app.put("/user/{user_id}")
def user_update(user_id:int, user_data:user):
    if user_id in user_db:
        user_db[user_id] = user_data.dict()
        return {"message": "User updated successfully", "user": user_db[user_id]}
    else:
        return {"message": "User not found"}
    
class get_user(BaseModel):
    user_id:int
@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id in user_db:
        return {"user": user_db[user_id]}
    else:
        return {"message": "User not found"}    
    
@app.delete("/user/{user_id}")
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return{"message":"user not found"}
    