from pathlib import Path

from revops.loaders.csv_loader import load_csv

CRM_FILE = Path(__file__).resolve().parent.parent / "data" / "crm_accounts.csv"


def test_load_csv_reads_crm_accounts():
    rows = load_csv(str(CRM_FILE))

    assert isinstance(rows, list)
    assert rows
    assert isinstance(rows[0], dict)
    assert set(rows[0]) == {
        "company_name",
        "industry",
        "annual_revenue",
        "account_owner_email",
        "health_rating",
    }
