"""
La notation polonaise inverse (NPI) est une méthode pour représenter les expressions mathématiques 
de manière à ce que l'opérateur suit ses opérandes

Pour créer une calculatrice en NPI on doit :

1) Créez en quelque sort une pile pour stocker les opérandes.
2) Divisez l'expression en entrée en une liste de chaînes de caractères.
3) Pour chaque élément de la liste :
    a. Si l'élément est un nombre, ajoutez-le à la pile.
    b. Sinon, l'élément est un opérateur. Retirez deux éléments de la pile, appliquez l'opérateur aux deux éléments et ajoutez le résultat à la pile.
4) Le résultat final est le seul élément restant dans la pile.
"""

def calculatrice_NPI(expression):
    pile = []
    operateurs = ["+", "-", "*", "/","%"]
    elements = expression.split()

    for element in elements:
        if element not in operateurs:
            pile.append(float(element))
        else:
            x = pile.pop()
            y = pile.pop()
            if element == "+":
                pile.append(x + y)
            elif element == "-":
                pile.append(x - y)
            elif element == "*":
                pile.append(x * y)
            elif element == "/":
                pile.append(x / y)
            elif element == "%":
                pile.append(x % y)
            elif element == "**":
                pile.append(x ** y)
    return pile[0]