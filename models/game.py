
class Game:
    def __init__(
        self,
        game_id=None,
        week_number=0,
        away_team="",
        home_team="",
        game_time=None,
        game_date=None,
        results=""
    ):
        self.game_id = game_id
        self.week_number = week_number
        self.away_team = away_team
        self.home_team = home_team
        self.game_time = game_time
        self.game_date = game_date
        self.results = results


