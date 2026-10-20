import pytest

from pycatia3dx import CATMeasurableModeOfCalc, CATResultCalcType
from pycatia3dx import CATOpnsMeasureEdgeType
from pycatia3dx import CATOpnsMeasureItemType
from pycatia3dx import CATOpnsMeasureSurfaceType
from pycatia3dx.measure.measure_service import MeasureService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import geom_set_lines, geom_set_points, geom_set_arcs
from tests.test_part_parameters import geom_set_surfaces
from tests.test_part_parameters import TEST_3DSHAPE_ONE


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_angle(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((line_1,))
    measure_item.set_computation_mode(CATMeasurableModeOfCalc.MeasExactCalculation)
    angle = measure_item.get_angle()

    assert angle == 0.0


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_area(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((surface_1,))
    measure_item.set_computation_mode(CATMeasurableModeOfCalc.MeasExactCalculation)

    area = measure_item.get_area()

    assert area == 0.01


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_axis(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((surface_1,))
    measure_item.set_computation_mode(CATMeasurableModeOfCalc.MeasExactCalculation)

    axis = measure_item.get_axis()

    assert axis == (0.0, 0.0, 0.0)


# @pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
# def test_get_axis_system_from_measure(file_open):
#     editor = application.active_editor
#     measure_service: MeasureService = editor.get_service('MeasureService')
#
#     part = Part(editor.active_com_object)
#     axis_system_1 = part.axis_systems.item(1)
#     hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
#     line_1 = hb_geom_set_lines.hybrid_shapes[0]
#     line_2 = hb_geom_set_lines.hybrid_shapes[1]
#
#     measure_item = measure_service.get_measure_item((line_1, line_2, axis_system_1))
#     measure_item.set_computation_mode(CATMeasurableModeOfCalc.MeasExactCalculation)
#
#     axis = measure_item.get_axis_system_from_measure()
#
#     assert axis == None

@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_c_of_g(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((surface_1,))
    measure_item.set_computation_mode(CATMeasurableModeOfCalc.MeasExactCalculation)

    cog = measure_item.get_c_of_g()

    assert cog == (50.00000000000001, 50.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_center(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((line_1,))
    measure_item.set_computation_mode(CATMeasurableModeOfCalc.MeasExactCalculation)

    cog = measure_item.get_center()

    assert cog == (0.0, 0.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_computation_mode(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((line_1,))
    computation_mode = measure_item.get_computation_mode()

    assert computation_mode == CATMeasurableModeOfCalc.MeasExactElseApproxCalculation


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_curve_points(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((line_1,))
    curve_points = measure_item.get_curve_points()

    assert curve_points == (
        (0.0, 0.0, 0.0),
        (50.000000000000014, 50.000000000000014, 0.0),
        (100.00000000000003, 100.00000000000003, 0.0)
    )


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_direction(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((line_1,))
    direction = measure_item.get_direction()

    assert direction == (0.7071067811865476, 0.7071067811865476, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_length(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((line_1,))
    lenth = measure_item.get_length()

    assert lenth == 141.42135623730954


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_measure_edge_type(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((line_1,))
    measure_edge_type = measure_item.get_measure_edge_type()

    assert measure_edge_type == CATOpnsMeasureEdgeType.catOpnsUnknownEdge


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_measure_item_type(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((line_1,))
    measure_item_type = measure_item.get_measure_item_type()

    assert measure_item_type == CATOpnsMeasureItemType.catOpnsUnknownItem


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_measure_surface_type(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')

    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]

    measure_item = measure_service.get_measure_item((surface_1,))
    measure_surface_type = measure_item.get_measure_surface_type()

    assert measure_surface_type == CATOpnsMeasureSurfaceType.catOpnsUnknownSurface


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_origin(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')
    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]
    measure_item = measure_service.get_measure_item((surface_1,))
    origin = measure_item.get_origin()

    assert origin == (0.0, 0.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_perimeter(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')
    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]
    measure_item = measure_service.get_measure_item((surface_1,))
    get_perimeter = measure_item.get_perimeter()

    assert get_perimeter == 400.0


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_plane(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')
    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]
    measure_item = measure_service.get_measure_item((surface_1,))
    plane = measure_item.get_plane()

    assert plane == (0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_point(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')
    part = Part(editor.active_com_object)
    hb_geom_set_point = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_point.hybrid_shapes[3]
    measure_item = measure_service.get_measure_item((point_1,))
    point = measure_item.get_point()

    assert point == (0.0, 100.0, 0.0)


# @pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
# def test_get_points(file_open):
#     editor = application.active_editor
#     measure_service: MeasureService = editor.get_service('MeasureService')
#     part = Part(editor.active_com_object)
#     hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
#     line_1 = hb_geom_set_lines.hybrid_shapes[0]
#     measure_item = measure_service.get_measure_item((line_1,))
#     points = measure_item.get_points()
#
#     assert points == (50.000000000000014, 50.000000000000014, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_radius(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')
    part = Part(editor.active_com_object)
    hb_geom_set_arcs = part.hybrid_bodies.item(geom_set_arcs)
    arc_1 = hb_geom_set_arcs.hybrid_shapes[0]
    measure_item = measure_service.get_measure_item((arc_1,))
    radius = measure_item.get_radius()

    assert radius == 25.0


# @pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
# def test_get_result_computation_type(file_open):
#     editor = application.active_editor
#     measure_service: MeasureService = editor.get_service('MeasureService')
#     part = Part(editor.active_com_object)
#     hb_geom_set_arcs = part.hybrid_bodies.item(geom_set_arcs)
#     arc_1 = hb_geom_set_arcs.hybrid_shapes[0]
#     measure_item = measure_service.get_measure_item((arc_1,))
#     computation_type = measure_item.get_result_computation_type()
#
#     assert computation_type == CATResultCalcType.ResApproximateCalculation

# @pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
# def test_get_selection(file_open):
#     editor = application.active_editor
#     measure_service: MeasureService = editor.get_service('MeasureService')
#     part = Part(editor.active_com_object)
#     hb_geom_set_arcs = part.hybrid_bodies.item(geom_set_arcs)
#     arc_1 = hb_geom_set_arcs.hybrid_shapes[0]
#     measure_item = measure_service.get_measure_item((arc_1,))
#     selection = measure_item.get_selection()
#
#     assert selection == 25.0


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_volume(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')
    part = Part(editor.active_com_object)
    part_body = part.bodies.item('PartBody')

    measure_item = measure_service.get_measure_item((part_body,))
    volume = measure_item.get_volume()

    assert volume == 0.0005


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_volume_area_c_of_g(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')
    part = Part(editor.active_com_object)
    part_body = part.bodies.item('PartBody')

    measure_item = measure_service.get_measure_item((part_body,))
    volume = measure_item.get_volume_area_c_of_g()

    assert volume == (0.0005, 0.04, 50.0, 50.0, 25.0)


# def test_set_axis_system_on_measure(file_open):

# pass

@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_set_computation_mode(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')
    part = Part(editor.active_com_object)
    part_body = part.bodies.item('PartBody')

    measure_item = measure_service.get_measure_item((part_body,))
    measure_item.set_computation_mode(CATMeasurableModeOfCalc.MeasExactCalculation)

    assert CATMeasurableModeOfCalc.MeasExactCalculation == measure_item.get_computation_mode()


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_set_measure_item_type(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service('MeasureService')
    part = Part(editor.active_com_object)
    part_body = part.bodies.item('PartBody')

    measure_item = measure_service.get_measure_item((part_body,))
    measure_item.set_measure_item_type(CATOpnsMeasureItemType.catOpnsVolumeItem)

    assert CATOpnsMeasureItemType.catOpnsVolumeItem == measure_item.get_measure_item_type()

# def test_set_selection(file_open):

# pass
