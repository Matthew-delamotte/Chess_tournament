from pprint import pprint


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
        pprint("[1] ..Jouez/Continuer..")
        pprint("[2] ..Ajoutez des joueurs..")
        choice = input()
        print()
        return choice

    @classmethod
    def show_match_name(cls, tournament, matchs_list):
        print()
        for match in range(tournament.round):
            print(f'Match n* {match + 1}')
            x = matchs_list[match]
            pprint(x[0].name + " :J1:-- vs --:J2: " + x[1].name)

    @classmethod
    def show_score(cls, sorted_player):
        sorted_player = sorted_player
        print("---------------------- Score ------------------------")
        for i in sorted_player:
            pprint(f"{i.name}:  {i.score} score.")
        print()
        return

    @classmethod
    def show_ranking(cls, sorted_player):
        sorted_player = sorted_player
        print("--------------- Classement final -------------------")
        for i in sorted_player:
            pprint(f"{i.name}:  {i.rank + 1} rank.")
        print()
        return
