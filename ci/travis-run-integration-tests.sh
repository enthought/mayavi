#!/bin/bash
set -e
cd integrationtests/mayavi
edm run -- coverage run --rcfile=../../.coveragerc -p run.py
cd ../..
cp integrationtests/mayavi/.coverage.* ./
