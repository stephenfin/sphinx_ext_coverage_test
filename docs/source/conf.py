# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../../py_src'))
print(os.path.abspath('../../py_src'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Hello world API docs'
copyright = '2023, Stephen Finucane'
author = 'Stephen Finucane'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.coverage',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'


# -- Options for sphinx.ext.coverage -----------------------------------------

coverage_c_path = [
    '../../c_src/*.h',
]

# NOTE: This is a lazy regex and we should be far more explicit, but that's
# more work than we need here and this is okay for now
coverage_c_regexes = {
    'function': r'^void\s+([^_][\w_]+)',
}
