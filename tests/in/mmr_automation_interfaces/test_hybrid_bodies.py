import pytest

from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_CATPART_ONE, geom_set_arcs, geom_set_surfaces


# def test_add():

# pass

@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_item(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hbs = part.hybrid_bodies
    item = hbs.item(1)

    assert item.name == geom_set_arcs


# def test___getitem__():

# pass


def test___iter__():
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hbs = part.hybrid_bodies
    last_item = len(hbs) - 1
    hb_first = hbs[0]
    hb_last = hbs[last_item]

    assert hb_first.name == geom_set_arcs
    assert hb_last.name == geom_set_surfaces
