from pycatia3dx import catia3dx
from pycatia3dx.interfaces.application import Application
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService
from pycatia3dx.product_structure_client.vpm_rep_reference import VPMRepReference

application: Application = catia3dx()
plm_service = PLMNewService(application.get_session_service('PLMNewService').com_object)
plm_service.plm_create("3DShape", application.active_editor)

editor = application.active_editor
part = Part(editor.active_object)
vpm_ref = VPMRepReference(part.parent)

print(vpm_ref.get_attribute_value('PLM ExternalID'))
