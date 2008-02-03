from enthought.envisage.api import PluginDefinition
from enthought.envisage.core.core_plugin_definition import \
     ApplicationObject
from enthought.envisage.workbench.workbench_plugin_definition import \
     Workbench, View, Perspective

my_app_obj = ApplicationObject(class_name='explorer_app.Explorer3D',
                               uol='service://explorer3d.Explorer3D')
views = [View(name='3D function explorer',
              id='explorer3d.Explorer3D',
              uol='service://explorer3d.Explorer3D',
              traits_ui_view='view',
              position='left',
              width=0.05),
         ]

perspectives = [
    Perspective(id='explorer3d.default_perspective',
                name='Explorer3D',
                contents =
                [ Perspective.Item(id='explorer3d.Explorer3D',
                                   position='left',
                                   width=0.05),
                  ],
                enabled=True,
                )
    ]

workbench = Workbench(views=views, perspectives=perspectives,
                      default_perspective='explorer3d.default_perspective')
requires = ["enthought.envisage.workbench",
            "enthought.mayavi",
            "enthought.mayavi_ui",
            ]

PluginDefinition(
    # This plugins unique identifier.
    id = "explorer3d.Explorer3D",

    # General info.
    name = "3D function explorer",
    version = "1.0",
    provider_name = "Prabhu Ramachandran",
    provider_url = "www.enthought.com",
    enabled = True,
    autostart = True,

    # Id's of plugin that this one requires.
    requires = requires,
    
    # The extension points that we provide.
    extension_points = [],

    # The contributions that this plugin makes to extension points offered by
    # either itself or other plugins.
    extensions = [workbench, my_app_obj]
)
