# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
from sphinx.ext.autodoc import between

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pycatia3dx'
copyright = '2026, Paul Bourne'
author = 'Paul Bourne'
release = '0.2.0'

sys.path.insert(0, os.path.abspath('../..'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']


def remove_note_directives(app, what, name, obj, options, lines):
    """Filters out '.. note::' directives and their contents from docstrings."""
    modified_lines = []
    in_note = False
    note_indent = 0

    for line in lines:
        # Check if we are currently inside a note block
        if in_note:
            # If the line is not empty and its indentation drops below the note's
            # indentation, we have exited the note block.
            stripped = line.lstrip()
            if stripped:
                current_indent = len(line) - len(stripped)
                if current_indent <= note_indent:
                    in_note = False  # Exited the note
                else:
                    continue  # Skip everything inside the note block
            else:
                continue  # Skip empty lines inside the note block

        # Detect the start of a note block
        if ".. note::" in line:
            in_note = True
            # Determine the baseline indentation of the block
            note_indent = len(line) - len(line.lstrip())
            continue  # Skip the directive line itself

        modified_lines.append(line)

    # Modify the lines list in-place as required by Sphinx
    lines[:] = modified_lines


def setup(app):
    # Connect the handler to the autodoc docstring processor
    app.connect('autodoc-process-docstring', remove_note_directives)
