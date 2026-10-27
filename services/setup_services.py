from database import setup_db


def setup_tables():

    result = setup_db.create_tables()

    return result
