# Based on
# https://github.com/getsentry/sentry-python/blob/master/scripts/bump-version.sh
#!/bin/bash

PROJECT="botmaker"
SCRIPT_DIR="$( dirname "$0" )"
cd ${SCRIPT_DIR}/..

OLD_VERSION="${1}"
NEW_VERSION="${2}"

echo "Current version: $OLD_VERSION"
echo "Bumping version: $NEW_VERSION"

function replace() {
    ! grep "$2" $3
    perl -i -pe "s/$1/$2/g" $3
    grep "$2" $3  # verify that replacement was successful
}

replace "version=\'[0-9.]+\'" "version=\'$NEW_VERSION\'" ./setup.py
replace "__version__ = \'[0-9.]+\'" "__version__ = \'$NEW_VERSION\'" ./${PROJECT}/__init__.py

git commit ./setup.py ./${PROJECT}/__init__.py -m "Bump version."