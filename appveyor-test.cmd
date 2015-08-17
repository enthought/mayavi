"%sdkverpath%" -q -version:"%sdkver%"
call setenv /x64
coverage erase
coverage run -p -m nose.core -v tvtk/tests
if %errorlevel% neq 0 exit /b %errorlevel%
coverage run -p -m nose.core -v mayavi
if %errorlevel% neq 0 exit /b %errorlevel%
coverage combine
coverage report
