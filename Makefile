#!/usr/bin/make

prepare:
	python -m venv .venv --prompt posta && source .venv/bin/activate && pip install -r requirements.txt -r requirements-dev.txt

start:
	python -m flask run --port 5999