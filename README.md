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
