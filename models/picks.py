
class Picks:
    def __init__(self, name, week_number, picks=None, id=None):
        self.id = id
        self.name = name
        self.weeknumber = week_number

        # Initialize the 17 game picks
        for i in range(1, 18):
            setattr(self, f"game{i}", None)

        # Assign the supplied picks to the game properties
        if picks is not None:
            for i, pick in enumerate(picks, start=1):
                if i <= 17:
                    setattr(self, f"game{i}", pick)


