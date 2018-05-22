#test

project is a websocket with django

python3 manage.py test chat.tests

#run

python3 manage.py runserver 0.0.0.0:9000

#uwsgi
#notification: uwsgi should installed by pip3

daphne django_websocket.asgi:application --port 9001 & uwsgi --http :9000 --module django_websocket.wsgi

#add nginx with uwsgi

uwsgi --socket ./../web/compass.sock --wsgi-file ./django_websocket/wsgi.py --chmod-socket=666 --master --processes 2 --threads 2 & daphne django_websocket.asgi:application --port 8001
