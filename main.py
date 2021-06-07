
"""
Etape:
1: Creation du tournoi
2: Ajouter 8 joueurs
3: Génération de pair de joueur aléatoire pour le premier tour
4: Lorsque le tour est terminé, entrer les resultat
5: Repetez les étape 3 et 4 jusqu'a la fin du tournoi


Spec du tournoi:
- Nom
- Lieu
- Date
    (Jusqu'à présent, tous nos tournois sont des événements d'un jour,
    mais nous pourrions en organiser de plusieurs jours à l'avenir,
    ce qui devrait donc permettre de varier les dates.)
- Nombre de tour
    (par defaut 4)
- Tournées
    (Liste des instance ronde) (?)-------------------------------
- Joueurs
    (Liste des indices correspondant aux instances du joueur stockées en mémoire.)
- Contrôle du temps
    (bullet, Biltz, ou coup rapide)
- Description
    (Les remarque général du directeur du tournoi)


Spec d'un joueur:
- Nom
- Prénom
- Date de naissance
- Sexe
- Classement
    (Chiffre positif)


Spec Tour/Match:
- Chaque match est un paire de joueur
- Champ de resultat pour chaque joueur
- Saisi des resultat par le gestionnaire en fin de match + génération autot du prochain tour
- Gagnant +1 point, perdant +0 point, match nul +0.5 point pour chaque joueurs
- Un match doit etre stocker dans un tuple avec 2 listes:
    - Une référence à un instance de joueur
    - Le score
- Les match multiple doivent être stocker sous forme de liste sur l'instance du tour
- En plus de la liste de correspondance, donner un nom au tour (Round 1, Round 2, ...)
- Date et heure du début du tour (Automatique en début de tour)
- Date et heure de la fin du tour (Automatique en fin de tour)
- Instance du round doivent être stockées dans une liste sur l'instance du tournoi qui lui correspond


Génération des paires:
- Systéme suisse (cf. l'algorythme)


MàJ des classement:
- Mise a jour manuel des classement, juste affichage des resultat


Rapport:
- Liste de tout les acteur:
    - Par ordre alphabétique
    - Par classement
- Liste de tout les joueur:
    - Par ordre alphabétique
    - par classement
- Liste des tournois
- Liste de tout les tours d'un tournoi
- Liste de tout les matchs d'un tournoi
- Pas d'exportation pour l'instant


Sauvegarde/Chargement des donnée
- Possibilité de sauvegarde et de chargement a tout moment entre 2 actions utilisateur.
- Systéme TinyDB
- Deux table:
    - Joueur
    - Tournoi

------------------------------------------------------------------------------------------
LE SYSTÈME SUISSE DES TOURNOIS
GÉNÉRATION DES PAIRES DE JOUEURS
Nos paires sont générées selon le système de tournoi suisse. Vous trouverez ci-dessous la
manière dont nous préférons mettre en œuvre ce système :

1. Au début du premier tour, triez tous les joueurs en fonction de leur classement.
2. Divisez les joueurs en deux moitiés, une supérieure et une inférieure. Le meilleur joueur
    de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure, et
    ainsi de suite. Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé avec
    le joueur 5, le joueur 2 est jumelé avec le joueur 6, etc.
3. Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points.
    Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
4. Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite.
    Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
5. Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé.

ÉQUILIBRER LES COULEURS
Un tirage au sort des joueurs définira qui joue en blanc et qui joue en noir ;
il n'est donc pas nécessaire de mettre en place un équilibrage des couleurs.

--------------------------------------------------------------

"""
from enum import Enum
from datetime import datetime
from pprint import pprint
from operator import attrgetter


class Player:
    def __init__(self, name, born, gender, rank):
        self.name = name
        self.born = born
        self.gender = gender
        self.ranking = rank

    def get_age(self, today=datetime.now()):
        born = self.born
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age

    def read_ranking_player(self):
        return self.ranking

    def increase_player_ranking(self):
        self.ranking += 1
        return self.ranking

    def get_attribute(self):
        return {'name': self.name,
                'birthday': self.born,
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

    # def make_player_pair(self):
    #     # swiss_alogorythm():
    #     pass

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

    def swiss_algorythm(self):
        sorted_player = self.sort_player()
        for i in sorted_player:
            print(i.name + str(i.ranking))
        # division en 2 groupes: un superieur et un inferieur
        length = len(sorted_player)
        middle_index = length//2

        superior_list = sorted_player[:middle_index]
        inferior_list = sorted_player[middle_index:]

        for i in inferior_list:
            pprint("liste inferieur: " + i.name + " rang " + str(i.ranking))

        for i in superior_list:
            pprint("liste superieur: " + i.name + " rang " + str(i.ranking))

        # Jumelez meilleur joueur des deux moitier superieur et inférieur

        # Jumelez joueur 2 superieur avec joueur 2 inferieur
        # ect jusqu'a que tout les joueur est été jumelez

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

    def pair_first_round(self):
        sorted_players = self.order_players(self.players)
        S1count = len(self.list_player) / 2
        for index in range(S1count):
            self.pairs.append([sorted_players[index], sorted_players[S1count + index]])
        if len(self.players) % 2 == 1:
            self.pairs.append([sorted_players[S1count * 2 + 1], None])
        pass


class Score(Enum):
    WIN = 0
    DRAW = 1
    LOSE = 2


class Timer(Enum):
    BULLET = 0
    QUICK = 1
    BLITZ = 2


class Gender(Enum):
    MALE = 0
    FEMALE = 1


# class View:
#     born_year = int(input('Entrer date de naissance(aaaa): '))
#     born_month = int(input('(mm): '))
#     born_day = int(input('(jj): '))
#     birthday = datetime(born_year, born_month, born_day)
#     player2 = Player('Matt', birthday, Gender.MALE)
#     pprint(player2.get_age())
#     pprint(player2.get_attribut())
    

player1 = Player('Edd', datetime(1995, 6, 28), Gender.MALE, 2)
player2 = Player('Matt', datetime(1995, 12, 7), Gender.MALE, 1)
player3 = Player('Paul', datetime(1995, 5, 25), Gender.MALE, 3)
player4 = Player('Thony', datetime(1995, 8, 9), Gender.MALE, 4)
player5 = Player('Seb', datetime(1983, 2, 5), Gender.MALE, 5)
player6 = Player('Joddie', datetime(2000, 5, 6), Gender.FEMALE, 6)
player7 = Player('Manon', datetime(1995, 6, 28), Gender.MALE, 7)
player8 = Player('Cécile', datetime(1978, 6, 15), Gender.FEMALE, 8)
list_player = [player1, player2, player3, player4, player5, player6, player7, player8]

algo = Algorythm(list_player)
algo.swiss_algorythm()

# for player in list_player:
#     pprint(player.ranking)

# pprint(player2.get_age())
# pprint(player2.get_attribut())

# tournoi = Tournament('name', 'Paris', list_player, Timer.QUICK, "Exemple")

# pprint(tournoi.get_attributes())