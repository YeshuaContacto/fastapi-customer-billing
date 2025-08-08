from fastapi import APIRouter, status

from models import  Invoice 

router= APIRouter(tags=["Invoices"])

@router.post("/invoices", status_code=status.HTTP_201_CREATED)
async def create_invoice(invoice_data: Invoice):
    return invoice_data