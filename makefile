install:
	pip install -r requirements.txt --user

runserver:
	cd web && gunicorn api:app