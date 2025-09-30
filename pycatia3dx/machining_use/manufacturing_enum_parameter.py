"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class ManufacturingEnumParameter(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingEnumParameter
                | 
                | This interface is used to handle with Enumeration Parameters for
                | Manufacturing
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_mode(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMode() As Parameter
                |     Retrieves the value for mode.
                | 
                |     Parameters:
                | 
                |         oMode
                |             The return value

        :return: Parameter
        """
        return Parameter(self.com_object.GetMode())

    def get_mode_bool(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetModeBool() As boolean
                |     Retrieves the value for mode.
                | 
                |     Parameters:
                | 
                |         oMode
                |             The return value

        :return: bool
        """
        return self.com_object.GetModeBool()

    def get_mode_str(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetModeStr() As CATBSTR
                |     Retrieves the value for mode.
                | 
                |     Parameters:
                | 
                |         oMode
                |             The return value

        :return: str
        """
        return self.com_object.GetModeStr()

    def get_object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetObject() As AnyObject
                |     Retrieves the value of mode.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The return value

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetObject())

    def set_mode_bool(self, i_mode: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetModeBool(boolean iMode)
                |     Set the value for mode.
                | 
                |     Parameters:
                | 
                |         iMode
                |             The value to set

        :param bool i_mode:
        :return: None
        """
        return self.com_object.SetModeBool(i_mode)

    def set_mode_str(self, i_mode: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetModeStr(CATBSTR iMode)
                |     Set the value for mode.
                | 
                |     Parameters:
                | 
                |         iMode
                |             The value to set

        :param str i_mode:
        :return: None
        """
        return self.com_object.SetModeStr(i_mode)

    def set_object(self, i_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetObject(AnyObject iValue)
                |     Set the value of mode.
                | 
                |     Parameters:
                | 
                |         iValue
                |             The value to set

        :param AnyObject i_value:
        :return: None
        """
        return self.com_object.SetObject(i_value.com_object)

    def __repr__(self):
        return f'ManufacturingEnumParameter(name="{ self.name }")'
