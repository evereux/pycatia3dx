"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.sfd_panel import SfdPanel
from pycatia3dx.str.srm_planning_breaks import SrmPlanningBreaks
from pycatia3dx.str.srm_proxy_profiles import SrmProxyProfiles


class SrmProxyPanel(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SrmProxyPanel
                | 
                | Object to manage the Proxy Panel.
                | Planning breaks are treated similar like limits.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_location(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLocation() As long
                |     Returns the proxy panel location under the proxy tool.
                | 
                |     Parameters:
                | 
                |         oLocation
                |             Legal Values:
                |             1 : IN.
                |             2 : OUT.

        :return: int
        """
        return self.com_object.GetLocation()

    def get_panel(self) -> SfdPanel:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPanel() As SfdPanel
                |     Returns the panel pointed by the proxy.

        :return: SfdPanel
        """
        return SfdPanel(self.com_object.GetPanel())

    def get_planning_breaks(self) -> SrmPlanningBreaks:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPlanningBreaks() As SrmPlanningBreaks
                |     Create the planning break to the Proxy Panel.
                | 
                |     Example:
                | 
                | 
                |              This example gets the list of planning breaks of
                |              SrmProxyPanel.
                |              
                | 
                |               Dim ObjSrmProxyPanel As SrmProxyPanel
                |               Set ObjSrmProxyPanel = ObjSrmProxies.Item(1)
                |               Set ObjSrmPlanningBreaks = ObjSrmProxyPanel.GetPlanningBreaks

        :return: SrmPlanningBreaks
        """
        return SrmPlanningBreaks(self.com_object.GetPlanningBreaks())

    def get_profile_proxies(self, i_location: int) -> SrmProxyProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfileProxies(long iLocation) As SrmProxyProfiles
                |     Returns the List of Profile Proxies
                | 
                |     Parameters:
                | 
                |         iLocation
                |             Return Values 1 : ProxyStiffenerTool_IN. 2 : ProxyStiffenerTool_OUT. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the SrmProxyProfiles of
                |              SrmProxyPanel.
                |              
                | 
                |               Set ListOfProfileProxies = ObjSrmProxyPanel.GetProfileProxies

        :param int i_location:
        :return: SrmProxyProfiles
        """
        return SrmProxyProfiles(self.com_object.GetProfileProxies(i_location))

    def __repr__(self):
        return f'SrmProxyPanel(name="{ self.name }")'
