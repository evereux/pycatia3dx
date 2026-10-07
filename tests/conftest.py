import os
import sys

import pytest

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))

from pycatia3dx import catia3dx
from pycatia3dx.exceptions import CATIAApplicationException
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.plm_access.search_service import SearchService

test_app = catia3dx()


def check_open_documents():
    windows = test_app.windows
    for window in windows:
        if window.name != "Welcome Page":
            raise RuntimeError(f'"{window.name}" is still open. Please close all documents prior to running tests.')


check_open_documents()


def open_plm_entity(title: str, base_type: str) -> Editor:
    """

    base_type = 'VPMReference', '3DShape' or 'Drawing'

    :param title:
    :param str base_type:
    """

    search: SearchService = test_app.get_session_service('Search')
    db_search = search.database_search
    db_search.base_type = base_type
    db_search.all_minor_versions = True
    db_search.add_easy_criteria('V_Name', title)

    search.search()

    plm_entities = db_search.results

    if plm_entities.count == 0:
        raise CATIAApplicationException('No plm entities found')

    if plm_entities.count > 1:
        raise CATIAApplicationException('More than one plm entity found. Try restricting your search.')

    plm_entity = plm_entities[0]

    editor = test_app.get_session_service('PLMOpenService').plm_open(plm_entity)

    return editor


def close_all():
    windows = test_app.windows
    for window in windows:
        window.close()


@pytest.fixture
def file_open(file_name: str, base_type: str):
    open_plm_entity(file_name, base_type)


# typically used for the last test within a module or if a change has been
# made that might break later tests.
@pytest.fixture
def file_open_test_close_all(file_name: str, base_type: str):
    open_plm_entity(file_name, base_type)
    yield
    close_all()


# typically used for the first test within a module
@pytest.fixture
def document_close_all_open(file_name: str, base_type: str):
    close_all()
    open_plm_entity(file_name, base_type)


@pytest.fixture
def document_close_all_open_test_close(file_name: str, base_type: str):
    close_all()
    editor = open_plm_entity(file_name, base_type)
    yield
    close_all()
