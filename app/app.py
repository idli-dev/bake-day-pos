from .modules.sql import initDb


def main():
    try:
        initDb()
    except Exception as e:
        print(e)
        return

    print("Database created.")
