""" Exercice 1 – 
Demander un nombre à l’utilisateur et afficher sa table de multiplication de 1 à 10.
 """

def multiplication():
    multi=1
    nbr=(input())
    print(f"la table de multipliction de {nbr}")
    while nbr.isalpha():
        print(f"ecrire un nombre")
        nbr=input()
    for i in range (1,11):
        nbr=int(nbr)
        if  nbr==0:
            print(f"la multiplication par 0 est nulle")
            nbr=int(input("donnez un nombre differant de zero"))
        else:    
            multi=i*nbr
            print(f"{i}*{nbr}={multi}")
    
print("Donnez le nombre a multiplie") 
print(multiplication())   
       
   


    