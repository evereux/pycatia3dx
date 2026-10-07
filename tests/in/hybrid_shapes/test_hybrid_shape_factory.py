import pytest

from pycatia3dx.mmr_automation_interfaces.part import Part
from tests.conftest import test_app
from tests.test_part_parameters import TEST_CATPART_ONE, geom_set_points, geom_set_lines, geom_set_arcs


# def test_add_new_3d_corner():

# pass


# def test_add_new_3d_curve_offset():

# pass


# def test_add_new_affinity():

# pass


# def test_add_new_axis_line():

# pass


# def test_add_new_axis_to_axis():

# pass


# def test_add_new_blend():

# pass


# def test_add_new_boundary():

# pass


# def test_add_new_boundary_of_surface():

# pass


# def test_add_new_bump():

# pass


# def test_add_new_circle2_points_rad():

# pass


# def test_add_new_circle3_points():

# pass


# def test_add_new_circle_bitangent_point():

# pass


# def test_add_new_circle_bitangent_radius():

# pass


# def test_add_new_circle_center_axis():

# pass


# def test_add_new_circle_center_axis_with_angles():

# pass


# def test_add_new_circle_center_tangent():

# pass


# def test_add_new_circle_ctr_pt():

# pass


# def test_add_new_circle_ctr_pt_with_angles():

# pass


# def test_add_new_circle_ctr_rad():

# pass


# def test_add_new_circle_ctr_rad_with_angles():

# pass


# def test_add_new_circle_datum():

# pass


# def test_add_new_circle_tritangent():

# pass


# def test_add_new_combine():

# pass


# def test_add_new_conic():

# pass


# def test_add_new_conical_reflect_line_with_type():

# pass


# def test_add_new_connect():

# pass


# def test_add_new_corner():

# pass


# def test_add_new_curve_datum():

# pass


# def test_add_new_curve_par():

# pass


# def test_add_new_curve_smooth():

# pass


# def test_add_new_cylinder():

# pass


# def test_add_new_datums():

# pass


# def test_add_new_develop():

# pass


# def test_add_new_direction():

# pass


# def test_add_new_direction_by_coord():

# pass


# def test_add_new_disconnect():

# pass


# def test_add_new_empty_rotate():

# pass


# def test_add_new_empty_translate():

# pass


# def test_add_new_extract():

# pass


# def test_add_new_extract_multi():

# pass


# def test_add_new_extrapol_length():

# pass


# def test_add_new_extrapol_until():

# pass


# def test_add_new_extremum():

# pass


# def test_add_new_extremum_polar():

# pass


# def test_add_new_extrude():

# pass


# def test_add_new_fill():

# pass


# def test_add_new_fillet_bi_tangent():

# pass


# def test_add_new_fillet_tri_tangent():

# pass


# def test_add_new_healing():

# pass


# def test_add_new_helix():

# pass


# def test_add_new_hybrid_scaling():

# pass


# def test_add_new_hybrid_split():

# pass


# def test_add_new_hybrid_trim():

# pass


# def test_add_new_integrated_law():

# pass


# def test_add_new_intersection():

# pass


# def test_add_new_inverse():

# pass


# def test_add_new_join():

# pass


# def test_add_new_law_dist_proj():

# pass


# def test_add_new_line_angle():

# pass


# def test_add_new_line_bi_tangent():

# pass


# def test_add_new_line_bisecting():

# pass


# def test_add_new_line_bisecting_on_support():

# pass


# def test_add_new_line_bisecting_on_support_with_point():

# pass


# def test_add_new_line_bisecting_with_point():

# pass


# def test_add_new_line_datum():

# pass


# def test_add_new_line_normal():

# pass


# def test_add_new_line_pt_dir():

# pass


# def test_add_new_line_pt_dir_on_support():

# pass


# def test_add_new_line_pt_pt():

# pass


# def test_add_new_line_pt_pt_extended():

# pass


# def test_add_new_line_pt_pt_on_support():

# pass


# def test_add_new_line_pt_pt_on_support_extended():

# pass


# def test_add_new_line_tangency():

# pass


# def test_add_new_line_tangency_on_support():

# pass


# def test_add_new_loft():

# pass


# def test_add_new_mid_surface():

# pass


# def test_add_new_mid_surface_with_auto_threshold():

# pass


# def test_add_new_near():

# pass


# def test_add_new_offset():

# pass


# def test_add_new_plane1_curve():

# pass


# def test_add_new_plane1_line1_pt():

# pass


# def test_add_new_plane2_lines():

# pass


# def test_add_new_plane3_points():

# pass


# def test_add_new_plane_angle():

# pass


# def test_add_new_plane_between():

# pass


# def test_add_new_plane_datum():

# pass


# def test_add_new_plane_equation():

# pass


# def test_add_new_plane_mean():

# pass


# def test_add_new_plane_normal():

# pass


# def test_add_new_plane_offset():

# pass


# def test_add_new_plane_offset_pt():

# pass


# def test_add_new_plane_tangent():

# pass


# def test_add_new_point_between():

# pass

@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_add_new_point_center(file_open):
    editor = test_app.active_editor
    part = Part(editor.active_com_object)
    hsf = part.hybrid_shape_factory
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    hb_geom_set_arcs = part.hybrid_bodies.item(geom_set_arcs)
    arc = hb_geom_set_arcs.hybrid_shapes.item(1)
    ref_arc = part.create_reference_from_object(arc)
    point = hsf.add_new_point_center(ref_arc)
    hb_geom_set_points.append_hybrid_shape(point)
    part.update()
    assert point.get_coordinates() == (0, 100, 0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_add_new_point_coord(file_open):
    editor = test_app.active_editor
    part = Part(editor.active_com_object)
    hsf = part.hybrid_shape_factory
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point = hsf.add_new_point_coord(100, 100, 100)
    hb_geom_set_points.append_hybrid_shape(point)
    part.update()
    assert point.get_coordinates() == (100, 100, 100)


@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_add_new_point_coord_with_reference(file_open):
    editor = test_app.active_editor
    part = Part(editor.active_com_object)
    hsf = part.hybrid_shape_factory
    hb_geom_set_points = part.hybrid_bodies.item(geom_set_points)
    point_source = hb_geom_set_points.hybrid_shapes.item(2)
    ref_point = part.create_reference_from_object(point_source)
    point = hsf.add_new_point_coord_with_reference(100, 100, 100, ref_point)
    hb_geom_set_points.append_hybrid_shape(point)
    part.update()
    assert point.get_coordinates() == (200.0, 100.0, 100.0)


@pytest.mark.parametrize('file_name,base_type', [(TEST_CATPART_ONE, "3DShape")])
def test_add_new_point_datum(file_open_test_close_all):
    editor = test_app.active_editor
    part = Part(editor.active_com_object)
    hsf = part.hybrid_shape_factory
    hb = part.hybrid_bodies.item(geom_set_points)
    point = hb.hybrid_shapes.item(1)
    ref_point = part.create_reference_from_object(point)
    new_point = hsf.add_new_point_datum(ref_point)
    hb.append_hybrid_shape(new_point)
    part.update()

    assert new_point.get_coordinates() == (0, 0, 0)

# def test_add_new_point_on_curve_along_direction():

# pass


# def test_add_new_point_on_curve_from_distance():

# pass


# def test_add_new_point_on_curve_from_percent():

# pass


# def test_add_new_point_on_curve_with_reference_along_direction():

# pass


# def test_add_new_point_on_curve_with_reference_from_distance():

# pass


# def test_add_new_point_on_curve_with_reference_from_percent():

# pass


# def test_add_new_point_on_plane():

# pass


# def test_add_new_point_on_plane_with_reference():

# pass


# def test_add_new_point_on_surface():

# pass


# def test_add_new_point_on_surface_with_reference():

# pass


# def test_add_new_point_tangent():

# pass


# def test_add_new_polyline():

# pass


# def test_add_new_position_transform():

# pass


# def test_add_new_project():

# pass


# def test_add_new_reflect_line():

# pass


# def test_add_new_reflect_line_with_type():

# pass


# def test_add_new_revol():

# pass


# def test_add_new_rotate():

# pass


# def test_add_new_section():

# pass


# def test_add_new_sphere():

# pass


# def test_add_new_spine():

# pass


# def test_add_new_spiral():

# pass


# def test_add_new_spline():

# pass


# def test_add_new_surface_datum():

# pass


# def test_add_new_sweep_circle():

# pass


# def test_add_new_sweep_conic():

# pass


# def test_add_new_sweep_explicit():

# pass


# def test_add_new_sweep_line():

# pass


# def test_add_new_symmetry():

# pass


# def test_add_new_transfer():

# pass


# def test_add_new_translate():

# pass


# def test_add_new_unfold():

# pass


# def test_add_new_volume_datum():

# pass


# def test_add_new_wrap_curve():

# pass


# def test_add_new_wrap_surface():

# pass


# def test_change_feature_name():

# pass


# def test_delete_object_for_datum():

# pass


# def test_gsm_visibility():

# pass


# def test_get_geometrical_feature_type():

# pass
