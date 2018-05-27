
Objects populating the Mayavi pipeline
========================================

.. currentmodule:: mayavi.core.api

Here we give a brief description of the key objects in the Mayavi pipeline.

.. image:: images/pipeline_and_scene.jpg
    :align: center


.. note::

    Given a Mayavi object, a simple way to see what important attribute
    is, display it to call it's ``print_traits()``. Note that, for
    certain objects, when used in IPython, this can cause a segfault, due
    to threading problems in IPython.

Scene
------

====================== ========================================================
Key attributes
====================== ========================================================
``scene``		a ``TVTKScene`` (``tvtk.pyface.tvtk_scene``) 
			object which is where all the rendering occurs.

 ``children``		a list of ``Source`` objects.
====================== ========================================================

The ``Scene`` class is defined in the ``mayavi.core.scene`` module.

.. seealso:: 

    API reference for the :class:`Scene` class. 

Source
--------

All the data sources, file readers, Parametric surface etc. are
subclasses of the ``Source`` class.

====================== ========================================================
Key attributes
====================== ========================================================
``children``		a list of either ``Modules`` or ``Filters``

``outputs``		``List`` of outputs produced by the source. These are 
			TVTK datasets, that are explained in 
			the section :ref:`data-structures-used-by-mayavi`.
====================== ========================================================

The ``Source`` class is defined in the ``mayavi.core.source`` 
module.  

.. seealso:: 

    API reference for the :class:`Source` class.

Filter
--------

All the ``Filters`` described in the :ref:`filters` section are
subclasses of this class.

====================== ========================================================
Key attributes
====================== ========================================================
``children``		a list of either ``Modules`` or other ``Filters``.

``inputs``		a ``List`` of input TVTK dataset objects that feed into 
			the filter.

``outputs``		a list of outputs produced by the filter. These are 
			TVTK datasets, that are explained in 
			the section :ref:`data-structures-used-by-mayavi`.
====================== ========================================================
  

====================== ========================================================
Key methods
====================== ========================================================
``setup_pipeline()``	used to create the underlying TVTK pipeline objects if 
			needed.

``update_pipeline()``   called when the upstream pipeline 
			has been changed, i.e. an upstream object fires a 
			``pipeline_changed`` event.

``update_data()``	called when the upstream pipeline 
			has **not** been changed but the data in the
			pipeline has been changed.  This happens when the 
			upstream object fires a ``data_changed`` event.
====================== ========================================================

The filter class is defined in the ``mayavi.core.filter`` module.

.. seealso:: 

    API reference for the :class:`Filter` class.

ModuleManager: Colors and legends node
---------------------------------------

This object is the one called *Colors and legends* in the tree view on
the UI.  The main purpose of this object is to control how data is turned
in colors in the ``Modules`` it manages.  All modules typically will use
a lookup table (LUT) in order to produce a meaningful visualization.
This lookup table is managed by the module manager.

====================== ========================================================
Key attributes
====================== ========================================================
``source``		the ``Source`` or ``Filter`` object that is the input
			of this object.

``children``		a list of the ``Modules`` it manages.

``scalar_lut_manager``  an instance of a ``LUTManager`` which 
			basically manages the color mapping from
			scalar values to colors on the visualizations.  
			This is basically a mapping from scalars to colors.

``vector_lut_manager`` an instance of a ``LUTManager`` which manages the 
		       color mapping from vector values to colors on the 
		       visualizations.

``lut_data_mode``      'auto', 'point data' and 'cell data'.
			Specifies the data type to use for the LUTs.  This can 
			be changed inbetween .  Changing this setting will 
			change the data range and name of the lookup
			table/legend bar.  If set to 'auto' (the default), 
			it automatically looks for cell and point data with 
			point data being preferred over cell data and 
			chooses the one available. If set to 'point data' it 
			uses the input point data for the LUT and if set to 
			'cell data' it uses the input cell data.
====================== ========================================================

This class is defined in the ``mayavi.core.module_manager``
module.

.. seealso:: 

    API reference for the :class:`ModuleManager` class.

Module
-------

These objects are the ones that typically produce a visualization on the
scene.  All the modules defined in the :ref:`modules` section are
subclasses of this.

A module is typically returned by the mlab 
:ref:`3D plotting functions <mlab_plotting_functions>`.

====================== ========================================================
Key attributes
====================== ========================================================
``module_manager``	The ``ModuleManager`` instance that controls the 
			colormaps and the legends of this ``Module``

``actor``		The TVTK actor of the modules, in other words
			the object displayed in the scene. This is where
			you will have the properties such as scaling, or
			GL material properties.

``components``		a list of various reusable components that are used 
			by the module.  These usually are never used directly 
			by the user.  However, they are extremely useful 
			when creating new modules.  A ``Component`` is
			basically a reusable piece of code that is used by 
			various other objects.  For example, almost every 
			``Module`` uses a TVTK actor, mapper and property.  
			These are all "componentized" into a reusable 
			`Actor` component that the modules use.  Thus,
			components are a means to promote reuse between 
			mayavi pipeline objects.
====================== ========================================================

====================== ========================================================
Key methods
====================== ========================================================
``setup_pipeline()``	used to create the underlying TVTK pipeline objects if 
			needed.

``update_pipeline()``   called when the upstream pipeline 
			has been changed, i.e. an upstream object fires a 
			``pipeline_changed`` event.

``update_data()``	called when the upstream pipeline 
			has **not** been changed but the data in the
			pipeline has been changed.  This happens when the 
			upstream object fires a ``data_changed`` event.
====================== ========================================================


Defined in the ``mayavi.core.module`` module.

.. seealso:: 

    API reference for the :class:`Module` class.

Engine
--------

The Mayavi engine is the central object dealing with life-cycle of
visualization objects and scene, as well as connecting and updating the
pipeline. It is at the root of the pipeline and is not displayed in the
pipeline view.

For contextual operation, the engine has the notion of a 'current object'
and a 'current scene' and features several methods that let one add a
``Filter/Source/Module`` instance to it. The contextual operations are
important in a menu-driven graphical user interface. 

It allows one to create new scenes and delete them.  Also has methods to
load and save the entire visualization.

.. currentmodule:: mayavi

When using mlab, the engine used by mlab can be retrieved using
:func:`mlab.get_engine`.

.. currentmodule:: mayavi.core.api

====================== ========================================================
Key attributes
====================== ========================================================
``scenes``		a list of ``Scene`` objects.

``current_object``	the object on which contextual operations, such
			as ``add_module`` will apply.

``current_scene``	the scene in which data sources will be added by
			default.

``current_selection``  The object selected in the pipeline view.
====================== ========================================================

====================== ========================================================
Key methods
====================== ========================================================
``new_scene()``		this is the method called to create a new scene.
			Subclasses override this method.
====================== ========================================================


====================== ========================================================
Important sub-classes
====================== ========================================================
``EnvisageEngine``	defined in the 
			``mayavi.plugins.envisage_engine``
			module. It is the subclass of
			used in the ``mayavi2`` application.

``OffScreenEngine``	defined in the
			``mayavi.core.off_screen_engine`` module. 
			It creates scenes that are not displayed on
			screen by default.

``NullEngine``		defined in the
			``mayavi.core.null_engine`` module.
			With this engine, visualization objects are
			not added to a scene, and thus cannot be rendered. 
			This engine is useful for testing and pure-data 
			handling use of Mayavi's data structures.
====================== ========================================================

.. image:: images/design2c.jpg
   :alt: The ``Engine`` object.
   :align: center

The `Engine` base class is defined in the ``mayavi.engine`` module.

.. seealso:: 

    API reference for the :class:`Engine` class.

Base class: PipelineBase
--------------------------

The ``PipelineBase`` is the base class for all
objects in the mayavi pipeline except the ``Scene`` and ``Engine``
(which really isn't *in* the pipeline but contains the pipeline).
Defined in the ``mayavi.core.pipeline_base`` module.
Derives from ``Base`` which merely abstracts out common
functionality.  

====================== ========================================================
Key attributes
====================== ========================================================
``pipeline_changed``	This is an ``Event`` Trait: it can only be
			assigned to and determines when the pipeline has
			been changed. Therefore, if one does::

				object.pipeline_changed = True 

			then the ``pipeline_changed`` event is fired.
			Objects downstream of ``object`` in the pipeline
			are automatically setup to listen to events from
			an upstream object and will call their
			``update_pipeline`` method.  

``data_changed``	Similarly, if the ``data_changed`` event is fired 
			then downstream objects will automatically call 
			their ``update_data`` methods.

``outputs``		a list of outputs produced by the object.

``scene``		the scene to which the object is attached.

``visible``		a boolean that toggle the Hide/Show status of the
			object and its downstream pipeline.
====================== ========================================================

====================== ========================================================
Key methods
====================== ========================================================
``remove()``		can be used to remove the object (if added)
			from the mayavi pipeline.
====================== ========================================================

.. seealso:: 

    API reference for the :class:`PipelineBase` class.

Class hierarchy
---------------------

The following figures show the class hierarchy of the various objects
involved.

.. image:: images/design2a.jpg
   :alt: Basic object hierarchy
   :align: center

*This hierarchy depicts the ``Base`` object, the ``Scene``,
``PipelineBase`` and the ``ModuleManager``.*

.. image:: images/design2b.png
   :alt: More object hierarchy
   :align: center

*This hierarchy depicts the ``PipelineBase`` object, the ``Source``,
``Filter``, ``Module`` and the ``Component``.*


