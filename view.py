from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter

class View:
    def ask_birthday(self):
        born_year = int(input('Entrer date de naissance(aaaa): '))
        born_month = int(input('(mm): '))
        born_day = int(input('(jj): '))
        birthday = datetime(born_year, born_month, born_day)
        player2 = Player('Matt', birthday, Gender.MALE)
        pprint(player2.get_age())

    def create_player(self):
        pass