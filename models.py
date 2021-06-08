from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter


class Player:
    def __init__(self, name, birthday, gender, rank):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.ranking = rank
        self.score = 0

    def get_age(self):
        return int((datetime.now() - self.birthday).days/365.25)

    # Autre methode pour get_age
    # def get_age(self, today=datetime.now()):
    #     birthday = self.birthday
    #     age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    #     return age

    def get_ranking(self):
        return self.ranking

    def update_ranking(self):
        return self.ranking

    def update_score(self, result):
        # while self.valid_result:
        # point_to_add = 0
        # result = input("Enter result: ")
        if result == 'win':
            self.score += 1
            pprint('+1 points added')
        elif result == 'draw':
            self.score += 0.5
            pprint('+0.5 points added')
        elif result == 'lose':
            pprint('No point added')
        else:
            raise Exception("Sorry, enter valid result")

    def reset_score(self):
        pass

    def get_attribute(self):
        return {'name': self.name,
                'birthday': self.birthday,
                'gender': self.gender,
                'ranking': self.ranking,
                }

    # (Manipulate ranking)


class Tournament:
    LIST_ROUND = []

    def __init__(self, name, place, players, timer, description, date=datetime.now(), round=4):
        self.name = name
        self.place = place
        self.date = date
        self.round = round
        self.players = players
        self.timer = timer
        self.description = description
        self.current_round = 0
        self.list_round = []

    def append_list_round(self):
        pass

    def instance_round(self, pair_match):
        # instancier un round
        # append le round dans le list_round
        return

    # TODO: append list_round with instance round

    def get_attributes(self):
        return {'name': self.name,
                'place': self.place,
                'date': self.date,
                'round': self.round,
                'players': self.players,
                'timer': self.timer,
                'description': self.description,
                }


class Round:
    def __init__(self, name, players_list, daytime_start=datetime.now):
        self.name = name
        self.players_list = players_list
        self.start = daytime_start

    def generate_match(self):
        # Use player list for generate match during the round
        pass

    def update_players_result_in_round(self):
        pass

    def update_match_result(self):
        pass

    def generate_next_round(self):
        pass

    def update_ranking(self):
        pass

    def get_daytime_of_start(self):
        pass

    def get_daytime_of_end(self):
        pass

    # match = ([player1, Score], [player2, Score])
    # multipe_match = []
    # multipe_match.append(match)


class Algorythm:
    def __init__(self, player_list):
        self.list_player = player_list
        self.pairs = []

    def sort_player(self):
        # Triez tous les joueurs par leurs classement
        sorted_player = sorted(self.list_player, key=attrgetter('ranking'))
        return sorted_player

    def list_division(self):
        # division en 2 groupes: un superieur et un inferieur
        sorted_player = self.sort_player()
        length = len(sorted_player)
        middle_index = length // 2

        superior_list = sorted_player[:middle_index]
        inferior_list = sorted_player[middle_index:]
        return superior_list, inferior_list

    def generate_pair(self):
        # Jumelez meilleur joueur des deux moitier superieur et inférieur
        superior_list, inferior_list = self.list_division()
        match_list = list(zip(superior_list, inferior_list))
        return match_list
        # count = 1
        # for round in a:
        #     pprint("New round " + str(count))
        #     count += 1
        #
        # return round

    def start_algorythm(self):
        # Triez tous les joueurs par leurs classement
        # division en 2 groupes: un superieur et un inferieur

        # Jumelez meilleur joueur des deux moitier superieur et inférieur
        # Jumelez joueur 2 superieur avec joueur 2 inferieur
        # ect jusqu'a que tout les joueur est été jumelez
        # pprint(self.make_pairs_round())

        # etape 3
        # Nouveau tour: triez les joueur par leurs nombre total de point
        # Si deux joueurs on le meme nombre de points alors triez par leurs ranking

        #  etape 4
        # Associez le joueur 1 et 2
        # Associez le joueur 3 et 4
        # ect
        # Si un joueur a deja joué avec le meme (exemple 1 et 2), alors l'associez avec joueur 3

        # repetez etape 3 et 4 jusqu'a la fin du tournoi

        # (en plus) tirez au sort qui joue blanc et noir
        pass


class Timer(Enum):
    BULLET = 0
    QUICK = 1
    BLITZ = 2


class Gender(Enum):
    MALE = 0
    FEMALE = 1


# class Score:
#     # WIN = 0
#     # DRAW = 1
#     # LOSE = 2
#     def __init__(self, score):
#         self.score = score
#         self.valid_result = True
#
#     def ask_result(self):
#         while self.valid_result:
#             # point_to_add = 0
#             result = input("Enter result: ")
#             if result == 'win':
#                 self.score = self.score + 1
#                 self.valid_result = False
#                 pprint('+1 points added')
#             elif result == 'draw':
#                 self.score = self.score + 0.5
#                 self.valid_result = False
#                 pprint('+0.5 points added')
#             elif result == 'lose':
#                 pprint('No point added')
#                 self.valid_result = False
#             else:
#                 pprint('Enter valid result (win, draw or lose)')
#
#     def get_score(self):
#         pprint(self.score)
#         return

