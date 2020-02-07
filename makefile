install:
	pip install -r requirements.txt --user

runserver:
	gunicorn web.api:app --access-logfile access.log &> server.log