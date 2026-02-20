from pydantic import BaseModel
class Bank(BaseModel):
    id:int
    name:str
    balance:float

from typing import Optional
class Bankupdate(BaseModel):
    name:Optional[str]=None
    balance:Optional[float]=None
        