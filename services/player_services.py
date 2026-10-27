from database import players_db
from models import player

def player_exists(name):
    return players_db.player_exists(name)

def add_player(name):
    players_db.add_player(name)

def get_all_players():
    return players_db.get_all_players()

def get_player_count():
    return len(players_db.get_all_players())

def update_player_points(points, name):
    return players_db.update_player_points(points,name)

def update_weekly_winner(name):
    players_db.update_weekly_winner(name)

def get_player_leader():
    return players_db.get_player_leader()

def get_player_score(name):
    return players_db.get_player_score(name)
   
   