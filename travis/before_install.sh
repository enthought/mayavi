if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    brew update
    brew tap homebrew/science
    brew tap homebrew/python
    brew install python
    brew install pyqt
    brew install wxpython
    brew install numpy

    which python
    python --version
else
    ccache -s
    export PATH=/usr/lib/ccache:${PATH}
    pip install --upgrade pip
    export DISPLAY=:99.0
    /sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_99.pid --make-pidfile --background --exec /usr/bin/Xvfb -- :99 -ac -screen 0 1024x768x24
    sleep 3
fi
