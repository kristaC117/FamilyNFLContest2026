class Player:

    def __init__(self, name, score=0, player_id=None):
        self.id = player_id
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name} - Score: {self.score}"