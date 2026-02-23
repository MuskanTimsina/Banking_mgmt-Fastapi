# This file include the routes for HTTP request
from fastapi import APIRouter,HTTPException,status
from app.schemas import Bankcreate,Bankupdate
from app.services import (
    create_account_service,
    get_account_by_id_service,
    get_all_account_service,
    delete_account_service,
    update_account_service,
    patch_account_service
)


router=APIRouter()
Accounts=[]

@router.get("/banks/{account_id}")
def get_bankdetails(account_id:int):
    return get_account_by_id_service(account_id)

@router.get("/banks")
def get_all_acc():
    return get_all_account_service()

@router.post("/banks",status_code=status.HTTP_201_CREATED)
def create_account(account:Bankcreate):
    return create_account_service(account)

@router.put("/banks/{account_id}")
def update_account(account_id:int,updated_account:Bank):
    return update_account_service(account_id,updated_account)

@router.patch("/banks/{account_id}")
def patch_account(account_id:int,update_account:Bankupdate):
    return patch_account_service(account_id,update_account)
    
@router.delete("banks/{account_id}")
def delete_account(account_id:int):
    return delete_account_service(account_id)