import pytest

from pycatia3dx.plm_modeller_base import plm_entity
from tests.conftest import test_app

from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService


def test_plm_create():
    plm_service: PLMNewService = test_app.get_session_service('PLMNewService')
    editor = plm_service.plm_create('3DShape')

    window = test_app.active_window

    assert editor

    test_app.display_file_alerts = False

    window.close()

    test_app.display_file_alerts = True

# def test_set_attribute_value():

# pass
