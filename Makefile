SHELL := bash
PATH := ./venv/bin:${PATH}
PYTHON=python3.7


all: test

venv:
		$(PYTHON) -m venv --prompt botmaker venv
		source venv/bin/activate
		pip install --quiet --upgrade pip

install-test:
		pip install -q .[test]

test: clean install-test lint
		python setup.py test

coverage: clean install-test lint
		coverage run --source=botmaker setup.py test
		coverage report -m

lint:
		pycodestyle setup.py botmaker/ tests/

clean:
		find . -name '*.pyc' -exec rm -f {} +
		find . -name '*.pyo' -exec rm -f {} +
		find . -name '*~' -exec rm -f {} +
		rm -rf build dist botmaker.egg-info

release: clean
		python setup.py sdist bdist_wheel
		twine upload dist/*


.PHONY: all install-test release test clean-pyc
