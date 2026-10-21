import pytest

from pycatia3dx import CATMeasurableType
from pycatia3dx.measure.measurable_service import MeasurableService
from pycatia3dx.measure.measurable_surface import MeasurableSurface
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_surfaces


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_area(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableSurface = measure_service.get_measurable(surface_1, CATMeasurableType.CAAMeasurableSurface)

    assert measurable.get_area() == 0.01


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_area_c_of_g(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableSurface = measure_service.get_measurable(surface_1, CATMeasurableType.CAAMeasurableSurface)

    assert measurable.get_area_c_of_g() == (0.01, 50.00000000000001, 50.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_c_of_g(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableSurface = measure_service.get_measurable(surface_1, CATMeasurableType.CAAMeasurableSurface)

    assert measurable.get_c_of_g() == (50.00000000000001, 50.0, 0.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_perimeter(file_open):
    editor = application.active_editor
    part = Part(editor.active_com_object)
    hb_geom_set_surfaces = part.hybrid_bodies.item(geom_set_surfaces)
    surface_1 = hb_geom_set_surfaces.hybrid_shapes[0]

    measure_service: MeasurableService = editor.get_service("MeasurableService")
    measurable: MeasurableSurface = measure_service.get_measurable(surface_1, CATMeasurableType.CAAMeasurableSurface)

    assert measurable.get_perimeter() == 400.0
