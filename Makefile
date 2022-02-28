PYTHON := python

dev:
	export FLASK_ENV=development && $(PYTHON) src/main.py
