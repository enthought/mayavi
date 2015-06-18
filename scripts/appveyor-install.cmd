"%sdkver%" -q -version:v7.0
call setenv /x64
pip install nose
pip install Sphinx
pip install coverage
pip install numpy
pip install pyside
# Test against the current master of traits, traitsui and apptools
pip install git+http://github.com/enthought/traits.git#egg=traits
pip install git+http://github.com/enthought/traitsui.git#egg=traitsui
pip install git+http://github.com/enthought/apptools.git#egg=apptools
pip install git+http://github.com/enthought/pyface.git#egg=pyface
pip install git+http://github.com/enthought/envisage.git#egg=envisage
python setup.py develop
