release: pipenv run python src/manage.py migrate
watcher: pipenv run python src/manage.py watch_transactions
watcher: pipenv run python src/manage.py check_trustlines --loop
web: gunicorn --pythonpath src app.wsgi
