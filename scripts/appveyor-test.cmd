"%sdkver%" -q -version:v7.0
call setenv /x64
coverage erase
coverage run -p -m nose.core -v tvtk/tests
coverage run -p -m nose.core -v mayavi
# Run the integration tests.
cd integrationtests/mayavi
coverage run --rcfile=../../.coveragerc -p run.py
cd ../../
cp integrationtests/mayavi/.coverage.* ./
coverage combine
coverage report
