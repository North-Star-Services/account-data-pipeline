# RevOps Service

Internal service over our CRM, support desk, and finance data. Holds a table
per upstream system, recent exports from each, and the reporting code and API
built on top of them.

## Layout

- `revops/models.py` — one table per upstream system.
- `revops/database.py` — async SQLAlchemy engine and session.
- `revops/loaders/` — file readers.
- `revops/reports/` — reporting queries (CRM health, support satisfaction).
- `revops/api.py` — read-only HTTP API (account financials).
- `data/` — exports from the CRM, support desk, and finance systems.

## Setup

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create the database
python -m revops.main
```

## Running Tests

```bash
pytest
```

## Running the API

```bash
uvicorn revops.api:app --reload
```

## Output

The database lives at `output/app.db` (SQLite) and is created on first run.
