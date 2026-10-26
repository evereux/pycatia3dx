import pytest

from pycatia3dx import CatVisPropertyType
from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import application
from tests.test_part_parameters import TEST_3DSHAPE_ONE, geom_set_lines


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_layer(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    layer = selection.vis_properties.get_layer()
    assert layer == (0, 1, 1023)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_pick(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    pick = selection.vis_properties.get_pick()
    assert pick == (0, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_real_color(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    real_colour = selection.vis_properties.get_real_color()
    assert real_colour == (0, 0, 0, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_real_inheritance(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    real_inheritance = selection.vis_properties.get_real_inheritance(CatVisPropertyType.catVisPropertyColor)
    assert real_inheritance == (1, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_real_line_type(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    real_line_type = selection.vis_properties.get_real_line_type()
    assert real_line_type == (0, 1)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_real_opacity(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    real_line_type = selection.vis_properties.get_real_opacity()
    assert real_line_type == (1, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_real_width(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    real_width = selection.vis_properties.get_real_width()
    assert real_width == (0, 1)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_show(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    real_show = selection.vis_properties.get_show()
    assert real_show == (0, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_symbol_type(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    real_show = selection.vis_properties.get_symbol_type()
    assert real_show == (1, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_visible_color(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    visible_colour = selection.vis_properties.get_visible_color()
    assert visible_colour == (0, 0, 0, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_visible_inheritance(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    visible_inheritance = selection.vis_properties.get_visible_inheritance(CatVisPropertyType.catVisPropertyColor)
    assert visible_inheritance == (1, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_visible_line_type(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    visible_line_type = selection.vis_properties.get_visible_line_type()
    assert visible_line_type == (0, 1)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_visible_opacity(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    visible_opacity = selection.vis_properties.get_visible_opacity()
    assert visible_opacity == (1, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_3DSHAPE_ONE, "3DShape")])
def test_get_visible_width(file_open):
    editor = application.active_editor
    selection = editor.selection
    selection.clear()
    part = Part(editor.active_com_object)
    hb_geom_set_lines = part.hybrid_bodies.item(geom_set_lines)
    line_1 = hb_geom_set_lines.hybrid_shapes[0]
    selection.add(line_1)
    visible_width = selection.vis_properties.get_visible_width()
    assert visible_width == (0, 1)

# def test_reset_property(file_open):
# pass

# def test_set_layer():

# pass


# def test_set_pick():

# pass


# def test_set_real_color():

# pass


# def test_set_real_line_type():

# pass


# def test_set_real_opacity():

# pass


# def test_set_real_width():

# pass


# def test_set_show():

# pass


# def test_set_symbol_type():

# pass


# def test_set_visible_color():

# pass


# def test_set_visible_line_type():

# pass


# def test_set_visible_opacity():

# pass


# def test_set_visible_width():

# pass
