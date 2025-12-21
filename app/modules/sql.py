import sqlite3
from pathlib import Path

baseDir = Path(__file__).resolve().parents[1]
dbDir = baseDir / "db"
dbFile = dbDir / "pos.db"


def initDb():
    if dbFile.exists():
        print("Database already exists.. skipping initialisation.")
        return

    # check if directory exists
    dbDir.mkdir(exist_ok=True)

    try:
        with sqlite3.connect(dbFile) as conn:
            cursor = conn.cursor()

            # Enforce foreign keys (SQLite default is OFF)
            cursor.execute("PRAGMA foreign_keys = ON;")

            # feed the schema
            with open(dbDir / "schema.sql", "r", encoding="utf-8") as f:
                cursor.executescript(f.read())

            # feed the menu
            with open(dbDir / "menu-seed.sql", "r", encoding="utf-8") as f:
                cursor.executescript(f.read())

            # with-context commits automatically if no exception
            print("Database initialized successfully.")

    except sqlite3.Error as e:
        if dbFile.exists():
            dbFile.unlink(missing_ok=True)
        raise RuntimeError(f"Database initalisation failed: {e}") from e
