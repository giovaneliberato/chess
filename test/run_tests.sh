set -e

cd $(dirname $0) && cd ..

flake8 . --ignore=E501

coverage erase
coverage run test/run_tests.py
coverage report -m --include=chess/* --omit=test/*
