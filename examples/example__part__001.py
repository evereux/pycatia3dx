"""

    Example - Part - 001

    Description:
        Create a new Part.

    Requirements:
        - 3DExperience CATIA running.

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))
##########################################################

from pycatia3dx import catia3dx
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService

# com3dx=False is required if com3dx.py cannot be found in your system.
application = catia3dx(com3dx=False)

plm_service: PLMNewService = application.get_session_service('PLMNewService')
plm_service.plm_create('3DShape', application.active_editor)

editor = application.active_editor
part = Part(editor.active_com_object)
