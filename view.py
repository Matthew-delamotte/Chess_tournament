from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter



class ShowView:
    @classmethod
    def show_create_tournament(cls):
        tournament = CreationView.create_tournament()
        pprint('Nom du tournois: ' + tournament[0])
        pprint('Lieux: ' + tournament[1])
        pprint('Date de début: ' + tournament[2])
        pprint('Vitesse de jeu: ' + tournament[3])
        pprint('Description: ' + tournament[4])

    @classmethod
    def show_new_player(cls):
        new_player = CreationView.create_player()
        print()
        pprint('Nom: ' + new_player[0])
        pprint('Date de naissance: ' + str(new_player[1]))
        pprint('Genre: ' + new_player[2])
        AskView.ask_create_player()


    @classmethod
    def show_menu(cls):
        pprint("Bienvenue sur le programme de tournois d'échecs.")
        print()
        pprint("Que voulez vous faire?")
        pprint("[1] ..Créer un tournois..")
        pprint("[2] ..Continuez un tournois..")
        pprint("[3] ..Ajoutez des joueur..")
        choice = input()
        print()
        return choice

    @classmethod
    def show_match_name(cls, tournament, matchs_list):
        for match in range(tournament.round):
            print(f'Match n* {match + 1}')
            x = matchs_list[match]
            pprint(x[0].name + " :J1:-- vs --:J2: " + x[1].name)



class CreationView:
    @classmethod
    def create_player(cls):
        print("Création d'un joueur")
        print()
        name = AskView.ask_name()
        gender = AskView.ask_gender()
        birthday = AskView.ask_birthday()
        rank = AskView.ask_rank()
        new_player = (name, birthday, gender, rank)
        return new_player

    @classmethod
    def create_tournament(cls):
        pprint("Paramétre du tournoi: ")
        name = input("Entrer nom: ")
        place = input("Entrer l'endroit: ")

        date_start = cls.take_time()

        timer = AskView.ask_timer()

        description = input("Entrez une description: ")
        tournament_init = (name, place, date_start, timer, description)
        return tournament_init

    @classmethod
    def take_time(cls):
        now = datetime.now()  # current date and time

        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time

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
        born_year = int(input('Entrer date de naissance(aaaa): '))
        born_month = int(input('(mm): '))
        born_day = int(input('(jj): '))
        birthday = datetime(born_year, born_month, born_day)
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
    def ask_player_for_tournament(cls):
        pass

    def show_ranking(self):
        pass

    def show_match(self):
        pass

    @classmethod
    def enter_match_result(cls, tournament, matchs_list):
        print()
        pprint("Fin du round")
        pprint("Saisie des resultat")
        result_list = []
        for i in range(len(matchs_list)):
            print()
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


        return result_list

    @classmethod
    def update_score(cls, tournament, matchs_list):
        result_list = cls.enter_match_result(tournament, matchs_list)
        pprint(result_list)
        p = 0
        for result in result_list:
            pprint(result)
            match = matchs_list[p]
            players_of_match = match
            players = players_of_match
            player1 = players[0]
            player2 = players[1]
            p += 1
            if result == '1':
                pprint(f'Joueur {player1.name} gagne, score +1 point.')
                player1.score += 1
                pprint('Verification')
                pprint(player1.score)
                pprint(player2.score)
            elif result == '2':
                pprint(f'Joueur {player2.name} gagne, score +1 point.')
                player2.score += 1
                pprint('Verification')
                pprint(player1.score)
                pprint(player2.score)
            elif result == '0':
                pprint(f'Joueur {player1.name} et {player2.name} sont égalité, score +0.5 point.')
                player1.score += 0.5
                player2.score += 0.5
                pprint('Verification')
                pprint(player1.score)
                pprint(player2.score)

                    # pprint(x[0].name + " :J1:-- vs --:J2: " + x[1].name)
            # while self.valid_result:
            #     point_to_add = 0
            #     result = input("Enter result: ")
            #     if result == 'win':
            #         self.score += 1
            #         pprint('+1 points added')
            #     elif result == 'draw':
            #         self.score += 0.5
            #         pprint('+0.5 points added')
            #     elif result == 'lose':
            #         pprint('No point added')
            #     else:
            #         raise Exception("Sorry, enter valid result")


# pprint(AskView.ask_create_player())