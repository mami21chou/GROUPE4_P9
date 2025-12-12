mot_de_passe_correcte = "python123"
tentative = 0
max_tentative = 3

est_correct = False

while (tentative < 3):
    mot_de_passe_saisi = input("Veuillez saisir le mot de passe correct : ")

    if mot_de_passe_saisi == mot_de_passe_correcte :
        est_correct = True
        break
    
    else :
        print("Mot de passe incorrecte!")
        tentative += 1
        
   
   
    
if est_correct == True : 
    print('Acces autorise')
else :
    print("Acces refuse")
