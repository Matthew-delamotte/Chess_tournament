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

# def change_attribute(Attribute, value):
#     "In this function I can not access car.color directly"
#     Attribute.score = value

# def increase_score():
#     for player in make_player_list():
#         if player.score == 0:
#             change_attribute(i, )
#             pprint(i.score)
#     return

# score = Score(0)
# list_player = make_player_list()
# algo = Algorythm(list_player)
# pprint(algo.generate_pair())
#

# algo = Algorythm(make_player_list())
# pprint(increase_score())


# for player in list_player:
#     pprint(player.ranking)

# pprint(player2.get_age())
# pprint(player2.get_attribut())

# tournoi = Tournament('name', 'Paris', list_player, Timer.QUICK, "Exemple")

# pprint(tournoi.get_attributes())

from controller import Control


def main():
    Control.run_tournament()


if __name__ == "__main__":
    main()
