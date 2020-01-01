""" Powerful utility for running a TCP/UDP server that is used to script
Mayavi2 from the network.  This uses Twisted.  This particular version
has been written for the wxPython, adding support for a Qt4 version
should be trivial.

The key functions exposed are::

 serve_tcp(...)
 serve_udp(...)

See the function documentation for more information.  Here is sample
usage::

    from mayavi import mlab
    from mayavi.tools import server
    mlab.test_plot3d()
    server.serve_tcp()

The TCP server will listen on port 8007 by default in the above.  Any
data sent to the server is simply exec'd, meaning you can do pretty much
anything you want.  The `engine`, `scene`, `camera` and `mlab` are all
available and can be used.  For example after running the above you can
do this::

    $ telnet localhost 8007
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.
    scene.camera.azimuth(45)
    mlab.clf()
    mlab.test_contour3d()
    scene.camera.zoom(1.5)

The nice thing about this is that you do not loose any interactivity of
your app and can continue to use its UI as before, any network commands
will be simply run on top of this.

**Warning** while this is very powerful it is also a **huge security
hole** since the remote user can do pretty much anything they want.

"""

# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2009-2020, Enthought, Inc.
# License: BSD Style.

import sys
import wx
# Install wxreactor; must be done before the reactor is imported below.
from twisted.internet import wxreactor
wxreactor.install()

# The usual twisted imports.
from twisted.internet.protocol import Protocol, DatagramProtocol, Factory
from twisted.internet import reactor
from twisted.python import log


###############################################################################
# `M2UDP` protocol.
###############################################################################
class M2UDP(DatagramProtocol):

    """Implements a brain dead but supremely powerful UDP API.  Any data
    coming in is simply exec'd.  Meaning you can do pretty much anything
    you want.  The `engine`, `scene`, `camera` and `mlab` are all
    available and can be used.  For example you can easily send this on
    the network::

      scene.camera.azimuth(45)
      mlab.clf()
      mlab.test_contour3d()
      scene.camera.zoom(1.5)

    And these will run just fine retaining the full interactivity of the
    mayavi app.
    """

    def datagramReceived(self, data, host_port):
        """Given a line of data, simply execs it to do whatever."""
        host, port = host_port
        log.msg("Received: %r from %s:%d" % (data, host, port))
        c = data.strip()
        if len(c) > 0:
            mlab = self.mlab
            engine = self.engine
            scene = self.scene
            camera = scene.camera
            try:
                exec(c, locals(), globals())
            except:
                log.err()
            scene.render()


###############################################################################
# `M2TCP` protocol
###############################################################################
class M2TCP(Protocol):

    """Implements a brain dead but suprememly powerful TCP API.  Any
    data coming in is simply exec'd.  Meaning you can do pretty much
    anything you want.  The `engine`, `scene`, `camera` and `mlab` are
    all available and can be used.  For example you can easily send this
    on the network::

      scene.camera.azimuth(45)
      mlab.clf()
      mlab.test_contour3d()
      scene.camera.zoom(1.5)

    And these will run just fine retaining the full interactivity of the
    mayavi app.
    """

    # Maximum number of concurrent connections allowed.
    maxConnect = 1

    def connectionMade(self):
        log.msg('ConnectionMade')
        self.factory.numConnect += 1
        if self.factory.numConnect > self.maxConnect:
            self.transport.write("Server already in use, try later\n")
            self.transport.loseConnection()

    def connectionLost(self, reason):
        log.msg('ConnectionLost')
        self.factory.numConnect -= 1

    def dataReceived(self, data):
        """Given a line of data, simply execs it to do whatever."""
        c = data.strip()
        log.msg('Received:', c)
        if len(c) > 0:
            mlab = self.factory.mlab
            engine = self.factory.engine
            scene = self.factory.scene
            camera = scene.camera
            try:
                exec(c, locals(), globals())
            except:
                log.err()
            scene.render()


###############################################################################
# Utility functions.
###############################################################################
def serve_udp(engine=None, port=9007, logto=sys.stdout):
    """Serve the `M2UDP` protocol using the given `engine` on the
    specified `port` logging messages to given `logto` which is a
    file-like object.  This function will block till the service is
    closed.  There is no need to call `mlab.show()` after or before
    this.  The Mayavi UI will be fully responsive.

    **Parameters**

     :engine: Mayavi engine to use. If this is `None`,
              `mlab.get_engine()` is used to find an appropriate engine.

     :port: int: port to serve on.

     :logto: file : File like object to log messages to.  If this is
                    `None` it disables logging.

    **Examples**

    Here is a very simple example::

        from mayavi import mlab
        from mayavi.tools import server
        mlab.test_plot3d()
        server.serve_udp()

    Test it like so::

        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', 9008))
        s.sendto('camera.azimuth(10)', ('', 9007))

    **Warning**

    Data sent is exec'd so this is a security hole.
    """

    from mayavi import mlab
    e = engine or mlab.get_engine()
    # Setup the protocol with the right attributes.
    proto = M2UDP()
    proto.engine = e
    proto.scene = e.current_scene.scene
    proto.mlab = mlab

    if logto is not None:
        log.startLogging(logto)
    log.msg('Serving Mayavi2 UDP server on port', port)
    log.msg('Using Engine', e)

    # Register the running wxApp.
    reactor.registerWxApp(wx.GetApp())
    # Listen on port 9007 using above protocol.
    reactor.listenUDP(port, proto)
    # Run the server + app.  This will block.
    reactor.run()


def serve_tcp(engine=None, port=8007, logto=sys.stdout, max_connect=1):
    """Serve the `M2TCP` protocol using the given `engine` on the
    specified `port` logging messages to given `logto` which is a
    file-like object.  This function will block till the service is
    closed.  There is no need to call `mlab.show()` after or before
    this.  The Mayavi UI will be fully responsive.

    **Parameters**

     :engine: Mayavi engine to use. If this is `None`,
              `mlab.get_engine()` is used to find an appropriate engine.

     :port: int: port to serve on.

     :logto: file: File like object to log messages to.  If this is
                   `None` it disables logging.

     :max_connect: int: Maximum number of simultaneous connections to
                        support.

    **Examples**

    Here is a very simple example::

        from mayavi import mlab
        from mayavi.tools import server
        mlab.test_plot3d()
        server.serve_tcp()

    The TCP server will listen on port 8007 by default in the above.
    Any data sent to the server is simply exec'd, meaning you can do
    pretty much anything you want.  The `engine`, `scene`, `camera` and
    `mlab` are all available and can be used.  For example after running
    the above you can do this::

        $ telnet localhost 8007
        Trying 127.0.0.1...
        Connected to localhost.
        Escape character is '^]'.
        scene.camera.azimuth(45)
        mlab.clf()
        mlab.test_contour3d()
        scene.camera.zoom(1.5)

    **Warning**

    Data sent is exec'd so this is a security hole.
    """

    from mayavi import mlab
    e = engine or mlab.get_engine()
    # Setup the factory with the right attributes.
    factory = Factory()
    factory.protocol = M2TCP
    factory.maxConnect = max_connect
    factory.numConnect = 0
    factory.engine = e
    factory.scene = e.current_scene.scene
    factory.mlab = mlab

    if logto is not None:
        log.startLogging(logto)
    log.msg('Serving Mayavi2 TCP server on port', port)
    log.msg('Using Engine', e)

    # Register the running wxApp.
    reactor.registerWxApp(wx.GetApp())
    # Listen on port 9007 using above protocol.
    reactor.listenTCP(port, factory)
    # Run the server + app.  This will block.
    reactor.run()


###############################################################################
# Examples and tests.
###############################################################################
def test_tcp():
    """Simple test for the TCP server."""
    from mayavi import mlab
    mlab.test_plot3d()
    serve_tcp()


def test_udp():
    """Simple test for the UDP server."""
    from mayavi import mlab
    mlab.test_plot3d()
    serve_udp()

if __name__ == '__main__':
    test_tcp()
