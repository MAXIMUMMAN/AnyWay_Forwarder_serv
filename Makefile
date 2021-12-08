TESTS = tests

VENV ?= .venv
CODE = tests app

.PHONY: venv
venv:
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

.PHONY: run
run:
	$(VENV)/bin/uvicorn main:app  --host '127.0.0.1' --reload
