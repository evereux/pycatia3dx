"""
    Example - Hybrid Shape Factory - 002

    Description:
        Creates a new CATIA file and reads a csv file containing point data and adds to the new catia part.
        Formatting of csv data should be:
            <point_name>,<x coordinate>,<y coordinate>,<z coordinate>
        There should be no column name headers, just raw point data.

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
# # disable display refreshing to try tp speed up point generation.
# application.refresh_display = False
# # hide catia window
# application.visible = False

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

# full path name to csv file.
file = r"..\tests\Sample_Point_CSV_File1_small.csv"

# create the points.
create_points(part, file, units="mm", geometry_set_name="Points_Construction")

# if you can't see the points hide your origin planes and reframe window.

# # re-enable display refresh
# application.refresh_display = True
# # unhide catia window
# application.visible = True