"""
CE PROGRAMME FAIT 6 GRAPHIQUES DE PLUS (suite de analyser_offres.py) :
5. Le niveau d'études demandé
6. La répartition des 5 métiers les plus fréquents (camembert)
7. Les départements qui recrutent le plus, hors Île-de-France
8. Pour chaque métier : télétravail oui / non
9. Pour chaque métier : niveau d'expérience demandé
10. Pour chaque métier : niveau d'études demandé

Les graphiques 8, 9 et 10 sont des graphiques "croisés" : on regarde deux
colonnes en même temps (par exemple le métier ET le télétravail).
"""

import pandas as pd  # pandas : pour manipuler le tableau de données
import matplotlib.pyplot as plt  # matplotlib : pour dessiner les graphiques

# ------------------------------------------------------------
# CHARGER LE FICHIER PROPRE
# ------------------------------------------------------------

offres = pd.read_csv("offres_data_propres.csv", sep=";", dtype={"Département": str})  # on lit le CSV (départements lus comme du texte)

print("Nombre d'offres analysées :", len(offres))  # on affiche le nombre de lignes pour vérifier

# On prépare la liste des 5 métiers les plus fréquents : on s'en servira pour les graphiques croisés
# (avec tous les métiers, les graphiques seraient illisibles)
top5_metiers = offres["Métier"].value_counts().head(5).index  # .index récupère juste les NOMS des 5 métiers (pas leurs nombres)


# ------------------------------------------------------------
# GRAPHIQUE 5 : le niveau d'études demandé
# ------------------------------------------------------------

# On enlève les offres où le niveau d'études n'est pas indiqué, sinon cette barre écraserait toutes les autres
etudes_connues = offres[offres["Niveau d'études"] != "Non renseigné"]  # != veut dire "est différent de"

etudes = etudes_connues["Niveau d'études"].value_counts()  # on compte combien d'offres par niveau d'études

plt.figure(figsize=(10, 5))  # taille du graphique (10 de large, 5 de haut)
etudes.sort_values().plot(kind="barh")  # on trie et on dessine des barres horizontales
plt.title("Niveau d'études demandé (uniquement les offres qui le précisent)")  # le titre
plt.xlabel("Nombre d'offres")  # le texte sous l'axe horizontal
plt.ylabel("")  # pas de texte sur l'axe vertical
plt.tight_layout()  # on ajuste les marges
plt.savefig("graphique_5_etudes.png")  # on enregistre l'image
plt.close()  # on ferme le graphique


# ------------------------------------------------------------
# GRAPHIQUE 6 : camembert des 5 métiers les plus fréquents
# ------------------------------------------------------------

metiers_top5 = offres["Métier"].value_counts().head(5)  # on compte les offres par métier et on garde les 5 premiers

plt.figure(figsize=(13, 6))  # taille du graphique (large pour que les noms de métiers ne soient pas coupés)
metiers_top5.plot(kind="pie", autopct="%1.0f%%")  # "pie" = camembert, autopct affiche les pourcentages sur chaque part
plt.title("Répartition entre les 5 métiers les plus fréquents")  # le titre
plt.ylabel("")  # on enlève le texte sur le côté (inutile pour un camembert)
plt.tight_layout()  # on ajuste les marges
plt.savefig("graphique_6_camembert_metiers.png")  # on enregistre l'image
plt.close()  # on ferme le graphique


# ------------------------------------------------------------
# GRAPHIQUE 7 : les départements hors Île-de-France
# ------------------------------------------------------------

# Les numéros des départements d'Île-de-France
ile_de_france = ["75", "77", "78", "91", "92", "93", "94", "95"]  # une liste de textes

# On garde les offres dont le département est connu ET n'est pas en Île-de-France
# .isin(liste) vérifie si la valeur est dans la liste ; le ~ devant veut dire "le contraire" (donc : PAS dans la liste)
# le & veut dire "et" : les deux conditions doivent être vraies
hors_idf = offres[(offres["Département"] != "Non renseigné") & (~offres["Département"].isin(ile_de_france))]

departements_hors_idf = hors_idf["Département"].value_counts().head(10)  # on compte par département et on garde les 10 premiers

plt.figure(figsize=(8, 5))  # taille du graphique
departements_hors_idf.plot(kind="bar")  # barres verticales
plt.title("Les 10 départements qui recrutent le plus en data (hors Île-de-France)")  # le titre
plt.ylabel("Nombre d'offres")  # texte sur l'axe vertical
plt.xlabel("Numéro du département")  # texte sur l'axe horizontal
plt.xticks(rotation=0)  # numéros à l'horizontale
plt.tight_layout()  # on ajuste les marges
plt.savefig("graphique_7_departements_hors_idf.png")  # on enregistre l'image
plt.close()  # on ferme le graphique


# ------------------------------------------------------------
# GRAPHIQUE 8 : pour chaque métier, télétravail oui / non
# ------------------------------------------------------------

# On garde seulement les 5 métiers principaux, et les offres où le télétravail est précisé
# .isin(top5_metiers) vérifie que le métier fait partie des 5 premiers ; & veut dire "et"
sous_tableau = offres[offres["Métier"].isin(top5_metiers) & (offres["Télétravail"] != "Non renseigné")]

# pd.crosstab compte, pour chaque métier, combien d'offres ont "Oui" et combien ont "Non"
# Le résultat est un petit tableau : une ligne par métier, une colonne par réponse
croise_teletravail = pd.crosstab(sous_tableau["Métier"], sous_tableau["Télétravail"])

croise_teletravail.plot(kind="barh", stacked=True, figsize=(10, 5))  # barres horizontales "empilées" (Oui et Non dans la même barre)
plt.title("Télétravail selon le métier (offres qui le précisent)")  # le titre
plt.xlabel("Nombre d'offres")  # texte sous l'axe horizontal
plt.ylabel("")  # pas de texte sur l'axe vertical
plt.tight_layout()  # on ajuste les marges
plt.savefig("graphique_8_metier_teletravail.png")  # on enregistre l'image
plt.close()  # on ferme le graphique


# ------------------------------------------------------------
# GRAPHIQUE 9 : pour chaque métier, niveau d'expérience demandé
# ------------------------------------------------------------

# Même principe que le graphique 8, mais avec la colonne "Niveau d'expérience min. requis"
sous_tableau = offres[offres["Métier"].isin(top5_metiers) & (offres["Niveau d'expérience min. requis"] != "Non renseigné")]  # 5 métiers + expérience précisée

croise_experience = pd.crosstab(sous_tableau["Métier"], sous_tableau["Niveau d'expérience min. requis"])  # on compte pour chaque métier

croise_experience.plot(kind="barh", stacked=True, figsize=(10, 5))  # barres horizontales empilées
plt.title("Niveau d'expérience demandé selon le métier (offres qui le précisent)")  # le titre
plt.xlabel("Nombre d'offres")  # texte sous l'axe horizontal
plt.ylabel("")  # pas de texte sur l'axe vertical
plt.tight_layout()  # on ajuste les marges
plt.savefig("graphique_9_metier_experience.png")  # on enregistre l'image
plt.close()  # on ferme le graphique


# ------------------------------------------------------------
# GRAPHIQUE 10 : pour chaque métier, niveau d'études demandé
# ------------------------------------------------------------

# Même principe, avec la colonne "Niveau d'études"
sous_tableau = offres[offres["Métier"].isin(top5_metiers) & (offres["Niveau d'études"] != "Non renseigné")]  # 5 métiers + études précisées

croise_etudes = pd.crosstab(sous_tableau["Métier"], sous_tableau["Niveau d'études"])  # on compte pour chaque métier

croise_etudes.plot(kind="barh", stacked=True, figsize=(11, 5))  # barres horizontales empilées
plt.title("Niveau d'études demandé selon le métier (offres qui le précisent)")  # le titre
plt.xlabel("Nombre d'offres")  # texte sous l'axe horizontal
plt.ylabel("")  # pas de texte sur l'axe vertical
plt.tight_layout()  # on ajuste les marges
plt.savefig("graphique_10_metier_etudes.png")  # on enregistre l'image
plt.close()  # on ferme le graphique

print("6 graphiques créés : fichiers graphique_5 à graphique_10 dans ton dossier.")  # message final
