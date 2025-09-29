"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.eng_connection.eng_connection import EngConnection
from pycatia3dx.system.any_object import AnyObject


class KinCommand(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinCommand
                | 
                | The interface to access a CATIAKinCommand.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def command_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CommandType() As CATKinMechanismCommandType (Read
                | Only)
                |     Returns the command type.
                | 
                |     Parameters:
                | 
                |         oType
                | 
                |             Legal Types:
                | 
                |             CATKinEmpty2,
                |             CATKinAngleCmd2,
                |             CATKinLengthCmd2,
                |             CATKinAngle1Cmd2,
                |             CATKinLength1Cmd2,
                |             CATKinAngle2Cmd2,
                |             CATKinLength2Cmd2

        :return: int
        """

        return self.com_object.CommandType

    @property
    def current_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentValue() As double (Read Only)
                |     Returns the current value of a Command.
                | 
                |     Parameters:
                | 
                |         oCurrentValue
                | 
                |             Units values:
                | 
                |             Millimiters
                |             for length commands.
                |             Degrees
                |             for angle commands.

        :return: float
        """

        return self.com_object.CurrentValue

    @property
    def joint(self) -> EngConnection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Joint() As EngConnection (Read Only)
                |     Returns the joint corresponding to the command.
                | 
                |     Parameters:
                | 
                |         oJoint

        :return: EngConnection
        """

        return EngConnection(self.com_object.Joint)

    @property
    def lower_limit(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LowerLimit() As double (Read Only)
                |     Returns the lower limit of the command if it is set. Otherwise returns 0 by
                |     default.
                | 
                |     Parameters:
                | 
                |         oLowerLimit
                | 
                |             Units values:
                | 
                |             Millimiters
                |             for length commands.
                |             Degrees
                |             for angle commands.

        :return: float
        """

        return self.com_object.LowerLimit

    @property
    def upper_limit(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UpperLimit() As double (Read Only)
                |     Returns the upper limit of the command if it is set. Otherwise returns 0 by
                |     default.
                | 
                |     Parameters:
                | 
                |         oUpperLimit
                | 
                |             Units values:
                | 
                |             Millimiters
                |             for length commands.
                |             Degrees
                |             for angle commands.

        :return: float
        """

        return self.com_object.UpperLimit

    def is_lower_limit_set(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsLowerLimitSet() As boolean
                |     Returns the status of the lower limit of the command.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             The status of the lower limit.

        :return: bool
        """
        return self.com_object.IsLowerLimitSet()

    def is_upper_limit_set(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsUpperLimitSet() As boolean
                |     Returns the status of the upper limit of the command.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             The status of the upper limit.

        :return: bool
        """
        return self.com_object.IsUpperLimitSet()

    def __repr__(self):
        return f'KinCommand(name="{self.name}")'
