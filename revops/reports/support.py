from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from revops.models import SupportRecord

LOW_SATISFACTION = 2.5


async def unhappy_customers(session: AsyncSession, limit: int = 20) -> list[SupportRecord]:
    """Support customers scoring below LOW_SATISFACTION, busiest first."""
    stmt = (
        select(SupportRecord)
        .where(SupportRecord.satisfaction_score < LOW_SATISFACTION)
        .order_by(SupportRecord.ticket_count.desc(), SupportRecord.customer_name)
        .limit(limit)
    )
    return list((await session.scalars(stmt)).all())
