"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingAxisSystem(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingAxisSystem
                | 
                | ManufacturingMachiningAxis defines a set of methods to manage a Machining Axis
                | System or an Origin.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_axis_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAxisType() As CATBSTR
                |     Gets the machining axis type.
                | 
                |     Parameters:
                | 
                |         oAxisType
                |             The type

        :return: str
        """
        return self.com_object.GetAxisType()

    def get_is_origin(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetIsOrigin() As long
                |     Gets if the machining axis system is an origin.
                | 
                |     Parameters:
                | 
                |         oFlag
                |             The flag

        :return: int
        """
        return self.com_object.GetIsOrigin()

    def get_origin_group(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOriginGroup() As long
                |     Gets the origin group in case of an origin usage.
                | 
                |     Parameters:
                | 
                |         oString
                |             The mode

        :return: int
        """
        return self.com_object.GetOriginGroup()

    def get_origin_number(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOriginNumber() As long
                |     Gets the origin number in case of an origin usage.
                | 
                |     Parameters:
                | 
                |         oFlag
                |             The origin number

        :return: int
        """
        return self.com_object.GetOriginNumber()

    def get_origin_point(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOriginPoint(double x,double y,double z)
                |     Gets the origin point of the machining axis system.
                | 
                |     Parameters:
                | 
                |         x,
                |             y, z The mathematical point

        :param float x:
        :param float y:
        :param float z:
        :return: None
        """
        return self.com_object.GetOriginPoint(x, y, z)

    def get_x_direction(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetXDirection(double x,double y,double z)
                |     Gets the X direction of the machining axis system.
                | 
                |     Parameters:
                | 
                |         x,
                |             y, z The mathematical direction

        :param float x:
        :param float y:
        :param float z:
        :return: None
        """
        return self.com_object.GetXDirection(x, y, z)

    def get_y_direction(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetYDirection(double x,double y,double z)
                |     Gets the Y direction of the machining axis system.
                | 
                |     Parameters:
                | 
                |         x,
                |             y, z The mathematical direction

        :param float x:
        :param float y:
        :param float z:
        :return: None
        """
        return self.com_object.GetYDirection(x, y, z)

    def get_z_direction(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetZDirection(double x,double y,double z)
                |     Gets the Z direction of the machining axis system.
                | 
                |     Parameters:
                | 
                |         x,
                |             y, z The mathematical direction

        :param float x:
        :param float y:
        :param float z:
        :return: None
        """
        return self.com_object.GetZDirection(x, y, z)

    def set_axis_type(self, i_axis_type: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxisType(CATBSTR iAxisType)
                |     Sets the machining axis type.
                | 
                |     Parameters:
                | 
                |         iAxisType
                |             The type

        :param str i_axis_type:
        :return: None
        """
        return self.com_object.SetAxisType(i_axis_type)

    def set_is_origin(self, i_flag: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetIsOrigin(long iFlag)
                |     Sets if the machining axis system is used as an origin.
                | 
                |     Parameters:
                | 
                |         iFlag
                |             The flag

        :param int i_flag:
        :return: None
        """
        return self.com_object.SetIsOrigin(i_flag)

    def set_origin_group(self, i_flag: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOriginGroup(long iFlag)
                |     Sets the origin group number in case of an origin usage.
                | 
                |     Parameters:
                | 
                |         iFlag
                |             The flag

        :param int i_flag:
        :return: None
        """
        return self.com_object.SetOriginGroup(i_flag)

    def set_origin_number(self, i_flag: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOriginNumber(long iFlag)
                |     Sets the origin number in case of an origin usage.
                | 
                |     Parameters:
                | 
                |         iFlag
                |             The flag

        :param int i_flag:
        :return: None
        """
        return self.com_object.SetOriginNumber(i_flag)

    def set_origin_point(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOriginPoint(double x,double y,double z)
                |     Sets the origin point of the machining axis system.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The mathematical point

        :param float x:
        :param float y:
        :param float z:
        :return: None
        """
        return self.com_object.SetOriginPoint(x, y, z)

    def set_x_direction(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetXDirection(double x,double y,double z)
                |     Sets the X direction of the machining axis system.
                | 
                |     Parameters:
                | 
                |         iDirection
                |             The mathematical direction

        :param float x:
        :param float y:
        :param float z:
        :return: None
        """
        return self.com_object.SetXDirection(x, y, z)

    def set_z_direction(self, x: float, y: float, z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetZDirection(double x,double y,double z)
                |     Sets the Z direction of the machining axis system.
                | 
                |     Parameters:
                | 
                |         iDirection
                |             The mathematical direction

        :param float x:
        :param float y:
        :param float z:
        :return: None
        """
        return self.com_object.SetZDirection(x, y, z)

    def __repr__(self):
        return f'ManufacturingAxisSystem(name="{ self.name }")'
