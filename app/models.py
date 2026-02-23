# This file includes the actual data structure inside the bank
from pydantic import BaseModel
class Bank(BaseModel):
    id:int
    name:str
    balance:float

