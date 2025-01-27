import random
import time


def grille(nb_lignes, nb_colonnes):   # on initialise la grille avec des valeurs aléatoire comprise en tre 0 et 1
    grille = []
    for _ in range(nb_lignes):
        ligne = []
        for _ in range(nb_colonnes):
            ligne.append(random.randint(0, 1))
        grille.append(ligne)
    return grille


# grillejeu = grille(5, 5)
# for ligne in grillejeu:
    # print(ligne)


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


def nouvelle_grille(grille):
    # on créer une nouvelle grille avec les nouvelles valeurs
    grille2 = [[0 for _ in range(len(grille[0]))] for _ in range(len(grille))]
    # On parcours la grille a la recherche du nombre de voisin et on applique les règles

    for x in range(len(grille)):
        for y in range(len(grille[0])):
            voisins_vivants = voisinV(grille, x, y)
            if grille[x][y] == 1:   
                if voisins_vivants < 2 or voisins_vivants > 3:
                    grille2[x][y] = 0  # la cellule meurt
                else:
                    grille2[x][y] = 1  # La cellule survit
            else:  # Si la cellule est morte
                if voisins_vivants == 3:
                    grille2[x][y] = 1  # La cellule devient vivante

    return grille2


# grille2 = nouvelle_grille(grille)
# print("grille maj")
# for i in grille2:
    # print(i)


def jeu_de_la_vie(grille, iterations, pause=1):
    """
    Exécute le Jeu de la Vie pour un nombre donné d'itérations.

    :param grille: Grille initiale (liste de listes).
    :param iterations: Nombre d'étapes à exécuter.
    :param pause: Temps de pause (en secondes) entre chaque étape.
    """
    for etape in range(iterations):
        print(f"\nÉtape {etape + 1} :")
        for ligne in grille:
            print(" ".join(str(cell) for cell in ligne))  # Affiche la grille

        grille = nouvelle_grille(grille)  # Met à jour la grille
        time.sleep(pause)  # Pause entre les étapes

    print("\nFin du jeu !")


# Générer une grille initiale aléatoire 5x5
grille_initiale = grille(5, 5)

# Afficher la grille initiale
print("\nGrille initiale :")
for ligne in grille_initiale:
    print(" ".join(str(cell) for cell in ligne))

# Lancer le jeu pour 10 étapes avec une pause de 0.5 seconde entre chaque étape
jeu_de_la_vie(grille_initiale, iterations=10, pause=0.5)
