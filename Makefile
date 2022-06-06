#!/usr/bin/make

prepare:
	python -m venv .venv --prompt posta

start:
	python -m flask run --port 5999