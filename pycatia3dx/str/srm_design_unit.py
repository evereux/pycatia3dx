"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.srm_proxies import SrmProxies


class SrmDesignUnit(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SrmDesignUnit
                | 
                | Object to manage volume under the design unit.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_proxies(self, i_location: int) -> SrmProxies:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProxies(long iLocation) As SrmProxies
                |     Returns the List of Proxies
                | 
                |     Parameters:
                | 
                |         iLocation
                |             If iLocation == 1 : ProxyRootTool_IN. If iLocation == 2 : ProxyRootTool_OUT. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves list of Proxies.
                |              
                | 
                |              Dim ObjSrmDesignUnit As SrmDesignUnit
                |              ObjSelection.Add ObjPart
                |              Set ObjSrmDesignUnit = ObjSelection.FindObject("CATIASrmDesignUnit")
                |              Set ListOfProxies = ObjSrmDesignUnit.GetProxies

        :param int i_location:
        :return: SrmProxies
        """
        return SrmProxies(self.com_object.GetProxies(i_location))

    def __repr__(self):
        return f'SrmDesignUnit(name="{ self.name }")'
