.PHONY: install clean-venv \
	run test \
	site-build site-serve site-deploy

install:
	@poetry config virtualenvs.in-project true
	@poetry install
	$(MAKE) ~/.bash_completion
	@echo install complete

clean-venv:
	rm -rf .venv
	find -iname "*.pyc" -delete

~/.bash_completion:
	poetry completions bash >> ~/.bash_completion

run:
	@poetry run python wehyconfig

test:
	@poetry run pytest

site-build:
	@poetry run mkdocs build

site-serve:
	@poetry run mkdocs serve

site-deploy:
	@poetry run mkdocs gh-deploy

