# Algorithme Calculatrice-NPI sur Python avec Flask 

La notation polonaise inverse (NPI) est une méthode pour représenter les expressions mathématiques 
de manière à ce que l'opérateur suit ses opérandes

Pour créer une calculatrice en NPI sur Python on doit :

1) Créez en quelque sort une pile pour stocker les opérandes.
2) Divisez l'expression en entrée en une liste de chaînes de caractères.
3) Pour chaque élément de la liste :
    a. Si l'élément est un nombre, ajoutez-le à la pile.
    b. Sinon, l'élément est un opérateur. Retirez deux éléments de la pile, appliquez l'opérateur aux deux éléments et ajoutez le résultat à la pile.
4) Le résultat final est le seul élément restant dans la pile.


Sur le fichier main.py on retrouve un script main.py qui permettra de lancer Flask API 

Voici les différents connexions existants: 

Page d'accueil:  <br> 
Page à l'affichage des données du calculateur: <br>
Page pour insérer les opérations du calculateur:  <br>
Téléchargement du fichier CSV: <br>
