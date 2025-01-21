# Demander le nom complet de l'utilisateur
nom = input("Veuillez entrer votre nom complet: ")
# Demander l'âge de l'utilisateur
age = int(input("Veuillez entrer votre âge: "))
# Définir l'année actuelle
ANACT = 2025
# Calculer l'année de naissance
anNai = ANACT - age
# Afficher un message de bienvenue avec le nom complet
print('Bonjour', nom)
# Afficher l'année de naissance
print('Vous êtes né(e) en', anNai)
