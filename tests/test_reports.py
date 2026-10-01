from datetime import date

import pytest

from revops.models import CrmRecord, SupportRecord
from revops.reports.crm import low_health_companies
from revops.reports.support import unhappy_customers


@pytest.mark.asyncio
async def test_low_health_companies_returns_only_low_ratings(session):
    session.add_all(
        [
            CrmRecord(company_name="Struggling Co", health_rating=2),
            CrmRecord(company_name="Borderline Co", health_rating=4),
            CrmRecord(company_name="Thriving Co", health_rating=9),
        ]
    )
    await session.commit()

    names = [r.company_name for r in await low_health_companies(session)]

    assert names == ["Struggling Co", "Borderline Co"]


@pytest.mark.asyncio
async def test_unhappy_customers_orders_by_ticket_volume(session):
    session.add_all(
        [
            SupportRecord(customer_name="Quiet Co", ticket_count=3, satisfaction_score=1.5,
                          last_ticket_date=date(2026, 1, 5)),
            SupportRecord(customer_name="Noisy Co", ticket_count=40, satisfaction_score=2.0,
                          last_ticket_date=date(2026, 1, 9)),
            SupportRecord(customer_name="Happy Co", ticket_count=12, satisfaction_score=4.8,
                          last_ticket_date=date(2026, 1, 2)),
        ]
    )
    await session.commit()

    names = [r.customer_name for r in await unhappy_customers(session)]

    assert names == ["Noisy Co", "Quiet Co"]
