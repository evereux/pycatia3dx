"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2026-01-04 12:20:59.068917

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.mode.reference import Reference
from pycatia3dx.plm_modeller_base.plm_entities import PLMEntities
from pycatia3dx.plm_modeller_base.plm_occurrence import PLMOccurrence
from pycatia3dx.product_structure_client.vpm_rep_instance import VPMRepInstance
from pycatia3dx.product_structure_client.vpm_root_occurrence import VPMRootOccurrence
from pycatia3dx.system.any_object import AnyObject


class PLMProductService(Service):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMProductService
                | 
                | Interface representing service to manage VPM Editor content.
                | 
                | PLMProductService object can be retrieved from Editor object thanks to the
                | GetService method with the string "PLMProductService" as
                | input.
                | The get_EditedContent method implementation returns the root Product of the
                | editor.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def edited_content(self) -> PLMEntities:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917)
                | Property EditedContent() As PLMEntities (Read Only)
                |     Returns Root entities of active Editor, first of which is the root Product.

        :return: PLMEntities
        """

        return PLMEntities(self.com_object.EditedContent)

    @property
    def root_occurrence(self) -> VPMRootOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917)
                | Property RootOccurrence() As VPMRootOccurrence (Read Only)
                |     Returns the Root Product Occurrence being edited in current VPM Editor.

        :return: VPMRootOccurrence
        """

        return VPMRootOccurrence(self.com_object.RootOccurrence)

    def compose_link(self, i_plm_occurrence: PLMOccurrence, i_vpm_rep_instance: VPMRepInstance,
                     i_catia_reference: Reference) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917))
                | Func ComposeLink(PLMOccurrence iPLMOccurrence,VPMRepInstance
                | iVPMRepInstance,Reference iCATIAReference) As AnyObject
                |     Creates a Link memory object to be used later for persistent
                |     Link.
                | 
                |     Parameters:
                | 
                |         iPLMOccurrence
                |             The path to reach the target. It is optional, and must be a
                |             CATIAVPMOccurrence ou CATIAVPMRootOccurrence. 
                |         iVPMRepInstance
                |             The Product Representation Reference containing the target. It is
                |             optional. 
                |         iCATIAReference
                |             The target object. It is optional. 
                | 
                |     Returns:
                |         The CATIABase to be used to create a link.

        :param PLMOccurrence i_plm_occurrence:
        :param VPMRepInstance i_vpm_rep_instance:
        :param Reference i_catia_reference:
        :return: AnyObject
        """
        return AnyObject(self.com_object.ComposeLink(i_plm_occurrence.com_object, i_vpm_rep_instance.com_object,
                                                     i_catia_reference.com_object))

    def __repr__(self):
        return f'PLMProductService(name="{self.name}")'
