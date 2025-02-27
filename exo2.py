# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
nivBat = int(input("Entrez le niveau de charge actuel de la batterie : "))
# Vérifiez si le niveau de charge est valide
if not(nivBat >=0 and nivBat <= 100):
    print('Erreur : niveau de charge invalide.')
else:
    # Arrondir le pourcentage à la dizaine la plus proche
    nivBatRd = round(nivBat, -1)
    # Calculer le nombre de barres
    nb =  nivBatRd / 10
    # Afficher la représentation graphique de la charge de la batterie
    print('[' + '❚' * int(nb) + ' '* (10 - int(nb)) + ']')
    print (str(nivBat) +'%')
# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%