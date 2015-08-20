#!/bin/bash
set -e
cd ../integrationtests/mayavi
if [[ ${TRAVIS_PYTHON_VERSION} == "3.4"  ]]; then
    python -m lib2to3.py -w ./
fi
coverage run --rcfile=../../.coveragerc -p run.py
cd ../..
cp integrationtests/mayavi/.coverage.* ./
