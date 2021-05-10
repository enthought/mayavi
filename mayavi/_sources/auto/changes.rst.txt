Mayavi 4.7.3
============

This is a small bug fix release mainly concerned with compatability with Traits
6.2.0 and soon to be release TraitsUI 7.2.0.

Fixes
-----

10 Dec 2021 `#983 <https://github.com/enthought/mayavi/pull/983>`_ (larsoner)
   - MAINT: Support Python 3.9

06 May 2021 `#1030 <https://github.com/enthought/mayavi/pull/1030>`_ (aaronayres35)
   - import from pyface.image not traitsui.image

06 May 2021 `#1035 <https://github.com/enthought/mayavi/pull/1035>`_ (aaronayres35)
   - Pass a value in appropriate range to avoid failure


Mayavi 4.7.2
============

The significant update for this release is that it is compatible with the
latest VTK-9.x series and is known to work with VTK 9.0.1 from PyPI. The
picker UI has changed to no longer pop up a UI window but instead show the
picked attributes on the render window directly. The original picker UI is now
available on the scene's UI in a separate "Picker" tab. This is accessible
from either the pipeline view when one edits the properties of a scene or
through the "configure scene" gear icon on the scene window toolbar.

Many thanks to the following who contributed to this release (in alphabetical
order):

Amal S Sebastian, Eric Larson, Guillaume Favelier, Hans Moritz Günther, Magnus
Nord, Mark Dickinson, Poruri Sai Rahul, Prabhu Ramachandran, Scott Talbert,
Tetsuo Koyama.

This is largely a bug-fix release with one enhancement/change.
36 pull requests were merged.


Enhancements
------------

30 Apr 2020 `#820 <https://github.com/enthought/mayavi/pull/820>`_ (amalss18)
   - New picker UI that shows on the render window and not as a pop-up UI.
     1. Shifted picker GUI to configure GUI (the Scene's properties).
     2. Old UI is in the scene properties or window's configure scene button.
     3. Picker data appears as a text widget on the scene.
     4. added a mlab.set_picker_props() to set properties of the picker.

Fixes
-----

27 Jul 2020 `#931 <https://github.com/enthought/mayavi/pull/931>`_ (larsoner)
   - MAINT: Deal with traitsui deprecation of `TraitPrefixMap`

27 Jul 2020 `#928 <https://github.com/enthought/mayavi/pull/928>`_ (hamogu)
   - Add formats to `savefig` docstring

30 Apr 2020 `#913 <https://github.com/enthought/mayavi/pull/913>`_ (PR)
   - Add tests to check if hand-crafted views work.

30 Apr 2020 `#912 <https://github.com/enthought/mayavi/pull/912>`_ (PR)
   - Fix CI and remove 2.7 tests.

25 Apr 2020 `#909 <https://github.com/enthought/mayavi/pull/909>`_ (larsoner)
   - ENH: VTK 9 compatibility.

25 Apr 2020 `#901 <https://github.com/enthought/mayavi/pull/901>`_ (tkoyama010)
   - Document use of `PyVirtualDisplay`

25 Apr 2020 `#900 <https://github.com/enthought/mayavi/pull/900>`_ (larsoner)
   - FIX: Work around NumPy deprecation

25 Apr 2020 `#896 <https://github.com/enthought/mayavi/pull/896>`_ (GuillaumeFavelier)
   - Replace TraitTuple by Tuple in modules.py

30 Apr 2020 `#893 <https://github.com/enthought/mayavi/pull/893>`_ (tkoyama010)
   - Use importlib instead of imp.

30 Apr 2020 `#877 <https://github.com/enthought/mayavi/pull/877>`_ (swt2c)
   - Fix support for wxPython 3.0

25 Apr 2020 `#876 <https://github.com/enthought/mayavi/pull/876>`_ (swt2c)
   - Remove spurious executable permissions from test data files

24 Dec 2019 `#868 <https://github.com/enthought/mayavi/pull/868>`_ (mdickinson)
   - Replace uses of traits.api.Long with traits.api.Int

05 Dec 2019 `#866 <https://github.com/enthought/mayavi/pull/866>`_ (mdickinson)
   - Replace uses of the deprecated trait types 'false' and 'true'

02 Dec 2019 `#859 <https://github.com/enthought/mayavi/pull/859>`_ (rahulporuri)
   - Replace deprecated rich_compare kwarg when creating traits

18 Nov 2019 `#853 <https://github.com/enthought/mayavi/pull/853>`_ (rahulporuri)
   - Update edm and install/config scripts

25 Apr 2020 `#843 <https://github.com/enthought/mayavi/pull/843>`_ (tkoyama010)
   - Avoid using eval

25 Apr 2020 `#841 <https://github.com/enthought/mayavi/pull/841>`_ (tkoyama010)
   - Added section on "Translating the documentation".

24 Dec 2019 `#840 <https://github.com/enthought/mayavi/pull/840>`_ (larsoner)
   - BUG: Fix literal comparison. Fixes on Python-3.8.

05 Oct 2019 `#822 <https://github.com/enthought/mayavi/pull/822>`_ (tkoyama010)
   - Fixed old TVTK documentation.


Mayavi 4.7.1
============

Thanks to the following who contributed to this release (in alphabetical
order): Poruri Sai Rahul, Prabhu Ramachandran

This is a bug-fix release.  3 pull-requests were merged.

Fixes
-----

21 Jul 2019 `#807 <https://github.com/enthought/mayavi/pull/807>`_ (PR)
   - Fix old pipeline errors in image actor.

16 Jul 2019 `#804 <https://github.com/enthought/mayavi/pull/804>`_ (rahulporuri)
   - Use the decorator for classmethod
     Instead of explicitly calling it in the class definition

04 Jul 2019 `#800 <https://github.com/enthought/mayavi/pull/800>`_ (PR)
   - Misc bug fixes
     Fixes 3 issues that affect the new release due to changes in traits, pyface etc.
     - Fix issue with CTF editor not showing.
     - Fix issue with lut editor not launching.
     - Fix issue with cut/pasting tree nodes and drag drop onto shell.


Mayavi 4.7.0
============

Thanks to the following who contributed to this release (in alphabetical
order): Eric Larson, Poruri Sai Rahul, Prabhu Ramachandran, Stefan Sandfeld,
and Todd.

Thanks to Enthought for funding the work that led to the significantly
improved Jupyter notebook support.

19 pull requests were merged.

This release has one very powerful new feature -- jupyter notebook support
with complete interactivity.

Enhancements
------------

26 Nov 2018 `#739 <https://github.com/enthought/mayavi/pull/739>`_ (PR)

   - New Jupyter notebook 'ipy' backend which is now the default and
     requires that VTK's offscreen support work correctly. This backend
     requires ipywidgets and ipyevents. It allows complete interactivity and
     behaves almost exactly like a normal UI backend but inside a notebook.
     Note that this will still require an xserver or windowing toolkit unless
     VTK is compiled to be able to work without those.

     Many thanks to Enthought for supporting this.

09 Oct 2018 `#723 <https://github.com/enthought/mayavi/pull/723>`_ (PR)
   - Improve offscreen window creation.
     Creating a renderwindow in some configurations can actually make UI
     calls.  So if EGL is available we try that.  Also, when we are using
     offscreen rendering we only need a GenericRenderWindowInteractor.
     Also add a convenient set method so one can set a different interactor if needed.

08 Sep 2018 `#712 <https://github.com/enthought/mayavi/pull/712>`_ (PR)
   - ENH: Feature to disable automatic updates.
     This can be very handy at times when the automatic updates can trigger
     several changes that are not desirable.  For example on certain VTK
     calls, internal ModifiedEvents may be fired which will automatically
     call the update_traits method which can be wired to other events
     triggering problems.  In these cases one can use the
     `global_disable_update` function to temporarily disable updates.


Fixes
-----

30 Jun 2019 `#795 <https://github.com/enthought/mayavi/pull/795>`_ (rahulporuri)
   - Test against ETS packages from source using travis cron jobs.

23 Jun 2019 `#793 <https://github.com/enthought/mayavi/pull/793>`_ (rahulporuri)
   - Use xenial linux instead of trusty

19 Jun 2019 `#792 <https://github.com/enthought/mayavi/pull/792>`_ (ssandfeld)
   - add fix for str conversion from bad bytes array
     This fixes issue `#791 <https://github.com/enthought/mayavi/issues/791>`_.

26 Apr 2019 `#771 <https://github.com/enthought/mayavi/pull/771>`_ (prabhuramachandran)
   - Fix issue `#770 <https://github.com/enthought/mayavi/issues/770>`_
     The issue arises in a few of the mlab sources where when we reset to a
     polydata with a smaller number of points.

26 Apr 2019 `#754 <https://github.com/enthought/mayavi/pull/754>`_ (larsoner)
   - FIX: Fix nose leftovers in tests.

26 Apr 2019 `#747 <https://github.com/enthought/mayavi/pull/747>`_ (larsoner)
   - FIX: Escape chars in code.

27 Nov 2018 `#740 <https://github.com/enthought/mayavi/pull/740>`_ (toddrme2178)
   - Also catch exceptions in generating documentation

15 Nov 2018 `#736 <https://github.com/enthought/mayavi/pull/736>`_ (PR)
   - Some UI fixes for ivtk.
     This fixes `#734 <https://github.com/enthought/mayavi/issues/734>`_.

16 Nov 2018 `#735 <https://github.com/enthought/mayavi/pull/735>`_ (larsoner)
   - FIX: Fix set_range causing lookup table errors.

26 Oct 2018 `#731 <https://github.com/enthought/mayavi/pull/731>`_ (larsoner)
   - FIX: Fix type check

15 Nov 2018 `#729 <https://github.com/enthought/mayavi/pull/729>`_ (larsoner)
   - FIX: Fix for VTKNoneArray

11 Oct 2018 `#724 <https://github.com/enthought/mayavi/pull/724>`_ (PR)
   - Try and fix `#477 <https://github.com/enthought/mayavi/issues/477>`_.
     If OSMesa is available and user requests an offscreen window, use an
     OSOpenGLRenderWindow, this will not require X and can be safely used on
     a remote server.

16 Nov 2018 `#722 <https://github.com/enthought/mayavi/pull/722>`_ (rahulporuri)
   - Fix bug related to SurfaceSource.scalars This bug manifests when the
     SurfaceSource object in question does not have a scalars attribute and
     many of them do not have this.

23 Sep 2018 `#716 <https://github.com/enthought/mayavi/pull/716>`_ (PR)
   - Fix `#713 <https://github.com/enthought/mayavi/issues/713>`_ with pip
     installs failing.

23 Sep 2018 `#715 <https://github.com/enthought/mayavi/pull/715>`_ (prabhuramachandran)
   - Fix detection of color transfer function.
     The original code was written for very old VTK versions but ever since
     5.x we have a get_node_value method that actually provides the values of
     the nodes given an index.  We now use this instead of the earlier hack.


Mayavi 4.6.2
============

Thanks to the following who contributed to this release (in alphabetical
order): solarjoe, François Boulogne, Prabhu Ramachandran (PR), and Ioannis
Tziakos.

11 pull requests were merged.

This is largely a bugfix release with a few useful enhancements. This will be
the last release to properly support VTK versions less than 7.0.

Enhancements
------------

03 Aug 2018 `#695 <https://github.com/enthought/mayavi/pull/695>`_ (PR)
   - Wrap user defined algorithm
   - Ensure VTKPythonAlgorithmBase is wrapped
   - `tvtk.to_tvtk` now wraps VTK subclasses by using a nearest base class.
     This allows us to add VTK objects easily to the mayavi pipeline.

02 Aug 2018 `#694 <https://github.com/enthought/mayavi/pull/694>`_ (PR)
   - Allow adding a vtkAlgorithm to the Mayavi pipeline
   - Allow `mlab.pipeline.add_dataset` to also accept raw VTK objects.
   - Generalize the TVTK pipeline browser so it can be plugged into other
     HasTraits objects easily.
   - Add a `VTKObjectSource` to Mayavi:
      - allows us to add any VTK algorithm to the mayavi pipeline and then
        process that with the rest of Mayavi.
      - It provides a convenient UI to configure the raw TVTK objects.
      - these can be added to the pipeline with `mlab.pipeline.add_dataset`.
      - does not yet support user-defined algorithms via subclasses of
        VTKPythonAlgorithmBase.

25 Jul 2018 `#687 <https://github.com/enthought/mayavi/pull/687>`_ (PR)
   - Add smart volume mapper
   - This is a much nicer volume mapper.
   - Also fix an issue with the tvtk_doc and the recent change to use desc
     instead of help for the trait metadata.

24 Jul 2018 `#684 <https://github.com/enthought/mayavi/pull/684>`_ (PR)
   - Use `desc` instead of `help` for traits. This is much more useful than
     `help` as it shows up nicely as a tooltip for each trait on the UI.

Fixes
-----

01 Aug 2018 `#693 <https://github.com/enthought/mayavi/pull/693>`_ (PR)
   - Fix wrapping VTK's Get* methods
   - Fix array handler tests for newer numpy versions. These versions have a
     float16/float128 dtype which are not directly supported in VTK.
   - BUG: wrap the `Get` methods correctly. Many of the new pipeline methods
     were not wrapped correctly. For example the
     `vtkAlgorithm.GetInputAlgorithm` has multiple signatures. TVTK was
     wrapping any getter which had one of its signatures with no args as a
     pure property and not exposing the method itself. This means that users
     cannot call `obj.get_input_algorithm(0, 0)` which is broken. We now wrap
     the no arg call as a property but also wrap the generic method as a
     callable method.
   - Fix the pipeline browser for the new pipeline.
   - Add a few reasonable tests for the browser

30 Jul 2018 `#691 <https://github.com/enthought/mayavi/pull/691>`_ (PR)
   - Fix issue `#689 <https://github.com/enthought/mayavi/issues/689>`_.
     The error was because the example uses the old pipeline.

24 Jul 2018 `#683 <https://github.com/enthought/mayavi/pull/683>`_ (PR)
   - Fix compiler check on windows. The check does not work when msvc is not
     installed and this should fix it. This allows us to install Mayavi on
     windows without having a compiler setup!

24 Jul 2018 `#680 <https://github.com/enthought/mayavi/pull/680>`_ (solarjoe)
   - fix upper case extension pyface will throw a KeyError if a filename with
     an upper case extension like "my_image.PNG" it entered in the textbox as
     the extension is not in the `meth_map`.


Mayavi 4.6.1
============

Thanks to the following who contributed to this release (in alphabetical
order):  Eric Larson, Hongzhuo Liang, and Prabhu Ramachandran (PR).

15 pull requests were merged.

Enhancements
------------

04 Jul 2018 `#669 <https://github.com/enthought/mayavi/pull/669>`_ (PR)
   - ENH: Expose `process_ui_events` in mlab.

30 Jun 2018 `#666 <https://github.com/enthought/mayavi/pull/666>`_ (PR)
   - Add attribute data to datasets. This makes it very easy to add new
     scalar/vector/tensor attributes to either a VTKDataSource or to an
     ArraySource using the `add_attribute`, `remove_attribute`, and
     `rename_attribute` methods.

29 Jun 2018 `#663 <https://github.com/enthought/mayavi/pull/663>`_ (PR)
   - Support PySide2.  Set `QT_API=pyside2` for this to work.

28 Jun 2018 `#661 <https://github.com/enthought/mayavi/pull/661>`_ (PR)
   - Make `tvtk.array_ext` optional on systems with no compiler. This makes
     Mayavi easy to install via pip without a compiler to build the extension
     module.  For those who have a compiler, the extension is built.

Fixes
-----

04 Jul 2018 `#672 <https://github.com/enthought/mayavi/pull/672>`_ (PR)
   - Fix Python3 error in some examples and fix picking of multi-component
     scalars.

03 Jul 2018 `#667 <https://github.com/enthought/mayavi/pull/667>`_ (lianghongzhuo)
   - Fix help icon so it actually works and loads the documentation in a browser.

29 Jun 2018 `#665 <https://github.com/enthought/mayavi/pull/665>`_ (PR)
   - Fix annoying warning when running Mayavi tests.

29 Jun 2018 `#664 <https://github.com/enthought/mayavi/pull/664>`_ (larsoner)
   - ENH: Use views in set_id_type_array_py making it more efficient.

28 Jun 2018 `#662 <https://github.com/enthought/mayavi/pull/662>`_ (PR)
   - Fix the broken help links and icon to launch TVTK class browser.

27 Jun 2018 `#660 <https://github.com/enthought/mayavi/pull/660>`_ (larsoner)
   - MRG: Fix window size for screenshot on HiDPI

05 Jun 2018 `#651 <https://github.com/enthought/mayavi/pull/651>`_ (PR)
   - Fix description/long description in setup.py.
   - Cleanup setup.py so just pip install mayavi works correctly without
     needing numpy first.


Mayavi 4.6.0
============

Thanks to the following who contributed to this release (in alphabetical order):

Bhavesh Thakkar, Christian Brodbeck, David Haberthür, Emmanuelle Gouillart,
Eric Larson, Federico Miorelli, James Booth, Krishna Wadhwani, Marijn van
Vliet, Min RK, Nelle Varoquaux, Prabhu Ramachandran, Stefano Borini, solarjoe.

48 pull requests were merged for this release.

Enhancements
------------

Thanks to the VTK wheels now available on PyPI, this release is the first
version of Mayavi that can be installed via ``pip install mayavi``.

23 May 2018 `#641 <https://github.com/enthought/mayavi/pull/641>`_ (PR)
   - Use new pyface toolkit

19 Jul 2017 `#528 <https://github.com/enthought/mayavi/pull/528>`_ (PR)
   - Qt5 support. This is critical for Python 3.x as this is the only toolkit
     that *currently* works reliably with Python 3.x and ETS.

Fixes
-----

26 May 2018 `#646 <https://github.com/enthought/mayavi/pull/646>`_ (PR)
   - Update installation documentation.
   - Fix warning message when updating mlab_source data without scalars/vectors.

22 May 2018 `#642 <https://github.com/enthought/mayavi/pull/642>`_ (PR)
   - Fix nbextension and missing bug with global.

20 May 2018 `#630 <https://github.com/enthought/mayavi/pull/630>`_ (PR)
   - Improve tests so Python 2.7, 3.x are tested and the tests run using VTK 8.x and 7.x.

06 Mar 2018 `#616 <https://github.com/enthought/mayavi/pull/616>`_ (PR)
   - Misc fixes for PyQt4 and Python 3.6.

16 Feb 2018 `#609 <https://github.com/enthought/mayavi/pull/609>`_ (PR)
   - Fix bug with mlab.screenshot and VTK 8.1.0.

16 Feb 2018 `#608 <https://github.com/enthought/mayavi/pull/608>`_ (PR)
   - Fix travis builds

15 Feb 2018 `#607 <https://github.com/enthought/mayavi/pull/607>`_ (PR)
   - Fix `#605 <https://github.com/enthought/mayavi/issues/605>`_: Interactors now work correctly with Qt5.

07 Feb 2018 `#599 <https://github.com/enthought/mayavi/pull/599>`_ (PR)
   - Fix some wxPython issues so mayavi works with recent wxPython releases.

06 Feb 2018 `#597 <https://github.com/enthought/mayavi/pull/597>`_ (PR)
   - Fix 8.1 issues phase 2

05 Feb 2018 `#596 <https://github.com/enthought/mayavi/pull/596>`_ (PR)
   - Fix 8.1 issues

23 Jan 2018 `#588 <https://github.com/enthought/mayavi/pull/588>`_ (larsoner)
   - MRG: Avoid NumPy deprecation

23 Jan 2018 `#584 <https://github.com/enthought/mayavi/pull/584>`_ (FedeMiorelli)
   - Fix bug with "p" keypress

23 Jan 2018 `#583 <https://github.com/enthought/mayavi/pull/583>`_ (FedeMiorelli)
   - VTK 8.x compatibility fixes

14 Dec 2017 `#578 <https://github.com/enthought/mayavi/pull/578>`_ (larsoner)
   - FIX: Remove debug print

06 Dec 2017 `#572 <https://github.com/enthought/mayavi/pull/572>`_ (PR)
   - BUG: Undo a couple of accidental trait_set changes.

30 Nov 2017 `#571 <https://github.com/enthought/mayavi/pull/571>`_ (NelleV)
   - DOC improve the mlab introduction

14 Dec 2017 `#566 <https://github.com/enthought/mayavi/pull/566>`_ (ghost)
   - Bug fix: solve the unicode encode error in windows

23 Nov 2017 `#564 <https://github.com/enthought/mayavi/pull/564>`_ (wmvanvliet)
   - Prevent get_tvtk_class_names from hijacking stderr

15 Nov 2017 `#559 <https://github.com/enthought/mayavi/pull/559>`_ (wmvanvliet)
   - Prevent get_tvtk_class_names from hijacking stdout

05 Dec 2017 `#556 <https://github.com/enthought/mayavi/pull/556>`_ (larsoner)
   - FIX: Tiny spelling fix

05 Dec 2017 `#555 <https://github.com/enthought/mayavi/pull/555>`_ (larsoner)
   - FIX: Fix deprecated .set / .get use

11 Aug 2017 `#544 <https://github.com/enthought/mayavi/pull/544>`_ (FedeMiorelli)
   - Fix numpy issues in lut_manager

11 Aug 2017 `#543 <https://github.com/enthought/mayavi/pull/543>`_ (PR)
   - Fix long standing test failure with ply reader.

06 Aug 2017 `#541 <https://github.com/enthought/mayavi/pull/541>`_ (PR)
   - Fix numpy warnings.

05 Aug 2017 `#540 <https://github.com/enthought/mayavi/pull/540>`_ (PR)
   - Try fix appveyor test failures.

05 Aug 2017 `#539 <https://github.com/enthought/mayavi/pull/539>`_ (PR)
   - Add test for the fix provided in `#514 <https://github.com/enthought/mayavi/issues/514>`_.

05 Aug 2017 `#538 <https://github.com/enthought/mayavi/pull/538>`_ (PR)
   - Fix bug with reset method of mlab sources.

05 Aug 2017 `#537 <https://github.com/enthought/mayavi/pull/537>`_ (PR)
   - Fix tests

05 Aug 2017 `#536 <https://github.com/enthought/mayavi/pull/536>`_ (PR)
   - Update readme and add link to mailing lists.

08 Aug 2017 `#531 <https://github.com/enthought/mayavi/pull/531>`_ (krishnaw14)
   - Update installation instructions for conda/conda-forge/edm.

11 Jul 2017 `#523 <https://github.com/enthought/mayavi/pull/523>`_ (solarjoe)
   - doc: Typo fix

11 Jul 2017 `#515 <https://github.com/enthought/mayavi/pull/515>`_ (PR)
   - Fix a bug with array source and vectors.

05 Aug 2017 `#514 <https://github.com/enthought/mayavi/pull/514>`_ (christianbrodbeck)
   - FIX shared data in testing backend

09 Jun 2017 `#510 <https://github.com/enthought/mayavi/pull/510>`_ (bhavesh2109)
   - Update extract_grid.py

11 May 2017 `#508 <https://github.com/enthought/mayavi/pull/508>`_ (FedeMiorelli)
   - Fix pick_world bug with VTK >= 6

19 Jul 2017 `#507 <https://github.com/enthought/mayavi/pull/507>`_ (FedeMiorelli)
   - Fix bug in mouse_pick_dispatcher

09 May 2017 `#506 <https://github.com/enthought/mayavi/pull/506>`_ (FedeMiorelli)
   - Remove focus-stealing code

09 May 2017 `#498 <https://github.com/enthought/mayavi/pull/498>`_ (minrk)
   - avoid loading nbextension via absolute URL

09 May 2017 `#486 <https://github.com/enthought/mayavi/pull/486>`_ (jabooth)
   - Remove known bug about Python 3 support

19 Jul 2017 `#471 <https://github.com/enthought/mayavi/pull/471>`_ (habi)
   - Adding information/tip about figure width

05 Oct 2016 `#444 <https://github.com/enthought/mayavi/pull/444>`_ (stefanoborini)
   - Fix for setuptools 28.0

05 Oct 2016 `#435 <https://github.com/enthought/mayavi/pull/435>`_ (emmanuelle)
   - [MRG] Added a volume_slice helper function in mlab.

13 Aug 2016 `#426 <https://github.com/enthought/mayavi/pull/426>`_ (PR)
   - Update readme.

13 Aug 2016 `#425 <https://github.com/enthought/mayavi/pull/425>`_ (PR)
   - Fix lurking old pipeline code


Mayavi 4.5.0
============

Enhancements
------------

21 Jul 2016 `#415 <https://github.com/enthought/mayavi/pull/415>`_ (PR)
   - Jupyter notebook support!  Adds support for displaying Mayavi images or
     x3d scenes on the notebook. The x3d scenes allow one to fully interact
     with the scene in the notebook.  More documentation is available at
     :ref:`jupyter_notebook`.

09 Jul 2016 `#411 <https://github.com/enthought/mayavi/pull/411>`_ (PR)
   - Adds support for recording movies and animating timesteps.  See
     :ref:`animating_a_timeseries` and :ref:`animating_a_visualization` for
     more details.

07 Jul 2016 `#410 <https://github.com/enthought/mayavi/pull/410>`_ (daytonb)
   - Updated LUTs to include new matplotlib colorschemes, this includes the
     new viridis colormap.

Fixes
-----

01 Aug 2016 `#416 <https://github.com/enthought/mayavi/pull/416>`_ (PR)
   - Fix several bugs, `#397 <https://github.com/enthought/mayavi/issues/397>`_
     where PDF files were not saved properly. Fix issues with ``tvtk.visual``
     and add many tests for it, this fixes `#387
     <https://github.com/enthought/mayavi/issues/387>`_.  Refactor the save
     screenshot dialog popups.  Fix problem with the picker point not showing
     when "p" is pressed on the scene.

29 Jul 2016 `#417 <https://github.com/enthought/mayavi/pull/417>`_ (patricksnape)
   - Python 3 fixes for the jupyter notebook support.

08 Jul 2016 `#413 <https://github.com/enthought/mayavi/pull/413>`_ (PR)
   - Fixes `#388 <https://github.com/enthought/mayavi/issues/388>`_ where
     tubes were not showing on protein demo.

03 Jul 2016 `#408 <https://github.com/enthought/mayavi/pull/408>`_ (ryanpepper)
   - Add additional save options.

04 Jul 2016 `#406 <https://github.com/enthought/mayavi/pull/406>`_ (PR)
   - Fixes `#403 <https://github.com/enthought/mayavi/issues/403>`_ where the
     image plane widget and volume modules were broken.

06 Jul 2016 `#405 <https://github.com/enthought/mayavi/pull/405>`_ (itziakos)
   - Debug info on code gen for wrapper generation.

16 Jun 2016 `#394 <https://github.com/enthought/mayavi/pull/394>`_ (PR)
   - BUG: Fix slice unstructured grid module.

17 Jun 2016 `#391 <https://github.com/enthought/mayavi/pull/391>`_ (SiggyF)
   - Fix typo in readme.

13 May 2016 `#386 <https://github.com/enthought/mayavi/pull/386>`_ (itziakos)
   - update codecov configuration

04 May 2016 `#376 <https://github.com/enthought/mayavi/pull/376>`_ (stefanoborini)
   - Documentation for QString API failure.

04 May 2016 `#375 <https://github.com/enthought/mayavi/pull/375>`_ (stefanoborini)
   - Fixes incorrect signature of ``EnvisageEngine.new_scene``.

03 May 2016 `#374 <https://github.com/enthought/mayavi/pull/374>`_ (stefanoborini)
   - Fix for unexpected test code.

13 May 2016 `#370 <https://github.com/enthought/mayavi/pull/370>`_ (kitchoi)
   - Fix "_p_void" values in TVTK with VTK 6.x

29 Apr 2016 `#364 <https://github.com/enthought/mayavi/pull/364>`_ (stefanoborini)
   - Fix failing test for custom import in some circumstances

27 Apr 2016 `#358 <https://github.com/enthought/mayavi/pull/358>`_ (stefanoborini)
   - Removes ``array_ext.so/pyd`` on clean

25 Apr 2016 `#356 <https://github.com/enthought/mayavi/pull/356>`_ (stefanoborini)
   - Check if test successful with the appropriate filename.

27 Apr 2016 `#355 <https://github.com/enthought/mayavi/pull/355>`_ (stefanoborini)
   - Unicode trait handling for those vtk methods returning unicode data

24 Apr 2016 `#352 <https://github.com/enthought/mayavi/pull/352>`_ (kitchoi)
   - ENH: Nice load pylab_luts.pkl

27 Apr 2016 `#351 <https://github.com/enthought/mayavi/pull/351>`_ (stefanoborini)
   - Document object identity behavior matching VTK

21 Apr 2016 `#349 <https://github.com/enthought/mayavi/pull/349>`_ (kitchoi)
   - Revert "Fix savefig size and black image"

27 Apr 2016 `#348 <https://github.com/enthought/mayavi/pull/348>`_ (stefanoborini)
   - Added setup.py documentation for Qt requirements

27 Apr 2016 `#345 <https://github.com/enthought/mayavi/pull/345>`_ (kitchoi)
   - Add VTK 6.3 and VTK 7 to travis ci

20 Apr 2016 `#341 <https://github.com/enthought/mayavi/pull/341>`_ (kitchoi)
   - Fix traitsdoc setup and compliance with py3

20 Apr 2016 `#340 <https://github.com/enthought/mayavi/pull/340>`_ (kitchoi)
   - Import and integer division in python3

20 Apr 2016 `#335 <https://github.com/enthought/mayavi/pull/335>`_ (kitchoi)
   - Fix texture on ``mlab.surf``, issue `#211 <https://github.com/enthought/mayavi/issues/211>`_.

20 Apr 2016 `#334 <https://github.com/enthought/mayavi/pull/334>`_ (stefanoborini)
   - Fixes Quiver3d Failure with different argument types

20 Apr 2016 `#332 <https://github.com/enthought/mayavi/pull/332>`_ (kitchoi)
   - Fix Text3D in VTK 6.0+

21 Apr 2016 `#331 <https://github.com/enthought/mayavi/pull/331>`_ (kitchoi)
   - Fix savefig size and black image

20 Apr 2016 `#330 <https://github.com/enthought/mayavi/pull/330>`_ (stefanoborini)
   - Fix for exception when modifying extents

01 Apr 2016 `#329 <https://github.com/enthought/mayavi/pull/329>`_ (stefanoborini)
   - Suppresses test for VTK 6.2 (solves appVeyor random failure)

20 Apr 2016 `#327 <https://github.com/enthought/mayavi/pull/327>`_ (stefanoborini)
   - Forces pipeline update when LUT changes

01 Apr 2016 `#326 <https://github.com/enthought/mayavi/pull/326>`_ (stefanoborini)
   - Fix for test failure on mayavi -t

28 Mar 2016 `#323 <https://github.com/enthought/mayavi/pull/323>`_ (stefanoborini)
   - Enforce ordering of attribute labels in VTKDataSource.

28 Mar 2016 `#315 <https://github.com/enthought/mayavi/pull/315>`_ (stefanoborini)
   - Apply has_attribute to the output in VTKFileReader

17 Mar 2016 `#313 <https://github.com/enthought/mayavi/pull/313>`_ (kitchoi)
   - Replacing links to code. and svn.enthought.com

09 Mar 2016 `#310 <https://github.com/enthought/mayavi/pull/310>`_ (kitchoi)
   - Fix Camera off-centered when loading saved visualization

09 Mar 2016 `#309 <https://github.com/enthought/mayavi/pull/309>`_ (PR)
   - Update to use new VTK pipeline where possible.  This fixes a number of
     issues with the pipeline was not updating properly.

09 Mar 2016 `#306 <https://github.com/enthought/mayavi/pull/306>`_ (kitchoi)
   - Fix issue with ``mlab.move``

01 Apr 2016 `#304 <https://github.com/enthought/mayavi/pull/304>`_ (kitchoi)
   - Fix issue `#302 <https://github.com/enthought/mayavi/issues/302>`_,
     segfault when savefig is called multiple times.

09 Mar 2016 `#303 <https://github.com/enthought/mayavi/pull/303>`_ (kitchoi)
   - Fix get_engine behavior when backend is changed again.


Contributions from itziakos, stefanoborini and kitchoi are funded and supported
by the `SimPhoNy <http://www.simphony-project.eu/>`_ project, an EU-project
funded by the 7th Framework Programme (Project number 604005) under the
call NMP.2013.1.4-1.


Mayavi 4.4.4
============

Enhancements
------------

21 Jan 2016 (PR)
   - Add experimental Python3 support

Fixes
-----

27 Feb 2016 (PR)
   - Ensure the cut plane is updated when the plane is changed in the GUI

27 Feb 2016 (kitchoi)
   - Use off screen engine when mlab's offscreen option is enabled

26 Feb 2016 (mabl)
   - Cast the window id to an int in the render window interactor

27 Feb 2016 (kitchoi)
   - Update installation guide

27 Feb 2016 (PR)
   - Update docs to use Qt instead of wx

24 Feb 2016 (kitchoi)
   - Update documentation setup

24 Feb 2016 (PR)
   - Allow TVTK to be used without UI/X server

23 Feb 2016 (kitchoi)
   - Update documentation links

17 Feb 2016 (kitchoi)
   - Make sure the array shape and size match

17 Feb 2016 (IT)
   - Ensure __file__ attribute points to the correct path when running a script
     from Mayavi2

09 Feb 2016 (jonathanrocher)
   - Avoid multiple identical keys in keyPressEvent. This is observed on slow
     machines

22 Jan 2016 (IT)
   - Do not use get-pip or wheel to upgrade pip on appveyor

10 Sep 2015 (alexendreleroux)
   - Fix broken link in docs left hand side menu bar

Mayavi 4.4.3
============

Enhancements
------------

01 Jul 2015 (IT)
    - Update the readme fixing dead links

01 Jul 2015 (IT)
    - Use new Travis CI containers for faster builds

22 Jun 2015 (IT)
    - Add CI tests on Windows using Appveyor

Fixes
-----

11 Aug 2015 (DS, IT, PR)
    - Remove reference cycles from various objects to fix memory leaks. Add
      unit test that provides an API to test garbage collection.

10 Aug 2015 (PR)
    - Fix the LUT manager to select the correct lut mode for QT backend

04 Aug 2015 (IT)
    - Use the python-wxtool package to speed up Travis CI build

04 Aug 2015 (DS)
    - Fix TVTK wrapper to allow look up with long keys for Points

23 Jul 2015 (DS)
    - Fix glyph to handle the masking of input points

22 Jul 2015 (IT)
    - Update the docs with known bugs, issues list and describe the PR
      workflow on github for development and documentation.

20 Jul 2015 (DS)
    - Fix TVTK wrapper to update number of cells when a cell is inserted in a
      VTK cell array

15 Jul 2015 (DS)
    - Fix VKTFileReader to update output when using standalone

24 Jun 2015 (PR)
    - Fix the sdist command

Mayavi 4.4.2
============

Enhancements
------------

11 Jun 2015 (DS)
    - Upgrade the VTK parser to add support for VTK 6.2.

Mayavi 4.4.1
============

Fixes
-----

23 Apr 2015 (DS)
    - Fix trackpad scrolling to zoom in/out smoothly on OS X.

Mayavi 4.4.0
============

Enhancements
------------

22 Dec 2014 (DS)
    - Add function to set data at input port, add stanford (bunny,
      dragon, lucy) examples, and use new volume mapper for new pipeline.

24 Jan 2014 (DS)
    - Upgrade to VTK 6.0 with VTK's new pipeline.

Fixes
-----

22 Dec 2014 (DS)
    - Support dynamic dimensions in array source.

03 Dec 2014 (paulmueller)
    - Fix MRI brain data URL.

13 Nov 2014 (DS)
    - More fixes for connection topology, information request and tube filter
      after upgrading to new pipeline.

24 Sep 2014 (pberkes)
    - Handle the non-Latin-1 keypresses.

23 Sep 2014 (rkern)
    - Prevent ndarray comparisions with None.

17 Jul 2014 (mdickinson)
    - Fix the trait error raised when the threshold range is updated.

24 May 2014 (markkness)
    - Update installation documentation links.

21 Apr 2014 (PR)
    - Fix integration tests after upgrade to VTK's new pipeline.

Mayavi 4.3.1
=============

Enhancements
------------

20 Jan 2014 (PR)
    - New example `mlab.test_mesh_mash_custom_colors` illustrating masking
      and a custom color map.

12 Jan 2014 (PR)
    - Enabled Travis-CI for the repo.

17 Dec 2013 (dmsurti)
    - Upgrade to VTK 5.10.1 with VTK's old pipeline. This upgrade does not yet
      make use of VTK's new pipeline.

07 Aug 2013 (pratikmallya)
    - Added interactive superquadrics example. Thanks to Pratik for contributing
      this example.

03 Jun 2013 (PR)
    - Refactor the animation component so that corresponding examples
      display animations.

Fixes
------

27 Jan 2014 (PR)
    - Many fixes to the test suite so the unit tests and integration tests
      all pass on OS X, Linux and Windows 32 and 64 bit with VTK 5.6.

08 Jan 2014 (PR)
    - tvtk_doc: Fix search when user enters a search string.

09 Jan 2014 (mindw)
    - Fix creation of scripts on win32 using gui_scripts. Thanks to Gabi Davar
      for this fix.

23 Dec 2013 (jenshnielsen)
    - Fix imshow by handling TraitError. Thanks to Jens Nielsen for this fix.

05 Apr 2013 (mindw)
    - Fix class browser when VTK is built with QT/SIP support. Thanks to Gabi
      Davar for this fix.

05 Apr 2013 (mluessi)
    - Fix wxpython 2.9 compatibility. Thanks to Martin Luessi for this fix.

19 Aug 2013 (senganal)
    - Fix MGlyphSource when assigning multi dimensional arrays to individual
      components of vector data. Thanks to Senganal for this fix.
    - Fix inconsistent handling of scalars. Thanks to Senganal for this fix.

10 Jun 2013 (PR)
    - Fix to use front buffer when off screen is False.


Mayavi 4.3.0
=============

Enhancements
------------

30 Oct 2012 (PR)
    - NEW: Adding a Qt version of the gradient editor. With this, all of
      Mayavi's UI should be usable on Qt.

Fixes
------

11 Mar 2013 (Aestrivex)
    - Fixed bug with incorrectly tiled snapshots while using savefig.

30 Oct 2012 (PR)
    - BUG: Qt: fix crashing full-screen-mode.  Fixed segfault when you click on
      full-screen and press escape/q/e.


Mayavi 4.2.1
=============

Enhancements
------------

9 August 2012 (GV)
  - ENH: Add null engine to mlab.pipeline.open.


Mayavi 3.4.0 (Oct 15, 2010)
===========================

Enhancements
------------

22 July 2010 (GV)
  - ENH: Add error management for extents in mlab: some module cannot be
    scaled [25683].

16 July 2010 (GV)

  - ENH: Enable LUT defined by tables to have their number of colors
    adjusted [25663].

Fixes
------


2 August 2010 (GV)
  - BUG: Fix a segfault when updating lines on a MLineSource using 'reset'
    and reducing the number of points [25700].

1 August 2010 (GV)
  - BUG: Fix updating scalar scatters using mlab_source.set: a race condition
    under Qt prevented the scalar range to be updated in time [25699].

25 July 2010 (GV)
  - BUG: Fix corner cases in the pipeline browser: objects for which the
    number of inputs is misreported, and iterable objects to do not contain
    TVTKBase entries [25685,25686].

14 July 2010 (GV)
  - BUG: Fix a bug in the poll_file example. Thanks to Jonathan Guyer for
    pointing out the solution [25660].

Mayavi 3.3.2 (May 25, 2010)
===============================

Enhancements
------------

DOCs: many docs and example improvements (GV).

13 April 2010 (GV)
  - API: Enforces wx >= 2.8 [25465,25471,25529]

11 April 2010 (GV)
  - ENH: Add figure management to mlab.roll [25464].

6 March 2010 (GV)
  - MISC: Change the default in iso_surface to compute normals, as with
    recent VTK versions colors look ugly when normals are not computed
    [25400].

Fixes
------

17 May 2010 (PR)
  - BUG: Fixing wrapping for VTK-5.6 and above where one of the string
    traits default to a value with a special character like "\n" "\r"
    [25546].

17 April 2010 (GV)
  - BUG: Fix integer casting in magnification for mlab.savefig [25483]

5 April 2010 (GV)
  - BUG: A slight modification to enable inserting graph objects
    in the Mayavi pipeline: the polydata created by the GraphToPolyData
    filter had some 'None' arrays in their point_data [25434].

3 April 2010 (GV)
  - BUG: Make the 'use_lookup_table' traits of the image_plane_widget
    work. [25430]


Mayavi 3.3.1 (Feb 24, 2010)
===========================

Enhancements
------------

20 Dec, 2009 (GV):
  - ENH: Merge in Scott Wart's patch to add an 'ImageChangeInformation
    filter to ArraySource, with additional work to get the tests to pass
    [25036], [25043]

14 Dec, 2009 (GV)
  - ENH: Add helper functions to interact with object via callbacks by
    clicking on them. The core function is the scene.on_mouse_pick, that is
    demoed in the new example 'on_mouse_pick' [25016], [25019]

13 Dec, 2009 (GV):
  - ENH: Make array_handler more robust to buffer protocole [25013]
  - ENH: Add support for assigning numbers to MGlyphSource x, y, z, and u, v,
    w [25015]

27 Nov 2009 (GV):
  - ENH: Add an auto mode for mlab.view, for distance and focal point
    [24971]

26 Nov, 2009 (GV):
  - ENH: Add a probe_data to retrieve data from Mayavi or VTK objects [24966]

25 Nov, 2009 (GV):
  - ENH: Usability: change the label of the '*.*' extension in th
    decorated scene save snapshot dialog [24963]

12 Oct, 2009 (GV):
  - ENH: Add script recording to the widget position for the DataSetClipper
    filter [24826]

17 Sep, 2009 (PR):
  - ENH: Making the widgets recordable [24738]

02 Sept 2009 (GV):
  - ENH: Add a new glyph source: a cross, that can be used as a cursor, or a
    axes [24678]

02 Sep, 2009 (GV):
  - ENH: Add a figure argument to mlab.view and try to lift the figure on
    screenshot [24676]
  - DOC: Add a detailed example of using 'UserDefined' contributed b
    Emmanuelle Gouillart [24677]

20 Aug, 2009 (PR):
  - ENH: Don't persist mlab_source [24567]

14 Aug, 2009 (GV):
  - ENH: Stop gap solution to limit the cost of auto-scaling the glyph
    size with large arrays in barchart, when the positionning is
    implicite, and thus distance calculation is pointless [24526]
  - ENH: Do not update the rendering of the scene when using mlab
    helper functions that build one object after another [24529]
  - ENH: Add an argument to barchart to avoid expensive scaling computation
    [24531]
  - ENH: Make the scalars argument of mlab.pipeline.vector_field work with
    lists too [24532]

13 Aug, 2009 (GV):
  - ENH: Force an update of the data when using the set_active_attribute
    filter, so that the names of all defined arrays are displayed [24464]
    [24466], [24520], [24521], [24520]

04 Aug, 2009 (GV)
  - ENH: Add a screenshot function to mlab for easy capture of the pixmap to
    [24445]
  - ENH: Add a patch contributed by Chris Colbert for control of the array
    type in mlab.screenshot (rgb vs rgba) [24453]

03 Aug, 2009 (GV):
  - MISC: Fix long-standing usability complain: OK button on adder nodes
    not creating object [24443]

03 Aug, 2009 (PR):
  - ENH: Adding to/from_array to the Matrix4x4 class for convenience
    [24437]
  - ENH: Thanks to a suggestion from Gary Ruben, mlab.plot3d now uses
    tvtk.Stripper in the pipeline to produce smooth tubes [24438] [24442]
    [24439]

01 Aug, 2009 (GV):
  - DOC: Merge in Ondrej's more precise instructions on installing SVN on an
    already-installed system [24428]

15 Jul, 2009 (GV):
   - ENH: Open the possibility to have image plane widget working with
     RGBA data [24169]

10 Jul, 2009 (GV):
  - ENH: Allows for use of lists as a scalar argument in mlab function
    [24094]

09 Jul 2009 (PR):
  - ENH/API: Checking in patch from Erik Tollerud which adds a `move`, `yaw
    and `pitch` to the mlab camera.  Many thanks to Erik for this patch
    [24083], [24084]

08 Jul, 2009 (GV):
  - ENH: Capture any errors while building docs and fail gracefully
    during the build [24067]

08 Jul, 2009 (GV):
  - ENH: Try to force the use of wx2.8, or else do not display the logger
    [24064], [24060]

07 Jul, 2009 (GV):
  - ENH: Add a button and a menu entry to display the VTK documentation
    browser [25058]

22 Jul, 2009 (Dave Peterson):
  - Updated all __init__.py files with modulefinder code so that
    py2app/py2exe can correctly determine what to include when packaging a
    distribution.  This is necessary due to the use of namespace packages
    [24339]


Fixes
-----

21 Feb, 2010 (GV)
   - BUG: Make the threshold filter better behaved when there are nans in
     the data [25280]
   - BUG: Remove callbacks on OrientationAxis that where triggering
     useless redraws [25279]

15 Feb, 2010 (PR):
  - BUG: Fix issue when an automatically generated trait name was actually
    Python keyword. In these cases the trait name is simply appended with a
    underscore (_). This should hopefully fix problems with building TVTK
    with VTK from CVS [25236]

12 Feb, 2010 (Scott Warts):
  - Reset the current scene if it is removed [ 25219]

08 Jan, 2010 (GV):
  - BUG: Radius and length of a cylinder had upper bounds to 100, where
    they should really be confined only to positive numbers. Fix with
    kludge. Thanks to Michele Mattioni for pointing out the bug, and
    providing the patch [25097]

20 Dec, 2009 (GV):
  - BUG: Correct bug with visibility of OrientationAxes reported by Uche
    Mennel [25037]
  - BUG: Patch by Varun Hiremath to make build docs more robust [25039]
  - BUG: Fix scalarbar positionning for VTK >= 5. [25040]
  - BUG: Avoid a segfault when enabling the OrientationAxes without an
    interactor [25044]
  - MISC: Disable the use of IPython by default, there are right now too many
    bugs with it [25041]

14 Dec, 2009 (GV):
  - BUG: Fix test on pick dispatcher [25020]
  - BUG: Fix a bug in tvtk.py, in the loading of tvtk classes generated code
    when the path is not in the sys.path
    Thank you to Ram Rachum for finding this problem, and the fix [25021]

26 Nov, 2009 (GV):
  - BUG: Add forgotten file. Thanks to Darren Dale for reporting [24967]
  - BUG: Fix mlab.pipeline.get_vtk_src for VTK dataset [24968]

25 Nov, 2009 (GV):
  - BUG: Fix a bug in barchart [24962]

18 Nov, 2009 (Scott Warts):
  - Don't reset the zoom level if there are volumes or actors. Before we
    were just checking for actors [24932]

04 Nov, 2009 (GV):
  - BUG: mlab.clf() was renabling rendering on figures, had it been
    disabled [24874]

22 Oct, 2009 (Scott Warts):
  - BUG: Fixed memory leak. Switched to using tvtk.messenger when adding
    observers to keep from creating uncollectable cycles [24856], [24857]

14 Sep, 2009 (GV):
  - BUG: Fix trivial bug when size in savefig was not specified, and
    magnification was set to auto [24733]

19 Aug, 2009 (GV):
  - BUG: Fix 'feature' of mlab.colorbar which would show up on objects with
    scalar representation not enabled [24559]

19 Aug, 2009 (PR):
  - BUG: Fixing some of the issues with colorbar and VTK versions greater
    than 5.2 [24558]

18 Aug, 2009 (GV):
  - BUG: The figure magnification was not working correctly. Fix [24569]
  - BUG: Fix a traceback in mlab.show_pipeline if no scene was open [24553]

17 Aug, 2009 (PR):
  - BUG: TVTK was not correctly wrapping newer versions of VTK
    Specifically the vtkArray class was causing a traceback.  This patch
    appears to fix the problem.  Thanks to Kyle Mandli for helping with
    debugging this issue and testing the fix

14 Aug, 2009 (GV):
  - BUG: Fix a bug when reseting the MlabTriangularMeshSource: when growing
    the number of points, triangles were created before the corresponding
    points. Thanks to Ondrej Certik for reporting this one

08 Aug, 2009 (GV):
  - BUG: Fix a bug for with the notebook in wx example for which objects were
    not added to the right scene [24492]

07 Aug, 2009 (Scott Warts):
  - Added two more exceptions to state methods from ImageReslice:
    SetOutputOriginToDefault and SetOutputExtentToDefault [24480]

06 Aug, 2009 (PR):
  - BUG: vtkImageReslice's SetOutputSpacingToDefault does not make
    OutputSpacing a state method.  Thanks to Scott Swarts for pointing this
    out [24476]

01 Aug, 2009 (Robert Kern):
    - BUG: With a vtkWin32OpenGLRenderWindow, set the parent widget info
      before resizing in order to avoid an offset bug [24427]

23 Jul, 2009 (Evan Patterson):
  -  BUG: Replacing deprecated calls to wx.Yield() [24379]


Mayavi 3.3.0 (July 15, 2009)
============================

Enhancements
------------

06 Jul, 2009 (PR):
  - ENH/API: No longer save to a file (with a popup when a user unchecks the
    record icon).  Also added `start_recording` and `stop_recording`
    functions to mlab to make it easier to do this via scripts [24048]

08 Jul, 2009 (GV):
  - ENH: Make the MlabSceneModel manage the mlab current scene so that in
    plots to the embedded scene, but does not upset the current
    mlab figure [24040], [24065]

05 Jul 2009 (GV):
  - ENH: Add the possibility to specify figures to mlab.figure by instance
    rather than name [24039]
  - ENH: Add an example of using multiple mlab scene models [24041]
  - ENH: Add a figure keyword argument to mlab.pipeline factories to
    control which figure objects are added on [2403]

02 July, 2009 (PR):
  - ENH: The record icon on the engine view is smarter now and will
    automatically be checked on and off if the engine's recorder trait in
    set.  This paves the way for a convenient mlab one liner to start
    recording [24025]

01 Jul, 2009 (PR):
  - NEW: Adding a new filter that clips an input dataset.  Also added an
    `ImplicitWidgets` component that abstracts a box, plane, sphere and
    implicit plane widget into one reusable component.  An  initial patch was
    contributed by Suyog and them modified by PR.  Many thanks to Suyog for
    this patch [24017]

01 Jul, 2009 (GV):
  - ENH: Add an mlab.close function to close figures controled by mlab
    [24006]

30 Jun, 2009 (PR):
  - ENH/API: Checking in improved patch sent by Suyog along with fixes from me.
    This adds a can_read_test metadata attribute for sources which can be
    optionally specified, the function should return True if the reader can
    read a given file.  The patch also adds a volume reader and a chaco
    reader and also supports the .xyz format reader provided in VTK.  A test
    for the new registry functionality is also added.  The API has only
    changed for the manner in which the registry is queried for a reader
    using the file itself rather than the file extension.  Many thanks to
    Suyog for this work [24002]

29 Jun, 2009 (GV):
  - ENH: Add an option to show_engine to show the rich view [23981]

14 Jun, 2009 (GV):
  - BUG: mlab.set_engine was not registering engines, causing testing to
    be difficult [23819]
  - ENH: expose text3d in mlab [23820]
  - ENH/TEST: rewamp the mlab testing infrastructure [23822]

13 Jun, 2009 (GV):
  - ENH: Adapt mlab.savefig code to make it easier to save figures with size
    larger than window size [23813]
  - ENH: Add a text3d module, for displaying text located in the 3D scene
    scaling and hiding as the other 3D actors [23809], [23810].
  - ENH: Add a helper function to mlab to syncronize cameras on two
    scenes [23814]

10 Jun, 2009 (PR):
  - API: The name of the scene created on the mayavi2 app now defaults to
    "Mayavi Scene %d" rather than "TVTK Scene %d".  This is to make this
    consistent with what `mlab.figure()` does and to avoid user confusion
    [23787]

2 Jun, 2009 (PR):
  - ENH: Ensuring that the scene editor's name is synced with the scene'
    name.  Also making the scene itself "renamable" [23710]

29 May, 2009 (PR):
  - ENH: Also pickle the name of the scene -- it shouldn't hurt [23691]

18 May, 2009 (GV):
  - ENH: cleaner exception capture for sensible error message [23660]

10 May, 2009 (GV):
  - ENH: Use pickle rather than numpy npz for lookup table [23618]
    [23619]
  - API: Add PipelineBase to mayavi.core.api as it is needed for
    the interactive example [23617]

9 May, 2009 (PR):
  - ENH/API: Adding to the API of the lut manager with a show_legend boo
    which is an alias for show_scalar_bar.  This makes the UI a littl
    clearer [23608]
  - ENH: Adding ID's to the various pop-up editors for the lut manager s
    their sizing etc. is persisted [23609]
  - ENH/API: Exposing the scalar_bar_widget's representation in the UI an
    API and recording it so changes to the scalar bar's position ar
    recorded and editable on the UI [23610]


20 Apr, 2009 (GV):
ENH [23545]:
     - Add an example gallery to the documentation

     - Rewamp the documentation-generation code, and its packaging. Th
       generation code was made more robust, and as a result n
       generated test files are checked in svn. The images for th
       mlab documentation and the mlab examples are generated by th
       render_images.py script
     - Space has been optimized by removing duplicated artwork an
       moving outside of the source distribution files no
       required for distribution

19 Apr, 2009 (GV)
  - ENH: Use numpy's npz format for storing LUT information. This saves ~1Mo
    from the source and binary distributions[23544]

11 Apr, 2009 (GV):
  - ENH/API: add an API module to core, to give a central place for
    important core import [23520]


Fixes
-----

15 Jul, 2009 (PR):
  - BUG: Fix what I think is a long standing bug.  You couldn't use the
    envisage backend with mlab because of a problem with envisage'.
    workbench application.  I've worked around the problem in mayavi'
    workbench subclass and added a test to ensure that this is now fixed
    This basically adds a new trait to the Mayavi app and the mayavi
    workbench application called `start_gui_event_loop` that is disabled
    when used from mlab [24171]

6 Jul, 2009 (Dave Martin):
  - BUG: If the scene being closed has None for scene.scene, call
    registry.find_scene_engine(scene) instead of "scene.scene" [24052]
    [24055]

05 Jul, 2009 (GV):
  - BUG: small fix for successive builds of the tvtk code generation, by
    Rakesh Pandit [24038]
  - BUG: Do not create application directories on import of mayavi
    preferences. [24036]

29 Jun, 2009 (GV):
  - BUG: Make sure that the vertical vector source used for barchart is
    well-behaved with regards to mlab_source.update [23983]

28 Jun, 2009 (PR):
  - BUG: Mlab's barchart uses the scale_by_vector_components which was not
    exposed by the glyph component leading to update problems reported by
    Christian Vollmer.  This is now fixed along with a simple test case.
    There are deeper problems with barchart that do need attention though -
    if a user changes the data inplace and calls the mlab_source.update()
    nothing updates correctly since the data is really copied over to the
    vector components.  This can be fixed with a callback and will be done
    later. [23980]

25 Jun, 2009 (PR):
  - BUG: Was checking for attribute in editor assuming they were all scene
    editors which is clearly wrong.  This bug fixes problems with using
    mayavi and a text editor say [23933]

2, Jun 2009 (PR):
  - BUG: With recent versions of VTK when a VTK array is exported to a numpy
    array, the numpy array is already a view so resetting the VTK array back
    to the numpy array for some reason triggers a segfault.  This is now
    fixed [23711]
  - BUG: The Engine's open method did not work with a null engine.  Tested
    and fixed [23713]

30 May, 2009 (PR):
  - [TVTK] BUG: Working around problem with parser for
    vtkRenderedGraphRepresentation which has non-standard arguments for some
    of its SetIvarToState methods [23696]

26 Lay, 2009 (GV):
  - BUG: Fix scaling bug for surf with warp_scale='auto'. Thanks to Jakob
    Rohrhirsch for reporting it [23682]

6 May, 2009 (PR):
  - BUG: The implicit plane widget was not recordable [23595]
  - BUG: [mlab] mlab.pipeline.contour_grid_plane was broken [23596]

27 Apr, 2009 (GV):
  - API: add an API module for core.ui [23562]
  - DOC: Put up to date information on the engine [23560]

23 Apr, 2009 (GV):
  - DOC: Add an example to show how you can have different engines in an
    application [23558]

13 April, 2009 (PR):
  - BUG: The trailing '|' in the wildcard breaks the file dialog's filterin
    for user defined readers.  Thanks to B. P. Thrane for reporting the bug

27 March, 2009 (GV):
  - BUG: Fixed bug with importing customization contributions.  Added a test
    case for this.  Thanks to Mario Ceresa for reporting the bug [23438]

23 March, 2009 (GV):
  - BUG: Fix TVTK possible build failure, reported by Andrew Straw
    https://bugs.launchpad.net/bugs/34693 [23371]



20 March, 2009 (PR):
  - TEST/BUG: Adding a new test for the `tvtk.util.ctf` utility
    functions.  Also fixed a bug that affects VTK-5.2 and above where the
    range of the CTF must be set [23267]
  - BUG/CLEAN: Fixing a 5.2 specific bug in the volume module mlab function
    Also cleaned up the mlab code for this a little [23268]


Mayavi 3.2.0 (March 23, 2009)
=============================

A log of significant changes made to the package especially API changes.
This is only partial and only covers the developments after the 2.x
series.

17, 18 March, 2009 (PR):
    - NEW: A simple example to show how one can use TVTK's visual module
      with mlab. [23250]
    - BUG: The size trait was being overridden and was different from
      the parent causing a bug with resizing the viewer. [23243]

15 March, 2009 (GV):
    - ENH: Add a volume factory to mlab that knows how to set color, vmin and
      vmax for the volume module [23221].

14 March, 2009 (PR):
    - API/TEST: Added a new testing entry point: 'mayavi -t' now runs
      tests in separate process, for isolation.  Added
      ``mayavi.api.test`` to allow for simple testing from the
      interpreter [23195]...[23200], [23213], [23214], [23223].
    - BUG: The volume module was directly importing the
      wx_gradient_editor leading to an import error when no wxPython is
      available. This has been tested and fixed. Thanks to Christoph
      Bohme for reporting this issue. [23191]

14 March, 2009 (GV):
    - BUG: [mlab]: fix positioning for titles [23194], and opacity for titles
      and text [23193].
    - ENH: Add the mlab_source attribute on all objects created by mlab,
      when possible [23201], [23209].
    - ENH: Add a message to help the first-time user, using the new banner
      feature of the IPython shell view [23208].

13 March, 2009 (PR):
    - NEW/API: Adding a powerful TCP/UDP server for scripting mayavi via
      the network. This is available in
      ``mayavi.tools.server`` and is fully documented. It uses
      twisted and currently only works with wxPython. It is completely
      insecure though since it allows a remote user to do practically
      *anything* from mayavi.

13 March, 2009 (GV)
    - API: rename mlab.orientationaxes to mlab.orientation_axes [23184]

11 March, 2009 (GV)
    - API: Expose 'traverse' in mlab.pipeline [23181]

10 March, 2009 (PR)
    - BUG: Fixed a subtle bug that affected the ImagePlaneWidget. This
      happened because the scalar_type of the output data from the
      VTKDataSource was not being set correctly. Getting the range of any
      input scalars also seems to silence warnings from VTK. This should
      hopefully fix issues with the use of the IPW with multiple scalars.
      I've added two tests for this, one is an integration test since those
      errors really show up only when the display is used. The other is a
      traditional unittest. [23166]

08 March, 2009 (GV)
    - ENH: Raises an error when the user passes to mlab an array with
      infinite values [23150]

07 March, 2009 (PR)
    - BUG: A subtle bug with a really gross error in the GridPlane
      component, I was using the extents when I should really have been
      looking at the dimensions. The extract grid filter was also not
      flushing the data changes downstream leading to errors that are also
      fixed now. These errors would manifest when you use an ExtractGrid to
      select a VOI or a sample rate and then used a grid plane down stream
      causing very wierd and incorrect rendering of the grid plane (thanks to
      conflation of extents and dimensions). This bug was seen at NAL for a
      while and also reported by Fred with a nice CME. The CME was then
      converted to a nice unittest by Suyog and then improved. Thanks to
      them all. [23146]

28 February, 2009 (PR)
    - BUG: Fixed some issues reported by Ondrej Certik regarding the use
      Of mlab.options.offscreen, mlab.options.backend = 'test', removed cruft
      from earlier 'null' backend, fixed bug with incorrect imports,
      add_dataset set no longer adds one new null engine each time figure=False
      is passed, added test case for the options.backend test. [23088]

23 February, 2009 (PR)
    - ENH: Updating show so that it supports a stop keyword argument that
      pops up a little UI that lets the user stop the mainloop
      temporarily and continue using Python [23049]

21 February, 2009 (GV)
    - ENH: Add a richer view for the pipeline to the MayaviScene [23035]
    - ENH: Add safegards to capture wrong triangle array sizes in
      mlab.triangular_mesh_source. [23037]

21 February, 2009 (PR)
    - ENH: Making the transform data filter recordable. [23033]
    - NEW: A simple animator class to make it relatively to create
      animations. [23036] [23039]

20 February, 2009 (PR)
    - ENH: Added readers for various image file formats, poly data
      readers and unstructured grid readers. These include DICOM,
      GESigna, DEM, MetaImage (mha,mhd) MINC, AVSucd, GAMBIT, Exodus, STL,
      Points, Particle, PLY, PDB, SLC, OBJ, Facet and BYU files. Also added
      several tests for most of this functionality along with small data files.
      These are additions from PR's project staff, Suyog Jain and Sreekanth
      Ravindran.  [23013]
    - ENH: We now change the default so the ImagePlaneWidget does not
      control the LUT. Also made the IPW recordable. [23011]

18 February, 2009 (GV)
    - ENH: Add a preference manager view for editing preferences outside
      envisage [22998]

08 February, 2009 (GV)
    - ENH: Center the glyphs created by barchart on the data points, as
      mentioned by Rauli Ruohonen [22906]

29 January, 2009 (GV)
    - ENH: Make it possible to avoid redraws with mlab by using
      `mlab.gcf().scene.disable_render = True` [22869]

28 January, 2009 (PR and GV)
    - ENH: Make the mlab.pipeline.user_defined factory function usable to
      add arbitrary filters on the pipeline. [22867], [22865]

11 January, 2009 (GV)
    - ENH: Make mlab.imshow use the ImageActor. Enhance the ImageActor to
      map scalars to colors when needed. [22816]



Mayavi 3.1.0
============

3 December, 2008 (PR)
    - BUG: Fixing bugs with persistence of VTKDataSource objects
      wrapping a structured grid in VTK-5.2.  This resulted in hard to
      debug test errors.  [22624]

1 December, 2008 (GV):
    - API: Promote the TestEngine to a first-class citizen NullEngine and
           make mlab use it when a source has a keyword argument
           "figure=False". [22594]

30 November, 2008 (PR)
    - NEW: New sources called BuiltinSurface and BuiltinImage that let
      users create simple polygonal data and images using basic VTK
      sources.  Thanks to Suyog Jain for this code. [22586], [22597].

27 November, 2008 (GV):
    - ENH: Add control of the seed size and resolution to
           mlab.pipeline_basene.streamline [22573].
    - DOC: Documentation work, especially in the scripting parts of the
           docs. [22572], [22561], [22560], [22546], [22545]

26 November, 2008 (GV):
    - ENH: Add keyword arguments to the cutplanes in mlab.pipeline. [22567]
           Also add masking to glyph-based mlab.pipeline factories [22568]

19 November, 2008 (GV):
    - UI: Rename 'Modules' to 'Colors and legends' [22512]
    - API: Change defaults [22513]:
        - CellToPointData and PointToCellData filters to pass the existing
          dataset.
        - The ouline of the implicite plane is no longer draggable by
          default.

15-16 November, 2008 (PR)
    - ENH/API: Exposing the glyph source choices via a dictionary rather
      than having the user remember the index in a list. [22497]
    - ENH: Adding a button to the LUT UI so the LUT editor can be
      launched from the UI. [22498]
    - DOC: Updating advanced scripting chapter. [22495].

13 November, 2008 (GV)
    - ENH: [mlab]  Add keyword arguments to colobars to control label
      number and format, as well as colors number. [22489]

10 November, 2008 (PR)
    - TEST: Adding 43 new mayavi tests.  These are based on the
      integration tests but don't pop up a user interface.   Thanks to
      Suyog Jain for doing bulk of the work. [22465]

27 October, 2008 (GV)
    - ENH: [mlab] If a module or filter is added to the pipeline using
      the mlab.pipeline functions, the source on which it is added
      onto is automatically added to the scene if not alread present. It
      is also automatically converted from a tvtk dataset to a mayavi
      source, if needed. [22375], [22377]
    - ENH: [mlab] Make mlab.axes and mlab.outline use the extents of the
      current object when none specified explicitely. [22372]

24-27 October, 2008 (PR)
    - NEW: Adding an ImageChangeInformation filter to let users change
      the origin, spacing and extents of input image data, [22351].
    - API: Adding a `set_viewer` function to
      `tvtk.tools.visual` so one may specify a viewer to
      render into.  This lets us use visual with a mayavi scene. [22363]
    - BUG: Fix a major bug with TVTK when VTK is built with 64 bit ids
      (VTK_USE_64BIT_IDS is on).  The examples and tests should all run
      in this case now. [22365]
    - ENH: [mlab] Added an `mlab.view` method that actually works
      [22366].

19 October, 2008 (GV)
    - ENH: mlab.text can now take 3D positioning [22331].

17-20 October, 2008 (PR)
    - ENH: Modified TVTK and Mayavi UI editors so that text entry boxes
      are only set when the user hits <enter> or <tab> rather than on
      each keystroke.  [22321], [22323]
    - ENH/BUG/WARN: Fixed warnings at TVTK build time, fixed bugs with
      ImageData's scalar_type trait. [22320], [22321], [22325].
    - NEW/API: Adding preference option to ease task of loading contrib
      packages (via a pkg/user_mayavi.py) in mayavi.  Also added a
      contrib finder that trawls sys.path to find contributions.  This
      can be set from the preferences UI. [22324], [22326], [22327].
    - BUG: Fixing problems with the gradient_editor and newer VTK
      versions.  This is required for the Volume module to work
      correctly. [22329], [22341]

13 October, 2008 (GV):
    - ENH: Bind the 'explore' function in the python shell [22307]
    - ENH: mlab: axes and outline now find the extents from the objects
           they are given, if any. [22305]

12 October, 2008 (GV):
    - API: mlab: Add a barchart function, with the corresponding pipeline
      source function. [22286]

11 October, 2008 (PR):
    - ENH/API: Improving texture map support, you can now generate the
      texture coords on an arbitrary actor.  This adds to the API of the
      actor component.  [22283]
    - API: Adding a `mayavi.preferences.bindings` module that
      abstracts out setting of preferences for common objects.
      Currently it exposes a `set_scene_preferences` so the
      non-envisage and off screen scenes have the right preferences.
      See [22280] and [22295].
    - REFACTOR/API: The script recording code is now in
      `apptools.scripting`,  the `mayavi.core.recorder` was
      only a temporary solution. See [22277] and [22279].

10 October, 2008 (GV):
    - API: mlab: Expose pipeline.set_extent (former private function
      tools._set_extent) [22251]

9 October, 2008 (GV):
    - ENH: Use the IPython shell plugin only if the ipython, envisage and
      pyface versions are recent-enough.
      Mayavi now uses an ipython widget instead of the pyshell one if you
      have the right components installed, but should fall back to
      pyshell gracefully. [21678], [22245]

4 October, 2008 (PR):
    - TEST: Added a 'test' backend to mlab so you can run mlab tests
      without a display. Fixing core code so that all the unittests run
      when the ETS_TOOLKIT env var is set to 'null'. [22198]

30 September, 2008 (GV):
    - API: mlab: Expose pipeline.add_dataset (former private function
      tools._data) [22162].
    - API: The mlab source functions can now optionaly work without creating
      a figure (using figure=None) [22161].
    - API: The mlab source functions are more  robust to various
      input-argument shape (they accept lists, and 1D or 2D arrays when
      possible) [22161].

29 September, 2008 (GV):
    - NEW: Add a mlab.triangular_mesh function to create meshes with
      arbitrary triangular connectivity. Also add a corresponding
      triangular_mesh_source mlab source. [22155]
    - ENH: Make mlab.points3d and other mlab functions accept scalars as
      coordinnates, in addition to arrays. [22156]

12 September, 2008 (PR)
    - NEW: Create a separate OffScreenEngine for use to reduce code
      duplication.  This is also available as part of
      mayavi.api. [21880]
    - TEST: Creating a common.py that contains a TestEngine mayavi
      engine subclass for easily testing mayavi. [21881]

8-12 September, 2008 (PR)
    - NEW: Adding full support for script recording.  With this you can
      pretty much record all UI actions performed on the Mayavi UI (both
      standalone and application) to human-readable and runnable Python
      scripts.  It also serves as a nice learning tool since it shows
      the lines of code as the UI actions are performed.  Note that
      interacting with the camera is also recorded which is very
      convenient.  This has been implemented in a pretty general fashion
      (using TDD) so is reusable in other traits based applications
      also.   Major checkins [21722], [21728], [21776], [21812], [21865]
      [21878].




Mayavi 3.0.3
============

7 September, 2008 (PR):
    - ENH: The mayavi2 application now ([21713], [21714]) supports
      command line args like the following::

        mayavi2 -d ParametricSurface -s "function='dini'" -m Surface \
        -s "module_manager.scalar_lut_manager.show_scalar_bar = True" \
        -s "scene.isometric_view()" -s "scene.save('snapshot.png')"

6 September, 2008 (PR):
    - ENH/API: Cleaned up the mayavi.core.traits to remove
      buggy, and unused DRange and SimpleDRange traits. [21705]
    - BUG/TEST: Added tests for some of the MlabSource subclasses and
      fixed many bugs in the code. [21708]
    - TEST: Modified pipeline_base.py so mayavi objects may be started
      without creating a scene (and therefore a UI).  This allows us to
      create completely non-interactive tests.  [21709]
    - ENH: Adding X3D and POVRAY export options. [21711]

23 August, 2008 (PR):
    - ENH: Adding an offscreen option for mlab.  Now you can set
      mlab.options.offscreen = True. [21510]
    - ENH: Setting the window size to (1,1) if the window is offscreen,
      this prevents the window from showing up prominently -- it still
      does show up though. [21519]

21 August, 2008 (PR):
    - ENH: Adding the logger plugin to the mayavi2 app. [21487]



Mayavi 3.0.1 and 3.0.2
======================

16 August, 2008 (PR):
    - BUG: fixed various miscellaneous bugs including a testing
      error[21304], a long standing Mac bug with picking [21310], a
      segfault [21453] and a bug in tvtk when wrapping certain methods
      [21475].



Mayavi 3.0.0
============

15 August, 2008 (PR):
    - NEW: Adding a fully tested data set manager that lets users
      add/remove/modify attribute arrays to a tvtk dataset. This is
      fully tested and also does not influence any other code. [21300]

10 August, 2008 (PR):
    - ENH/API: [mlab] Added a `MlabSource` class to abstract out the
      data creation and modification into one object that may be
      modified.  This source object is injected in the form of a
      `mlab_source` trait on objects returned by any of the helper
      functions (`surf`, `plot3d` etc.) or the sources.  The user can
      use this to modify the data visualized without recreating the
      pipeline each time, making animations very easy and smooth.  There
      are several examples of the form `test_blah_anim` showing how this
      is done.  [21098], [21103].

27 July, 2008 (GV):
    - ENH: Add an option (on by default) to open the docs in a chromeless
      window when using firefox. [20451] [20450]
    - ENH: Add toolbar to the engine view [20447]
    - ENH: Selected item on the tree jumps to newly created objects
      [20454]
    - ENH: Add a button on the viewer using by mayavi in standalone to
      open up the engine view [20456] [20462]
    - ENH: Clean UI for adding sources/filters/modules (Adder nodes)
      [20461] [20460] [20458] [20452]
    - ENH: [mlab] add a resolution argument to glyphs [20465]
    - API: [mlab] API Breakage!
        Make mlab source names compatible with ETS standards:
        grid_source rather than gridsource [20466]
    - NEW: Add image_plane_widget to mlab.pipeline, with helpful keyword
        arguments.

23 July, 2008 (GV):
    - ENH: The mlab API can now take either engine or figure keyword
      arguments. This allows to avoid the use of the global sate set
      in the mlab engine. Mlab also now exposes a set_engine function.
      [20245]

23 July, 2008 (PR)
    - ENH/NEW: The mlab.pipeline sources, modules and filters now
      feature automatic source/filter/module generation functions from
      registry information.  This means mlab fully supports creating
      objects on the mayavi pipeline with easy one-liners. [20239]
    - API: The API has broken!  Sources, filters and modules that mirror
      an existing mayavi class now are named with underscores.  For
      example, isosurface has become iso_surface, extractedges becomes
      extract_edges etc.
    - NEW: Exposing the engine's open method to mlab so it is easy to
      open data files from mlab also.
    - ENH: Implemented an mlab.show decorator so one can write out a
      normal function for visualization which will work from ipython,
      standalone and mayavi completely seamlessly.

18, 19 July, 2008 (PR)
    - TEST/API: The mayavi tests are now split into integration and unit
      tests.  Unit tests go into mayavi/tests.  Integration
      tests are in integrationtests/mayavi. Major changes:

        - Removed most of the image based tests except one
          (test_streamline.py) for reference.
        - Modified the testing code so the standalone mode is the
          default.
        - Modified so nose picks up the integrationtests.  However,
          there are problems running the test via nosetests on Linux
          that need investigating.

    - ENH: Creating a new object on the pipeline via envisage or right
      click now sets the active selection to the created object so it is
      easy to edit.
    - API: Moving mayavi/view/engine_view.py to
      mayavi/core/ui. [20098]
    - API: Added method to engine (get_viewer) so it gets the viewer
      associated with a particular scene. [20101]

12 July, 2008 (PR):
    - ENH/API: Adding support for global (system wide) and local
      customizations via a site_mayavi.py and user_mayavi.py (in
      ~/.mayavi2/). This allows users to register new modules/filters
      and sources and also add any envisage plugins to the mayavi2 app
      easily. [19920]

9 July, 2008 (Judah, PR)
    - ENH: Adding the core code for an AdderNode that shows up on the
      engine view and lets a user easily create new
      scenes/sources/filters and modules.

8 July, 2008 (PR)
    - BUG: Ported various bug fixes from branches for ETS-2.8.0 release.
    - ENH/API: Added datatype, attribute type and attribute information
      to all pipeline objects (both at the object and metadata levels).
      This lets one query if an object will support a given input and
      what outputs it will provide (this can be changed dynamically
      too).  This allows us to create context sensitive menus. The
      traits UI menus for the right click is now modified to use this
      information. We therefore have context sensitive right click menus
      depending on the nature of the object we right click on. At this
      point we don't yet check for the attribute_type and attributes
      metadata information to enable/disable menus, this may be
      implemented later -- the framework makes this quite easy to do.
      [19512].
    - ENH: Envisage menus are now context sensitive [19520].

5 July, 2008 (PR):
    - ENH: One can create objects on the pipeline using right-clicks
      [19469].
    - ENH: All the envisage menus and actions for sources, filters and
      modules now are autogenerated from the metadata for these.
    - NEW/API: [19458] adds the following features:
        - A Registry (mayavi.core.registry.Registry) to
          register engines, sources, filters and modules. Source, filter
          and module metadata is registered and this can be used to do
          various things like generate menus, register data file
          extension handlers and whatnot. The metadata related classes
          are in mayavi.core.metadata.
        - This registry and metadata information is used to generate the
          envisage menus and actions.
        - The registry can be used by users to register new sources,
          readers, filters and modules.
        - A method to Engine and Script to easily open any supported
          data file.
        - Simplify the open file interface so it is just one menu item
          that supports different file extensions.
        - Changed the command line options for the mayavi2 application
          so you can open *any* supported data file format with the -d
          option.  This breaks backwards compatibility but makes it very
          easy to open supported data files -- even if the new ones are
          added by users.
        - Fixed the PLOT3DReader so it opens the q file using the xyz
          filenames basename.

29 June, 2008 (GV):
    - ENH: Updated Sphinx docs [19318].
    - ENH: New splash screen [19319].
    - ENH: mlab now works with envisage, including in "mayavi2 -x"
      [19321] [19323]


27 June, 2008 (Vibha):
    - API: Remove SimpleScene class [19285].
    - API: Moved tvtk-related examples from TraitsGUI to Mayavi [19191]
      [19197] [19231] [19280]

27 June, 2008 (GV):
    - BUG: tvtk: proper handling of non-float numpy arrays. Added test
      case [19297]

25 June, 2008 (GV):
   - ENH: Add autoscale to mlab.surf (scalez keyword argument) [19131]
   - ENH: mlab.usrf and mlab.mesh can now take x and y arguments with a
     more flexible shape [19114].

12 June, 2008 (PR):
    - ENH: Adding an offscreen option to the mayavi2 application.  This
      lets you run a normal mayavi Python script in offscreen mode
      without the full UI.  This is very convenient when you want to
      render a huge number of images from a visualization and don't want
      the UI to bother you or create a special script for the purpose.
      See [18951], [18955].

07, 08 June, 2008 (PR):
    - API: TVTK: Added two methods `setup_observers` and
      `teardown_observers` that let one turn on/off the observer for the
      ModifiedEvent fired on each VTK object that a TVTK object wraps to
      keep the traits updated.  Thus, if you call `teardown_observers`
      the traits will not be automatically updated if the wrapped VTK
      object is changed.  This can be manually updated by calling the
      `update_traits` method.  It is OK to call the
      setup/teardown_observers method as often as needed.  This is also
      tested.  See [18885].
    - API: TVTK: Removed the `__del__` method on all TVTK objects.  This
      should make it much nicer for proper garbage collection.  See
      [18886], [18887].

06 June, 2008 (PR):
    - TEST: Added a standalone mode to the tests so you can test without
      starting up the envisage app.  Envisage imports may be required
      however.  To use this run any test with the -s option. [18880]
    - TEST: Added a way to run the tests on one application launch
      instead of starting mayavi each time.  To use this execute run.py
      with the --one-shot command line option.  [18880] [18881].
    - TEST: The standalone offscreen mode now should work without a
      single Traits UI showing up with just a dummy blank window being
      used.  This demonstrates how mayavi scripts can work in completely
      different contexts.  [18881].


31 May, 2008 (PR):
    - PORT: Backported important additions to the 2.2.0 branch.
    - BUG: Added a test case for the hide/show functionality and fixed
      known bugs.
    - API: Adding elementary support for texturing an actor (if it has
      texture coords).  This was thanks to a patch from Chandrashekhar
      Kaushik. [18827]

30 May, 2008 (PR):
    - API: Adding closing, closed lifecycle events to the scene [18806].

27 May, 2008 (PR):
    - NEW: Adding a Labels module to label input data.  This is like
      MayaVi1's module and with this checkin all important mayavi1
      modules and filters are supported in mayavi2.  The only missing
      one is Locator which hardly anyone uses I think.  See [18801].

27 May, 2008 (PR):
    - NEW: Adding an ImageDataProbe filter which does the same thing
      that MayaVi-1.5's StructuredPointsProbe does. [18792]

25 May, 2008 (PR):
    - NEW: Adding CellDerivatives and Vorticity filters. [18785]

24 May, 2008 (PR):
    - NEW: Adding a tvtk_doc.py module that doubles as a
      TVTK Class/Filter/Source/Sink chooser and also as a documentation
      browser (with search!) like Mayavi1.x's vtk_doc.py.  tvtk_doc is
      also installed as a console script now. [18776]
    - NEW: Adding a UserDefined filter where the user can wrap around
      any TVTK filter. [18780]

23 May, 2008 (PR):
    - NEW: SetActiveAttribute filter that lets you select the active
      attribute.  This makes it very easy to find the contours of one
      scalar on the iso-contour of another.  The example
      contour_contour.py shows how this is done.  See [18774], [18775].

22 May, 2008 (PR):
    - NEW: Adding Contour and CutPlane filters that use the Wrapper
      filter and respective components.  This is very convenient.
    - Checked in modified patch from Chandrashekhar Kaushik (CSE IITB),
      which reimplements hide/show using a visible trait.


21 May, 2008 (PR):
    - TEST: Adding an @test decorator to make it easy to create a mayavi
      test case from a mayavi script.  While this is convenient, I still
      prefer to explicitly use the TestCase class since this makes the
      code compatible with the 2.2.0 branch.
    - The GenericModule is now tested.

20 May, 2008 (PR):
    - NEW: Adding a GenericModule to easily put together a bunch of
      Filters and Components.  Using this code it takes 30 simple
      lines of code for a ScalarCutPlane compared to the 300 complex
      ones we need for the current implementation!  This is because the
      module takes care of all the dirty work.
    - NEW: Adding Wrapper, Optional and Collection filters that make it
      easy to wrap around existing Components and Filters, make them
      optional and create collections of them very easily.  This gives
      us a great deal of reuse and makes it very easy to create new
      filters.

18 May, 2008 (PR):
    - ENH: Improved the PLOT3D reader and added a test for it.
    - Added a menu item to allow a user to run a Python script from the
      UI.
    - API: Added a close method to
      `pyface.tvtk.tvtk_scene.TVTKScene`.  This class is
      inherited by all Scenes (DecoratedScene and Scene).  The close
      method shuts down the scene properly.  This should hopefully
      prevent async errors when closing editors/windows containing
      scenes.  See [18708].
    - Updated the scene plugin, scene_editor (TraitsBackend*),
      actor_editor and the ivtk code to use the close method.
    - TEST: All the tests run on the trunk and pass when the offscreen
      option is used (which was also added).

17 May, 2008 (PR):
    - NEW: Adding an SelectOutput filter that should address bug number
      478359 in the Debian BTS.  See [18700].
    - API: mayavi.plugins.app.Mayavi now defines a
      setup_logger method so this can be overridden by subclasses, see
      [18703].

13 May, 2008 (PR):
    - NEW: Adding an ExtractVectorComponents filter contributed by Varun
      Hiremath.

11,12 May 2008 (PR):
    - ENH/API: The plugins now start the engine themselves and also do
      the binding to the shell. Earlier this was done by the
      application.  This makes the plugins reusable. Also added a
      running trait to the engine to check on its status. [18672],
      [18678].
    - At this point all examples in trunk work save the mayavi_custom_ui
      plugin stuff.

10 May 2008 (PR):
    - API: Moving mayavi/engine.py ->
      mayavi/core/engine.py where it really belongs; see
      [18667].

7,8 May 2008 (PR):
    - API: The plugins_e3 package is now moved into plugins.  This
      breaks the tvtk.plugins API and also the
      mayavi.mayavi_*_definition modules.  The older envisage2
      plugin code is all removed. See: [18649], [18650], [18651],
      [18652], [18655], [18657], [18662].

6 May 2008 (PR):
    - API: The mayavi.core.Base.confirm_delete class attribute
      is gone since it is no longer needed [18635].
    - API: Removed config directory, integrated all mlab preferences
      into the the mayavi preferences framework, see [18632].
      To get the preferences just do::

        from mayavi.preferences.api import preference_manager

      This is the preference manager that manages all prefs.  To see the
      code look in mayavi.preferences.preference_manager.  It
      is also a good idea to read the apptools.preferences
      documentation.
    - BUG: [18627] Fixed bug number 478844 on the Debian BTS here:
      http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=478844

4 May 2008 (PR):
    - API: Added to api.  Added a new preferences framework for mayavi2.
      This uses apptools.preferences and works well both standalone and
      with envisage3. It makes it easy to create/define/change
      preferences at the application and library level.

2 May, 2008 (PR):
    - API: Ported the mayavi2 application and plugin to work with Envisage3.
      See changesets [18595] and [18598].  *This obviously breaks the
      plugin API completely!*
    - Got the mlab envisage_engine_manager working with new changes
      [18599].

Before this changeset, the code was that of the 2.x series.
