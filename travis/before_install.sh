if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then 
    brew update         
    brew install python
    brew install pyqt
    brew install vtk
    brew install wxpython
else
    ccache -s
    export PATH=/usr/lib/ccache:${PATH}
    pip install --upgrade pip
    export DISPLAY=:99.0
    sh -e /etc/init.d/xvfb start
fi
