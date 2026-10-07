import pytest

from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.interfaces.editors import Editors
from pycatia3dx.interfaces.printers import Printers
from pycatia3dx.os.file_system import FileSystem
from pycatia3dx.os.system_configuration import SystemConfiguration
from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService
from tests.conftest import test_app, close_all
from tests.test_part_parameters import TEST_CATPART_ONE


@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_active_editor(file_open):
    assert 'Editor(name="CATIAEditor' in test_app.active_editor.__repr__()


def test_active_printer():
    assert 'Printer(name=' in test_app.active_printer.__repr__()


def test_active_window():
    assert 'Window(name=' in test_app.active_window.__repr__()


# def test_cache_size():
# todo: this doesn't work
#     assert 500 == test_app.cache_size()

def test_caption():
    assert type(test_app.caption) is str


def test_display_file_alerts():
    assert type(test_app.display_file_alerts) is bool


def test_editors():
    assert type(test_app.editors) is Editors


def test_file_system():
    assert type(test_app.file_system) is FileSystem


def test_full_name():
    assert type(test_app.full_name) is str


def test_hso_synchronized():
    assert type(test_app.hso_synchronized) is bool


def test_height():
    assert type(test_app.height) is float


def test_interactive():
    assert type(test_app.interactive) is bool


def test_left():
    assert type(test_app.left) is float


def test_local_cache():
    assert type(test_app.local_cache) is str


def test_path():
    assert type(test_app.path) is str


def test_printers():
    assert type(test_app.printers) is Printers


def test_refresh_display():
    assert type(test_app.refresh_display) is bool


# def test_script_command():

# pass


# def test_status_bar():

# pass


def test_system_configuration():
    assert type(test_app.system_configuration) is SystemConfiguration


# def test_system_service():

# pass


def test_top():
    assert type(test_app.top) is float


# def test_undo_redo_lock():

# pass


def test_user_interface_language():
    assert type(test_app.user_interface_language) is str


def test_visible():
    assert type(test_app.visible) is bool


def test_width():
    assert type(test_app.width) is float


def test_windows():
    windows = test_app.windows

    assert len(windows) > 0


# def test_disable_new_undo_redo_transaction():

# pass


# def test_enable_new_undo_redo_transaction():

# pass


# def test_file_selection_box():

# pass


# def test_folder_selection_box():

# pass


def test_get_session_service():
    plm_service: PLMNewService = test_app.get_session_service("PLMNewService")

    assert 'PLMNewService' in plm_service.__repr__()


def test_get_workbench_id():
    test_app.start_workbench('PrtCfg')
    assert test_app.get_workbench_id() == "PrtCfg"


# def test_help():
# todo: this doesn't work, at least for my configuration
#   pass


# def test_quit():

# pass


# def test_start_command():

# pass

@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_start_workbench(file_open_test_close_all):
    test_app.start_workbench('CATGS1Workbench')
    assert test_app.get_workbench_id() == "CATGS1Workbench"

# pass
