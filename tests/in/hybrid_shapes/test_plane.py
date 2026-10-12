import pytest

from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_CATPART_ONE, geom_set_planes


@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_get_first_axis(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_planes = part.hybrid_bodies.item(geom_set_planes)
    plane_hybrid_shapes = hb_geom_set_planes.hybrid_shapes
    plane_1 = Plane(plane_hybrid_shapes.item(1).com_object)

    assert plane_1.get_first_axis() == (1.0, 0.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_get_origin(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_planes = part.hybrid_bodies.item(geom_set_planes)
    plane_hybrid_shapes = hb_geom_set_planes.hybrid_shapes
    plane_1 = Plane(plane_hybrid_shapes.item(1).com_object)

    assert plane_1.get_origin() == (0.0, 0.0, -200.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_get_position(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_planes = part.hybrid_bodies.item(geom_set_planes)
    plane_hybrid_shapes = hb_geom_set_planes.hybrid_shapes
    plane_1 = Plane(plane_hybrid_shapes.item(1).com_object)

    assert plane_1.get_position() == (0.0, 0.0, 0.0)


def test_get_second_axis():
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_planes = part.hybrid_bodies.item(geom_set_planes)
    plane_hybrid_shapes = hb_geom_set_planes.hybrid_shapes
    plane_1 = Plane(plane_hybrid_shapes.item(1).com_object)

    assert plane_1.get_second_axis() == (0.0, 1.0, 0.0)


def test_is_a_ref_plane():
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_planes = part.hybrid_bodies.item(geom_set_planes)
    plane_hybrid_shapes = hb_geom_set_planes.hybrid_shapes
    plane_1 = Plane(plane_hybrid_shapes.item(1).com_object)

    assert plane_1.is_a_ref_plane() == True

# def test_put_first_axis():

# pass


# def test_put_origin():

# pass


# def test_put_second_axis():

# pass


# def test_remove_position():

# pass


# def test_set_position():

# pass
