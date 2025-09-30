"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingActivityToolAxis(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingActivityToolAxis
                | 
                | Interface to handle with Tool Axis of Manufacturing Activity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_tool_axis(self, o_tool_axis_x: float, o_tool_axis_y: float, o_tool_axis_z: float, o_type: int, o_mode: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetToolAxis(double oToolAxisX,double oToolAxisY,double oToolAxisZ,long
                | oType,CATBSTR oMode)
                |     Retrieves the tool axis information.
                | 
                |     Parameters:
                | 
                |         oToolAxis
                |             X Y Z the tool axis coordinates 
                |         oType
                |             the tool axis type 
                | 
                |     See also:
                |         DELIMfgActivityToolAxis::MfgTypeOfToolAxis
                |     Parameters:
                | 
                |         oMode
                |             the tool axis mode

        :param float o_tool_axis_x:
        :param float o_tool_axis_y:
        :param float o_tool_axis_z:
        :param int o_type:
        :param str o_mode:
        :return: None
        """
        return self.com_object.GetToolAxis(o_tool_axis_x, o_tool_axis_y, o_tool_axis_z, o_type, o_mode)

    def set_tool_axis(self, i_tool_axis_x: float, i_tool_axis_y: float, i_tool_axis_z: float, i_mode: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetToolAxis(double iToolAxisX,double iToolAxisY,double iToolAxisZ,CATBSTR
                | iMode)
                |     Sets the tool axis information.
                | 
                |     Parameters:
                | 
                |         iToolAxis
                |             X Y Z the tool axis coordinates 
                |         oMode
                |             the tool axis mode ("Manual")

        :param float i_tool_axis_x:
        :param float i_tool_axis_y:
        :param float i_tool_axis_z:
        :param str i_mode:
        :return: None
        """
        return self.com_object.SetToolAxis(i_tool_axis_x, i_tool_axis_y, i_tool_axis_z, i_mode)

    def __repr__(self):
        return f'ManufacturingActivityToolAxis(name="{ self.name }")'
