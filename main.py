from fastapi import FastAPI,HTTPException,status # fastapi to create server,Http exception for error message 
# and status is for error code or success code 
from pydantic import BaseModel # for the structure of input data

app=FastAPI()

class Bank(BaseModel):
    id:int
    name:str
    balance:float
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
            updated_account.id=account_id
            Accounts[i]=updated_account
            return{"message":f"The account with id:{account_id} is updated successfully",
                   "account":updated_account}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The account with this id:{account_id} is not found")      