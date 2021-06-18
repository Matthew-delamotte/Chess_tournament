class Player:
    def __init__(self, name, birthday, gender, rank, score):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.score = score

    def get_ranking(self):
        return self.ranking

    @classmethod
    def update_ranking(cls, player_list):
        for player in player_list:
            player.rank = player_list.index(player)

    def get_json(self):
        return {
            "name": self.name,
            "birthday": self.birthday,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
        }
