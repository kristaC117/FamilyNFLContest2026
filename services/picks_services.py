from services import player_services
from database import picks_db

from models import picks

def add_picks(name,week_number,picks):
    #First add player if not in the contest yet
    player_services.add_player(name)

    result = picks_db.add_picks(name,week_number,picks)
   
    return result




