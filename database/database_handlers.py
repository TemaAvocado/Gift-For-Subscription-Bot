import aiosqlite


async def add_user(telegram_id: int, username: str, first_name: str):
    async with aiosqlite.connect("database/database.db") as db:
        await db.execute(
            """
            INSERT INTO users (telegram_id, username, first_name)
            VALUES (?, ?, ?)
            ON CONFLICT(telegram_id) DO NOTHING
        """,
            (telegram_id, username, first_name),
        )
        await db.commit()

async def get_user(telegram_id: int):
    async with aiosqlite.connect("database/database.db") as db:
        cursor = await db.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        row = await cursor.fetchone()

        if row is None:
            return None

        user = {
            "telegram_id": row[0],
            "username": row[1],
            "first_name": row[2],
            "subscribe_status": bool(row[3]),
            "gift_status": bool(row[4])
        }
        return user
    
async def update_subscribe_status(telegram_id: int, subscribe_status: bool):
    async with aiosqlite.connect("database/database.db") as db:
        await db.execute("""
            UPDATE users
            SET subscribe_status = ?
            WHERE telegram_id = ?
        """, (subscribe_status, telegram_id))
        await db.commit()

async def update_get_gift_status(telegram_id: int, get_gift: bool):
    async with aiosqlite.connect("database/database.db") as db:
        await db.execute("""
            UPDATE users
            SET get_gift = ?
            WHERE telegram_id = ?
        """, (get_gift, telegram_id))
        await db.commit()

    