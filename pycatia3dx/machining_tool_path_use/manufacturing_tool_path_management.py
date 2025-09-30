"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingToolPathManagement(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingToolPathManagement
                | 
                | Interface on the operation to manage links between it and its tool
                | path.
                | Role: DELIMfgToolPathManagement has methods to set, retrieve and remove tool
                | path on the operation
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def has_a_tool_path(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HasAToolPath() As boolean (Read Only)
                |     Indicates if the operation owns a tool path.

        :return: bool
        """

        return self.com_object.HasAToolPath

    def get_tool_path_limit_z(self, o_zmin: float, o_zmax: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetToolPathLimitZ(double oZmin,double oZmax)
                |     Get the min and max Z of tool path.
                | 
                |     Parameters:
                | 
                |         oZmin
                |             return the mininum of Z in tool path 
                |         oZmax
                |             return the maxinum of Z in tool path 
                | 
                |     Returns:
                |         E_FAIL if no tool path found and toolpath don't contain machining
                |         motion

        :param float o_zmin:
        :param float o_zmax:
        :return: None
        """
        return self.com_object.GetToolPathLimitZ(o_zmin, o_zmax)

    def __repr__(self):
        return f'ManufacturingToolPathManagement(name="{ self.name }")'
