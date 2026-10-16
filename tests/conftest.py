"""
    Prior to running the tests the test files will need to be created or checked
    for validity.
    To check or create the test files run the following command from the command
    prompt:
    >>> python .\\tests\\check_test_files.py
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))

from pycatia3dx import catia3dx
from tests.plm_helpers import open_plm_entity

application = catia3dx()


@pytest.fixture(scope="session", autouse=True)
def cleanup_after_all_tests():
    yield  # runs the tests
    # close all open documents
    close_all()


def check_open_documents():
    windows = application.windows
    for window in windows:
        if window.name != "Welcome Page":
            raise RuntimeError(f'"{window.name}" is still open. Please close all documents.')


check_open_documents()


def close_all():
    application.display_file_alerts = False
    windows = application.windows
    for window in windows:
        if window.name != "Welcome Page":
            window.close()
    application.display_file_alerts = True


@pytest.fixture
def file_open(file_name: str, base_type: str):
    open_plm_entity(application, file_name, base_type)
