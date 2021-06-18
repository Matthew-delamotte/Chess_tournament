from datetime import datetime
from pprint import pprint

from views.askview import AskView


class CreationView:
    @classmethod
    def create_player(cls):
        print("Création d'un joueur")
        print()
        name = AskView.ask_name()
        gender = AskView.ask_gender()
        birthday = AskView.ask_birthday()
        rank = AskView.ask_rank()
        score = 0
        new_player = (name, birthday, gender, rank, score)
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
