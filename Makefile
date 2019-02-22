init:
	pip install -r requirements.txt

test:
	py.test --cov-config .coveragerc -vv --cov-report term --cov-report xml --cov=src tests/*

PHONY: init test
