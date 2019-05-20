find . -iname "*.py" | xargs pylint

pycodestyle .

# to blackify code remove --check flag
black --check .
