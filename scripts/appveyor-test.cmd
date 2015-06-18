"%sdkver%" -q -version:v7.0
call setenv /x64
coverage erase
coverage run -p -m nose.core -v tvtk/tests
coverage run -p -m nose.core -v mayavi
cd integrationtests/mayavi
coverage run --rcfile=../../.coveragerc -p run.py
cd ../../
copy integrationtests/mayavi/.coverage.* ./
coverage combine
coverage report
b
