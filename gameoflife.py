import random


def initialiser_grille(nb_lignes, nb_colonnes):
    grille = []
    for _ in range(nb_lignes):
        ligne = []
        for _ in range(nb_colonnes):
            ligne.append(random.randint(0, 1))
        grille.append(ligne)
    return grille


grille = initialiser_grille(5, 5)
for ligne in grille:
    print(ligne)
