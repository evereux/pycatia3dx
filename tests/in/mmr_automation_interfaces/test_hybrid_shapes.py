import pytest

from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_lines


# @pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
# def test_get_boundary(file_open):
#     pass

@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_item(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hbs = part.hybrid_bodies
    hbs_lines = hbs.item(geom_set_lines)
    hbs_lines_shapes = hbs_lines.hybrid_shapes
    line_1 = hbs_lines_shapes.item(1)

    assert line_1.name == "Line.1"


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test___getitem__(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hbs = part.hybrid_bodies
    hbs_lines = hbs.item(geom_set_lines)
    hbs_lines_shapes = hbs_lines.hybrid_shapes
    line_1 = hbs_lines_shapes.get_item('Line.1')

    assert line_1.name == "Line.1"


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test___iter__(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hbs = part.hybrid_bodies
    hbs_lines = hbs.item(geom_set_lines)
    hbs_lines_shapes = hbs_lines.hybrid_shapes
    line_1 = hbs_lines_shapes[0]

    assert line_1.name == "Line.1"
