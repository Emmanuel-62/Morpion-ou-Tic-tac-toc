import random


# Bienvenue dans le fichier du jeu du morpion !
print("Bienvenue dans le fichier du jeu du morpion !")

# Initialisation du plateau
place_poin = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

# Fonction pour afficher le plateau de manière stylisée
def afficher_plateau():
    for ligne in place_poin:
        poin = " | ".join(ligne)
        print(poin)
        print("-" * len(poin))

# Fonction pour placer un pion à un emplacement donné
def placer_pion(ligne, colonne, symbole):
    if place_poin[ligne][colonne] == "-":
        place_poin[ligne][colonne] = symbole
        return True
    else:
        print("Case déjà occupée. Choisissez une autre case.")
        return False

# Fonction pour vérifier s'il y a une victoire
def verifier_victoire(symbole):
    # Vérifier les lignes et les colonnes
    for i in range(3):
        if all(place_poin[i][j] == symbole for j in range(3)) or all(place_poin[j][i] == symbole for j in range(3)):
            return True
    
    # Vérifier les diagonales
    if all(place_poin[i][i] == symbole for i in range(3)) or all(place_poin[i][2 - i] == symbole for i in range(3)):
        return True

    return False

# Fonction pour vérifier s'il y a une égalité
def verifier_egalite():
    return all(place_poin[i][j] != "-" for i in range(3) for j in range(3))

# Logique du jeu
tour = 1
symboles = ["❌", "⭕️"]


# Choix du mode de jeu
mode_jeu = input("Choisissez le mode de jeu (1 pour jouer à deux joueurs, 2 pour jouer contre l'IA) : ")

if mode_jeu == "1":
    print("Mode deux joueurs.")

    while True:
        # Afficher le plateau
        print(f"\nTour {tour}")
        afficher_plateau()

        # Demander au joueur de placer son pion
        joueur = (tour % 2) - 1  # Alterne entre 0 et 1 pour choisir le symbole du joueur
        symbole = symboles[joueur]
        print(f"Au tour du joueur {symbole}.")

        ligne = int(input("Entrez le numéro de ligne (0, 1, 2) : "))
        colonne = int(input("Entrez le numéro de colonne (0, 1, 2) : "))

        # Placer le pion et vérifier la validité du coup
        if placer_pion(ligne, colonne, symbole):
            # Vérifier la victoire
            if verifier_victoire(symbole):
                afficher_plateau()
                print(f"Le joueur {symbole} a gagné !")
                break

            # Vérifier l'égalité
            if verifier_egalite():
                afficher_plateau()
                print("Match nul !")
                break

            tour += 1
else:
    print("Mode contre l'IA.")

    while True:
        # Afficher le plateau
        print(f"\nTour {tour}")
        afficher_plateau()

        # Joueur humain
        joueur = tour % 2
        symbole = symboles[joueur]

        if joueur == 0:
            print(f"Au tour du joueur {symbole}.")
            ligne = int(input("Entrez le numéro de ligne (0, 1, 2) : "))
            colonne = int(input("Entrez le numéro de colonne (0, 1, 2) : "))
            
            if not (0 <= ligne <= 2) or not (0 <= colonne <= 2) or place_poin[ligne][colonne] != "-":
                print("Coup invalide. Veuillez réessayer.")
                continue
            placer_pion(ligne, colonne, symbole)
        else:
            # Tour de l'IA
            print(f"Au tour de l'IA ({symbole}).")
            positions_disponibles = [(i, j) for i in range(3) for j in range(3) if place_poin[i][j] == "-"]
            if positions_disponibles:
                ligne, colonne = random.choice(positions_disponibles)
                print(f"L'IA ({symbole}) joue en ({ligne}, {colonne}).")
                placer_pion(ligne, colonne, symbole)

        # Vérifier la victoire
        if verifier_victoire(symbole):
            afficher_plateau()
            print(f"Le joueur {symbole} a gagné !")
            break

        # Vérifier l'égalité
        if verifier_egalite():
            afficher_plateau()
            print("Match nul !")
            break

        tour += 1


# Fin du jeu
 
# Afficher le plateau une dernière fois
afficher_plateau()
