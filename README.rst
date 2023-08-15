Demo of ``sphinx.ext.coverage``
===============================

A demo of the `sphinx.ext.coverage`__ extension found in core Sphinx.

.. note::

   There's an `open issue`__ regarding the C coverage support, which is
   currently broken in Sphinx 7.x (and likely much earlier versions). As such,
   the C parts of this demo won't work until that's addressed.

Usage
-----

Install Sphinx:

.. code-block:: shell

   virtualenv .venv
   source .venv/bin/activate
   pip install sphinx

Once done, build documentation using the coverage builder:

.. code-block:: shell

   make -C docs coverage

Coverage reports can be found in the ``docs/build/coverage`` directory.
You'll note that two APIs - one from the C API docs and one Python API docs -
are noted as undocumented. If you go into the ``docs/source/api.rst`` file you
will see these are documented but commented out. Uncomment these are run the
build again:

.. code-block:: shell

   make -C docs coverage

You will now see no undocumented methods.

.. __: https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html
.. __: https://github.com/sphinx-doc/sphinx/issues/11590
