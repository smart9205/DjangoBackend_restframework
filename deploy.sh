docker build . --tag django-backend:latest
docker rm --force django-backend
docker run --detach --name django-backend --publish 80:80 django-backend:latest