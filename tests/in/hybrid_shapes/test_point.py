import pytest

from pycatia3dx.hybrid_shapes.point import Point
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_CATPART_ONE, geom_set_points


@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_get_coordinates(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    points_hybrid_shapes = hb_geom_set_points.hybrid_shapes
    point_1 = Point(points_hybrid_shapes.item(1).com_object)

    assert point_1.get_coordinates() == (0.0, 0.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_set_coordinates(file_open_test_close_all):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    points_hybrid_shapes = hb_geom_set_points.hybrid_shapes
    point_1 = Point(points_hybrid_shapes.item(1).com_object)
    point_1.set_coordinates((1.0, 1.0, 1.0))
    part.update()
    assert point_1.get_coordinates() == (1.0, 1.0, 1.0)
