.. _installation:

Installation
============

For the development of python scripts using pycatia3dx it's recommended you
follow the steps detailed below.


Python Installation
~~~~~~~~~~~~~~~~~~~

Download and install python from `python.org <https://www.python.org/>`_.


Virtual Env
~~~~~~~~~~~

It's good practise and thoroughly encouraged to use a virtual environment for each project.

See the python documentation about `virtual environments <https://docs.python.org/3/tutorial/venv.html>`_.

There are a few ways this can be accomplished. The following is just one of those methods.

In the terminal navigate to your nominated working directory for pycatia3dx work. For example::

    cd D:\code\github\pycatia3dx

Install the `virtualenv` module::

    python -m pip install virtualenv

The actual virtual environment would normally be installed in your working directory like this, where `env` is the
directory name of the environment::

    python -m virtualenv env

Activate the virtualenv environment::

    .\env\Scripts\activate

Each time a new terminal session is started the virtual environment will need to be activated.

pypi
~~~~

To install from `pypi <https://pypi.org/>`_::

    pip install pycatia3dx

To upgrade your current installed version::

    pip install pycatia3dx --upgrade


