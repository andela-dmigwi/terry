# Created by Migwi Ndung'u  @April 2017
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
gunicorn manage:app --log-file=-