.. _getting_started:

Getting Started
===============

Before proceeding you shall already have pycatia3dx install. See the
:ref:`installation` page for details.

Before going this these introductory examples you should have pycatia3dx
installed (:ref:`installation`), CATIA 3DEXPERIENCE  running and a CMD terminal
open with the environment that has pycatia3dx installed and activated prior to
starting the python interpreter.

To start the python interpreter simple type `python` into the terminal. You
should see something like this::

    (env) PS D:\code\github\pycatia3dx> python
    Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

To exit the interpreter enter `exit()`::

    (env) PS D:\code\github\pycatia3dx> python
    Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> exit()
    (env) PS D:\code\github\pycatia3dx>


The Application Object
----------------------

The start of any pycatia3dx will always require you to initialise the
:ref:`Application<Application>` object.

Within the python interpreter enter the following::

    from pycatia3dx import catia3dx
    application = catia3dx()

The variable `application` is now a representation of the
:ref:`Application<Application>` object. The `application` object has a number
of methods that can be directly accessed. Check the API documention for the
`Application` object for further information.

A few examples::

    # this will return the full path name of the 3DExperience executable.
    application.full_name

    # this will return the name of the application
    application.name


Create A New 3DShape
--------------------

Here is a small script that you can enter into the python interpreter.

.. code-block:: python

    from pycatia3dx import catia3dx
    from pycatia3dx.mmr_automation_interfaces.part import Part
    from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService
    application = catia3dx()

    plm_service: PLMNewService = application.get_session_service('PLMNewService')
    plm_service.plm_create('3DShape', application.active_editor)
    # assign a name to the new 3DShape
    plm_service.set_attribute_value("V_Name", "L573P0001-101")

    editor = application.active_editor
    part = Part(editor.active_com_object)


The `plm_create` method of the class `PLMService` expects the string "3DShape"
or "Drawing". "VPMReference" and "3DPart" can also be used, license permitting.

If you know type the following into your terminal the output will now be
`L573P0001-101`.

.. code-block:: python

    part.name
    # returns the name of the new document.
