from mayavi import mlab
f1=mlab.figure()
print "f1", f1
print mlab.test_contour_surf()
f2=mlab.figure()
print "f2", f2
print mlab.test_simple_surf()
print "writing text"
mlab.text(0.5, 0.5, 'test', figure=f1)
print "showing"
mlab.show()
