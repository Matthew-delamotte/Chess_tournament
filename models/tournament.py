from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter


class Tournament:
    def __init__(self, name, place, date, timer, description, player_dict, current_round=0):
        self.name = name
        self.place = place
        self.date_start = date
        self.round = 4
        self.current_round = current_round
        self.timer = timer
        self.description = description
        self.player_dict = player_dict
        self.end = False

    def append_list_round(self):
        match = Round()
        self.list_round.append(match.generate_match())

    def get_json(self):
        return {'name': self.name,
                'place': self.place,
                'date_start': self.date_start,
                'current_round': self.current_round,
                'round': self.round,
                'timer': self.timer,
                'description': self.description,
                'end': self.end,
                }
