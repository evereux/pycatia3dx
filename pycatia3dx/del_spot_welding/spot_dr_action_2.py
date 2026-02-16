"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotDrAction2(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrAction2

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def config(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Config() As short
                |     Gets the Robot Configuration for the DR Action
                | 
                |     Parameters:
                | 
                |         iConfig
                |             The Robot Configuration 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: int
        """

        return self.com_object.Config

    @config.setter
    def config(self, value: int):
        """
        :param int value:
        """

        self.com_object.Config = value

    @property
    def elbow_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ElbowAngle() As double
                |     Gets the Elbow angle for the DR Action
                | 
                |     Parameters:
                | 
                |         oElbowAngle
                |             The Elbow angle. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: float
        """

        return self.com_object.ElbowAngle

    @elbow_angle.setter
    def elbow_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.ElbowAngle = value

    @property
    def interpolation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterpolationMode() As short
                |     Gets the Interpolation Mode for the DR Action
                | 
                |     Parameters:
                | 
                |         oInterpolationMode
                |             The Interpolation Mode. 0 for NEARMODE, // Shortest Angle Strategy
                |             1 for KEEPCFG_KEEPTURN // The posture and the turn values are unchanged at the
                |             end of move 2 for KEEPCFG_SETTURN, // The turn values in the robot motion is
                |             applied at the end of move 3 for SETCFG_KEEPTURN, // The posture set in the
                |             robot motion is applied at the end of move 4 for SETCFG_SETTURN // The posture
                |             and the turn values in the robot motion is applied at the end of move
                |             
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: int
        """

        return self.com_object.InterpolationMode

    @interpolation_mode.setter
    def interpolation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.InterpolationMode = value

    @property
    def motion_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionType() As short
                |     Gets the Motion Type for the DR Action
                | 
                |     Parameters:
                | 
                |         oMotionType
                |             The Motion Type. 0 for JointMOVE, // Interpolated movement of
                |             joints 1 for LINEARMOVE // The TCP moves in a linear fashion 2 for PREDEFINED,
                |             // PREDEFINED MOVE, JOINT Interpolated 3 for CIRCULAR, // The TCP moves in a
                |             circular fashion 4 for CIRCULARVIA // via point in the TCP moves in a circular
                |             fashionon 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: int
        """

        return self.com_object.MotionType

    @motion_type.setter
    def motion_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.MotionType = value

    @property
    def tcp_orientation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TCPOrientationMode() As short
                |     Gets the TCP Orientation Mode for the DR Action
                | 
                |     Parameters:
                | 
                |         oOrientationMode
                |             The TCP Orientation Mode 0 for TCPOrientOneAxis 1 for
                |             TCPOrientTwoAxis 2 for TCPOrientThreeAxis 3 for TCPOrientWristAxis
                |             
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: int
        """

        return self.com_object.TCPOrientationMode

    @tcp_orientation_mode.setter
    def tcp_orientation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.TCPOrientationMode = value

    @property
    def turn_numbers(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TurnNumbers() As CATSafeArrayVariant
                |     Gets the Turn Numbers for the DR Action
                | 
                |     Parameters:
                | 
                |         oTurnNumbers
                |             List of Turn Numbers. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: tuple
        """

        return self.com_object.TurnNumbers

    @turn_numbers.setter
    def turn_numbers(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.TurnNumbers = value

    @property
    def turn_signs(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TurnSigns() As CATSafeArrayVariant
                |     Gets the Turn Signs for the DR Action
                | 
                |     Parameters:
                | 
                |         oTurnSigns
                |             List of Turn Signs. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: tuple
        """

        return self.com_object.TurnSigns

    @turn_signs.setter
    def turn_signs(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.TurnSigns = value

    def get_auxiliary_axis_values(self, i_auxiliary_dev_mca: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAuxiliaryAxisValues(AnyObject iAuxiliaryDevMCA) As
                | CATSafeArrayVariant
                |     Retrieves the Auxiliary device Joint values for the DR
                |     Action
                | 
                |     Parameters:
                | 
                |         iAuxiliaryDevMCA
                |             The List of User profiles to be used. 
                |         oAuxiliaryAxisValues
                |             List of joint values of the device. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param AnyObject i_auxiliary_dev_mca:
        :return: tuple
        """
        return self.com_object.GetAuxiliaryAxisValues(i_auxiliary_dev_mca.com_object)

    def get_user_profiles_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetUserProfilesList() As CATSafeArrayVariant
                |     Gets the user profiles for the DR Action
                | 
                |     Parameters:
                | 
                |         oUserProfileList
                |             The List of User profiles to be used. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: tuple
        """
        return self.com_object.GetUserProfilesList()

    def set_auxiliary_axis_values(self, i_auxiliary_dev_mca: AnyObject, i_auxiliary_axis_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAuxiliaryAxisValues(AnyObject iAuxiliaryDevMCA,CATSafeArrayVariant
                | iAuxiliaryAxisValues)
                |     Sets the Auxiliary device Joint values for the DR Action
                | 
                |     Parameters:
                | 
                |         iAuxiliaryDevMCA
                |             The List of User profiles to be used. 
                |         iAuxiliaryAxisValues
                |             List of joint values of the device. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param AnyObject i_auxiliary_dev_mca:
        :param tuple i_auxiliary_axis_values:
        :return: None
        """
        return self.com_object.SetAuxiliaryAxisValues(i_auxiliary_dev_mca.com_object, i_auxiliary_axis_values)

    def set_user_profiles_list(self, i_user_profile_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetUserProfilesList(CATSafeArrayVariant iUserProfileList)
                |     Sets the user profiles for the DR Action
                |
                |     Parameters:
                |
                |         iUserProfileList
                |             The List of User profiles to be used.
                |
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param tuple i_user_profile_list:
        :return: None
        """
        return self.com_object.SetUserProfilesList(i_user_profile_list)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_user_profiles_list'
        # vba_code = """
        # Public Function set_user_profiles_list(spot_dr_action2)
        #     Dim iUserProfileList (2)
        #     spot_dr_action2.SetUserProfilesList iUserProfileList
        #     set_user_profiles_list = iUserProfileList
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SpotDrAction2(name="{self.name}")'
