from datetime import date, datetime

from sqlalchemy import Date, DateTime, Float, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from revops.database import Base


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )


class CrmRecord(TimestampMixin, Base):
    """A company as tracked in the CRM."""

    __tablename__ = "crm_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    company_name: Mapped[str] = mapped_column(String, nullable=False)
    industry: Mapped[str | None] = mapped_column(String, nullable=True)
    annual_revenue: Mapped[float | None] = mapped_column(Float, nullable=True)
    owner_email: Mapped[str | None] = mapped_column(String, nullable=True)
    health_rating: Mapped[int | None] = mapped_column(Integer, nullable=True)


class SupportRecord(TimestampMixin, Base):
    """A customer's ticket history from the support desk."""

    __tablename__ = "support_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name: Mapped[str] = mapped_column(String, nullable=False)
    ticket_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    last_ticket_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    satisfaction_score: Mapped[float | None] = mapped_column(Float, nullable=True)


class FinanceContract(TimestampMixin, Base):
    """A contract from the finance system."""

    __tablename__ = "finance_contracts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    account_name: Mapped[str] = mapped_column(String, nullable=False)
    contract_value: Mapped[float | None] = mapped_column(Float, nullable=True)
    renewal_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    payment_status: Mapped[str | None] = mapped_column(String, nullable=True)
