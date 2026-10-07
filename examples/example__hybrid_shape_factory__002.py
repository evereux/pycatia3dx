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

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))
##########################################################

from pathlib import Path
from pycatia3dx import catia3dx
from pycatia3dx.scripts.csv_tools import create_points
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService

application = catia3dx()

plm_service: PLMNewService = application.get_session_service('PLMNewService')
editor = plm_service.plm_create('3DShape')

part = Part(editor.active_com_object)

# full path name to csv file.
file = Path(r"D:\code\github\pycatia3dx\tests\Sample_Point_CSV_File1_small.csv")

# create the points.
create_points(part, file, units="mm", geometry_set_name="Points_Construction")

# if you can't see the points hide your origin planes and reframe window.
# # re-enable display refresh
# application.refresh_display = True
# # unhide catia window
# application.visible = True
