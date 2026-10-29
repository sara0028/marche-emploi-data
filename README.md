# Observatoire du Marché de l'Emploi Data (Fonction Publique)

Ce projet est une chaîne complète d'analyse de données portant sur les offres d'emploi dans le domaine de la Data au sein de la fonction publique française. Les données d'origine proviennent de *data.gouv.fr*

Le projet part d'un fichier brut pour aller jusqu'à la création de tableaux de bord interactifs, en passant par le nettoyage des données et la génération de graphiques statiques.

##  Démarche et Choix Techniques

* **Source des données (API vs CSV) :** Au cours de ce projet, j'ai étudié et compris le fonctionnement des API pour la récupération automatisée de données. Cependant, j'ai fait le choix de continuer avec l'extraction des fichiers CSV statiques de *data.gouv.fr* afin de me concentrer pleinement sur le pipeline de traitement, le nettoyage et la restitution visuelle.
* **La double approche Dashboard :** J'ai voulu réaliser deux tableaux de bord distincts pour démontrer ma maîtrise de deux approches différentes :
  1. **L'approche "Code" :** Un dashboard développé de A à Z en Python en utilisant la bibliothèque **Streamlit**.
  2. **L'approche "Outil BI" :** Un dashboard construit "à la main" visuellement à l'aide de **Microsoft Power BI**.

##  Fonctionnalités

Le projet est divisé en 5 grandes étapes :

1. **Filtrage** : Extraction des offres liées à la Data depuis le fichier global de la fonction publique.
2. **Nettoyage** : Suppression des doublons, traitement des valeurs manquantes et formatage (ex: extraction des numéros de département).
3. **Analyse statique** : Génération de 10 graphiques (.png) pour comprendre les tendances (métiers les plus recherchés, télétravail, niveau d'études, etc.) via Python.
4. **Dashboard interactif codé (Streamlit)** : Une interface web codée en Python permettant de filtrer les données en temps réel.
5. **Dashboard interactif BI (Power BI)** : Une analyse visuelle interactive complète réalisée manuellement pour une exploration approfondie.

##  Prérequis et Installation

Assure-toi d'avoir Python installé sur ta machine, ainsi que [Power BI Desktop](https://powerbi.microsoft.com/desktop/) si tu souhaites ouvrir le fichier `.pbix`.

1. Clone ce projet dans ton dossier local.
2. Ouvre un terminal dans le dossier du projet.
3. Installe les bibliothèques Python requises en utilisant le fichier `requirements.txt` :
   ```bash
   pip install -r requirements.txt
   ```
   *(Les bibliothèques utilisées sont `pandas`, `matplotlib` et `streamlit`)*.

##  Comment utiliser le projet ?

Pour que le traitement des données fonctionne correctement, les scripts Python doivent être lancés dans cet ordre :

### Étape 1 : Filtrage des données
Génère le fichier `offres_data_filtrees.csv` à partir des données brutes.
```bash
python filtrer_offres_simple.py
```

### Étape 2 : Nettoyage des données
Crée le fichier propre et prêt à être analysé `offres_data_propres.csv`.
```bash
python nettoyer_offres.py
```

### Étape 3 : Création des graphiques
Ces deux scripts vont générer 10 images `.png` (graphique_1 à graphique_10) dans le dossier de ton projet.
```bash
python analyser_offres.py
python analyser_offres2.py
```

### Étape 4 : Lancement du Dashboard codé (Streamlit)
Lance l'application web Streamlit pour explorer les données visuellement.
```bash
streamlit run dashboard_Streamlit.py
```

### Étape 5 : Exploration du Dashboard BI (Power BI)
Ouvre simplement le fichier `Dashboard PowerBI.pbix` en faisant un double-clic dessus (nécessite d'avoir installé Power BI Desktop). Le fichier est déjà connecté aux données nettoyées pour explorer les rapports de manière interactive.

##  Structure des fichiers

* **Scripts Python** :
  * `filtrer_offres_simple.py` : Script d'extraction des offres "data".
  * `nettoyer_offres.py` : Script de nettoyage (doublons, valeurs nulles, départements).
  * `analyser_offres.py` : Génération des 4 premiers graphiques d'analyse de base.
  * `analyser_offres2.py` : Génération de 6 graphiques avancés et croisés.
  * `dashboard_Streamlit.py` : Code de l'application web interactive.
* **Tableaux de Bord** :
  * `Dashboard PowerBI.pbix` : Rapport interactif complet Microsoft Power BI.
* **Configuration** :
  * `requirements.txt` : Liste des dépendances Python.
* **Données** :
  * Fichiers CSV : `offres_data_filtrees.csv` (intermédiaire) et `offres_data_propres.csv` (final).

##  Limites de l'analyse

* Les données ne concernent **que la fonction publique** (le secteur privé n'est pas inclus).
* Beaucoup d'offres manquent de précision concernant le télétravail, l'expérience requise ou le niveau d'études (marquées comme "Non renseigné").