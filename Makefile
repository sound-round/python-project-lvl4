build:
	poetry build

package-install:
	pip install --user dist/*.whl

force-package-install:
	pip install --force-reinstall --user dist/*.whl

install:
	poetry install

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 task_manager

test:
	poetry run coverage run manage.py test task_manager -v 2

test-log:
	poetry run pytest -vv -o log_cli=true --log-level debug

test-coverage:
	poetry run coverage xml