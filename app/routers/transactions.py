from fastapi import APIRouter

from models import  Transaction


router= APIRouter(tags=["Transactions"])

@router.post("/transactions")
async def create_transaction(transaction_data: Transaction):
    return transaction_data
