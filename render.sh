curl -sSL https://install.python-poetry.org | python3 -
poetry install
make migrate
make addadmin
make collectstatic
