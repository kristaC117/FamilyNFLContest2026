import sqlite3

from pathlib import Path

# Get the project folder (the folder above database)
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Path to the SQLite database file
DATABASE_NAME = PROJECT_DIR / "nfl_pickem.db"


def get_connection():
    """Create and return a connection to the database."""
    connection = sqlite3.connect(DATABASE_NAME)
    return connection