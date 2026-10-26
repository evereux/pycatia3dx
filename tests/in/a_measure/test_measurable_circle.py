import pytest

from pycatia3dx import CATMeasurableType
from pycatia3dx.measure.measurable_circle import MeasurableCircle
from pycatia3dx.measure.measurable_service import MeasurableService
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_arcs


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_angle(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_arcs = part.hybrid_bodies.item(geom_set_arcs)
    arc_1 = hb_geom_set_arcs.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCircle = measure_service.get_measurable(arc_1, CATMeasurableType.CAAMeasurableCircle)

    assert measurable.get_angle() == 360.0


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_axis(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_arcs = part.hybrid_bodies.item(geom_set_arcs)
    arc_1 = hb_geom_set_arcs.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCircle = measure_service.get_measurable(arc_1, CATMeasurableType.CAAMeasurableCircle)

    assert measurable.get_axis() == (0.0, 0.0, 441.94173824159225)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_center(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_arcs = part.hybrid_bodies.item(geom_set_arcs)
    arc_1 = hb_geom_set_arcs.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCircle = measure_service.get_measurable(arc_1, CATMeasurableType.CAAMeasurableCircle)

    assert measurable.get_center() == (0.0, 100.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_radius(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_arcs = part.hybrid_bodies.item(geom_set_arcs)
    arc_1 = hb_geom_set_arcs.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableCircle = measure_service.get_measurable(arc_1, CATMeasurableType.CAAMeasurableCircle)

    assert measurable.get_radius() == 25.0
