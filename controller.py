from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter
from tinydb import TinyDB, Query

from models import Player
from models import Tournament
from models import Round

from view import CreationView
from view import ShowView
from view import AskView


class Control:
    @classmethod
    def make_player_dict(cls):
        tournament, player_data = cls.load()
        player_dict = {}
        p = 0
        for player in player_data:
            player_dict[f'Player{p + 1}'] = Player(player.get('name'),
                                                   player.get('birthday'),
                                                   player.get('gender'),
                                                   player.get('rank'),
                                                   player.get('score')
                                                   )
            p += 1
        return player_dict

    @classmethod
    def create_new_player(cls):
        player_dict = cls.append_player_to_tournament()
        return player_dict

    @classmethod
    def player_dict(cls):
        # list_player = (player1, player2, player3, player4, player5, player6, player7, player8)
        player_dict = {'player1': Player('Edd', ('', '', ''), 'homme', 2, 0),
                       'player2': Player('Matt', ('', '', ''), 'homme', 1, 0),
                       'player3': Player('Paul', ('', '', ''), 'homme', 3, 0),
                       'player4': Player('Thony', ('', '', ''), 'homme', 4, 0),
                       'player5': Player('Seb', ('', '', ''), 'homme', 5, 0),
                       'player6': Player('Joddie', ('', '', ''), 'femme', 6, 0),
                       'player7': Player('Manon', ('', '', ''), 'femme', 7, 0),
                       'player8': Player('Cécile', ('', '', ''), 'femme', 8, 0)
                       }
        # player_dict = cls.append_player_to_tournament()
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
                AskView.ask_create_player()
                valid_choice = False
            else:
                print("Enter valid value.[1, 2 ou 3]")

    @classmethod
    def run_tournament(cls):
        data_tournament, data_player = cls.load()
        tournament = ()
        # tournament = Tournament('Nom', 'Lieux', 'date', 'Timer', 'I am description', cls.player_dict())
        if len(data_tournament) == 0:
            print("Création du tournoi...")
            tournament_init = CreationView.create_tournament()
            tournament = Tournament(tournament_init[0],
                                    tournament_init[1],
                                    tournament_init[2],
                                    tournament_init[3],
                                    tournament_init[4],
                                    cls.player_dict()
                                    )
        else:
            for tournament_db in data_tournament:
                pprint("--------------------- Reprise du tournoi ----------------------")
                tournament = Tournament(tournament_db.get('name'),
                                        tournament_db.get('place'),
                                        tournament_db.get('date_start'),
                                        tournament_db.get('timer'),
                                        tournament_db.get('description'),
                                        cls.make_player_dict(),
                                        tournament_db.get('current_round')
                                        )

        round_instance = Round(tournament.player_dict)
        match_list = round_instance.generate_match_by_list(tournament)
        for i in range(tournament.current_round, tournament.round):
            pprint(f'------------ Round {i + 1} ---------------')
            ShowView.show_match_name(tournament, match_list)
            AskView.update_score(tournament, match_list)
            cls.save(tournament)
            tournament.current_round += 1
            print('------------- Score ----------------')
            sorted_player = Round.sort_player_by_score(tournament)
            new_match_list = Round.generate_match_by_score(sorted_player, match_list)
            sorted_player_by_score = Round.sort_player_by_score(tournament)
            print()
            cls.save(tournament)
            pprint("Score des joueurs:")
            ShowView.show_score(sorted_player_by_score)

        cls.save(tournament)
        sorted_player_by_score = Round.sort_player_by_score(tournament)
        Player.update_ranking(sorted_player_by_score)
        ShowView.show_ranking(sorted_player_by_score)
        tournament.end = True
        pprint("Fin du tournoi")
        cls.save(tournament)
        db_tournament = TinyDB('tournament.json')
        db_tournament.truncate()  # clear the table
        cls.load()

    @classmethod
    def append_player_to_tournament(cls):
        player_dict = {}
        print()
        for p in range(8):
            print(f'Ajoutez joueur {p + 1}:')
            player = CreationView.create_player()
            player_dict[f'Player{p + 1}'] = Player(player[0],
                                                   player[1],
                                                   player[2],
                                                   player[3],
                                                   player[4]
                                                   )
        return player_dict

    @classmethod
    def if_save(cls):
        db = TinyDB('tournament.json')
        # tournament = []
        v = db.table()
        # for i in db:
        #     pprint(i)
        # pprint(tournament)
        # if db_tournament.end == False:
        #     pprint("Chargement tournoi")
        #     cls.load()
        # else:
        #     pprint("Nouveau tournois")

    @classmethod
    def save(cls, tournament):
        db_player = TinyDB('players.json')
        db_tournament = TinyDB('tournament.json')
        db_player.truncate() # clear the table
        db_tournament.truncate()
        tournament_dict = tournament.get_json()
        db_tournament.insert(tournament_dict)
        player_dict = tournament.player_dict
        for key, value in player_dict.items():
            db_player.insert(value.get_json())

    @classmethod
    def load(cls):
        db_player = TinyDB('players.json')
        db_tournament = TinyDB('tournament.json')
        player_table = db_player.table('players')
        tournament_table = db_tournament.all()
        player_table = db_player.all()
        return tournament_table, player_table;
        # return tournament_table, player_table
        # pprint("_________________STOP__________________")
        # for item in db_player:
        #     pprint(item)
        #     # player_dict[f'Player{item + 1}'] = Player(item[0],
        #     #                                                item[1],
        #     #                                                item[2],
        #     #                                                item[3]
        #     #                                                )
        # print()


# Control.run_tournament()
# Control.save()
# Control.load()

# list = controller.make_player_list()
# for player in list:
#     pprint(player.name)
