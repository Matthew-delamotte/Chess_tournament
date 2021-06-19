from pprint import pprint


class ShowView:
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
