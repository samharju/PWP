#!/usr/bin/env sh
set -e

echo "Running all tests:"
coverage run -m pytest -v

echo "Test coverage:"
coverage report -m --skip-covered
echo "Saving coverage report to ./htmlcov/index.html"
coverage html

echo "Code syntax check:"
flake8
echo "- Code syntax ok."
echo "++ PASSED ++"
