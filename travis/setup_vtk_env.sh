#!/bin/bash

if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then 
    if [[ "${VTK_VERSION}" == "5.8" ]]; then 
        # With vtk 5, we install the 5.8 standard we get from brew
        brew install vtk5
        export PYTHONPATH=/usr/local/opt/vtk5/lib/python2.7/site-packages
        export DYLD_LIBRARY_PATH=/usr/local/opt/vtk5/lib
    elif [[ "${VTK_VERSION}" == "6.3" ]]; then 
        # unfortunately we can't do this, for the following reasons:
        #  - brew does not provide VTK 6, so we would have to have to download it
        #  - unfortunately, it's built against the Apple python, so we would have 
        #    to change the dependency path for the python library with install_name_tool
        #  - also unfortunately, it's built against python 2.6, so we can't use it against
        #    libpythn2.7
        echo "Cannot work against VTK 6.3. VTK provided links against incorrect python version"
        exit 1
    elif [[ "${VTK_VERSION}" == "7.0" ]]; then 
        # Brew has vtk 7 at this handle
        brew install vtk
        # but apparently binds against the system framework, hardcoded,
        # so we need to change it manually.
        for f in `/usr/local/Cellar/vtk/lib/*.dylib`; do
            install_name_tool -change /System/Library/Frameworks/Python.framework/Versions/2.7/Python /usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/Python $f
        done
        for f in `/usr/local/Cellar/vtk/lib/*.so`; do
            install_name_tool -change /System/Library/Frameworks/Python.framework/Versions/2.7/Python /usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/Python $f
        done
        export PYTHONPATH=/usr/local/opt/vtk/lib/python2.7/site-packages
        export DYLD_LIBRARY_PATH=/usr/local/opt/vtk/lib
    fi
else
    # Linux
    if [[ "${VTK_VERSION}" == "5.8" ]]; then
        # Do nothing. 5.8 is already on the system
        :
    else
        # This is the name of the directory after unpacking
        VTK_PYTHON=VTK-${VTK_VERSION}.0-Linux-64bit

        # Download link to the vtkPython
        DOWNLOAD_LINK=http://www.vtk.org/files/release/${VTK_VERSION}/vtkpython-${VTK_VERSION}.0-Linux-64bit.tar.gz

        # Cache directory
        CACHE_DIR=${HOME}/.cache

        # Locate the unpacked directory, or unpack if it wasn't done already
        if [ -d "${CACHE_DIR}/${VTK_PYTHON}" ]; then
            echo "${VTK_PYTHON} is found"
        else
            echo "Downloading ${VTK_PYTHON}"
            wget ${DOWNLOAD_LINK} -O vtk_python.tar.gz
            gunzip vtk_python.tar.gz
            tar -xf vtk_python.tar -C ${CACHE_DIR}
            rm -f vtk_python.tar
        fi

        export PYTHONPATH=${CACHE_DIR}/${VTK_PYTHON}/lib/python2.7/site-packages
        export LD_LIBRARY_PATH=${CACHE_DIR}/${VTK_PYTHON}/lib
    fi
fi
