from collections import defaultdict


class Bridge(object):
    def add_widget(self, scene_id, widget):
        '''Add widget corresponding to a given scene id.
        '''
        pass

    def remove_widget(self, scene_id, widget):
        '''Remove a widget corresponding to a given scene_id.
        '''
        pass

    def get_scenes(self):
        '''Returns a list of the available scenes.
        '''
        pass

    def handle_event(self, event_data):
        '''Handle an event sent by the server.
        '''
        pass

    def run(self):
        '''Run any code for the bridge to do its job.
        '''
        pass


class LocalBridge(Bridge):
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        # In the local case, we are the client of
        # the scene manager and manage those events.
        self.scene_manager.add_client(self)
        self.widgets = defaultdict(list)

    def add_widget(self, scene_id, widget):
        '''Add widget corresponding to a given scene id.
        '''
        self.widgets[scene_id].append(widget)

    def remove_widget(self, scene_id, widget):
        '''Remove a widget corresponding to a given scene_id.
        '''
        w = self.widgets[scene_id]
        w.remove(widget)
        if len(w) == 0:
            del self.widgets[scene_id]

    def get_scenes(self):
        '''Returns a list of the available scenes.
        '''
        return self.scene_manager.scenes

    def handle_event(self, event_data):
        s_id, obj_name, event, data = event_data
        for w in self.widgets[s_id]:
            w.handle_vtk_event(obj_name, event, data)
