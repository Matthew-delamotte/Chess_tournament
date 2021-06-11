from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter

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
        # print("Création du tournoi...")
        # tournament_init = CreationView.create_tournament()
        # tournament = Tournament(tournament_init[0],
        #                         tournament_init[1],
        #                         tournament_init[2],
        #                         tournament_init[3],
        #                         tournament_init[4],
        #                         cls.append_player_to_tournament()
        #                         )

        tournament = Tournament('Nom', 'Lieux', 'date', 'Timer', 'I am description', cls.make_player_list())
        round_instance = Round(tournament.player_dict)
        matchs_list = round_instance.generate_match()
        ShowView.show_match_name(tournament, matchs_list)
        AskView.update_score(tournament, matchs_list)
            # Ask result for all matchs
            # Update score

            # Verify score player
            # if score p1 == score p2 else sort by rank

            # Associate best player with second player ect...
            # if p1 already play with p2, then match with p3

        # Show score
        # Update_ranking
        # Show new ranking
        # End

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





Control.run_tournament()

# list = controller.make_player_list()
# for player in list:
#     pprint(player.name)
