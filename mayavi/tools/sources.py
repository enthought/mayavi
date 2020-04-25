"""
Data sources classes and their associated functions for mlab.
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Prabhu Ramachandran
# Copyright (c) 2007-2020, Enthought, Inc.
# License: BSD Style.

import numpy as np

from traits.api import Bool, HasTraits, Instance, on_trait_change
from tvtk.api import tvtk
from tvtk.common import camel2enthought

from mayavi.sources.array_source import ArraySource
from mayavi.core.registry import registry
from mayavi.core.trait_defs import ArrayNumberOrNone, ArrayOrNone

from . import tools
from .engine_manager import get_null_engine, engine_manager

__all__ = ['vector_scatter', 'vector_field', 'scalar_scatter',
    'scalar_field', 'line_source', 'array2d_source', 'grid_source',
    'open', 'triangular_mesh_source', 'vertical_vectors_source',
]


###############################################################################
# `MlabSource` class.
###############################################################################
class MlabSource(HasTraits):
    """
    This class represents the base class for all mlab sources.  These
    classes allow a user to easily update the data without having to
    recreate the whole pipeline.
    """

    # The TVTK dataset we manage.
    dataset = Instance(tvtk.DataSet)

    # The Mayavi data source we manage.
    m_data = Instance(HasTraits)

    ########################################
    # Private traits.

    # Disable the update when data is changed.
    _disable_update = Bool(False)

    ######################################################################
    # `MlabSource` interface.
    ######################################################################
    def reset(self, **traits):
        """Function to create the data from input arrays etc.

        This is to be used when the size of the arrays change or the
        first time when the data is created.  This regenerates the data
        structures and will be slower in general.
        """
        raise NotImplementedError()

    def update(self):
        """Update the visualization.

        This is to be called after the data of the visualization has
        changed.
        """
        if not self._disable_update:
            self.dataset.modified()
            md = self.m_data
            if md is not None:
                aa = getattr(md, '_assign_attribute', None)
                vectors = getattr(self, 'vectors', None)
                scalars = getattr(self, 'scalars', None)
                if aa is not None and (scalars is not None or
                                       vectors is not None):
                    aa.update()
                md.data_changed = True

    def set(self, trait_change_notify=True, **traits):
        """Shortcut for setting object trait attributes.

        This is an overridden method that will make changing multiple
        traits easier.  This method is to be called when the arrays have
        changed content but not in shape/size.  In that case one must
        call the `reset` method.

        Parameters
        ----------
        trait_change_notify : Boolean
            If **True** (the default), then each value assigned may generate a
            trait change notification. If **False**, then no trait change
            notifications will be generated. (see also: trait_setq)
        traits : list of key/value pairs
            Trait attributes and their values to be set

        Returns
        -------
        self
            The method returns this object, after setting attributes.
        """
        try:
            self._disable_update = True
            super(MlabSource, self).trait_set(trait_change_notify, **traits)
        finally:
            self._disable_update = False
        if trait_change_notify:
            self.update()
        return self

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _m_data_changed(self, ds):
        if not hasattr(ds, 'mlab_source'):
            ds.add_trait('mlab_source', Instance(MlabSource))
        ds.mlab_source = self


###############################################################################
# `MGlyphSource` class.
###############################################################################
class MGlyphSource(MlabSource):
    """
    This class represents a glyph data source for Mlab objects and
    allows the user to set the x, y, z, scalar/vector attributes.
    """

    # The x, y, z and points of the glyphs.
    x = ArrayNumberOrNone
    y = ArrayNumberOrNone
    z = ArrayNumberOrNone
    points = ArrayOrNone

    # The scalars shown on the glyphs.
    scalars = ArrayNumberOrNone

    # The u, v, w components of the vector and the vectors.
    u = ArrayNumberOrNone
    v = ArrayNumberOrNone
    w = ArrayNumberOrNone
    vectors = ArrayOrNone

    ######################################################################
    # `MlabSource` interface.
    ######################################################################
    def reset(self, **traits):
        """Creates the dataset afresh or resets existing data source."""
        # First convert numbers to arrays.
        for name in ('x', 'y', 'z', 'u', 'v', 'w', 'scalars'):
            if name in traits and traits[name] is not None:
                traits[name] = np.atleast_1d(traits[name])

        # First set the attributes without really doing anything since
        # the notification handlers are not called.
        self.trait_set(trait_change_notify=False, **traits)

        vectors = self.vectors
        scalars = self.scalars
        points = self.points
        x, y, z = self.x, self.y, self.z
        x = np.atleast_1d(x)
        y = np.atleast_1d(y)
        z = np.atleast_1d(z)

        if 'points' in traits:
            x = points[:, 0].ravel()
            y = points[:, 1].ravel()
            z = points[:, 2].ravel()
            self.trait_set(x=x, y=y, z=z, trait_change_notify=False)

        else:
            points = np.c_[x.ravel(), y.ravel(), z.ravel()].ravel()
            points.shape = (-1, 3)
            self.trait_set(points=points, trait_change_notify=False)

        u, v, w = self.u, self.v, self.w
        if u is not None:
            u = np.atleast_1d(u)
            v = np.atleast_1d(v)
            w = np.atleast_1d(w)
            if len(u) > 0:
                vectors = np.c_[u.ravel(), v.ravel(),
                                w.ravel()].ravel()
                vectors.shape = (-1, 3)
                self.trait_set(vectors=vectors, trait_change_notify=False)

        if 'vectors' in traits:
            u = vectors[:, 0].ravel()
            v = vectors[:, 1].ravel()
            w = vectors[:, 2].ravel()
            self.trait_set(u=u, v=v, w=w, trait_change_notify=False)

        else:
            if u is not None and len(u) > 0:
                vectors = np.c_[u.ravel(), v.ravel(),
                                w.ravel()].ravel()
                vectors.shape = (-1, 3)
                self.trait_set(vectors=vectors, trait_change_notify=False)

        if vectors is not None and len(vectors) > 0:
            assert len(points) == len(vectors)
        if scalars is not None:
            scalars = np.atleast_1d(scalars)
            if len(scalars) > 0:
                assert len(points) == len(scalars.ravel())

        # Create the dataset.
        polys = np.arange(0, len(points), 1, 'l')
        polys = np.reshape(polys, (len(points), 1))
        new_dataset = False
        if self.dataset is None:
            # Create new dataset if none exists
            pd = tvtk.PolyData()
            new_dataset = True
        else:
            # Modify existing one.
            pd = self.dataset
        # First set the polys to None to avoid accessing invalid points.
        pd.polys = None
        pd.trait_set(points=points)
        pd.trait_set(polys=polys)

        if self.vectors is not None:
            pd.point_data.vectors = self.vectors
            pd.point_data.vectors.name = 'vectors'
        if self.scalars is not None:
            pd.point_data.scalars = self.scalars.ravel()
            pd.point_data.scalars.name = 'scalars'

        self.dataset = pd
        if not new_dataset:
            self.update()

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _x_changed(self, x):
        x = np.atleast_1d(x)
        self.points[:, 0] = x.ravel()
        self.update()

    def _y_changed(self, y):
        y = np.atleast_1d(y)
        self.points[:, 1] = y.ravel()
        self.update()

    def _z_changed(self, z):
        z = np.atleast_1d(z)
        self.points[:, 2] = z.ravel()
        self.update()

    def _u_changed(self, u):
        u = np.atleast_1d(u)
        self.vectors[:, 0] = u.ravel()
        self.update()

    def _v_changed(self, v):
        v = np.atleast_1d(v)
        self.vectors[:, 1] = v.ravel()
        self.update()

    def _w_changed(self, w):
        w = np.atleast_1d(w)
        self.vectors[:, 2] = w.ravel()
        self.update()

    def _points_changed(self, p):
        p = np.atleast_2d(p)
        self.dataset.points = p
        self.update()

    def _scalars_changed(self, s):
        if s is None:
            self.dataset.point_data.scalars = None
            self.dataset.point_data.remove_array('scalars')
        else:
            s = np.atleast_1d(s)
            self.dataset.point_data.scalars = s.ravel()
            self.dataset.point_data.scalars.name = 'scalars'
        self.update()

    def _vectors_changed(self, v):
        self.dataset.point_data.vectors = v
        self.dataset.point_data.vectors.name = 'vectors'
        self.update()


###############################################################################
# `MVerticalGlyphSource` class.
###############################################################################
class MVerticalGlyphSource(MGlyphSource):
    """
    This class represents a vertical glyph data source for Mlab objects
    and allows the user to set the x, y, z, scalar attributes. The
    vectors are created from the scalars to represent them in the
    vertical direction.
    """

    def reset(self, **traits):
        """Creates the dataset afresh or resets existing data source."""
        if 'scalars' in traits:
            s = traits['scalars']
            if s is not None:
                traits['u'] = traits['v'] = np.ones_like(s),
                traits['w'] = s
        super(MVerticalGlyphSource, self).reset(**traits)

    def _scalars_changed(self, s):
        self.dataset.point_data.scalars = s
        self.dataset.point_data.scalars.name = 'scalars'
        self.trait_set(vectors=np.c_[np.ones_like(s),
                               np.ones_like(s),
                               s])
        self.update()


###############################################################################
# `MArraySource` class.
###############################################################################
class MArraySource(MlabSource):
    """
    This class represents an array data source for Mlab objects and
    allows the user to set the x, y, z, scalar/vector attributes.
    """

    # The x, y, z arrays for the volume.
    x = ArrayOrNone
    y = ArrayOrNone
    z = ArrayOrNone

    # The scalars shown on the glyphs.
    scalars = ArrayOrNone

    # The u, v, w components of the vector and the vectors.
    u = ArrayOrNone
    v = ArrayOrNone
    w = ArrayOrNone
    vectors = ArrayOrNone

    ######################################################################
    # `MlabSource` interface.
    ######################################################################
    def reset(self, **traits):
        """Creates the dataset afresh or resets existing data source."""

        # First set the attributes without really doing anything since
        # the notification handlers are not called.
        self.trait_set(trait_change_notify=False, **traits)

        vectors = self.vectors
        scalars = self.scalars
        x, y, z = [np.atleast_3d(a) for a in (self.x, self.y, self.z)]

        u, v, w = self.u, self.v, self.w
        if 'vectors' in traits:
            u = vectors[:, 0].ravel()
            v = vectors[:, 1].ravel()
            w = vectors[:, 2].ravel()
            self.trait_set(u=u, v=v, w=w, trait_change_notify=False)

        else:
            if u is not None and len(u) > 0:
                #vectors = np.concatenate([u[..., np.newaxis],
                #                             v[..., np.newaxis],
                #                             w[..., np.newaxis] ],
                #                axis=3)
                vectors = np.c_[u.ravel(), v.ravel(),
                                   w.ravel()].ravel()
                vectors.shape = (u.shape[0], u.shape[1], w.shape[2], 3)
                self.trait_set(vectors=vectors, trait_change_notify=False)

        if vectors is not None and len(vectors) > 0 and scalars is not None:
            assert len(scalars) == len(vectors)

        if x.shape[0] <= 1:
            dx = 1
        else:
            dx = x[1, 0, 0] - x[0, 0, 0]
        if y.shape[1] <= 1:
            dy = 1
        else:
            dy = y[0, 1, 0] - y[0, 0, 0]
        if z.shape[2] <= 1:
            dz = 1
        else:
            dz = z[0, 0, 1] - z[0, 0, 0]

        if self.m_data is None:
            ds = ArraySource(transpose_input_array=True)
        else:
            ds = self.m_data
        old_scalar = ds.scalar_data
        ds.trait_set(vector_data=vectors,
               origin=[x.min(), y.min(), z.min()],
               spacing=[dx, dy, dz],
               scalar_data=scalars)
        if scalars is old_scalar:
            ds._scalar_data_changed(scalars)

        self.dataset = ds.image_data
        self.m_data = ds

    ######################################################################
    # Non-public interface.
    ######################################################################
    @on_trait_change('[x, y, z]')
    def _xyz_changed(self):
        x, y, z = self.x, self.y, self.z
        dx = x[1, 0, 0] - x[0, 0, 0]
        dy = y[0, 1, 0] - y[0, 0, 0]
        dz = z[0, 0, 1] - z[0, 0, 0]
        ds = self.dataset
        ds.origin = [x.min(), y.min(), z.min()]
        ds.spacing = [dx, dy, dz]
        if self.m_data is not None:
            self.m_data.trait_set(origin=ds.origin, spacing=ds.spacing)
        self.update()

    def _u_changed(self, u):
        self.vectors[..., 0] = u
        self.m_data._vector_data_changed(self.vectors)

    def _v_changed(self, v):
        self.vectors[..., 1] = v
        self.m_data._vector_data_changed(self.vectors)

    def _w_changed(self, w):
        self.vectors[..., 2] = w
        self.m_data._vector_data_changed(self.vectors)

    def _scalars_changed(self, s):
        old = self.m_data.scalar_data
        self.m_data.scalar_data = s
        if old is s:
            self.m_data._scalar_data_changed(s)

    def _vectors_changed(self, v):
        self.m_data.vector_data = v


###############################################################################
# `MLineSource` class.
###############################################################################
class MLineSource(MlabSource):
    """
    This class represents a line data source for Mlab objects and
    allows the user to set the x, y, z, scalar attributes.
    """

    # The x, y, z and points of the glyphs.
    x = ArrayOrNone
    y = ArrayOrNone
    z = ArrayOrNone
    points = ArrayOrNone

    # The scalars shown on the glyphs.
    scalars = ArrayOrNone

    ######################################################################
    # `MlabSource` interface.
    ######################################################################
    def reset(self, **traits):
        """Creates the dataset afresh or resets existing data source."""

        # First set the attributes without really doing anything since
        # the notification handlers are not called.
        self.trait_set(trait_change_notify=False, **traits)

        points = self.points
        scalars = self.scalars
        x, y, z = self.x, self.y, self.z

        if 'points' in traits:
            x = points[:, 0].ravel()
            y = points[:, 1].ravel()
            z = points[:, 2].ravel()
            self.trait_set(x=x, y=y, z=z, trait_change_notify=False)

        else:
            points = np.c_[x.ravel(), y.ravel(), z.ravel()].ravel()
            points.shape = (len(x), 3)
            self.trait_set(points=points, trait_change_notify=False)

        # Create the dataset.
        n_pts = len(points) - 1
        lines = np.zeros((n_pts, 2), 'l')
        lines[:, 0] = np.arange(0, n_pts - 0.5, 1, 'l')
        lines[:, 1] = np.arange(1, n_pts + 0.5, 1, 'l')
        new_dataset = False
        if self.dataset is None:
            pd = tvtk.PolyData()
            new_dataset = True
        else:
            pd = self.dataset
        # Avoid lines refering to non existing points: First set the
        # lines to None, then set the points, then set the lines
        # refering to the new points.
        pd.trait_set(lines=None)
        pd.trait_set(points=points)
        pd.trait_set(lines=lines)

        if scalars is not None and len(scalars) > 0:
            assert len(x) == len(scalars)
            pd.point_data.scalars = np.ravel(scalars)
            pd.point_data.scalars.name = 'scalars'

        self.dataset = pd
        if not new_dataset:
            self.update()

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _x_changed(self, x):
        self.points[:, 0] = x
        self.update()

    def _y_changed(self, y):
        self.points[:, 1] = y
        self.update()

    def _z_changed(self, z):
        self.points[:, 2] = z
        self.update()

    def _points_changed(self, p):
        self.dataset.points = p
        self.update()

    def _scalars_changed(self, s):
        self.dataset.point_data.scalars = s.ravel()
        self.dataset.point_data.scalars.name = 'scalars'
        self.update()


###############################################################################
# `MArray2DSource` class.
###############################################################################
class MArray2DSource(MlabSource):
    """
    This class represents a 2D array data source for Mlab objects and
    allows the user to set the x, y  and scalar attributes.
    """

    # The x, y values.
    # Values of X and Y as None are accepted, in that case we would build
    # values of X and Y automatically from the shape of scalars
    x = ArrayOrNone
    y = ArrayOrNone

    # The scalars shown on the glyphs.
    scalars = ArrayOrNone

    # The masking array.
    mask = ArrayOrNone

    ######################################################################
    # `MlabSource` interface.
    ######################################################################
    def reset(self, **traits):
        """Creates the dataset afresh or resets existing data source."""

        # First set the attributes without really doing anything since
        # the notification handlers are not called.
        self.trait_set(trait_change_notify=False, **traits)
        x, y, mask = self.x, self.y, self.mask
        scalars = self.scalars

        # We may have used this without specifying x and y at all in
        # which case we set them from the shape of scalars.
        nx, ny = scalars.shape

        #Build X and Y from shape of Scalars if they are none
        if x is None and y is None:
            x, y = np.mgrid[-nx / 2.:nx / 2, -ny / 2.:ny / 2]

        if mask is not None and len(mask) > 0:
            scalars[mask.astype('bool')] = np.nan
            # The NaN trick only works with floats.
            scalars = scalars.astype('float')
            self.trait_set(scalars=scalars, trait_change_notify=False)

        z = np.array([0])

        self.trait_set(x=x, y=y, z=z, trait_change_notify=False)
        # Do some magic to extract the first row/column, independently of
        # the shape of x and y

        x = np.atleast_2d(x.squeeze().T)[0, :].squeeze()
        y = np.atleast_2d(y.squeeze())[0, :].squeeze()

        if x.ndim == 0:
            dx = 1
        else:
            dx = x[1] - x[0]
        if y.ndim == 0:
            dy = 1
        else:
            dy = y[1] - y[0]
        if self.m_data is None:
            ds = ArraySource(transpose_input_array=True)
        else:
            ds = self.m_data
        old_scalar = ds.scalar_data
        ds.trait_set(origin=[x.min(), y.min(), 0],
               spacing=[dx, dy, 1],
               scalar_data=scalars)
        if old_scalar is scalars:
            ds._scalar_data_changed(scalars)

        self.dataset = ds.get_output_dataset()
        self.m_data = ds

    #####################################################################
    # Non-public interface.
    #####################################################################
    @on_trait_change('[x, y]')
    def _xy_changed(self):
        x, y, scalars = self.x, self.y, self.scalars

        nx, ny = scalars.shape

        if x is None or y is None:
            x, y = np.mgrid[-nx / 2.:nx / 2, -ny / 2.:ny / 2]

        self.trait_setq(x=x, y=y)
        x = np.atleast_2d(x.squeeze().T)[0, :].squeeze()
        y = np.atleast_2d(y.squeeze())[0, :].squeeze()
        dx = x[1] - x[0]
        dy = y[1] - y[0]
        ds = self.dataset
        ds.origin = [x.min(), y.min(), 0]
        ds.spacing = [dx, dy, 1]
        if self.m_data is not None:
            self.m_data.trait_set(origin=ds.origin, spacing=ds.spacing)
        self.update()

    def _scalars_changed(self, s):
        mask = self.mask
        if mask is not None and len(mask) > 0:
            s[mask.astype('bool')] = np.nan
            # The NaN tric only works with floats.
            s = s.astype('float')
            self.trait_set(scalars=s, trait_change_notify=False)
        old = self.m_data.scalar_data
        self.m_data.scalar_data = s
        if s is old:
            self.m_data._scalar_data_changed(s)


##############################################################################
# `MGridSource` class.
##############################################################################
class MGridSource(MlabSource):
    """
    This class represents a grid source for Mlab objects and
    allows the user to set the x, y, scalar attributes.
    """

    # The x, y, z and points of the grid.
    x = ArrayOrNone
    y = ArrayOrNone
    z = ArrayOrNone
    points = ArrayOrNone

    # The scalars shown on the glyphs.
    scalars = ArrayOrNone

    # The masking array.
    mask = ArrayOrNone

    ######################################################################
    # `MlabSource` interface.
    ######################################################################
    def reset(self, **traits):
        """Creates the dataset afresh or resets existing data source."""

        # First set the attributes without really doing anything since
        # the notification handlers are not called.
        self.trait_set(trait_change_notify=False, **traits)

        points = self.points
        scalars = self.scalars
        x, y, z, mask = self.x, self.y, self.z, self.mask

        if mask is not None and len(mask) > 0:
            scalars[mask.astype('bool')] = np.nan
            # The NaN trick only works with floats.
            scalars = scalars.astype('float')
            self.trait_set(scalars=scalars, trait_change_notify=False)

        assert len(x.shape) == 2, "Array x must be 2 dimensional."
        assert len(y.shape) == 2, "Array y must be 2 dimensional."
        assert len(z.shape) == 2, "Array z must be 2 dimensional."
        assert x.shape == y.shape, "Arrays x and y must have same shape."
        assert y.shape == z.shape, "Arrays y and z must have same shape."

        # Points in the grid source will always be created using x,y,z
        # Changing of points is not allowed because it cannot be used to
        # modify values of x,y,z

        nx, ny = x.shape
        points = np.c_[x.ravel(), y.ravel(), z.ravel()].ravel()
        points.shape = (nx * ny, 3)
        self.trait_set(points=points, trait_change_notify=False)

        i, j = np.mgrid[0:nx - 1, 0:ny - 1]
        i, j = np.ravel(i), np.ravel(j)
        t1 = i * ny + j, (i + 1) * ny + j, (i + 1) * ny + (j + 1)
        t2 = (i + 1) * ny + (j + 1), i * ny + (j + 1), i * ny + j
        nt = len(t1[0])
        triangles = np.zeros((nt * 2, 3), 'l')
        triangles[0:nt, 0], triangles[0:nt, 1], triangles[0:nt, 2] = t1
        triangles[nt:, 0], triangles[nt:, 1], triangles[nt:, 2] = t2

        new_dataset = False
        if self.dataset is None:
            pd = tvtk.PolyData()
            new_dataset = True
        else:
            pd = self.dataset
        pd.trait_set(polys=None)
        pd.trait_set(points=points)
        pd.trait_set(polys=triangles)

        if scalars is not None and len(scalars) > 0:
            if not scalars.flags.contiguous:
                scalars = scalars.copy()
                self.trait_set(scalars=scalars, trait_change_notify=False)
            assert x.shape == scalars.shape
            pd.point_data.scalars = scalars.ravel()
            pd.point_data.scalars.name = 'scalars'

        self.dataset = pd
        if not new_dataset:
            self.update()

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _x_changed(self, x):
        self.trait_setq(x=x)
        self.points[:, 0] = x.ravel()
        self.update()

    def _y_changed(self, y):
        self.trait_setq(y=y)
        self.points[:, 1] = y.ravel()
        self.update()

    def _z_changed(self, z):
        self.trait_setq(z=z)
        self.points[:, 2] = z.ravel()
        self.update()

    def _points_changed(self, p):
        self.dataset.points = p
        self.update()

    def _scalars_changed(self, s):
        mask = self.mask
        if mask is not None and len(mask) > 0:
            s[mask.astype('bool')] = np.nan
            # The NaN tric only works with floats.
            s = s.astype('float')
            self.trait_set(scalars=s, trait_change_notify=False)

        self.dataset.point_data.scalars = s.ravel()
        self.dataset.point_data.scalars.name = 'scalars'
        self.update()


###############################################################################
# `MTriangularMeshSource` class.
###############################################################################
class MTriangularMeshSource(MlabSource):
    """
    This class represents a triangular mesh source for Mlab objects and
    allows the user to set the x, y, scalar attributes.
    """

    # The x, y, z and points of the grid.
    x = ArrayOrNone
    y = ArrayOrNone
    z = ArrayOrNone
    points = ArrayOrNone
    triangles = ArrayOrNone

    # The scalars shown on the glyphs.
    scalars = ArrayOrNone

    ######################################################################
    # `MlabSource` interface.
    ######################################################################
    def reset(self, **traits):
        """Creates the dataset afresh or resets existing data source."""

        # First set the attributes without really doing anything since
        # the notification handlers are not called.
        self.trait_set(trait_change_notify=False, **traits)

        points = self.points
        scalars = self.scalars

        x, y, z = self.x, self.y, self.z
        points = np.c_[x.ravel(), y.ravel(), z.ravel()].ravel()
        points.shape = (-1, 3)
        self.trait_set(points=points, trait_change_notify=False)

        triangles = self.triangles
        assert triangles.shape[1] == 3, \
            "The shape of the triangles array must be (X, 3)"
        assert triangles.max() < len(points), \
            "The triangles indices must be smaller that the number of points"
        assert triangles.min() >= 0, \
            "The triangles indices must be positive or null"

        new_dataset = False
        if self.dataset is None:
            pd = tvtk.PolyData()
            new_dataset = True
        else:
            pd = self.dataset
        # Set the points first, and the triangles after: so that the
        # polygone can refer to the right points, in the polydata.

        # Set the polys to None so that when the points are set, the
        # cells do not point to garbage.
        pd.polys = None
        pd.trait_set(points=points)
        pd.trait_set(polys=triangles)

        if ('scalars' not in traits and scalars is not None
           and scalars.shape != x.shape):
            # The scalars where set probably automatically to z, by the
            # factory. We need to reset them, as the size has changed.
            scalars = z

        if scalars is not None and len(scalars) > 0:
            if not scalars.flags.contiguous:
                scalars = scalars.copy()
                self.trait_set(scalars=scalars, trait_change_notify=False)
            assert x.shape == scalars.shape
            pd.point_data.scalars = scalars.ravel()
            pd.point_data.scalars.name = 'scalars'

        self.dataset = pd
        if not new_dataset:
            self.update()

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _x_changed(self, x):
        self.trait_setq(x=x)
        self.points[:, 0] = x.ravel()
        self.update()

    def _y_changed(self, y):
        self.trait_setq(y=y)
        self.points[:, 1] = y.ravel()
        self.update()

    def _z_changed(self, z):
        self.trait_setq(z=z)
        self.points[:, 2] = z.ravel()
        self.update()

    def _points_changed(self, p):
        self.dataset.points = p
        self.update()

    def _scalars_changed(self, s):
        self.dataset.point_data.scalars = s.ravel()
        self.dataset.point_data.scalars.name = 'scalars'
        self.update()

    def _triangles_changed(self, triangles):
        if triangles.min() < 0:
            raise ValueError('The triangles array has negative values')
        if triangles.max() > self.x.size:
            raise ValueError('The triangles array has values larger than' \
                                        'the number of points')
        self.dataset.polys = triangles
        self.update()


############################################################################
# Argument processing
############################################################################

def convert_to_arrays(args):
    """ Converts a list of iterables to a list of arrays or callables,
        if needed.
    """
    args = list(args)
    for index, arg in enumerate(args):
        if not callable(arg):
            if not hasattr(arg, 'shape'):
                arg = np.array(arg)
            arg = np.atleast_1d(arg)
            if np.any(np.isinf(arg)):
                raise ValueError("""Input array contains infinite values
                You can remove them using: a[np.isinf(a)] = np.nan
                """)
            args[index] = arg
    return args


def process_regular_vectors(*args):
    """ Converts different signatures to (x, y, z, u, v, w). """
    args = convert_to_arrays(args)
    if len(args) == 3:
        u, v, w = [np.atleast_3d(a) for a in args]
        assert len(u.shape) == 3, "3D array required"
        x, y, z = np.indices(u.shape)
    elif len(args) == 6:
        x, y, z, u, v, w = args
    elif len(args) == 4:
        x, y, z, f = args
        if not callable(f):
            raise ValueError("When 4 arguments are provided, the fourth must "
                             "be a callable")
        u, v, w = f(x, y, z)
    else:
        raise ValueError("wrong number of arguments")

    assert (x.shape == y.shape and
            y.shape == z.shape and
            u.shape == z.shape and
            v.shape == u.shape and
            w.shape == v.shape), "argument shape are not equal"

    return x, y, z, u, v, w


def process_regular_scalars(*args):
    """ Converts different signatures to (x, y, z, s). """
    args = convert_to_arrays(args)
    if len(args) == 1:
        s = np.atleast_3d(args[0])
        assert len(s.shape) == 3, "3D array required"
        x, y, z = np.indices(s.shape)
    elif len(args) == 3:
        x, y, z = args
        s = None
    elif len(args) == 4:
        x, y, z, s = args
        if callable(s):
            s = s(x, y, z)
    else:
        raise ValueError("wrong number of arguments")

    assert (x.shape == y.shape and
            y.shape == z.shape and
            (s is None
               or s.shape == z.shape)), "argument shape are not equal"

    return x, y, z, s


def process_regular_2d_scalars(*args, **kwargs):
    """ Converts different signatures to (x, y, s). """
    args = convert_to_arrays(args)
    for index, arg in enumerate(args):
        if not callable(arg):
            args[index] = np.atleast_2d(arg)
    if len(args) == 1:
        s = args[0]
        assert len(s.shape) == 2, "2D array required"
        x, y = np.indices(s.shape)
    elif len(args) == 3:
        x, y, s = args
        if callable(s):
            s = s(x, y)
    else:
        raise ValueError("wrong number of arguments")
    assert len(s.shape) == 2, "2D array required"

    if 'mask' in kwargs:
        mask = kwargs['mask']
        s[mask.astype('bool')] = np.nan
        # The NaN tric only works with floats.
        s = s.astype('float')

    return x, y, s


############################################################################
# Sources
############################################################################

def vector_scatter(*args, **kwargs):
    """ Creates scattered vector data.

    **Function signatures**::

        vector_scatter(u, v, w, ...)
        vector_scatter(x, y, z, u, v, w, ...)
        vector_scatter(x, y, z, f, ...)

    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If 4 positional arguments are passed the last one must be a callable, f,
    that returns vectors.

    **Keyword arguments**:

        :name: the name of the vtk object created.

        :scalars: optional scalar data.

        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization."""
    x, y, z, u, v, w = process_regular_vectors(*args)

    scalars = kwargs.pop('scalars', None)
    if scalars is not None:
        scalars = np.ravel(scalars)
    name = kwargs.pop('name', 'VectorScatter')

    data_source = MGlyphSource()
    data_source.reset(x=x, y=y, z=z, u=u, v=v, w=w, scalars=scalars)

    ds = tools.add_dataset(data_source.dataset, name, **kwargs)
    data_source.m_data = ds
    return ds


def vector_field(*args, **kwargs):
    """ Creates vector field data.

    **Function signatures**::

        vector_field(u, v, w, ...)
        vector_field(x, y, z, u, v, w, ...)
        vector_field(x, y, z, f, ...)

    If only 3 arrays u, v, w are passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If the x, y and z arrays are passed, they should have been generated
    by `numpy.mgrid` or `numpy.ogrid`. The function builds a scalar field
    assuming the points are regularily spaced on an orthogonal grid.

    If 4 positional arguments are passed the last one must be a callable, f,
    that returns vectors.

    **Keyword arguments**:

        :name: the name of the vtk object created.

        :scalars: optional scalar data.

        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization."""
    if len(args) == 3:
        x = y = z = np.atleast_3d(1)
        u, v, w = [np.atleast_3d(a) for a in args]
    else:
        x, y, z, u, v, w = [np.atleast_3d(a)
                        for a in process_regular_vectors(*args)]

    scalars = kwargs.pop('scalars', None)
    if scalars is not None:
        scalars = np.atleast_3d(scalars)
    data_source = MArraySource()
    data_source.reset(x=x, y=y, z=z, u=u, v=v, w=w, scalars=scalars)
    name = kwargs.pop('name', 'VectorField')
    return tools.add_dataset(data_source.m_data, name, **kwargs)


def scalar_scatter(*args, **kwargs):
    """
    Creates scattered scalar data.

    **Function signatures**::

        scalar_scatter(s, ...)
        scalar_scatter(x, y, z, s, ...)
        scalar_scatter(x, y, z, s, ...)
        scalar_scatter(x, y, z, f, ...)

    If only 1 array s is passed the x, y and z arrays are assumed to be
    made from the indices of vectors.

    If 4 positional arguments are passed the last one must be an array s, or
    a callable, f, that returns an array.

    **Keyword arguments**:

        :name: the name of the vtk object created.

        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization."""
    x, y, z, s = process_regular_scalars(*args)

    if s is not None:
        s = np.ravel(s)

    data_source = MGlyphSource()
    data_source.reset(x=x, y=y, z=z, scalars=s)

    name = kwargs.pop('name', 'ScalarScatter')
    ds = tools.add_dataset(data_source.dataset, name, **kwargs)
    data_source.m_data = ds
    return ds


def scalar_field(*args, **kwargs):
    """
    Creates a scalar field data.

    **Function signatures**::

        scalar_field(s, ...)
        scalar_field(x, y, z, s, ...)
        scalar_field(x, y, z, f, ...)

    If only 1 array s is passed the x, y and z arrays are assumed to be
    made from the indices of arrays.

    If the x, y and z arrays are passed they are supposed to have been
    generated by `numpy.mgrid`. The function builds a scalar field assuming
    the points are regularily spaced.

    If 4 positional arguments are passed the last one must be an array s, or
    a callable, f, that returns an array.

    **Keyword arguments**:

        :name: the name of the vtk object created.

        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization."""
    if len(args) == 1:
        # Be lazy, don't create three big arrays for 1 input array. The
        # MArraySource is clever-enough to handle flat arrays
        x = y = z = np.atleast_1d(1)
        s = args[0]
    else:
        x, y, z, s = process_regular_scalars(*args)

    data_source = MArraySource()
    data_source.reset(x=x, y=y, z=z, scalars=s)

    name = kwargs.pop('name', 'ScalarField')
    return tools.add_dataset(data_source.m_data, name, **kwargs)


def line_source(*args, **kwargs):
    """
    Creates line data.

    **Function signatures**::

        line_source(x, y, z, ...)
        line_source(x, y, z, s, ...)
        line_source(x, y, z, f, ...)

        If 4 positional arguments are passed the last one must be an array s,
        or a callable, f, that returns an array.

    **Keyword arguments**:

        :name: the name of the vtk object created.

        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization."""
    if len(args) == 1:
        raise ValueError("wrong number of arguments")
    x, y, z, s = process_regular_scalars(*args)

    data_source = MLineSource()
    data_source.reset(x=x, y=y, z=z, scalars=s)

    name = kwargs.pop('name', 'LineSource')
    ds = tools.add_dataset(data_source.dataset, name, **kwargs)
    data_source.m_data = ds
    return ds


def array2d_source(*args, **kwargs):
    """
    Creates structured 2D data from a 2D array.

    **Function signatures**::

        array2d_source(s, ...)
        array2d_source(x, y, s, ...)
        array2d_source(x, y, f, ...)

    If 3 positional arguments are passed the last one must be an array s,
    or a callable, f, that returns an array. x and y give the
    coordinates of positions corresponding to the s values.

    x and y can be 1D or 2D arrays (such as returned by numpy.ogrid or
    numpy.mgrid), but the points should be located on an orthogonal grid
    (possibly non-uniform). In other words, all the points sharing a same
    index in the s array need to have the same x or y value.

    If only 1 array s is passed the x and y arrays are assumed to be
    made from the indices of arrays, and an uniformly-spaced data set is
    created.

    **Keyword arguments**:

        :name: the name of the vtk object created.

        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.

        :mask: Mask points specified in a boolean masking array.
    """
    data_source = MArray2DSource()
    mask = kwargs.pop('mask', None)
    if len(args) == 1:
        args = convert_to_arrays(args)
        s = np.atleast_2d(args[0])
        data_source.reset(scalars=s, mask=mask)
    else:
        x, y, s = process_regular_2d_scalars(*args, **kwargs)
        data_source.reset(x=x, y=y, scalars=s, mask=mask)

    name = kwargs.pop('name', 'Array2DSource')
    return tools.add_dataset(data_source.m_data, name, **kwargs)


def grid_source(x, y, z, **kwargs):
    """
    Creates 2D grid data.

    x, y, z are 2D arrays giving the positions of the vertices of the surface.
    The connectivity between these points is implied by the connectivity on
    the arrays.

    For simple structures (such as orthogonal grids) prefer the array2dsource
    function, as it will create more efficient data structures.

    **Keyword arguments**:

        :name: the name of the vtk object created.

        :scalars: optional scalar data.

        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.

        :mask: Mask points specified in a boolean masking array.

        """
    scalars = kwargs.pop('scalars', None)
    if scalars is None:
        scalars = z
    mask = kwargs.pop('mask', None)

    x, y, z, scalars = convert_to_arrays((x, y, z, scalars))
    data_source = MGridSource()
    data_source.reset(x=x, y=y, z=z, scalars=scalars, mask=mask)

    name = kwargs.pop('name', 'GridSource')
    ds = tools.add_dataset(data_source.dataset, name, **kwargs)
    data_source.m_data = ds
    return ds


def vertical_vectors_source(*args, **kwargs):
    """
    Creates a set of vectors pointing upward, useful eg for bar graphs.

    **Function signatures**::

        vertical_vectors_source(s, ...)
        vertical_vectors_source(x, y, s, ...)
        vertical_vectors_source(x, y, f, ...)
        vertical_vectors_source(x, y, z, s, ...)
        vertical_vectors_source(x, y, z, f, ...)

    If only one positional argument is passed, it can be a 1D, 2D, or 3D
    array giving the length of the vectors. The positions of the data
    points are deducted from the indices of array, and an
    uniformly-spaced data set is created.

    If 3 positional arguments (x, y, s) are passed the last one must be
    an array s, or a callable, f, that returns an array. x and y give the
    2D coordinates of positions corresponding to the s values. The
    vertical position is assumed to be 0.

    If 4 positional arguments (x, y, z, s) are passed, the 3 first are
    arrays giving the 3D coordinates of the data points, and the last one
    is an array s, or a callable, f, that returns an array giving the
    data value.

    **Keyword arguments**:

        :name: the name of the vtk object created.

        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.
    """
    if len(args) == 3:
        x, y, data = args
        if np.isscalar(x):
            z = 0
        else:
            z = np.zeros_like(x)
        args = (x, y, z, data)

    x, y, z, s = process_regular_scalars(*args)

    if s is not None:
        s = np.ravel(s)

    data_source = MVerticalGlyphSource()
    data_source.reset(x=x, y=y, z=z, scalars=s)

    name = kwargs.pop('name', 'VerticalVectorsSource')
    ds = tools.add_dataset(data_source.dataset, name, **kwargs)
    data_source.m_data = ds
    return ds


def triangular_mesh_source(x, y, z, triangles, **kwargs):
    """
    Creates 2D mesh by specifying points and triangle connectivity.

    x, y, z are 2D arrays giving the positions of the vertices of the surface.
    The connectivity between these points is given by listing triplets of
    vertices inter-connected. These vertices are designed by there
    position index.

    **Keyword arguments**:

        :name: the name of the vtk object created.

        :scalars: optional scalar data.

        :figure: optionally, the figure on which to add the data source.
                 If None, the source is not added to any figure, and will
                 be added automatically by the modules or
                 filters. If False, no figure will be created by modules
                 or filters applied to the source: the source can only
                 be used for testing, or numerical algorithms, not
                 visualization.
        """
    x, y, z, triangles = convert_to_arrays((x, y, z, triangles))

    if triangles.min() < 0:
        raise ValueError('The triangles array has negative values')
    if triangles.max() > x.size:
        raise ValueError('The triangles array has values larger than' \
                                    'the number of points')
    scalars = kwargs.pop('scalars', None)
    if scalars is None:
        scalars = z

    data_source = MTriangularMeshSource()
    data_source.reset(x=x, y=y, z=z, triangles=triangles, scalars=scalars)

    name = kwargs.pop('name', 'TriangularMeshSource')
    ds = tools.add_dataset(data_source.dataset, name, **kwargs)
    data_source.m_data = ds
    return ds


def open(filename, figure=None):
    """Open a supported data file given a filename.  Returns the source
    object if a suitable reader was found for the file.

    If 'figure' is False, no view is opened, and the code does not need
    GUI or openGL context.
    """
    if figure is None:
        engine = tools.get_engine()
    elif figure is False:
        # Get a null engine that we can use.
        engine = get_null_engine()
    else:
        engine = engine_manager.find_figure_engine(figure)
        engine.current_scene = figure
    src = engine.open(filename)
    return src


############################################################################
# Automatically generated sources from registry.
############################################################################
def _create_data_source(metadata):
    """Creates a data source and adds it to the mayavi engine given
    metadata of the source.  Returns the created source.
    """
    factory = metadata.get_callable()
    src = factory()
    engine = tools.get_engine()
    engine.add_source(src)
    return src


def _make_functions(namespace):
    """Make the automatic functions and add them to the namespace."""
    for src in registry.sources:
        if len(src.extensions) == 0:
            func_name = camel2enthought(src.id)
            if func_name.endswith('_source'):
                func_name = func_name[:-7]
            func = lambda metadata=src: _create_data_source(metadata)
            func.__doc__ = src.help
            func.__name__ = func_name
            # Inject function into the namespace and __all__.
            namespace[func_name] = func
            __all__.append(func_name)

_make_functions(locals())
