#!/bin/bash
set -e
cd integrationtests/mayavi
coverage run --rcfile=../../.coveragerc -p run.py
cd ../..
cp integrationtests/mayavi/.coverage.* ./
