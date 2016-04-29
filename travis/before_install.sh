if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then 
    brew update         
    brew install python3
else
    ccache -s
    export PATH=/usr/lib/ccache:${PATH}
    pip install --upgrade pip
    export DISPLAY=:99.0
    sh -e /etc/init.d/xvfb start
fi
