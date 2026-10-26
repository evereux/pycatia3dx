"""

    Example - 3DPart - 001

    Description:
        Create new hybrid body in currently opened 3DPart.

        A 3DPart is a VPMReference that contains a 3DShape. A 3DPart
        (or VPMReference) can only be created if the user has access to the
        correct license.

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
from pycatia3dx.vpm_editor_context.plm_product_service import PLMProductService

application = catia3dx()
editor = application.active_editor

plm_product_service: PLMProductService = editor.get_service('PLMProductService')
root_occurrence = plm_product_service.root_occurrence
vpm_reference = root_occurrence.reference_root_occurrence_of
vpm_rep_instance = vpm_reference.rep_instances[0]

part: Part = vpm_rep_instance.reference_instance_of.get_item('Part')
hybrid_bodies = part.hybrid_bodies
hybrid_body = hybrid_bodies.add()
hybrid_body.name = 'My New Hybrid Body'
