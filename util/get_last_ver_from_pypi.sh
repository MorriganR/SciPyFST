#!/bin/bash
set -e

PACKAGE_JSON_URL="https://pypi.org/pypi/${1}/json"

curl -L -s "$PACKAGE_JSON_URL" | jq  -r '.info.version' 
