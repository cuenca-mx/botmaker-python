SHELL := bash
PATH := ./venv/bin:${PATH}
PYTHON=python3.7
PROJECT=botmaker
isort = isort $(PROJECT) tests setup.py
black = black -S -l 79 --target-version py37 $(PROJECT) tests setup.py


all: test

venv:
		$(PYTHON) -m venv --prompt $(PROJECT) venv
		source venv/bin/activate
		pip install --quiet --upgrade pip

install-test:
		pip install importlib-metadata==4.2.0
		pip install -q .[test]

test: clean install-test lint
		python setup.py test

format:
		$(isort)
		$(black)

lint:
		$(isort) --check-only
		$(black) --check
		flake8 $(PROJECT) tests setup.py
		mypy $(PROJECT) tests

clean:
		find . -name '*.pyc' -exec rm -f {} +
		find . -name '*.pyo' -exec rm -f {} +
		find . -name '*~' -exec rm -f {} +
		rm -rf build dist $(PROJECT).egg-info

release: clean
		python setup.py sdist bdist_wheel
		twine upload dist/*


.PHONY: all install-test test format lint clean release
