from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter

from models import Player
from models import Gender

def make_player_list():
    player1 = Player('Edd', datetime(1995, 6, 28), Gender.MALE, 2)
    player2 = Player('Matt', datetime(1995, 12, 7), Gender.MALE, 1)
    player3 = Player('Paul', datetime(1995, 5, 25), Gender.MALE, 3)
    player4 = Player('Thony', datetime(1995, 8, 9), Gender.MALE, 4)
    player5 = Player('Seb', datetime(1983, 2, 5), Gender.MALE, 5)
    player6 = Player('Joddie', datetime(1998, 2, 6), Gender.FEMALE, 6)
    player7 = Player('Manon', datetime(1995, 6, 28), Gender.MALE, 7)
    player8 = Player('Cécile', datetime(1978, 6, 15), Gender.FEMALE, 8)
    list_player = [player1, player2, player3, player4, player5, player6, player7, player8]
    return list_player

pprint(make_player_list())