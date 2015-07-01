#!/bin/bash
set -e
wget http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/wxPython-src-2.8.12.1.tar.bz2/download && md5sum -c checksums
tar -xf download
cd wxPython-src-2.8.12.1
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
