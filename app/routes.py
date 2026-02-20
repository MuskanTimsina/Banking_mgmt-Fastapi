from fastapi import APIRouter,HTTPException,status
from app.models import Bank,Bankupdate

router=APIRouter()
Accounts=[]

@router.get("/banks/{account_id}")
def get_bankdetails(account_id:int):
    for b in Accounts:
        if b.id==account_id:
            return {"message":".................BANK MANAGEMENT SYSTEM..................",
                    "account":b}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The bank account with id:{account_id} is not found")

@router.get("/banks")
def get_all_acc():
    if not Accounts:
        return{"message":"No any account is available",
               "accounts":[]}
    else:
        return{"message":".................BANK MANAGEMENT SYSTEM..................",
               "accounts":Accounts}
    
@router.post("/banks",status_code=status.HTTP_201_CREATED)
def create_account(account:Bank):
    for b in Accounts:
        if b.id==account.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"The bank account with id:{account.id} is already exist") 
    Accounts.append(account)
    return{"message":f"The account with id:{account.id} is created sucessfully",
           "Bank":account}

@router.put("/banks/{account_id}")
def update_account(account_id:int,updated_account:Bank):
    for i,b in enumerate(Accounts):
        if b.id==account_id:
            Warning=None
            if account_id !=updated_account.id:
                Warning="you are not supposed change the id of account !"
                updated_account.id=account_id
            Accounts[i]=updated_account
            response={"message":f"The account with id:{account_id} is updated sucessfully",
                      "updated_account":updated_account} 
            if Warning is not None:
                response["warning"]=Warning
            return response          
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The account with id:{account_id} is not found")

@router.patch("/banks/{account_id}")
def patch_account(account_id:int,update_account:Bankupdate):
    if hasattr(update_account,"id") and update_account.id is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="you are not suppose to change the id of an account")
    for i,b in enumerate(Accounts):
        if b.id==account_id:
            if update_account.name is not None:
                b.name=update_account.name
            if update_account.balance is not None:
                b.balance=update_account.balance
            Accounts[i]=b
            return{"message":f"The account with id:{account_id} is updated sucessfully",
                   "account":b}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The account with id:{account_id} is not found")            

@router.delete("banks/{account_id}")
def delete_account(account_id:int):
    for i , b in enumerate(Accounts):
        if b.id==account_id:
            Accounts.pop(i)
            return {"message":f"The account with id:{account_id} is deleted sucessfully "}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"The account with id:{account_id} is not found")    