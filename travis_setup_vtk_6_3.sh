#!/bin/bash

VTK_PYTHON=VTK-6.3.0-Linux-64bit
FILE_PREFIX=vtkpython-6.3.0-Linux-64bit
DOWNLOAD_LINK=http://www.vtk.org/files/release/6.3/${FILE_PREFIX}.tar.gz
CACHE_DIR=${HOME}/.cache

pushd .
cd $CACHE_DIR

if [ -d "${VTK_PYTHON}" ]; then
    echo "${VTK_PYTHON} is found"
else
    echo "Downloading ${VTK_PYTHON}"
    wget ${DOWNLOAD_LINK}
    gunzip ${FILE_PREFIX}.tar.gz
    tar -xf ${FILE_PREFIX}.tar
fi

export PYTHONPATH=${CACHE_DIR}/${VTK_PYTHON}/lib/python2.7/site-packages
export LD_LIBRARY_PATH=${CACHE_DIR}/${VTK_PYTHON}/lib
popd
