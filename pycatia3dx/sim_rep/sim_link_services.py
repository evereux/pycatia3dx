"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_modeller_base.plm_occurrence import PLMOccurrence
from pycatia3dx.product_structure_client.vpm_rep_instance import VPMRepInstance
from pycatia3dx.system.any_object import AnyObject


class SimLinkServices(Service):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SimLinkServices

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_occurrence(self, i_link: AnyObject) -> PLMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOccurrence(AnyObject iLink) As PLMOccurrence
                |     Gets the occurrence which contains the target of the link.
                | 
                |     Parameters:
                | 
                |         iLink:
                |             The link on which the occurrence must be retrieved.
                |             
                | 
                |     Returns:
                |         The occurrence.

        :param AnyObject i_link:
        :return: PLMOccurrence
        """
        return PLMOccurrence(self.com_object.GetOccurrence(i_link.com_object))

    def get_rep_instance(self, i_link: AnyObject) -> VPMRepInstance:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRepInstance(AnyObject iLink) As VPMRepInstance
                |     Gets the rep instance which contains the target of the
                |     link.
                | 
                |     Parameters:
                | 
                |         iLink:
                |             The link on which the rep instance must be retrieved.
                |             
                | 
                |     Returns:
                |         The rep instance.

        :param AnyObject i_link:
        :return: VPMRepInstance
        """
        return VPMRepInstance(self.com_object.GetRepInstance(i_link.com_object))

    def get_target(self, i_link: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTarget(AnyObject iLink) As AnyObject
                |     Gets the target of the link.
                | 
                |     Parameters:
                | 
                |         iLink:
                |             The link on which the target must be retrieved. 
                | 
                |     Returns:
                |         The link target.

        :param AnyObject i_link:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetTarget(i_link.com_object))

    def __repr__(self):
        return f'SimLinkServices(name="{self.name}")'
