#!/bin/bash

VTK_PYTHON=vtkpython-7.0.0-Linux-64bit
FILE_PREFIX=vtkpython-7.0.0-Linux-64bit
DOWNLOAD_LINK=http://www.vtk.org/files/release/7.0/${FILE_PREFIX}.tar.gz
CACHE_DIR=${HOME}/.cache

CURRENT_DIR=$PWD
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
cd $CURRENT_DIR

