# Connexion au service container d'Heroku
heroku container:login

# Création de l'application
heroku create dashboard-kevin-ynov

# Construction de l'image Docker sous MacOS Apple Silicon
docker buildx build --platform linux/amd64 -t dashboard-kevin-ynov .

# Construction de l'image Docker sous Windows
docker build . -t dashboard-kevin-ynov

# Tag Image Docker au registery d'Heroku
docker tag api-ynov-kevin registry.heroku.comdashboard-kevin-ynov/web

# Publication de l'image Docker dans le registery d'Heroku
docker push registry.heroku.com/dashboard-kevin-ynov/web

# Configuration du cotainer
heroku stack:set container -a dashboard-kevin-ynov

# Activation du container
heroku container:release web -a dashboard-kevin-ynov

# Ouverture de l'application
heroku open -a dashboard-kevin-ynov
