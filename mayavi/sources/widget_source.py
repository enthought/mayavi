from mayavi.core.source import Source


class WidgetSource(Source):
    ##############################################
    # 'Pipeline Interface'#
    ##############################################
    def add_actors(self):
        """Adds `self.widgets` to the scene.
        """
        if not self._actors_added:
            self._update()
            self._actors_added = True
            if not self.visible:
                self._visible_changed(self.visible)
            self.scene.render()

    def remove_actors(self):
        """Removes `self.widgets` from the scene.
        """
        if self._actors_added:
            self.scene.remove_widgets(self.widgets)
            self._actors_added = False
            self.scene.render()

    ######################################################################
    # Non-public interface
    ######################################################################

    def _update(self):
        if self.scene is None:
            return

    def _scene_changed(self, old, new):
        if self._actors_added:
            old.remove_wdigets(self.widgets)
            self._update()

    def _actors_changed(self, old, new):
        if self._actors_added:
            self.scene.remove_widgets(old)
            # The widgets are added automatically when the importer
            # does a read.
            self.scene.render()

    def _actors_items_changed(self, list_event):
        if self._actors_added:
            self.scene.remove_widgets(list_event.removed)
            # The widgets are added automatically when the importer
            # does a read.
            self.scene.render()
