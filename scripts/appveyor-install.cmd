"%sdkver%" -q -version:v7.0
call setenv /x64
pip install --cache-dir c:/tmp -r appveyor-requirements.txt
python setup.py develop
