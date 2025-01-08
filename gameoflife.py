import random


def grille(nb_lignes, nb_colonnes):   # on initialise la grille
    grille = []
    for _ in range(nb_lignes):
        ligne = []
        for _ in range(nb_colonnes):
            ligne.append(random.randint(0, 1))
        grille.append(ligne)
    return grille


grillejeu = grille(5, 5)
for ligne in grillejeu:
    print(ligne)


def voisinV(grille, x, y):  # fonction pour determiner le nbre de voisins vivants 
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # on verifie toutes les cellules adjacentes a une cellule donnée
    nbre_voisin_vivants = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy 
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]):
            nbre_voisin_vivants += grille[nx][ny]
    return nbre_voisin_vivants



