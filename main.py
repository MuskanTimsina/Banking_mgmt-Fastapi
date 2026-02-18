from fastapi import FastAPI,HTTPException,status # fastapi to create server,Http exception for error message 
# and status is for error code or success code 
from pydantic import BaseModel # for the structure of input data
from typing import Optional

app=FastAPI()

class Bank(BaseModel):
    id:int
    name:str
    balance:float
class Bankupdate(BaseModel):
    name:Optional[str]=None
    balance:Optional[float]=None

Accounts=[] #list to store the accounts details

@app.get("/banks/{account_id}")
def get_bankdetails(account_id:int):
    for b in Accounts:
        if b.id==account_id:
             return{"message":"..................Bank Management system..................",
                   "banks":b}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The bank detail with id:{account_id} is not found")

@app.get("/banks")
def get_all_acc():
    if not Accounts:
        return{"message":"No any account is available",
               "account":[]}
    else:
        return{"message":"..............BANK MANAGEMENT SYSTEM..............",
               "banks":Accounts}
    
@app.post("/banks",status_code=status.HTTP_201_CREATED)
def create_account(account:Bank):
    for b in Accounts:
        if b.id==account.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The account with id:{account.id} is already exist.")
    Accounts.append(account)
    return{"message":f"The account with id:{account.id} is created successfully!",
           "banks":account}

@app.delete("/banks/{account_id}")
def delete_account(account_id:int):
    for i, b in enumerate(Accounts):
        if b.id==account_id:
            Accounts.pop(i)
            return{"message":f"The account with id:{account_id} is deleted sucessfully!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The account with id:{account_id} is not found") 

@app.put("/banks/{account_id}")
def update_account(account_id:int,updated_account:Bank):
    for i, b in enumerate(Accounts):
        if b.id==account_id:
            warning=None
            if updated_account.id!=account_id:
                warning="The id of account cannot be changed,it remain same !"
                updated_account.id=account_id
            Accounts[i]=updated_account
            response={"message":f"The account with id:{account_id} is updated successfully",
                   "account":updated_account}
            if warning is not None:
                response["warning"]=warning
            return response    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The account with this id:{account_id} is not found")

@app.patch("/banks/{account_id}")
def patch_account(account_id:int,update_account:Bankupdate):
    if hasattr(update_account,"id") and update_account.id is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="You are not suppose to change the id of an account")
    for i,b in enumerate(Accounts):    
        if b.id==account_id:
            if update_account.name is not None:
                b.name=update_account.name
            if update_account.balance is not None:
                b.balance=update_account.balance  
            Accounts[i]=b
            return{"message":f"The account with id:{account_id} is updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The account with this id:{account_id} is not found")        
