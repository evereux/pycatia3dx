import pytest

from pycatia3dx.measure.measure_service import MeasureService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_lines


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
    measure_between_lines.compute()
    angle = measure_between_lines.get_angle()

    assert angle == 45.0

# def test_get_axis_system_from_measure():

# pass


# def test_get_band_analysis_parameters():

# pass


# def test_get_components():

# pass


# def test_get_computation_mode():

# pass


# def test_get_distance():

# pass


# def test_get_distance_measure_type():

# pass


# def test_get_extension_mode():

# pass


# def test_get_first_point_coordinates():

# pass


# def test_get_first_selection():

# pass


# def test_get_result_computation_type():

# pass


# def test_get_second_point_coordinates():

# pass


# def test_get_second_selection():

# pass


# def test_get_selection_calculation_types():

# pass


# def test_set_along_direction():

# pass


# def test_set_axis_system_on_measure():

# pass


# def test_set_band_analysis_parameters():

# pass


# def test_set_computation_mode():

# pass


# def test_set_distance_measure_type():

# pass


# def test_set_extension_mode():

# pass


# def test_set_first_selection():

# pass


# def test_set_result_computation_type():

# pass


# def test_set_second_selection():

# pass


# def test_set_selection_calculation_types():

# pass
