from services import player_services
from services import setup_services

from UI.contest_UI import run_contest_UI

def main():

    """Set up the tables for the program"""
    results = setup_services.setup_tables()
    run_contest_UI()

if __name__ == "__main__":
    main()