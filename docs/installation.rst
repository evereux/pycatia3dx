.. _installation:

Installation
============

For the development of python scripts using pycatia3dx it's recommended you
follow the steps detailed below.


The Short Version
-----------------

This assumes python 3.9 or later is already installed and you know how and when
(all the time really) to use  `virtual environments <https://docs.python.org/3/tutorial/venv.html>`_.

You can either install pycatia from pypi.org using `pip install` (other
environment manages are available) or clone the repository from github.

It's not recommended to do both within the same project unless you know what you
are doing.

pypi
~~~

To install from `pypi <https://pypi.org/>`_::

    pip install pycatia3dx

To upgrade your current installed version::

    pip install pycatia3dx --upgrade


github
~~~~~~

To get the latest master version from github::

    git clone https://github.com/evereux/pycatia3dx.git
    # change directory into cloned project
    cd pycatia3dx
    # install the python virtual env
    python -m virtualenv env
    # activate the virtual env
    .\env\Scripts\activate
    # install the pycatia requirements
    pip install -r requirements\requirements.txt

