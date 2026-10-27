
from database.connection import get_connection
from models.player import Player

##Add players to the Players table if not already in there

def player_exists(name):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT 1 FROM Players WHERE Name = ?",
            (name,)
        )
        connection.commit()
        result = cursor.fetchone()


    finally:
        connection.close()

    return result is not None


def add_player(name):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not player_exists(name):
            cursor.execute(
            "INSERT INTO Players (Name, Score) VALUES (?, ?)",
            (name, 0)
            )
        connection.commit()

    finally:
        connection.close()

def get_all_players():
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Players")

        rows = cursor.fetchall()

        players = []

        for row in rows:
            player = Player(
                name=row[1],
                score=row[2],
                player_id=row[0]
            )

            players.append(player)

        return players

    finally:
        connection.close()
###Updating the points in the Players table if a Player wins a week

def update_player_points(points,name):
    connection = get_connection()

    if not player_exists(name):
        return "player does not exist"
    
    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE Players
            SET Score = ?
            WHERE Name = ?
            """,(points,name))

        if cursor.rowcount == 0:
            return "Failed"

        connection.commit()
        return "Success"

    except Exception:
        connection.rollback()
        return "Failed"

    finally:
        connection.close()

def update_weekly_winner(name):
    connection = get_connection()

    if not player_exists(name):
        return "player does not exist"

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE Players
            SET Score = Score + 1
            WHERE Name = ?
            """,(name,))

        if cursor.rowcount == 0:
            return "Failed"

        connection.commit()
        return "Success"

    except Exception:
        connection.rollback()
        return "Failed"

    finally:
        connection.close()

    #print("Player name:", name)
    #print("Rows updated:", cursor.rowcount)


def get_player_leader():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Id, Name, Score
            FROM Players
            WHERE Score = (
                SELECT MAX(Score)
                FROM Players
            )
        """)

        leaders = cursor.fetchall()

        # No players or multiple players tied for first
        if len(leaders) != 1:
            return None

        result = leaders[0]

        player = Player(
            player_id=result[0],
            name=result[1],
            score=result[2]
        )

        return player

    finally:
        connection.close()



def get_player_score(name):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        if not player_exists(name):
            return "player does not exist"

        cursor.execute("""
            SELECT Score
            FROM Players
            WHERE Name = ?
        """,(name,))

        result = cursor.fetchone()

    finally:
        connection.close()

    return int(result[0])