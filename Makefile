PYTHON 	:= python
PORT	:= 9091

dev:
	cd src && uvicorn main:app --reload --port=$(PORT)

start:
	cd src && uvicorn main:app --port=$(PORT)
