#!/usr/bin/make

prepare:
	python -m venv .venv --prompt posta

start:
	python main.py