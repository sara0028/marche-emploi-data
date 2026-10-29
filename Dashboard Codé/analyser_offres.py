"""
CE PROGRAMME FAIT 3 CHOSES, DANS L'ORDRE :
1. Il charge le fichier propre (créé par nettoyer_offres.py)
2. Il compte les offres selon 4 critères : métier, télétravail, expérience, département
3. Il dessine un graphique pour chaque critère et l'enregistre en image (.png)
"""

import pandas as pd  # pandas : pour manipuler le tableau de données
import matplotlib.pyplot as plt  # matplotlib : pour dessiner des graphiques, on l'appelle "plt" pour faire plus court

# ------------------------------------------------------------
# ÉTAPE 1 : charger le fichier propre
# ------------------------------------------------------------

# dtype={"Département": str} dit à pandas de lire les départements comme du texte (sinon "75" deviendrait le nombre 75.0)
offres = pd.read_csv("offres_data_propres.csv", sep=";", dtype={"Département": str})  # on lit le CSV et on le met dans la variable "offres"

print("Nombre d'offres analysées :", len(offres))  # on affiche le nombre de lignes pour vérifier


# ------------------------------------------------------------
# GRAPHIQUE 1 : les métiers les plus recherchés
# ------------------------------------------------------------

metiers = offres["Métier"].value_counts().head(8)  # on compte combien d'offres par métier et on garde les 8 premiers

plt.figure(figsize=(10, 5))  # on crée un graphique plus grand (10 de large, 5 de haut) pour que le titre et les noms ne soient pas coupés
metiers.sort_values().plot(kind="barh")  # on trie du plus petit au plus grand et on dessine des barres horizontales ("barh")
plt.title("Les 8 métiers data les plus recherchés")  # le titre du graphique
plt.xlabel("Nombre d'offres")  # le texte sous l'axe horizontal
plt.ylabel("")  # on enlève le texte de l'axe vertical (inutile ici)
plt.tight_layout()  # on ajuste les marges pour que les noms de métiers ne soient pas coupés
plt.savefig("graphique_1_metiers.png")  # on enregistre le graphique dans une image
plt.close()  # on ferme le graphique pour repartir de zéro au suivant


# ------------------------------------------------------------
# GRAPHIQUE 2 : le télétravail
# ------------------------------------------------------------

teletravail = offres["Télétravail"].value_counts()  # on compte combien d'offres par réponse (Oui, Non, Non renseigné)

plt.figure(figsize=(8, 5))  # taille du graphique (8 de large, 5 de haut)
teletravail.plot(kind="bar")  # on dessine des barres verticales ("bar")
plt.title("Télétravail dans les offres data")  # le titre
plt.ylabel("Nombre d'offres")  # le texte sur l'axe vertical
plt.xlabel("")  # on enlève le texte de l'axe horizontal
plt.xticks(rotation=0)  # on garde les noms des barres à l'horizontale (sinon ils sont penchés)
plt.tight_layout()  # on ajuste les marges
plt.savefig("graphique_2_teletravail.png")  # on enregistre l'image
plt.close()  # on ferme le graphique


# ------------------------------------------------------------
# GRAPHIQUE 3 : le niveau d'expérience demandé
# ------------------------------------------------------------

experience = offres["Niveau d'expérience min. requis"].value_counts()  # on compte combien d'offres par niveau d'expérience

plt.figure(figsize=(8, 5))  # taille du graphique
experience.plot(kind="bar")  # barres verticales
plt.title("Niveau d'expérience demandé")  # le titre
plt.ylabel("Nombre d'offres")  # le texte sur l'axe vertical
plt.xlabel("")  # pas de texte sur l'axe horizontal
plt.xticks(rotation=0)  # noms à l'horizontale
plt.tight_layout()  # on ajuste les marges
plt.savefig("graphique_3_experience.png")  # on enregistre l'image
plt.close()  # on ferme le graphique


# ------------------------------------------------------------
# GRAPHIQUE 4 : les départements qui recrutent le plus
# ------------------------------------------------------------

# On enlève les offres sans département connu, pour ne pas fausser le classement
avec_departement = offres[offres["Département"] != "Non renseigné"]  # != veut dire "est différent de" : on garde les lignes où le département est connu

departements = avec_departement["Département"].value_counts().head(10)  # on compte par département et on garde les 10 premiers

plt.figure(figsize=(8, 5))  # taille du graphique
departements.plot(kind="bar")  # barres verticales
plt.title("Les 10 départements qui recrutent le plus en data")  # le titre
plt.ylabel("Nombre d'offres")  # le texte sur l'axe vertical
plt.xlabel("Numéro du département")  # le texte sur l'axe horizontal
plt.xticks(rotation=0)  # numéros à l'horizontale
plt.tight_layout()  # on ajuste les marges
plt.savefig("graphique_4_departements.png")  # on enregistre l'image
plt.close()  # on ferme le graphique

print("4 graphiques créés : regarde les fichiers graphique_1 à graphique_4 dans ton dossier.")  # message final
