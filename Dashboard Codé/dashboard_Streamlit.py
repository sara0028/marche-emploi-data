"""
DASHBOARD STREAMLIT : Observatoire du marché de l'emploi Data (fonction publique)

Ce programme:
- charge le fichier propre (offres_data_propres.csv)
- affiche des filtres sur le côté (métier, télétravail, expérience ; vide = tout afficher)
- applique ces filtres aux données
- affiche des chiffres, des graphiques et un tableau qui se mettent à jour

Pour le lancer :  py -m streamlit run app.py
"""

import pandas as pd  # pandas : pour manipuler le tableau de données
import streamlit as st  # streamlit : pour créer la page web


# TITRE DE LA PAGE

st.set_page_config(page_title="Marché de l'emploi Data", layout="wide")  # titre de l'onglet du navigateur, et page en pleine largeur
# layout: comment le contenu sera réparti dans la page
st.title("Observatoire du marché de l'emploi Data")  # le grand titre en haut de la page
st.write("Offres d'emploi data de la fonction publique française (source : data.gouv.fr, « Choisir le Service Public »).")  # une phrase de présentation



# CHARGER LE FICHIER

offres = pd.read_csv("offres_data_propres.csv", sep=";", dtype={"Département": str})  # on lit le CSV propre (départements lus comme du texte)



# LES FILTRES (dans la barre latérale à gauche)

st.sidebar.header("Filtres")  # un titre pour la barre latérale

# Pour chaque filtre : on fait la liste des valeurs possibles, puis l'utilisateur choisit celles qu'il veut
# Si l'utilisateur ne choisit rien, on affiche tout (placeholder="Tous" l'indique à l'écran)

liste_metiers = sorted(offres["Métier"].unique())  # tous les métiers présents dans le fichier
# sorted(...): range la liste dans l'ordre alphabétique 
# .unique(): enlève les doublons
choix_metiers = st.sidebar.multiselect("Métier", liste_metiers, placeholder="Tous")  # le filtre "Métier"
# placeholder: texte d'exemple grisé dans un champ vide 

liste_teletravail = sorted(offres["Télétravail"].unique())  # toutes les réponses possibles pour le télétravail
choix_teletravail = st.sidebar.multiselect("Télétravail", liste_teletravail, placeholder="Tous")  # le filtre "Télétravail"

liste_experience = sorted(offres["Niveau d'expérience min. requis"].unique())  # tous les niveaux d'expérience possibles
choix_experience = st.sidebar.multiselect("Niveau d'expérience", liste_experience, placeholder="Tous")  # le filtre "Expérience"



# APPLIQUER LES FILTRES

# On part de tout le tableau, puis on le réduit filtre après filtre
offres_filtrees = offres  # au départ, on garde toutes les offres

if choix_metiers:  # si au moins un métier est choisi
    offres_filtrees = offres_filtrees[offres_filtrees["Métier"].isin(choix_metiers)]  # on garde seulement ces métiers
    # .isin(liste) vérifie si la valeur est dans la liste choisie

if choix_teletravail:  # si au moins une réponse télétravail est choisie
    offres_filtrees = offres_filtrees[offres_filtrees["Télétravail"].isin(choix_teletravail)]  # on garde seulement ces réponses

if choix_experience:  # si au moins un niveau d'expérience est choisi
    offres_filtrees = offres_filtrees[offres_filtrees["Niveau d'expérience min. requis"].isin(choix_experience)]  # on garde seulement ces niveaux



# LES CHIFFRES CLÉS

col1, col2, col3 = st.columns(3)  # on crée 3 colonnes côte à côte pour afficher 3 chiffres

col1.metric("Offres affichées", len(offres_filtrees))  # nombre de lignes après filtrage
col2.metric("Métiers différents", offres_filtrees["Métier"].nunique())  
# .nunique(): compte les valeurs différentes
col3.metric("Départements", offres_filtrees[offres_filtrees["Département"] != "Non renseigné"]["Département"].nunique())  # nombre de départements connus

# Si les filtres ne laissent aucune offre, on prévient et on arrête là (sinon les graphiques seraient vides)
if len(offres_filtrees) == 0:  # si le tableau filtré est vide
    st.warning("Aucune offre ne correspond à ces filtres. Élargis ta sélection dans la barre de gauche.")  # un message d'avertissement
    st.stop()  # on arrête l'affichage de la page ici



# LES GRAPHIQUES

gauche, droite = st.columns(2)  # on crée 2 colonnes pour mettre deux graphiques côte à côte

# Graphique 1 : les métiers (colonne de gauche)
with gauche:  # dans la colonne de gauche
    st.subheader("Métiers les plus recherchés")  # le titre du graphique
    metiers = offres_filtrees["Métier"].value_counts().head(8)  # on compte les offres par métier, on garde les 8 premiers
    st.bar_chart(metiers, horizontal=True, sort=False)  
    # horizontal=True: : les options sont alignées en ligne
    # sort=False: garde l'ordre du plus grand au plus petit

# Graphique 2 : les départements (colonne de droite)
with droite:  # dans la colonne de droite
    st.subheader("Départements qui recrutent le plus")  # le titre du graphique
    departements_connus = offres_filtrees[offres_filtrees["Département"] != "Non renseigné"]  # on enlève les départements inconnus
    departements = departements_connus["Département"].value_counts().head(10)  # on compte par département, on garde les 10 premiers
    st.bar_chart(departements, sort=False)  
    # horizontal=False(par défaut): les options sont empilées

gauche2, droite2 = st.columns(2)  # deux nouvelles colonnes pour la deuxième ligne de graphiques

# Graphique 3 : le télétravail
with gauche2:  # colonne de gauche
    st.subheader("Télétravail")  # le titre
    teletravail = offres_filtrees["Télétravail"].value_counts()  # on compte les offres par réponse
    st.bar_chart(teletravail, sort=False)  # barres verticales

# Graphique 4 : l'expérience demandée
with droite2:  # colonne de droite
    st.subheader("Niveau d'expérience demandé")  # le titre
    experience = offres_filtrees["Niveau d'expérience min. requis"].value_counts()  # on compte les offres par niveau
    st.bar_chart(experience, sort=False)  # barres verticales



# LE TABLEAU DES OFFRES

st.subheader("Détail des offres")  # le titre du tableau
st.dataframe(offres_filtrees, width="stretch")  # on affiche le tableau filtré, sur toute la largeur de la page



# LES LIMITES DE L'ANALYSE

st.caption( 
    "Limites : ces données ne concernent que la fonction publique (pas le secteur privé), "
    "et beaucoup d'offres ne précisent pas le télétravail, l'expérience ou les études ('Non renseigné')."
)
# st.caption affiche un petit texte discret en bas de page
