.PHONY: install clean-venv \
	run test

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