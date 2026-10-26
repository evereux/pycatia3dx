import pytest

from pycatia3dx import CATMeasurableType
from pycatia3dx.measure.measurable_line import MeasurableLine
from pycatia3dx.measure.measurable_service import MeasurableService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_lines


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_direction(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableLine = measure_service.get_measurable(line_1, CATMeasurableType.CAAMeasurableLine)

    assert measurable.get_direction() == (0.7071067811865476, 0.7071067811865476, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_origin(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableLine = measure_service.get_measurable(line_1, CATMeasurableType.CAAMeasurableLine)

    assert measurable.get_origin() == (50.000000000000014, 50.000000000000014, 0.0)
