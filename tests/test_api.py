from fastapi.testclient import TestClient

from revops.api import app
from revops.database import get_db
from tests.conftest import make_session_factory


async def empty_db():
    engine, factory = await make_session_factory()
    async with factory() as s:
        yield s
    await engine.dispose()


def test_account_financials_returns_empty_list_on_empty_table():
    app.dependency_overrides[get_db] = empty_db
    try:
        response = TestClient(app).get("/account-financials")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json() == []
