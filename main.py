import numpy as np
import matplotlib.pyplot as plt

# Initialiser une grille vide (3x3) avec des zéros
def initialiser_grille():
    return np.zeros((3, 3), dtype=int)

# Afficher la grille avec Matplotlib et les marques 'X' et 'O'
def afficher_grille(grille):
    # Dessiner la grille
    for i in range(1, 3):
        plt.plot([0, 3], [i, i], color="black")  # Lignes horizontales
        plt.plot([i, i], [0, 3], color="black")  # Lignes verticales

    # Placer les marques 'X' et 'O'
    for i in range(3):
        for j in range(3):
            if grille[i, j] == 1:  # Joueur 1 : 'X'
                plt.text(j + 0.5, 2.5 - i, 'X', fontsize=40, ha='center', va='center')
            elif grille[i, j] == 2:  # Joueur 2 : 'O'
                plt.text(j + 0.5, 2.5 - i, 'O', fontsize=40, ha='center', va='center')

    # Configurations pour cacher les axes
    plt.xlim(0, 3)
    plt.ylim(0, 3)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')

    # Mettre à jour la figure
    plt.draw()
    plt.pause(0.1)

# Vérifier si la case est valide (vide et dans les limites)
def case_valide(grille, ligne, colonne):
    return 0 <= ligne < 3 and 0 <= colonne < 3 and grille[ligne, colonne] == 0

def recuperer_coordonnees(joueur):
    while True:
        try:
            ligne = int(input(f"Joueur {joueur}, entrez la ligne (0-2): "))
            colonne = int(input(f"Joueur {joueur}, entrez la colonne (0-2): "))
            if 0 <= ligne <= 2 and 0 <= colonne <= 2:
                return ligne, colonne
            else:
                print("Coordonnées invalides. Essayez à nouveau.")
        except ValueError:
            print("Veuillez entrer des nombres entiers.")

# Placer la marque du joueur (1 pour 'X', 2 pour 'O')
def placer_marque(grille, ligne, colonne, joueur):
    grille[ligne, colonne] = joueur

# Vérifier s'il y a un gagnant
def verifier_victoire(grille, joueur):
    # Vérification des lignes, colonnes et diagonales
    for i in range(3):
        if np.all(grille[i, :] == joueur) or np.all(grille[:, i] == joueur):
            return True
    if grille[0, 0] == grille[1, 1] == grille[2, 2] == joueur or grille[0, 2] == grille[1, 1] == grille[2, 0] == joueur:
        return True
    return False

# Vérifier si la grille est pleine (match nul)
def verifier_match_nul(grille):
    return np.all(grille != 0)

# Fonction principale du jeu
def jeu_morpion():
    grille = initialiser_grille()
    joueur = 1  # Joueur 1 commence ('X')

    plt.ion()  # Activer le mode interactif de matplotlib
    afficher_grille(grille)  # Afficher la grille une seule fois au début
    
    while True:
        ligne, colonne = recuperer_coordonnees(joueur)

        if case_valide(grille, ligne, colonne):
            placer_marque(grille, ligne, colonne, joueur)

            # Effacer la grille et afficher la mise à jour
            plt.cla()  # Nettoyer la figure sans fermer la fenêtre
            afficher_grille(grille)  # Mettre à jour l'affichage

            # Vérifier si le joueur actuel a gagné
            if verifier_victoire(grille, joueur):
                print(f"Félicitations ! Le joueur {joueur} a gagné !")
                break

            # Vérifier le match nul
            if verifier_match_nul(grille):
                print("Match nul !")
                break

            # Changer de joueur
            joueur = 2 if joueur == 1 else 1
        else:
            print("Case invalide, essayez à nouveau.")

    plt.ioff()  # Désactiver le mode interactif
    plt.show()  # Afficher la dernière grille

# Lancer le jeu
jeu_morpion()