# Personal website
Third version of my website, currently hosted on https://kevenimbeault.ca/. This version uses Python with various modules include Flask and SQL-Alchemy as well as SQLite.

# Launch project
WIP

# Files explanation

## Static files
All static files that are used by the application can be found in the /static folder. CSS stylesheets are in /static/css while javascript files are in /static/js.

*Template.css* – Stylesheet used for the entire application.

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
