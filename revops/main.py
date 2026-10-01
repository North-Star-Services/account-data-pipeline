import asyncio

from revops import models  # noqa: F401  (registers tables on Base.metadata)
from revops.database import Base, engine


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def main():
    asyncio.run(init_db())
    print("Database ready at output/app.db")


if __name__ == "__main__":
    main()
