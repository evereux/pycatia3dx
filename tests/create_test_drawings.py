import sys

from pycatia3dx import version
from pycatia3dx.drafting.drawing_gen_service import DrawingGenService
from pycatia3dx.drafting.drawing_root import DrawingRoot
from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.interfaces.application import Application
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService
from pycatia3dx.plm_session_builder.plm_propagate_service import PLMPropagateService
from pycatia3dx.vpm_editor_context.plm_product_service import PLMProductService
from tests.plm_helpers import open_plm_entity
from tests.test_part_parameters import TEST_3DPART_ONE, geom_set_planes, TEST_CATDRAWING_ONE


def create_test_drawing_one(application: Application):
    application.logger.info(f'Creating test file {TEST_CATDRAWING_ONE}.')

    editor = open_plm_entity(application, TEST_3DPART_ONE, 'VPMReference')

    plm_pd_service: PLMProductService = editor.get_service('PLMProductService')

    vpm_root_occurrence = plm_pd_service.root_occurrence
    vpm_root_ref = vpm_root_occurrence.reference_root_occurrence_of
    vpm_root_ref_rep_instance = vpm_root_ref.rep_instances[0]

    part: Part = vpm_root_ref_rep_instance.reference_instance_of.get_item('Part')

    drawing_gen_service: DrawingGenService = application.get_session_service('CATDrawingGenService')
    link_part_body = (vpm_root_occurrence,)
    if not drawing_gen_service.check_view_link_integrity(link_part_body):
        application.logger.warning('View link integrity check failed.')
        sys.exit()
    else:
        application.logger.info('View link integrity check succeeded.')

    # define the projection plane
    hb_planes = part.hybrid_bodies.item(geom_set_planes)
    hb_planes_shapes = hb_planes.hybrid_shapes
    projection_plane: Plane = hb_planes_shapes[0]
    first_axis = projection_plane.get_first_axis()
    second_axis = projection_plane.get_second_axis()
    plane_data = (
        first_axis[0],
        first_axis[1],
        first_axis[2],
        second_axis[0],
        second_axis[1],
        second_axis[2],
    )

    # create the new drawing
    plm_service: PLMNewService = application.get_session_service("PLMNewService")
    plm_service.set_attribute_value("V_Name", TEST_CATDRAWING_ONE)
    plm_service.set_attribute_value("V_description", version)
    editor = plm_service.plm_create("Drawing")
    drawing_root = DrawingRoot(editor.active_object.com_object)
    drawing_root.standard = "ISO"
    drawing_root.active_sheet.standard = "A0 ISO"

    # create the generative view
    views = drawing_root.active_sheet.views
    drawing_def_gen_view = views.drawing_define_gen_view

    gen_view_properties = drawing_gen_service.drawing_gen_view_prop

    # initialise the view
    front_view = drawing_def_gen_view.define_front_view(
        100,
        100,
        link_part_body,
        plane_data,
        "",
        False,
        gen_view_properties,
    )

    # modifies the generative view link
    front_view.drawing_gen_view.put_links(
        1,
        link_part_body
    )

    front_view.drawing_gen_view.update()

    plm_propagate_service: PLMPropagateService = application.get_session_service('PLMPropagateService')
    plm_propagate_service.plm_propagate()

    # ##### #
    # close #
    # ##### #

    application.active_window.close()

    application.logger.info(f'Created {TEST_CATDRAWING_ONE}.')
