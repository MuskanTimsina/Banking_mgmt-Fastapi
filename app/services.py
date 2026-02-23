# This file include all logic for the operaion.
from fastapi import HTTPException,status
from app.models import Bank
from app.schemas import Bankcreate,Bankupdate

Accounts=[]
# function for creating account.
def create_account_service(account:Bankcreate):
    for b in Accounts:
        if b.id==account.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"The account with this id:{account.id} is already exist!")
    new_account=Bank(
        id=account.id,
        name=account.name,
        balance=account.balance
    )
    Accounts.append(new_account)
    return{"message":"..............BANK MANAGEMENT SYSTEM..............",
           "accounts":new_account}   
 
# function for getting account details through id.
def get_account_by_id_service(account_id: int):

    # Search account
    for b in Accounts:
        if b.id == account_id:
          return{"message":"..............BANK MANAGEMENT SYSTEM..............",
                 "account":b
            } 
    # If not found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Account with id {account_id} not found"
    )

# function for getting all account
def get_all_account_service():
    if not Accounts:
        return{"message":"No any account is available",
               "accounts":[]}
    else:
        return{"message":".................BANK MANAGEMENT SYSTEM..................",
               "accounts":Accounts}
 # function for deleting account
def delete_account_service(account_id: int):

    for i, b in enumerate(Accounts):
        if b.id == account_id:
            Accounts.pop(i)
            return {"message": f"Account with id {account_id} deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Account with id {account_id} not found"
    )   
# update account through put.
def update_account_service(account_id: int, updated_account: Bankcreate):

    for i, b in enumerate(Accounts):

        if b.id == account_id:

            warning = None

            # Prevent ID change
            if updated_account.id != account_id:
                warning = "Account ID cannot be changed"
                updated_account.id = account_id

            # Replace account
            Accounts[i] = Bank(
                id=updated_account.id,
                name=updated_account.name,
                balance=updated_account.balance
            )

            response = {
                "message": f"Account with id {account_id} updated successfully",
                "account": Accounts[i]
            }

            if warning:
                response["warning"] = warning

            return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Account with id {account_id} not found"
    )
# function for updating account through patch.
def patch_account_service(account_id:int,update_account:Bankupdate):
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
