from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from revops.models import CrmRecord

LOW_HEALTH_RATING = 4


async def low_health_companies(session: AsyncSession, limit: int = 20) -> list[CrmRecord]:
    """CRM companies rated at or below LOW_HEALTH_RATING, worst first."""
    stmt = (
        select(CrmRecord)
        .where(CrmRecord.health_rating <= LOW_HEALTH_RATING)
        .order_by(CrmRecord.health_rating, CrmRecord.company_name)
        .limit(limit)
    )
    return list((await session.scalars(stmt)).all())
