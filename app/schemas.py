# This file is a for a data validation,i.e what user send data 

from pydantic import BaseModel

class Bankcreate(BaseModel):
    id:int
    name:str
    balance:str

class Bankupdate(BaseModel):
    name:str|None=None
    balance:float|None=None    


