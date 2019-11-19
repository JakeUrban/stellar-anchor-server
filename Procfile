release: pipenv run python src/manage.py migrate
watch_transactions: pipenv run python src/manage.py watch_transactions
check_trustlines: pipenv run python src/manage.py check_trustlines --loop
web: gunicorn --pythonpath src app.wsgi
