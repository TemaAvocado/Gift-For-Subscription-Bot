import aiosqlite


async def initialize_database():
    async with aiosqlite.connect("database/database.db") as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                telegram_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                subscribe_status BOOLEAN DEFAULT FALSE,
                get_gift BOOLEAN DEFAULT FALSE
            )
        """
        )

        await db.commit()
