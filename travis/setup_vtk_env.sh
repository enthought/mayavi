#!/bin/bash

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
