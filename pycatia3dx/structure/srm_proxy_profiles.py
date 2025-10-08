"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.srm_proxy_profile import SrmProxyProfile
from pycatia3dx.types.general import CATVariant


class SrmProxyProfiles(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SrmProxyProfiles
                | 
                | Object for SrmProxyProfiles
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SrmProxyProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SrmProxyProfile
                |     Retrieves a SrmProxyProfile
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of SrmProxyProfile 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first item from the list of
                |              SrmProxyProfiles.
                |              
                | 
                |               Dim ObjSrmProxyProfiles As SrmProxyProfiles
                |               ObjSrmProxyProfiles = ObjSrmProxyPanel.GetProfileProxies(1)
                |               Dim ObjSrmProxyProfile As SrmProxyProfile
                |               Set ObjSrmProxyProfile = ObjSrmProxyProfiles.Item(1)

        :param CATVariant i_index:
        :return: SrmProxyProfile
        """
        return SrmProxyProfile(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SrmProxyProfiles(name="{self.name}")'
