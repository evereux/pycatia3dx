"""

    Example - Hybrid Shape Factory - 003

    Description:
        Draws a line between two points.

    Requirements:
        - CATIA running.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))
##########################################################

from pycatia3dx import catia3dx

application = catia3dx()

# IMPORTANT NOTE:
# Unlike V5, as of Jan 2026 the Automation API only
# supports creating REPRESENTATION objects (3DShape and Drawing).
# In production, these must be children of a 3D Part.
# This mirrors ENOVIA V5, where REPR objects are documents, and 3DPart is Part Reference.
# Code bellow has been created for testing and example purposes.
plm_service = PLMNewService(application.get_session_service('PLMNewService').com_object)
plm_service.plm_create('3DShape', application.active_editor)

# remember to assign active_editor property to variable
# after you create 3DShape/Drawing; otherwise it will
# fail or perform operations in previous editor
editor = application.active_editor
part = Part(editor.active_object.com_object)

hybrid_bodies = part.hybrid_bodies
hsf = part.hybrid_shape_factory

# create a new hybrid body.
geom_set = hybrid_bodies.add()
geom_set.name = "Construction_Geometry"

co_ord_1 = (0, 0, 0)
co_ord_2 = (100, 0, 0)
point_1 = hsf.add_new_point_coord(co_ord_1[0], co_ord_1[1], co_ord_1[2])
point_1_reference = part.create_reference_from_object(point_1)

point_2 = hsf.add_new_point_coord(co_ord_2[0], co_ord_2[1], co_ord_2[2])
point_2_reference = part.create_reference_from_object(point_2)

geom_set.append_hybrid_shape(point_1)
geom_set.append_hybrid_shape(point_2)

line = hsf.add_new_line_pt_pt(point_1_reference, point_2_reference)

geom_set.append_hybrid_shape(line)

part.update()