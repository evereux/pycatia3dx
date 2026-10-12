import os
import sys

import pytest

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))

from pycatia3dx import catia3dx
from pycatia3dx.exceptions import CATIAApplicationException
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.plm_access.search_service import SearchService
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
            raise RuntimeError(f'"{window.name}" is still open. Please close all documents prior to running tests.')


check_open_documents()


def close_all():
    windows = application.windows
    for window in windows:
        if window.name != "Welcome Page":
            window.close()


@pytest.fixture
def file_open(file_name: str, base_type: str):
    open_plm_entity(application, file_name, base_type)


# typically used for the last test within a module or if a change has been
# made that might break later tests.
@pytest.fixture
def file_open_test_close_all(file_name: str, base_type: str):
    open_plm_entity(application, file_name, base_type)
    yield
    application.display_file_alerts = False
    close_all()
    application.display_file_alerts = True


# typically used for the first test within a module
@pytest.fixture
def document_close_all_open(file_name: str, base_type: str):
    close_all()
    open_plm_entity(application, file_name, base_type)


@pytest.fixture
def document_close_all_open_test_close(file_name: str, base_type: str):
    close_all()
    editor = open_plm_entity(application, file_name, base_type)
    yield
    close_all()
