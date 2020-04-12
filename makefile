N_PROC := $(shell grep -c ^processor /proc/cpuinfo)

install:
	pip install -r requirements.txt --user

dev:
	export FLASK_APP=web/api.py && flask run

runserver:
	gunicorn web.api:app --workers $(N_PROC) --access-logfile access.log &> server.log