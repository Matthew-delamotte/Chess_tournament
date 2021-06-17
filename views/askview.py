from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter

from models.round import Round


class AskView:
    @classmethod
    def ask_create_player(cls):
        valid_result = True
        while valid_result:
            choice = input("Ajouter des nouveau joueurs? (y ou n)")
            if choice == 'y':
                ShowView.show_new_player()
                valid_result = False
            elif choice == 'n':
                ShowView.show_menu()
            else:
                pprint('Enter valid value (y/n)')
        return choice

    @classmethod
    def ask_name(cls):
        last_name = input("Entrez nom: ")
        first_name = input("Entrez prénom: ")
        name = first_name + " " + last_name
        return name

    @classmethod
    def ask_gender(cls):
        valid_result = True
        while valid_result:
            gender = input("Entrez le sexe (h ou f): ")
            if gender == 'h':
                gender = 'Homme'
                valid_result = False
            elif gender == 'f':
                gender = "Femme"
                valid_result = False
            else:
                pprint('Enter valid result')
        return gender

    @classmethod
    def ask_birthday(cls):
        # born_year = int(input('Entrer date de naissance(aaaa): '))
        # born_month = int(input('(mm): '))
        # born_day = int(input('(jj): '))
        born_year = input('Entrer date de naissance(aaaa): ')
        born_month = input('(mm): ')
        born_day = input('(jj): ')
        birthday = (born_year, born_month, born_day)
        return birthday

    @classmethod
    def ask_rank(cls):
        rank = input("Entrer le classement: ")
        return rank

    @classmethod
    def ask_timer(cls):
        valid_result = True
        while valid_result:
            timer = input("Choissisez le type de temps (bullet, biltz ou rapide): ")
            if timer == "bullet":
                timer = "BULLET"
                valid_result = False
            elif timer == "blitz":
                timer = "BLITZ"
                valid_result = False
            elif timer == "rapide":
                timer = "QUICK"
                valid_result = False
            else:
                pprint("Entrer valeur valide")
        return timer

    @classmethod
    def enter_match_result(cls, tournament, matchs_list):
        print()
        pprint("Fin du round")
        pprint("Saisie des resultat")
        result_list = []
        for i in range(len(matchs_list)):
            valid_result = True
            while valid_result:
                result = input(f"Entrer resultat match {i + 1}: ")
                if result == '1':
                    result_list.append(result)
                    valid_result = False
                elif result == '2':
                    result_list.append(result)
                    valid_result = False
                elif result == '0':
                    result_list.append(result)
                    valid_result = False
                else:
                    pprint("Entrer un valeur valide: (1, 2 ou 0)")
        return result_list

    @classmethod
    def update_score(cls, tournament, matchs_list):
        print()
        result_list = cls.enter_match_result(tournament, matchs_list)
        p = 0
        for result in result_list:
            match = matchs_list[p]
            players_of_match = match
            players = players_of_match
            player1 = players[0]
            player2 = players[1]
            p += 1
            if result == '1':
                pprint(f'Joueur {player1.name} gagne, score +1 point.')
                player1.score += 1
            elif result == '2':
                pprint(f'Joueur {player2.name} gagne, score +1 point.')
                player2.score += 1
            elif result == '0':
                pprint(f'Joueur {player1.name} et {player2.name} sont égalité, score +0.5 point.')
                player1.score += 0.5
                player2.score += 0.5
        print()