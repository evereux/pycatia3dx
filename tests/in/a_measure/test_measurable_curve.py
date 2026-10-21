import pytest

from pycatia3dx import CATMeasurableType
from pycatia3dx.measure.measurable_curve import MeasurableCurve
from pycatia3dx.measure.measurable_service import MeasurableService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_lines


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_length(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes.get_item('Line.1')

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCurve = measure_service.get_measurable(line_1, CATMeasurableType.CAAMeasurableCurve)

    assert measurable.get_length() == 141.42135623730954


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_points(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCurve = measure_service.get_measurable(line_1, CATMeasurableType.CAAMeasurableCurve)

    assert measurable.get_points() == (
        (0.0, 0.0, 0.0),
        (50.000000000000014, 50.000000000000014, 0.0),
        (100.00000000000003, 100.00000000000003, 0.0)
    )
