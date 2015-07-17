#!/bin/bash
set -e
wget https://github.com/wxWidgets/wxPython/archive/wxPy-2.8.12.1.tar.gz && md5sum -c checksums
tar -xf wxPy-2.8.12.1.tar.gz
cd wxPython-wxPy-2.8.12.1
sed -i '/SEARCH_LIB=/a SEARCH_LIB=${SEARCH_LIB}" \/usr\/lib\/x86_64-linux-gnu"' ./configure
mkdir wxGTK-build
cd wxGTK-build
../configure --enable-unicode --prefix=$VIRTUAL_ENV --enable-debug_flag --enable-optimize --with-opengl
make -j 3
make install
make -C contrib/src/stc -j 3
make -C contrib/src/stc install
make -C contrib/src/gizmos -j 3
make -C contrib/src/gizmos install
cd ../wxPython
python setup.py install