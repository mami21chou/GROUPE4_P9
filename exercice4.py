""" Exercice 4 – 
Ecrire un algorithme qui permet de calculer le factoriel d’un nombre
 """

def factoriel():
    fact=1
    print(f"Calcul de factoriel")
    nbr = (input("donnez un nombre"))
    while nbr.isalpha():
        print(f"Entrez un entier")
        nbr=input()
    nbr=int(nbr)    
    for i in range (1,nbr+1):
        
        fact=fact*i
    print(f"le factoriel de {nbr}={fact}")  