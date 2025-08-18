import time
from typing import Annotated
import zoneinfo
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from db import create_all_tables
from .routers import customers, transactions, invoices, plans

app = FastAPI(lifespan=create_all_tables)

app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(invoices.router)
app.include_router(plans.router)


@app.middleware("http")
async def log_request_time(request: Request, call_netx):
    start_time = time.time()
    response = await call_netx(request)
    process_time = time.time() - start_time
    print(f"Request: {request.url} completed in: {process_time:.4f} seconds")
    return response


security = HTTPBasic()

@app.get('/')
async def root(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    print(credentials)
    if credentials.username == "yeshua" and credentials.password == "qwerty":
        return {"message": f"Hola, {credentials.username}"}
    else:
       raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time/{iso_code}")
async def get_time_by_iso_code(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return{"time": datetime.now(tz)}
