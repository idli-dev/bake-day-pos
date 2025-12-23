from app.modules.sql import initDb


def main():
    try:
        initDb()
    except Exception as e:
        print(f"An error has occured: {e}")
        return

    print("\nDatabase created.")
