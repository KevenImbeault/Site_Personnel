# Site web personnel
Troisième version de mon site web personnel héberger à l’adresse suivante : https://kevenimbeault.ca/ Cette version utilise Python, Flask, SQLite et Docker pour fonctionner !

# Lancer le projet
WIP

# Explication des fichiers

## Fichiers statiques
Tous les fichiers statiques utilisés par l’application se trouvent dans le dossier /static. Les stylesheets en css sont dans le chemin /static/css et les fichiers javascript sont dans /static/js.

*Template.css* – Stylesheeet pour l’application en entier. 

*Script.js* – Script qui crée une DataTable dans la page Développement logiciel, permettant ainsi de faire des recherches, avoir plusieurs pages et quelques autres choses.

## Templates
Les templates se trouvent dans le dossier /templates et servent à créer les différentes pages du site web.

*Template.html* – Ce fichier comprend la barre de navigation et le footer utiliser dans toutes les pages du site web

*Home.html* – Ce template sert à créer le contenu de la page Accueil

*Software.html* – Même chose que le template « home » mais pour la page Développement logiciel

## Autres fichiers
*Main.py* – Fichier principal de l’application, contient le timer pour faire la mise à jour de la base de donnés au lancement de l’application ainsi qu’à toutes les heures par la suite. Crée l’application Flask.

*DB_Updater.py* – Pour l’instant ce fichier contient seulement une fonction, ` Update_Database()`, qui permet de mettre à jour 

*Web.db* – Base de données SQLite contenant seulement une table nommé « GITHUB » pour créer le tableau de la page Développement logiciel
