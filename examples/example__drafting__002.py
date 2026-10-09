"""

    Example - Drafting - 003

    Description:

        Drafting: Creates a generative Front View from the selected VPMOccurance.

        This is a pycatia3dx re-write of the document
        CAAScdDriUcGenViewOnPartBodySource.htm provided in DSYAutomation.chm.

        If the right node is selected you will be asked to select the projection
        plane.

    Requirements:

        - An open VPMReference with a 3D Shape attached.
        - Nothing else shall be open.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))
##########################################################

from pycatia3dx import catia3dx
from pycatia3dx.drafting.drawing_gen_service import DrawingGenService
from pycatia3dx.drafting.drawing_root import DrawingRoot
from pycatia3dx.mmr_automation_interfaces.body import Body
from pycatia3dx.mmr_automation_interfaces.planar_face import PlanarFace
from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.product_structure_client.vpm_rep_instance import VPMRepInstance

application = catia3dx()
selection = application.active_editor.selection

message = '''
Please select one of the following:
    - The Product Representation Instance of the Reference on which the Part Body is Defined
'''
message_s = "Select a projection plane."

if selection.count2 == 1:
    link_part_body = None
    lpb = None

    sel_value = selection.item2(1).value

    if type(sel_value) == VPMRepInstance:
        lpb = selection.item2(1).value
    elif type(sel_value) == Body:
        lpb = selection.item2(1).value
    elif type(sel_value) == VPMOccurrence:
        lpb = selection.item2(1).value
    else:
        lpb = selection.item2(1).value

    drawing_gen_service: DrawingGenService = application.get_session_service("CATDrawingGenService")
    link_part_body = (lpb,)

    if not drawing_gen_service.check_view_link_integrity(link_part_body):
        print(message)
        exit()

else:
    print(message)
    exit()

print(message_s)
status = selection.select_element2(
    ("PlanarFace",),
    message_s,
    True
)

if status == "Cancel" or status == "Undo":
    exit()

# define the views projection plane
projection_plane: PlanarFace = selection.item(1).value
selection.clear()
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
