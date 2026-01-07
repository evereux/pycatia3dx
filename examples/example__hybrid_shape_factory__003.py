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
from pycatia3dx.scripts.csv_tools import create_points

application = catia3dx()
editor = application.active_editor

# IMPORTANT NOTE:
# In contrast to V5, currently (Jan 2026) Automation API exposes only
# methods for creating new REPRESENTATION objects (3D Shape and Drawing;
# You can compare representation objects to documents from ENOVIA V5).
# In production, both objects should be always children of 3D Part, since
# 3D Part is actual Part Reference (in Automation API- VPMReference).
# Code bellow has been created for testing and example purposes.
plm_service = PLMNewService(application.get_session_service('PLMNewService').com_object)
plm_service.plm_create('3DShape', editor)

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