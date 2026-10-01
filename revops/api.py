from contextlib import asynccontextmanager
from datetime import date
from typing import Annotated

from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from revops.database import get_db
from revops.main import init_db
from revops.models import FinanceContract


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="RevOps", lifespan=lifespan)


class AccountFinancials(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    account_name: str
    contract_value: float | None
    renewal_date: date | None
    payment_status: str | None


@app.get("/account-financials", response_model=list[AccountFinancials])
async def list_account_financials(
    db: Annotated[AsyncSession, Depends(get_db)],
    payment_status: str | None = None,
    limit: Annotated[int, Query(ge=1, le=500)] = 100,
    offset: Annotated[int, Query(ge=0)] = 0,
):
    stmt = select(FinanceContract).order_by(FinanceContract.id).limit(limit).offset(offset)
    if payment_status:
        stmt = stmt.where(FinanceContract.payment_status == payment_status)
    return (await db.scalars(stmt)).all()
