# Installation 

**Virtual environnement**
```powershell
python -m venv .venv
```
> .venv is the name of the virtual environnement 

**Connect to the venv** 

- mac/linux
`source .venv/bin/activate.fish`
- windows
`.venv/Scripts/activate` or `.venv/Scripts/activate.ps1` 

**create requirements.txt from pip**
`pip freeze > requirements.txt`

in a new environnement install the librairies
**install librairies**
`pip install -r requirements.txt`

**quit venv**
`deactivate` 

# Jeu de Morpion en Python

Ce projet implémente un jeu de morpion (tic-tac-toe) simple en Python en utilisant les bibliothèques `NumPy` et `Matplotlib`. Deux joueurs (Joueur 1 et Joueur 2) jouent à tour de rôle pour placer des marques ('X' et 'O') sur une grille de 3x3. Le premier joueur à aligner trois marques horizontalement, verticalement ou en diagonale gagne la partie. Si toutes les cases sont remplies sans qu'aucun joueur ne gagne, la partie se termine par un match nul.

## Fonctionnalités

- Initialisation d'une grille vide 3x3.
- Placement des marques 'X' (Joueur 1) et 'O' (Joueur 2).
- Affichage interactif de la grille à l'aide de `Matplotlib`.
- Vérification des conditions de victoire et de match nul.
- Gestion des entrées utilisateurs pour les coordonnées des cases.
- Détection des cases invalides (déjà remplies ou hors limites).

## Prérequis

Pour exécuter ce projet, assurez-vous d'avoir installé les bibliothèques suivantes :

- [NumPy](https://numpy.org/) : `pip install numpy`
- [Matplotlib](https://matplotlib.org/) : `pip install matplotlib`

## Comment jouer

1. Clonez le dépôt ou copiez le code dans un fichier Python (par exemple, `morpion.py`).
2. Installez les dépendances nécessaires avec `pip install numpy matplotlib`.
3. Exécutez le script en lançant la commande :

   ```bash
   python morpion.py
