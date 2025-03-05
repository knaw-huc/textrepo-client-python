.PHONY: docs docs-source help clean tests install publish version-update-patch version-update-minor version-update-major

all: help
SHELL=/bin/bash

docs:
	cd docs && rm -rf generated && make clean && make html

apidoc-doc-source:
	sphinx-apidoc -o docs/source/api --separate --force --module-first pagexml

clean:
	cd docs && rm -rf generated && make clean

tests:
	poetry run python -m unittest tests/*_test.py

poetry.lock: pyproject.toml
	poetry update --lock

docs/requirements.txt: poetry.lock
	poetry export -o docs/requirements.txt --without-hashes

install:
	poetry lock && poetry install

publish:
	poetry build && poetry publish

version-update-patch:
	poetry run version patch

version-update-minor:
	poetry run version minor

version-update-major:
	poetry run version major

help:
	@echo "make-tools for textrepo-client"
	@echo
	@echo "Please use \`make <target>', where <target> is one of:"
	@echo "  install               - to install the necessary requirements"
	@echo "  pdoc                  - generate pdoc html pages in docs"
	@echo "  clean                 - to remove all generated files and directories"
	@echo "  tests                 - to run the unit tests in tests/"
	@echo
	@echo "  version-update-patch  - to update the project version to the next patch version"
	@echo "  version-update-minor  - to update the project version to the next minor version"
	@echo "  version-update-major  - to update the project version to the next major version"
	@echo
	@echo "  publish               - to publish to pypi"
	@echo "  docs/requirements.txt - to update the requirements.txt based on poetry.lock (required by readthedocs)"
	@echo
