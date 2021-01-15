#. Start with the `Application` instance
  * Need to subclass `TasksApplication` instead of `WorkBenchApplication`.
    They are siblings so some methods can be left untouched which is nice.
  * `TasksApplication` has a `default_layout` and `always_use_default_layout`
    traits which need to be set. `WorkbenchApplication` has an `about_dialog`
    that no longer needs to be specified.

#. In a Workbench application, you will have a “Perspective” that defines a
   layout of various “Views”.  This Perspective needs to be changed into a
   “Task”, and the “Views” into “Dock Panes”.  
  * There are some useful classes to help when making a quick transition:
    * Pyface has a `TraitsDockPane` class for making dock panes which display a
      TraitsUI view.  “Views” from workbench application may be simple HasTraits
      classes.  Alternatively they may subclass either ‘View’ or `TraitsUIView`
      from `pyface.workbench.api`.  To use a `TraitsDockPane`, you simply need
      to set the `model` trait and provide a view to use for the dock pane.
      For example, if the Workbench View has its model and view defined on the
      same class one could do:
	      def _model_default(self):
              return OldWorkbenchView()
		  def default_traits_view(self):
			  return self.model.trait_view()
	  It is also important to note the following method on `TraitsDockPane`:
      https://github.com/enthought/pyface/blob/4a991afb5eb243af5d303b7281b906f6bf24e109/pyface/tasks/traits_dock_pane.py#L33-L38 ‘
      So you may need to be careful to ensure the view is using the correct
      things
    * By default, a Workbench Application has an “Editor Area”.  A “Perspective”
      defines a grouping of “Views” around this area.  A “Task” has a _slightly_
    analogous “Central Pane”.  However, the Central Pane is intended to be far
    more versatile.  The Editor Area is always a notebook style collection of
    editors.  In order to have a Tasks application that has this as well, one
    can use either the `EditorAreaPane`, `SplitEditorAreaPane` or the
    `AdvancedEditorAreaPane` from `pyface.tasks.api`.
      * Workbench editors can be activated by calling `edit` related methods on
        the WorkbenchWindow.  To do so with Tasks, the `EditorAreaPane`
        implement nearly the same api, so you simply need to instead of calling
        method on the window call them on window.central_pane for example.
      * It is also important to note that the `Editor` classes from
        `pyface.tasks.api` and `pyface.workbench.api` have a slightly different
        interface, so you can’t simply change your editor classes to subclass
        one instead of the other.  For example, with workbench the editors need
        to define a `create_control` method that creates and returns the
        toolkit-specific control.  Analogously with Tasks Editor you need to
        define a `create` method that creates and _sets_ the toolkit-specific
        control.  

#. WorkbenchPlugin vs. TasksPlugin
  * WorkbenchPlugin offers the following extension points:
    * ACTION_SETS = “envisage.ui.workbench.action_sets"
    * PERSPECTIVES = “envisage.ui.workbench.perspectives"
    * PREFERENCES_PAGES = “envisage.ui.workbench.preferences_pages"
    * WORKBENCH_SERVICE_OFFERS = “envisage.ui.workbench.service_offers"
    * VIEWS = “envisage.ui.workbench.views"
  * WorkbenchPlugin contributes to:
    * PREFERENCES = "envisage.preferences"
    * SERVICE_OFFERS = "envisage.service_offers"
  * TasksPlugin offers:
    * PREFERENCES_CATEGORIES = “envisage.ui.tasks.preferences_categories"
    * PREFERENCES_PANES = “envisage.ui.tasks.preferences_panes" 
    * TASKS = “envisage.ui.tasks.tasks"
    * TASK_EXTENSIONS = “envisage.ui.tasks.task_extensions"
  * TasksPlugin contributes to:
    * SERVICE_OFFERS = "envisage.service_offers"
  * One major thing to note is that Workbench has an extension point for
    `WORKBENCH_SERVICE_OFFERS`, which Tasks does not provide.  However, the
    `CorePlugin` from `envisage` already has a `SERVICE_OFFERS` extension point.
    Thus, in a tasks application we interact with services via the application
    instance whereas with workbench we can work with window specific services.
    * This can potentially lead to some seemingly unrelated issues.  With
      workbench service offers get registered once their corresponding window is
      opened.  The WorkbenchPlugin simply defines the extension point, but the
      actual registration is handled by the WorkbenchWindow instance and is
      triggered by the window opening.  As a result Workbench applications may
      have many trait listeners set up for events triggered by windows, or use
      the WorkbenchWindow instance for other things. With tasks you will need to
      update these listeners and services need to be accessed via the
      application.  You need to consider what really needs access to the
      application to get these services or if the services theemselves should
      be passed to objects rather than the application itself (previously the
      WorkbenchWindow would have been passed down or used).   A Workbench
      application may do things under the assumption that certain Service offers
      will not be registered until after a window is created, but with Tasks
      that may not necessarily be the case, in which case you will have to
      address those.  This is one of the bigger headaches of the whole process
      as things can be easy to miss / hard to track down depending on how much
      the workbench app took advantage of these workbench specific behaviors.
      The Task object API has a few methods that may be convenient to avoid
      needing to write your own specific trait listeners (namely `initialized`,
      `activated`, `prepare_destroy`)

#. Menu/Tool bars
  * With Workbench, Apps contribute to the “ACTION_SETS” extension point. To do
    so they define an ActionSet, which is composed of various `Action`, `Group`,
    and `Menu` from `envisage.ui.action.api`
  * Tasks Apps define `menu_bar` and `tool_bars` traits on Task itself.  To do
  so, you need to define Schemas.  This process is documented here:
  https://docs.enthought.com/envisage/tasks_user_manual/menus.html and In this
  currently open PR https://github.com/enthought/pyface/pull/837 
    * You can also contribute `SchemaAddition`s to the TASK_EXTENSIONS extension
      point to add to a Task’s already existing Toolbars/menubars
    * AFAIK there is no trivial way to make this conversion and you need to
      manually go through and define SMenu, SGroup, Action instances etc. based
      of the `Menu`, `Group` and `Action` instances defined for the actionset
      (note these are not the same types, they come from different places and
      have different traits)
  * One important thing to note:  With Workbench Views, the view can itself have
    its own toolbar, however a Tasks Dock pane cannot by default (at least on
    Qt). This is because, on Qt, toolbars can only be assigned to a QMainWindow
    instance.  Workbench works around this by defining a _ViewContainer class
    which subclasses QMainWindow.  To do something similar, when you define the
    create_contents method of a TraitsDockPane for example, you can create a
    panel which is a QMainWindow to wrap the rest of the dock pane contents.
    See example: …
  * Another important thing to note: as mentioned above action sets with
  workbench apps are contributed as per window service offers.  Therefore the
  actions they define will have access to the WorkbenchWindow.  However, with
  Tasks this is not the case, so you need to take extra care to ensure the
  actions defined only use what they truly need (try to avoid dependencies on
  specific Task/TaskWindow/TaskApplication where possible) and also if these
  objects truly are needed that they are passed to the action, or accessible in
  some way (at the appropriate time!  Note that the task may not be instantiated
  yet, or not yet hooked up to a window etc.    

#. Preferences
  * As mentioned above, the WorkbenchPlugin accepts PreferencePage
    contributions, whereas the TasksPlugin accepts PreferencesCatgeory and
    PreferencesPane contributions.  A transition is relatively straightforward.
    If you already have a preferences helper defined for your PrefrencesPage,
    you can simply use that as the model trait of your PreferencesPane, and you
    can typically use the same view.  Rather than specifying the `category`
    trait on the PreferencesPage class, you need to create a
    `PreferencesCatgeory` instance and contribute it to the appropriate
    extension point.
