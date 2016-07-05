import os
from glob import glob
from contextlib import contextmanager

from traits.api import Bool, Directory, HasTraits, Instance, Int, Str
from traits.util.home_directory import get_home_directory


class MovieMaker(HasTraits):
    record = Bool(False, desc='if a movie should be recorded')
    scene = Instance('tvtk.pyface.tvtk_scene.TVTKScene', record=False)
    directory = Directory
    filename = Str('anim%05d.png')
    anti_alias = Bool(True, desc='if the saved images should be anti-aliased')

    ##################
    # Private traits
    _subdir = Str
    _count = Int(0)

    def default_traits_view(self):
        from traitsui.api import Item, View
        view = View(
            Item('record'),
            Item('anti_alias'),
            Item('filename'),
            Item('directory'),
        )
        return view

    def animation_start(self):
        if self.record:
            self._update_subdir()
            self._count = 0
            self._save_scene(self._count)

    def animation_step(self):
        if self.record:
            self._count += 1
            self._save_scene(self._count)

    def animation_stop(self):
        pass

    @contextmanager
    def record_movie(self):
        """Context manager to record a movie.  Using this will turn on the
        recording automatically and also shut it off after it is done.

        For example::

            >>> s = mlab.test_simple_surf()
            >>> ms = s.mlab_source
            >>> x = ms.x
            >>> with s.scene.movie_maker.record_movie() as mm:
            ...     for i in range(10):
            ...         ms.scalars = numpy.asarray(x * 0.1 * (i + 1), 'd')
            ...         mm.animation_step()
            ...
        """
        self.record = True
        self.animation_start()
        try:
            yield self
        finally:
            self.animation_stop()
            self.record = False

    def _save_scene(self, count):
        dir = os.path.join(self.directory, self._subdir)
        if not os.path.exists(dir):
            os.makedirs(dir)

        fname = os.path.join(dir, self.filename%count)
        if not self.anti_alias:
            orig_aa = self.scene.anti_aliasing_frames
        self.scene.save(fname)
        if not self.anti_alias:
            self.scene.anti_aliasing_frames = orig_aa

    def _directory_default(self):
        home = get_home_directory()
        return os.path.join(home, 'Documents', 'mayavi_movies')

    def _update_subdir(self):
        pattern = os.path.join(self.directory, 'movie*')
        existing = sorted([x for x in glob(pattern) if os.path.isdir(x)])
        last_index = 1
        if existing:
            last = existing[-1]
            last_index = int(last[-3:]) + 1
        self._subdir = 'movie%03d'%last_index
