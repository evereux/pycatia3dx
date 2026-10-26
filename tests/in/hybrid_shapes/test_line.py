# import pytest
import pytest

from pycatia3dx.hybrid_shapes.line import Line
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_lines


# def test_first_upto_elem():

# pass


# def test_second_upto_elem():

# pass

@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_direction(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    lines_hybrid_shapes = hb_geom_set_lines.hybrid_shapes
    line_1 = Line(lines_hybrid_shapes.item(1).com_object)

    assert line_1.get_direction() == (0.7071067811865476, 0.7071067811865476, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_origin(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    lines_hybrid_shapes = hb_geom_set_lines.hybrid_shapes
    line_1 = Line(lines_hybrid_shapes.item(1).com_object)

    assert line_1.get_origin() == (0.0, 0.0, 0.0)

# def test_put_direction():

# pass
