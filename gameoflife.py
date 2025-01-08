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
    # on verifie toutes les cellules adjacentes a une cellule donnée
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]
    nbre_voisin_vivants = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]):
            nbre_voisin_vivants += grille[nx][ny]
    return nbre_voisin_vivants


def mettre_a_jour_grille(grille):
    # Crée une nouvelle grille qui va contenir les nouvelles valeurs
    grille2 = [[0 for _ in range(len(grille[0]))] for _ in range(len(grille))]

    for x in range(len(grille)):
        for y in range(len(grille[0])):
            voisins_vivants = voisinV(grille, x, y)
            if grille[x][y] == 1:  # Si la cellule est vivante
                if voisins_vivants < 2 or voisins_vivants > 3:
                    grille2[x][y] = 0  # La cellule meurt
                else:
                    grille2[x][y] = 1  # La cellule survit
            else:  # Si la cellule est morte
                if voisins_vivants == 3:
                    grille2[x][y] = 1  # La cellule devient vivante

    return grille2
