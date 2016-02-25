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
pip install --cache-dir c:/temp git+http://github.com/enthought/traits.git#egg=traits
pip install --cache-dir c:/temp git+http://github.com/enthought/traitsui.git#egg=traitsui
pip install --cache-dir c:/temp git+http://github.com/enthought/apptools.git#egg=apptools
pip install --cache-dir c:/temp git+http://github.com/enthought/pyface.git#egg=pyface
pip install --cache-dir c:/temp git+http://github.com/enthought/envisage.git#egg=envisage

rem install mayavi
python setup.py develop
