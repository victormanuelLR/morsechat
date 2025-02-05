#!/usr/bin/env bash 
#exit on error 

set -o errexit 

pip install -r requirements.txt 

python manage.py collectstatic --no-input 
python manage.py findstatic core/images/morse-chat.png

python manage.py migrate 
if [[ $CREATE_SUPERUSER ]]; 
then 
python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL" 
python manage.py shell -c "from room.models import Room; Room.objects.get_or_create(name='Morsechat', slug='default-room')"

fi