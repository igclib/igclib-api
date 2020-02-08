N_PROC := $(shell grep -c ^processor /proc/cpuinfo)

install:
	pip install -r requirements.txt --user

runserver:
	gunicorn web.api:app --workers $(N_PROC) --timeout=300 --access-logfile access.log &> server.log