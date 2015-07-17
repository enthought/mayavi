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
if [ -f $HOME/.cache/wxPython-2.8.12.1-cp27-none-linux_x86_64.whl ]; then
   echo "wxPython wheel found"
else
   echo "Building wxPython wheel"
   cd ../wxPython
   svn co http://svn.wxwidgets.org/svn/wx/wxPython/3rdParty/AGW/agw/ wx/lib/agw
   svn co http://svn.wxwidgets.org/svn/wx/wxPython/3rdParty/FloatCanvas/floatcanvas/ wx/lib/floatcanvas
   svn co http://svn.wxwidgets.org/svn/wx/wxPython/3rdParty/PubSub/pubsub/ wx/lib/pubsub
   mkdir wx/lib/pubsub/pubsub1
   mkdir wx/lib/pubsub/pubsub2
   svn co http://svn.wxwidgets.org/svn/wx/wxPython/3rdParty/XRCed/ wx/tools/XRCed
   svn co http://svn.wxwidgets.org/svn/wx/wxPython/3rdParty/Editra/ wx/tools/Editra
   python setup.py bdist_egg
   wheel convert ./dist/wxPython-2.8.12.1-py2.7-linux-x86_64.egg --dest-dir=$HOME/.cache/
fi

pip install $HOME/.cache/wxPython-2.8.12.1-cp27-none-linux_x86_64.whl
