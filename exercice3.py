

# Supposons que la variable liste contient des chaînes
liste = ['1', '2', '3', '4']

# Créer une liste vide pour stocker les entiers
liste_entiers = []

# Parcourir chaque élément de la liste de chaînes
for element in liste:
    # Convertir l'élément en entier
    entier = int(element)
    # Ajouter l'entier à la nouvelle liste
    liste_entiers.append(entier)

# Afficher le résultat
print("Liste de chaînes :", liste)
print("Liste d'entiers :", liste_entiers)

# Exemple : liste d'entiers
liste_entiers = [1, 2, 3, 4, 5]

# 1️⃣ Somme des nombres
somme = sum(liste_entiers)
print("Somme des nombres :", somme)

# 2️⃣ Moyenne des nombres
moyenne = somme / len(liste_entiers)
print("Moyenne des nombres :", moyenne)

# 3️⃣ Nombre de nombres supérieurs à la moyenne
compteur_sup_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        compteur_sup_moyenne += 1

print("Nombre de nombres supérieurs à la moyenne :", compteur_sup_moyenne)

def salaire_mensuel(salaire_annuel):
    """
    Calcule le salaire mensuel à partir du salaire annuel.
    
    Paramètre :
    salaire_annuel (float ou int) : salaire annuel
    
    Retour :
    float : salaire mensuel
    """
    return salaire_annuel / 12  # Retourne le résultat

# Exemple d'utilisation
mon_salaire_annuel = 36000
mon_salaire_mensuel = salaire_mensuel(mon_salaire_annuel)
print("Salaire mensuel :", mon_salaire_mensuel)

def salaire_hebdomadaire(salaire_mensuel):
   
    return salaire_mensuel / 4
    # Supposons que le salaire mensuel est déjà calculé
mon_salaire_mensuel = 3000

# Calcul du salaire hebdomadaire
mon_salaire_hebdo = salaire_hebdomadaire(mon_salaire_mensuel)

print("Salaire hebdomadaire :", mon_salaire_hebdo)

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    """
    Calcule le salaire horaire à partir du salaire hebdomadaire et du nombre d'heures travaillées par semaine.
    
    Paramètres :
    salaire_hebdomadaire (float ou int) : salaire hebdomadaire
    heures_travaillees (float ou int) : nombre d'heures travaillées par semaine
    
    Retour :
    float : salaire horaire
    """
    if heures_travaillees == 0:
        raise ValueError("Le nombre d'heures travaillées ne peut pas être 0")
    
    return salaire_hebdomadaire / heures_travaillees
# Exemple : salaire hebdomadaire et heures travaillées
mon_salaire_hebdo = 750
heures_par_semaine = 35

# Calcul du salaire horaire
mon_salaire_horaire = salaire_horaire(mon_salaire_hebdo, heures_par_semaine)

print("Salaire horaire :", mon_salaire_horaire)


# 1️⃣ Saisie du salaire annuel
salaire_annuel = float(input("Entrez votre salaire annuel en euros : "))

# 2️⃣ Saisie du nombre d'heures travaillées par semaine
heures_par_semaine = float(input("Entrez le nombre d'heures travaillées par semaine : "))

# 3️⃣ Calculs
mensuel = salaire_mensuel(salaire_annuel)
hebdo = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdo, heures_par_semaine)

# 4️⃣ Affichage du résultat
print(f"Votre salaire horaire est de {horaire:.2f} euros")

def addition(a, b):
    somme = a + b
    return somme






