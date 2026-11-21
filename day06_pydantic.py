from pydantic import Field, BaseModel, ValidationError

class User(BaseModel):
    username: str = Field(description="用户名")
    age: int = Field(gt = 0, lt = 150, description="年龄")

try:
    user1 = User(username = "duck", age = -5)
except ValidationError as e:
    print(e)
