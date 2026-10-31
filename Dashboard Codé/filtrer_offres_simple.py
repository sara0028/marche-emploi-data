"""
Ce programme :
- charge le fichier CSV
- garde seulement les offres qui parlent de "data"
- sauvegarde ces offres dans un nouveau fichier, plus petit et plus simple
"""

import pandas as pd

# On choisit les colonnes qu'on veut garder
colonnes_a_garder = [
    "Métier",
    "Intitulé du poste",
    "Localisation du poste",
    "Niveau d'études",
    "Niveau d'expérience min. requis",
    "Télétravail",
]

# On charge le fichier, en ne gardant que ces colonnes
toutes_les_offres = pd.read_csv("offres-datagouv-20260816.csv", sep=";", usecols=colonnes_a_garder)
# usecols charge uniquement les colonnes listées juste avant

print("Nombre total d'offres :", len(toutes_les_offres))

# On regarde si le mot "data" apparaît dans la colonne "Métier"
data_dans_metier = toutes_les_offres["Métier"].str.contains("data", case=False, na=False)
# str.contains(): est-ce que le texte contient ce mot "**" ?
# na: c'est une case vide du tableau

# On regarde si le mot "data" apparaît dans la colonne "Intitulé du poste"
data_dans_titre = toutes_les_offres["Intitulé du poste"].str.contains("data", case=False, na=False)

# On garde une ligne si l'une des deux conditions est vraie
offres_data = toutes_les_offres[data_dans_metier | data_dans_titre]

print("Nombre d'offres data :", len(offres_data))

# On sauvegarde le résultat dans un nouveau fichier
offres_data.to_csv("offres_data_filtrees.csv", sep=";", index=False)
# index=False: ne numérote pas chaque ligne du tableau, vu qu'il est fait automatiquement sur Excel ou autre

print("Fichier créé : offres_data_filtrees.csv")
