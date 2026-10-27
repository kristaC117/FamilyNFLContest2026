
from database.connection import get_connection
from models.picks import Picks
from services import player_services

# This is my Picks Database code


def add_picks(name, week_number, picks):

    if not player_services.player_exists(name):
        return "Player does not exist"

    pick_record = Picks(
        name=name,
        week_number=week_number,
        picks=picks
    )

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # Check whether picks already exist
        cursor.execute("""
            SELECT *
            FROM Picks
            WHERE Name = ?
              AND WeekNumber = ?
        """, (name, week_number))

        # Save the column names before another query is executed
        column_names = [
            column[0] for column in cursor.description
        ]

        existing_record = cursor.fetchone()

        if existing_record is None:
            add_picks_new_Player(connection, pick_record)
        else:
            add_picks_existing_player(
                connection,
                pick_record,
                column_names,
                existing_record
            )

        # Commit changes from either function
        connection.commit()

        # Verify what is saved
        cursor.execute("""
            SELECT *
            FROM Picks
            WHERE Name = ? AND WeekNumber = ?
        """, (name, week_number))

        #print("Saved picks:", cursor.fetchone())

        return pick_record

    except Exception as e:
        connection.rollback()
        print("Error saving picks:", e)
        raise

    finally:
        connection.close()


def add_picks_existing_player(
    connection, pick_record, column_names, existing_record
):
    cursor = connection.cursor()

    # Check all 18 games
    for i in range(1, 18):

        game_column = f"Game{i}"

        # Get the new pick from the Python object
        new_pick = getattr(pick_record, f"game{i}")

        # Get the existing pick from the database row
        column_index = column_names.index(game_column)
        existing_pick = existing_record[column_index]

        if (new_pick is not None):
            len_new_pick = len(new_pick)

        else:
            len_new_pick = 0

        # Update only if a new, different pick was submitted
        if (len_new_pick > 1 and new_pick != existing_pick):

            cursor.execute(
                f"""
                UPDATE Picks
                SET {game_column} = ?
                WHERE Name = ?
                  AND WeekNumber = ?
                """,
                (
                    new_pick,
                    pick_record.name,
                    pick_record.weeknumber
                )
            )

            print(
               # f"{game_column}: "
                #f"{existing_pick} -> {new_pick}"
            )


def add_picks_new_Player(connection, pick_record):

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Picks (
            Name, WeekNumber,
            Game1, Game2, Game3, Game4, Game5, Game6,
            Game7, Game8, Game9, Game10, Game11, Game12,
            Game13, Game14, Game15, Game16, Game17, Game18
        )
        VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """, (
        pick_record.name,
        pick_record.weeknumber,
        pick_record.game1,
        pick_record.game2,
        pick_record.game3,
        pick_record.game4,
        pick_record.game5,
        pick_record.game6,
        pick_record.game7,
        pick_record.game8,
        pick_record.game9,
        pick_record.game10,
        pick_record.game11,
        pick_record.game12,
        pick_record.game13,
        pick_record.game14,
        pick_record.game15,
        pick_record.game16,
        pick_record.game17
    ))

