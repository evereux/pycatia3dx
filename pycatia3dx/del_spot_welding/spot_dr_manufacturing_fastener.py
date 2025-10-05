"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class SpotDrManufacturingFastener(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrManufacturingFastener

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def diameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Diameter(double iDiameter)
                |     This method sets the diameter of the Manufacturing
                |     Fastener
                | 
                |     Parameters:
                | 
                |         iDiameter,
                |             name to be set 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: float
        """

        return self.com_object.Diameter

    @diameter.setter
    def diameter(self, value: float):
        """
        :param float value:
        """

        self.com_object.Diameter = value

    @property
    def length(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Length(double iLength)
                |     This method sets the length of the Manufacturing Fastener
                | 
                |     Parameters:
                | 
                |         iLength,
                |             name to be set 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: float
        """

        return self.com_object.Length

    @length.setter
    def length(self, value: float):
        """
        :param float value:
        """

        self.com_object.Length = value

    @property
    def reference_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceName(CATBSTR iReferenceName)
                |     This method sets the reference name of the Manufacturing
                |     Fastener
                | 
                |     Parameters:
                | 
                |         iReferenceName,
                |             name to be set 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: str
        """

        return self.com_object.ReferenceName

    @reference_name.setter
    def reference_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.ReferenceName = value

    def create_fastener_parameter(self, i_param_name: str, i_param_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateFastenerParameter(CATBSTR iParamName,CATVariant
                | iParamValue)

        :param str i_param_name:
        :param CATVariant i_param_value:
        :return: None
        """
        return self.com_object.CreateFastenerParameter(i_param_name, i_param_value)

    def get_fastener_parameter(self, i_param_name: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFastenerParameter(CATBSTR iParamName) As double

        :param str i_param_name:
        :return: float
        """
        return self.com_object.GetFastenerParameter(i_param_name)

    def get_position(self, o_xpos: float, o_ypos: float) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPosition(double oXpos,double oYpos) As double
                |     This method gets the position of the Manufacturing
                |     Fastener
                | 
                |     Parameters:
                | 
                |         oXpos,
                |             X Coordinate 
                |         oYpos,
                |             Y Coordinate 
                |         oZpos,
                |             Z Coordinate 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param float o_xpos:
        :param float o_ypos:
        :return: float
        """
        return self.com_object.GetPosition(o_xpos, o_ypos)

    def get_tangent(self, o_xdir: float, o_ydir: float) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTangent(double oXdir,double oYdir) As double
                |     This method gets the tangent direction of the Manufacturing
                |     Fastener
                | 
                |     Parameters:
                | 
                |         oXdir,
                |             X Direction 
                |         oYdir,
                |             Y Direction 
                |         oZdir,
                |             Z Direction 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param float o_xdir:
        :param float o_ydir:
        :return: float
        """
        return self.com_object.GetTangent(o_xdir, o_ydir)

    def remove_fastener_parameter(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveFastenerParameter(CATBSTR iName)
                |     This method removes a user parameter
                | 
                |     Parameters:
                | 
                |         iName,
                |             Parameter Name 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param str i_name:
        :return: None
        """
        return self.com_object.RemoveFastenerParameter(i_name)

    def set_fastener_parameter(self, i_param_name: str, i_param_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFastenerParameter(CATBSTR iParamName,CATVariant
                | iParamValue)

        :param str i_param_name:
        :param CATVariant i_param_value:
        :return: None
        """
        return self.com_object.SetFastenerParameter(i_param_name, i_param_value)

    def set_position(self, i_xpos: float, i_ypos: float, i_zpos: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPosition(double iXpos,double iYpos,double iZpos)
                |     This method sets the position of the Manufacturing
                |     Fastener
                | 
                |     Parameters:
                | 
                |         iXpos,
                |             X Coordinate 
                |         iYpos,
                |             Y Coordinate 
                |         iZpos,
                |             Z Coordinate 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param float i_xpos:
        :param float i_ypos:
        :param float i_zpos:
        :return: None
        """
        return self.com_object.SetPosition(i_xpos, i_ypos, i_zpos)

    def set_tangent(self, i_xdir: float, i_ydir: float, i_zdir: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTangent(double iXdir,double iYdir,double iZdir)
                |     This method sets the tangent direction of the Manufacturing
                |     Fastener
                | 
                |     Parameters:
                | 
                |         iXdir,
                |             X Direction 
                |         iYdir,
                |             Y Direction 
                |         iZdir,
                |             Z Direction 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param float i_xdir:
        :param float i_ydir:
        :param float i_zdir:
        :return: None
        """
        return self.com_object.SetTangent(i_xdir, i_ydir, i_zdir)

    def __repr__(self):
        return f'SpotDrManufacturingFastener(name="{ self.name }")'
