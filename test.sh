#!/usr/bin/env sh
set -e

pytest -v

flake8
echo "Code syntax ok."
