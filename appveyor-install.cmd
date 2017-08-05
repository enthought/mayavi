"%sdkver%" -q -version:v7.0
call setenv /x64

rem install python packages
pip install --cache-dir c:/temp nose
pip install --cache-dir c:/temp mock
pip install --cache-dir c:/temp Sphinx
pip install --cache-dir c:/temp coverage
pip install --cache-dir c:/temp numpy
pip install --cache-dir c:/temp pyside
pip install --cache-dir c:/temp psutil
pip install --cache-dir c:/temp traits
pip install --cache-dir c:/temp traitsui
pip install --cache-dir c:/temp apptools
pip install --cache-dir c:/temp pyface
pip install --cache-dir c:/temp envisage

rem install mayavi
python setup.py develop
