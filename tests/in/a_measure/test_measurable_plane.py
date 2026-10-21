import pytest

from pycatia3dx import CATMeasurableType
from pycatia3dx.measure.measurable_plane import MeasurablePlane
from pycatia3dx.measure.measurable_service import MeasurableService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import geom_set_planes
from tests.test_part_parameters import TEST_3DSHAPE_ONE


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_plane(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_planes = part.hybrid_bodies.item(geom_set_planes)
    plane_1 = hb_geom_set_planes.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurablePlane = measure_service.get_measurable(plane_1, CATMeasurableType.CAAMeasurablePlane)

    assert measurable.get_plane() == (0.0, 0.0, -200.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0)
