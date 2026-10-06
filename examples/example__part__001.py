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

application = catia3dx()

plm_service: PLMNewService = application.get_session_service('PLMNewService')
editor = plm_service.plm_create('3DShape')

part = Part(editor.active_com_object)
