from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter

class Round:
    def __init__(self, players_list):
        self.players_list = players_list
        self.pairs = []

    @classmethod
    def sort_player_by_ranking(cls, tournament):
        # Triez tous les joueurs par leurs classement
        sorted_player = list(tournament.player_dict.values())
        sorted_player.sort(key=attrgetter('rank'))
        return sorted_player

    @classmethod
    def sort_player_by_score(cls, tournament):
        # Triez les joueur par le score:
        sorted_player_by_score = list(tournament.player_dict.values())
        sorted_player_by_score.sort(key=attrgetter('score'), reverse=True)
        return sorted_player_by_score

    #____________________ Old version_____________
    # def sort_player_by_ranking(self):
    #     # Triez tous les joueurs par leurs classement
    #     sorted_player = sorted(self.players_list, key=attrgetter('rank'))
    #     return sorted_player

    def list_division(self, tournament):
        # division en 2 groupes: un superieur et un inferieur
        sorted_player = self.sort_player_by_ranking(tournament)
        length = len(sorted_player)
        middle_index = length // 2

        superior_list = sorted_player[:middle_index]
        inferior_list = sorted_player[middle_index:]
        return superior_list, inferior_list

    @classmethod
    def generate_match_by_score(self, sorted_player, match_list):
        player1_list = sorted_player[::2]
        player2_list = sorted_player[1::2]
        matchs_list = list(zip(player1_list, player2_list))
        return matchs_list

    def generate_match_by_list(self, tournament):
        # Jumelez meilleur joueur des deux moitier superieur et inférieur
        superior_list, inferior_list = self.list_division(tournament)
        match_list = list(zip(superior_list, inferior_list))
        return match_list