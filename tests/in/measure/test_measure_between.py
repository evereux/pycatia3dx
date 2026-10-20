import pytest

from pycatia3dx import CATMeasurableModeOfCalc, CATOpnsMeasureDistanceType, CATOpnsMeasureExtensionMode, \
    CATResultCalcType
from pycatia3dx.measure.measure_service import MeasureService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_lines, geom_set_points


# def test_compute():
# no need to test as it is used in several other tests.

@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_angle(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    line_2 = hb_geom_set_lines.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((line_1.com_object,), (line_2.com_object,))
    measure_between_lines.set_computation_mode(CATMeasurableModeOfCalc.MeasExactCalculation)
    measure_between_lines.compute()
    angle = measure_between_lines.get_angle()

    assert angle == 45.0


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_axis_system_from_measure(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    line_2 = hb_geom_set_lines.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((line_1.com_object,), (line_2.com_object,))
    measure_between_lines.compute()
    axis_system = measure_between_lines.get_axis_system_from_measure()

    # todo: this needs another test condition to test an actual system return
    assert axis_system is None


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_band_analysis_parameters(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    line_2 = hb_geom_set_lines.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((line_1.com_object,), (line_2.com_object,))
    measure_between_lines.compute()
    analysis_band_parameters = measure_between_lines.get_band_analysis_parameters()

    assert analysis_band_parameters == (0.0, 0.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_components(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    line_2 = hb_geom_set_lines.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((line_1.com_object,), (line_2.com_object,))
    measure_between_lines.compute()

    componenents = measure_between_lines.get_components()

    assert componenents == (0.0, 0.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_computation_mode(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    line_2 = hb_geom_set_lines.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((line_1.com_object,), (line_2.com_object,))
    measure_between_lines.compute()
    computation_mode = measure_between_lines.get_computation_mode()

    assert computation_mode == CATMeasurableModeOfCalc(2)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_distance(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")
    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.set_computation_mode(CATMeasurableModeOfCalc.MeasExactCalculation)
    measure_between_lines.compute()
    distance = measure_between_lines.get_distance()

    assert distance == 100.0


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_distance_measure_type(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.compute()
    measure_type = measure_between_lines.get_distance_measure_type()

    assert measure_type == CATOpnsMeasureDistanceType(0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_extension_mode(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.compute()
    extension_mode = measure_between_lines.get_extension_mode()

    assert extension_mode == (CATOpnsMeasureExtensionMode(0), CATOpnsMeasureExtensionMode(0))


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_first_point_coordinates(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.compute()
    point_coords = measure_between_lines.get_first_point_coordinates()

    assert point_coords == (0.0, 0.0, 0.0)


# def test_get_first_selection():
# todo: this currently crashes CATIA 3DExperience.

@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_result_computation_type(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.compute()
    computation_type = measure_between_lines.get_result_computation_type()

    assert computation_type == CATResultCalcType(0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_second_point_coordinates(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.compute()
    second_point_coordinates = measure_between_lines.get_second_point_coordinates()

    assert second_point_coordinates == (100.0, 0.0, 0.0)


# def test_get_second_selection():
# todo: this currently crashes CATIA 3DExperience.


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_selection_calculation_types(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.compute()
    calculation_types = measure_between_lines.get_selection_calculation_types()

    assert calculation_types == (CATResultCalcType.ResUnknownCalculation, CATResultCalcType.ResUnknownCalculation)


# def test_set_along_direction():

# pass

# def test_set_axis_system_on_measure():

# pass

# def test_set_band_analysis_parameters():

# pass

# def test_set_computation_mode():
# test not required as function is used elsewhere?


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_set_distance_measure_type(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")

    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]

    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.set_distance_measure_type(CATOpnsMeasureDistanceType.catOpnsMaximumDistance)

    measure_type = measure_between_lines.get_distance_measure_type()

    assert measure_type == CATOpnsMeasureDistanceType.catOpnsMaximumDistance


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_set_extension_mode(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")
    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]
    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.set_extension_mode(
        CATOpnsMeasureExtensionMode.catOpnsInfiniteExtend,
        CATOpnsMeasureExtensionMode.catOpnsInfiniteExtend
    )
    extension_mode = measure_between_lines.get_extension_mode()

    assert extension_mode == (CATOpnsMeasureExtensionMode.catOpnsInfiniteExtend,
                              CATOpnsMeasureExtensionMode.catOpnsInfiniteExtend)


# def test_set_first_selection():

# pass

@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_set_result_computation_type(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")
    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]
    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.compute()
    measure_between_lines.set_result_computation_type(
        CATResultCalcType.ResUnknownCalculation,
    )
    computation_type = measure_between_lines.get_result_computation_type()

    assert computation_type == CATResultCalcType.ResUnknownCalculation


# def test_set_second_selection():

# pass

@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_set_selection_calculation_types(file_open):
    editor = application.active_editor
    measure_service: MeasureService = editor.get_service("MeasureService")
    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]
    point_2 = hb_geom_set_points.hybrid_shapes[1]
    measure_between_lines = measure_service.get_measure_between((point_1.com_object,), (point_2.com_object,))
    measure_between_lines.compute()
    measure_between_lines.set_selection_calculation_types(
        CATResultCalcType.ResApproximateCalculation,
        CATResultCalcType.ResApproximateCalculation,
    )
    selection_computation_type = measure_between_lines.get_selection_calculation_types()

    assert selection_computation_type == (CATResultCalcType.ResApproximateCalculation,
                                          CATResultCalcType.ResApproximateCalculation)
