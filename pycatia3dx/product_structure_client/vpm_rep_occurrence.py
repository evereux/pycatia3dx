"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_rep_instance import VPMRepInstance
from pycatia3dx.system.any_object import AnyObject


class VPMRepOccurrence(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VPMRepOccurrence
                | 
                | Interface representing a VPM Product Rep Occurrence.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def related_rep_instance(self) -> VPMRepInstance:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RelatedRepInstance() As VPMRepInstance (Read Only)
                |     Returns the VPM Rep Instance
                |     Role : This method retrieves the corresponding VPM Product Rep Instance of the VPM Rep Occurrence
                | 
                |     Example:
                | 
                |           This example show you how to retrieve the VPM Product Rep Instance of
                |           the
                |           current VPM Rep Occurrence :
                |           
                | 
                |              Dim repOccurrence As VPMRepOccurrence
                |              ...
                |              Dim repInstance As VPMRepInstance
                |              Set repInstance = repOccurrence.RelatedRepInstance

        :return: VPMRepInstance
        """

        return VPMRepInstance(self.com_object.RelatedRepInstance)

    def __repr__(self):
        return f'VpmRepOccurrence(name="{self.name}")'
