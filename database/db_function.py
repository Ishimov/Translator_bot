import sqlite3 as sq

def db_start() -> None:
    global db, cur
    db = sq.connect('Language_Settings.db')
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, language TEXT)")
    db.commit()

async def create_profile(user_id) -> None:
    user = cur.execute(f"SELECT 1 FROM profile WHERE user_id == '{user_id}'").fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?)", (user_id, 'EN'))
        db.commit()

async def edit_profile(user_id, lang) -> None:
    cur.execute(f"UPDATE profile SET language = '{lang}' WHERE user_id == '{user_id}'")
    db.commit()

async def language_select(user_id) -> str:
    lang = cur.execute(f"SELECT language FROM profile WHERE user_id == '{user_id}'").fetchone()
    return lang[0]