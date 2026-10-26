import pytest

from pycatia3dx import CATMeasurableType
from pycatia3dx.measure.measurable_cylinder import MeasurableCylinder
from pycatia3dx.measure.measurable_service import MeasurableService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_cylinders


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_axis(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_cylinders = part.hybrid_bodies.item(geom_set_cylinders)
    cylinder_1 = hb_geom_set_cylinders.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCylinder = measure_service.get_measurable(cylinder_1, CATMeasurableType.CAAMeasurableCylinder)

    assert measurable.get_axis() == (0.0, 0.0, 50.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_point(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_cylinders = part.hybrid_bodies.item(geom_set_cylinders)
    cylinder_1 = hb_geom_set_cylinders.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCylinder = measure_service.get_measurable(cylinder_1, CATMeasurableType.CAAMeasurableCylinder)

    assert measurable.get_point() == (100.0, 100.0, 50.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_points(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_cylinders = part.hybrid_bodies.item(geom_set_cylinders)
    cylinder_1 = hb_geom_set_cylinders.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCylinder = measure_service.get_measurable(cylinder_1, CATMeasurableType.CAAMeasurableCylinder)

    assert measurable.get_points() == (100.0, 100.0, 100.0, 100.0, 100.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_radius(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_cylinders = part.hybrid_bodies.item(geom_set_cylinders)
    cylinder_1 = hb_geom_set_cylinders.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCylinder = measure_service.get_measurable(cylinder_1, CATMeasurableType.CAAMeasurableCylinder)

    assert measurable.get_radius() == 33.0
