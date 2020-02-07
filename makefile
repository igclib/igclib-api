install:
	pip install -r requirements.txt --user

runserver:
	gunicorn web.api:app --bind 0.0.0.0 --access-logfile access.log