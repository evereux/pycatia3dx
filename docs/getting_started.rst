.. _getting_started:

Getting Started
===============

Before proceeding you should already have pycatia3dx install. Visit the
:ref:`installation` page.

Before going this these introductory examples you should have have pycatia3dx
installed (:ref:`installation`), 3DXPERIENCE CATIA running and a CMD terminal
open with the environment that has pycatia3dx installed activated prior to
starting the python interpreter.


Opening A New Part
------------------

Import the `catia3dx` :ref:`Application<Application>`.

.. code-block:: python

    from pycatia3dx import catia3dx
    from pycatia3dx.mmr_automation_interfaces.part import Part
    from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService
    # initialise the catia automation application. CATIA V5 should already be running.
    # com3dx=False is required if com3dx.py cannot be found in your system.
    # if com3dx.py was bundled with your installation you can remove the parameter completely.
    application = catia3dx(com3dx=False)

    plm_service: PLMNewService = application.get_session_service('PLMNewService')
    plm_service.plm_create('3DShape', application.active_editor)

    editor = application.active_editor
    part = Part(editor.active_com_object)


the `plm_create` method of the class `PLMService` expects the string "3DShape"
or "Drawing".

.. code-block:: python

    part.name
    # returns the name of the new document.
