Site web personnel

Troisième version de mon site web personnel héberger à l’adresse suivante : https://kevenimbeault.ca/ Cette version utilise Python, Flask, SQLite et Docker pour fonctionner !


Lancer le projet

1.	Renommez le fichier « Github_Key_Public.txt » à « Github_Key.txt »
2.	Installez Docker CE sur votre machine selon les instructions disponibles sur le site officiel de Docker : https://docs.docker.com/install/
3.	Lancer la commande : docker build --tag=website
4.	Lancer un conteneur avec l’image créer : docker run -p 4000:80 website
5.	Si tous ce passe bien vous pouvez maintenant accédez au site web via http://localhost:4000

Explication des fichiers

Fichiers statiques

Tous les fichiers statiques utiliser par l’application 

Templates

Le dossier /templates 
