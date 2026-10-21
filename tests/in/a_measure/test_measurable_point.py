import pytest

from pycatia3dx import CATMeasurableType
from pycatia3dx.measure.measurable_point import MeasurablePoint
from pycatia3dx.measure.measurable_service import MeasurableService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import geom_set_points
from tests.test_part_parameters import TEST_3DSHAPE_ONE


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_point(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_1 = hb_geom_set_points.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurablePoint = measure_service.get_measurable(point_1, CATMeasurableType.CAAMeasurablePoint)

    assert measurable.get_point() == (0.0, 0.0, 0.0)
