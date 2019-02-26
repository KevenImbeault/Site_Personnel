# Site web personnel
Troisième version de mon site web personnel héberger à l’adresse suivante : https://kevenimbeault.ca/ Cette version utilise Python, Flask, SQLite et Docker pour fonctionner !

# Lancer le projet
1.	Renommez le fichier « Github_Key_Public.txt » à « Github_Key.txt »
2.	Installez Docker CE sur votre machine selon les instructions disponibles sur le site officiel de Docker : https://docs.docker.com/install/
3.	Lancer la commande : `docker build --tag=website`
4.	Lancer un conteneur avec l’image créer : `docker run –detach  --name website -p 4000:80 website`
5.	Si tous se passe bien vous pouvez maintenant accédez au site web via http://localhost:4000

Lorsque vous voulez arrêter le conteneur utilisez la commande : `docker container stop website`. Par la suite, vous pouvez supprimez le conteneur avec la commande : `docker container rm website`. Finalement, vous pouvez supprimez l’image avec la commande : `docker image remove website`.

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

## Docker
*Dockerfile* – Fichier utiliser par Docker pour créer l’image de l’application

*Requirement.txt* – Fichier texte contenant toutes les modules Python nécessaire pour faire fonctionner l’application

## Autres fichiers
*Main.py* – Fichier principal de l’application, contient le timer pour faire la mise à jour de la base de donnés au lancement de l’application ainsi qu’à toutes les heures par la suite. Crée l’application Flask.

*DB_Updater.py* – Pour l’instant ce fichier contient seulement une fonction, ` Update_Database()`, qui permet de mettre à jour 

*Web.db* – Base de données SQLite contenant seulement une table nommé « GITHUB » pour créer le tableau de la page Développement logiciel
