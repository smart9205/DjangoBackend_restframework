export $(grep -v '^#' .env | xargs)
python manage.py runserver