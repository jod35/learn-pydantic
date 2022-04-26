from pydantic import BaseModel,ValidationError,Field,BaseSettings,SecretStr
from typing import List
from enum import Enum
import json


class Gender(str,Enum):
    MALE="Male"
    FEMALE="Female"
    NON_BINARY="Non Binary"


class Person(BaseModel):
    username:str=Field(default=None,max_length=8,min_length=2)
    email:str=Field(default=None,max_length=80)
    age:int=Field(lt=60,gt=18)
    friends:List[str]=[]
    gender:Gender



data={
    "username":"user",
    "email":"testuser@gmail.com",
    "age":19,
    "friends":["john"],
    "gender":Gender.MALE
}

# try:
#     new_person=Person(**data)

#     schema=new_person.schema()

#     print(json.dumps(schema,indent=4))

# except ValidationError as e:
#     print(e.json())

class Settings(BaseSettings):
    api_key:str
    db_pass:SecretStr

    class Config:
        env_file=".env"
        env_encoding="utf-8"

my_settings=Settings()

print(my_settings)