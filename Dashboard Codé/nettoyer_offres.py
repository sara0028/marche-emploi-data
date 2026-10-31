"""
Ce programme :
- charge le fichier des offres data (celui créé par filtrer_offres_simple.py)
- supprime les lignes en double
- nettoie les colonnes (espaces en trop, cases vides)
- Il sauvegarde le résultat dans un nouveau fichier propre
"""

import pandas as pd  

# ÉTAPE 1 : charger le fichier

offres = pd.read_csv("offres_data_filtrees.csv", sep=";")  # on lit le fichier CSV (colonnes séparées par des ;) et on le met dans la variable "offres"

print("Nombre d'offres au départ :", len(offres))  # len() compte les lignes, print() affiche le résultat


# ÉTAPE 2 : supprimer les doublons

offres = offres.drop_duplicates()  
# drop_duplicates(): supprime les lignes identiques, on garde la première pour enlèver les copies

print("Nombre d'offres après suppression des doublons :", len(offres))  # on affiche le nouveau nombre de lignes


# ÉTAPE 3 : nettoyer les colonnes

# Dans la colonne Télétravail, il y a des espaces en trop (" Oui" au lieu de "Oui")
offres["Télétravail"] = offres["Télétravail"].str.strip()  
# .str.strip(): enlève les espaces au début et à la fin de chaque texte

# Certaines cases sont vides. On les remplace par un texte clair
# plutôt que de les laisser vides, pour que les graphiques soient lisibles
offres["Télétravail"] = offres["Télétravail"].fillna("Non renseigné")  
# fillna(): remplace les cases vides par le texte donné
offres["Niveau d'études"] = offres["Niveau d'études"].fillna("Non renseigné")  # même chose pour le niveau d'études
offres["Niveau d'expérience min. requis"] = offres["Niveau d'expérience min. requis"].fillna("Non renseigné")  # même chose pour l'expérience
offres["Localisation du poste"] = offres["Localisation du poste"].fillna("Non renseigné")  # même chose pour la localisation

# On crée une nouvelle colonne "Département" à partir de la localisation
# Exemple : "Paris (75)" devient "75"
offres["Département"] = offres["Localisation du poste"].str.extract(r"\((.*?)\)")  # le résultat est stocké dans la nouvelle colonne
# str.extract(): cherche dans le texte ce qui est entre parenthèses
# r"\((.*?)\)": prends ce qu'il y a entre ()
offres["Département"] = offres["Département"].fillna("Non renseigné")  # si la localisation était vide, il n'y a pas de département : on met aussi "Non renseigné"


# ÉTAPE 4 : sauvegarder le fichier propre

offres.to_csv("offres_data_propres.csv", sep=";", index=False)  # on écrit le tableau dans un nouveau fichier
print("Fichier créé : offres_data_propres.csv")  # message de confirmation


# TEST 

print()  # une ligne vide pour aérer l'affichage
print("Les 5 métiers les plus fréquents :")  # un titre
print(offres["Métier"].value_counts().head(5))  
# value_counts(): compte combien de fois chaque métier apparaît, head(5) garde les 5 premiers
