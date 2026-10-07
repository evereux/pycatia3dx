pycatia3dx
==========

alpha software
--------------

This is alpha software.

Please report any issues with using the package on github providing a stripped
down script.

Requirements
------------

* python >= 3.12
* **CATIA 3DExperience** running on Windows.
* see requirements.txt

Installation
------------

There is currently no pypi package available. You'll need to clone the github
repository or download the github archive.


Usage
-----

See the examples: https://github.com/evereux/pycatia3dx/tree/main/examples


Links
-----

todo



Examples And Scripts
--------------------

https://github.com/evereux/pycatia3dx/tree/main/examples


Asking Questions
----------------

Please read the following with regards to raising questions: https://github.com/evereux/pycatia/issues/28


Contributing
------------

See CONTRIBUTING.md in root of github repository.

Running The Tests
-----------------

Prior to running you will need to create the test files. This script will also
check that you have all the test files created and they are the latest version
so it's worth running each time you upgrade pycatia3dx

.. code-block:: python

    python .\tests\check_test_files.py

CATIA 3DExperience shall already be running and all documents are closed. If
this isn't the case the tests will not run and you'll be presented with a
warning.

To run the tests with coverage (-v is verbosity):

.. code-block:: python

    py.test -v --cov-report term-missing --cov=pycatia3dx

To run tests for a specific module

.. code-block:: python

    py.test -v tests/in/hybrid_shapes/test_hybrid_shape_factory.py

To stop tests running after first failure.

    py.test -vx


