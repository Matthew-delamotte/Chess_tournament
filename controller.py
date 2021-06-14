from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter
from tinydb import TinyDB

from models import Player
from models import Tournament
from models import Round

from view import CreationView
from view import ShowView
from view import AskView


class Control:
    @classmethod
    def make_player_list(cls):
        # list_player = (player1, player2, player3, player4, player5, player6, player7, player8)
        player_dict = {'player1': Player('Edd', datetime(1995, 6, 28), 'homme', 2),
                       'player2': Player('Matt', datetime(1995, 12, 7), 'homme', 1),
                       'player3': Player('Paul', datetime(1995, 5, 25), 'homme', 3),
                       'player4': Player('Thony', datetime(1995, 8, 9), 'homme', 4),
                       'player5': Player('Seb', datetime(1983, 2, 5), 'homme', 5),
                       'player6': Player('Joddie', datetime(1998, 2, 6), 'femme', 6),
                       'player7': Player('Manon', datetime(1995, 6, 28), 'femme', 7),
                       'player8': Player('Cécile', datetime(1978, 6, 15), 'femme', 8)
                       }
        return player_dict

    @classmethod
    def run_menu(cls):
        valid_choice = True
        while valid_choice:
            choice = ShowView.show_menu()
            if choice == '1':
                cls.run_tournament()
                valid_choice = False
            elif choice == '2':
                exit()
                valid_choice = False
            elif choice == '3':
                ShowView.show_new_player()
                AskView.ask_create_player()
                valid_choice = False
            else:
                print("Enter valid value.[1, 2 ou 3]")

    @classmethod
    def run_tournament(cls):
        print("Création du tournoi...")
        tournament_init = CreationView.create_tournament()
        tournament = Tournament(tournament_init[0],
                                tournament_init[1],
                                tournament_init[2],
                                tournament_init[3],
                                tournament_init[4],
                                cls.make_player_list()
                                )
        tournament = Tournament('Nom', 'Lieux', 'date', 'Timer', 'I am description', cls.make_player_list())
        round_instance = Round(tournament.player_dict)
        match_list = round_instance.generate_match_by_list(tournament)
        pprint(f'------------ Round ---------------')
        ShowView.show_match_name(tournament, match_list)
        # pprint(tournament.player_dict)
        cls.save(tournament)
        AskView.update_score(tournament, match_list)
        for i in range(3):
            print('------------- Score ----------------')
            sorted_player = Round.sort_player_by_score(tournament)
            new_match_list = Round.generate_match_by_score(sorted_player, match_list)
            # ShowView.show_score(sorted_player)

            # sorted_player = Round.sort_player_by_score(tournament)
            # ShowView.show_score(sorted_player)
            sorted_player_by_score = Round.sort_player_by_score(tournament)
            print()
            cls.save(tournament)
            pprint("Score des joueurs:")
            ShowView.show_score(sorted_player_by_score)
            pprint(f'------------ Round ---------------')
            ShowView.show_match_name(tournament, new_match_list)
            AskView.update_score(tournament, new_match_list)
            cls.save(tournament)
            cls.load()

        cls.save(tournament)
        sorted_player_by_score = Round.sort_player_by_score(tournament)
        Player.update_ranking(sorted_player_by_score)
        ShowView.show_ranking(sorted_player_by_score)
        cls.save(tournament)

    @classmethod
    def append_player_to_tournament(cls):
        player_dict = {}
        for p in range(1):
            print(f'Ajoutez joueur {p + 1}:')
            player = CreationView.create_player()
            player_dict[f'Player{p + 1}'] = Player(player[0],
                                                   player[1],
                                                   player[2],
                                                   player[3],
                                                   )
        return player_dict

    @classmethod
    def if_save(cls):
        # serialized_tournament =
        pass

    @classmethod
    def save(cls, tournament):
        db_player = TinyDB('players.json')
        db_tournament = TinyDB('tournanement.json')
        db_player.truncate() # clear the table
        db_tournament.truncate()
        tournament_dict = tournament.get_json()
        db_tournament.insert(tournament_dict)
        player_dict = tournament.player_dict
        for key, value in player_dict.items():
            db_player.insert(value.get_json())

        # pprint(tournament.get_json)
        # db_player.insert(player_dict)

    @classmethod
    def load(cls):
        db_player = TinyDB('players.json')
        db_tournament = TinyDB('tournanement.json')
        player_table = db_player.table('players')
        player_dict = {}
        pprint("_________________STOP__________________")
        for item in db_player:
            pprint(item)
            # player_dict[f'Player{item + 1}'] = Player(item[0],
            #                                                item[1],
            #                                                item[2],
            #                                                item[3]
            #                                                )
        print()
        for item in db_tournament:
            pprint(item)
        exit()

Control.run_tournament()

# list = controller.make_player_list()
# for player in list:
#     pprint(player.name)
