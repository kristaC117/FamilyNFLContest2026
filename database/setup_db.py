from database.connection import get_connection

### CREATE THE TABLES IF NEEDED: Players for tracking Player name and their points
### and Games for each game per week roughly 14-16 per week

def create_tables():
    create_players()
    create_games()
    create_picks()

def create_players():
    connection = get_connection()
    results = False
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Players
            (Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Score INTEGER NOT NULL DEFAULT 0
            )
        """)

        connection.commit()
        results = True
    finally:
        connection.close()

    return results

def create_games():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Games
            (Id INTEGER PRIMARY KEY AUTOINCREMENT,
            WeekNumber INTEGER NOT NULL,
            AwayTeam TEXT NOT NULL,
            HomeTeam TEXT NOT NULL,
            GameTime DATETIME NOT NULL,
            GameDate DATETIME NOT NULL,
            Results TEXT DEFAULT "")
        """)

        connection.commit()

    finally:
        connection.close()


def create_picks():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Picks
            (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                WeekNumber INTEGER NOT NULL,
                Game1 TEXT,
                Game2 TEXT,
                Game3 TEXT,
                Game4 TEXT,
                Game5 TEXT,
                Game6 TEXT,
                Game7 TEXT,
                Game8 TEXT,
                Game9 TEXT,
                Game10 TEXT,
                Game11 TEXT,
                Game12 TEXT,
                Game13 TEXT,
                Game14 TEXT,
                Game15 TEXT,
                Game16 TEXT,
                Game17 TEXT
            )
        """)

        connection.commit()

    finally:
        connection.close()


