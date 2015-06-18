"%sdkver%" -q -version:v7.0
call setenv /x64
python setup.py test
