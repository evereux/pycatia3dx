import pytest

from pycatia3dx import CATMeasurableType
from pycatia3dx.measure.measurable_axis_system import MeasurableAxisSystem
from pycatia3dx.measure.measurable_service import MeasurableService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_axis(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    axis = part.axis_systems[0]
    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableAxisSystem = measure_service.get_measurable(axis, CATMeasurableType.CAAMeasurableAxisSystem)

    assert measurable.get_axis() == (0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
