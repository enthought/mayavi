# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from tvtk.tools.tvtk_doc import TVTKFilterChooser, get_tvtk_filters

# Local imports.
from mayavi.filters.filter_base import FilterBase
from mayavi.core.common import handle_children_state, error
from mayavi.core.pipeline_info import PipelineInfo


################################################################################
# `UserDefined` class.
################################################################################
class UserDefined(FilterBase):

    """
    This filter lets the user define their own filter
    dynamically/interactively.  It is like `FilterBase` but allows a
    user to specify the class without writing any code.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    ######################################################################
    # `object` interface.
    ######################################################################
    def __set_pure_state__(self, state):
        # Create and set the filter.
        children = [f for f in [self.filter] if f is not None]
        handle_children_state(children, [state.filter])
        self.filter = children[0]
        self.update_pipeline()
        # Restore our state.
        super(UserDefined, self).__set_pure_state__(state)

    ######################################################################
    # `UserDefined` interface.
    ######################################################################
    def setup_filter(self):
        """Setup the filter if none has been set or check it if it
        already has been."""
        obj = self.filter
        if not self._check_object(obj):
            if obj is not None:
                cname = obj.__class__.__name__
                error('Invalid filter %s chosen!  Try again!'%cname)
            obj = self._choose_filter()
            self.filter = obj

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _choose_filter(self):
        chooser = TVTKFilterChooser()
        chooser.edit_traits(kind='livemodal')
        obj = chooser.object
        if obj is None:
            error('Invalid filter chosen!  Try again!')
        return obj

    def _check_object(self, obj):
        if obj is None:
            return False
        tvtk_filters = get_tvtk_filters()
        if obj.__class__.__name__ in tvtk_filters:
            return True
        return False

    def _filter_changed(self, old, new):
        self.name = 'UserDefined:%s'%new.__class__.__name__
        super(UserDefined, self)._filter_changed(old, new)
