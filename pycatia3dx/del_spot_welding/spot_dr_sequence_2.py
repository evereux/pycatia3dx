"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotDrSequence2(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrSequence2

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_auxiliary_axis_values(self, i_pos_index: int, i_auxiliary_dev_mca: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAuxiliaryAxisValues(short iPosIndex,AnyObject iAuxiliaryDevMCA) As
                | CATSafeArrayVariant
                |     Retrieves the Auxiliary device Joint values for the specified
                |     index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iAuxiliaryDevMCA
                |             The List of User profiles to be used. 
                |         oAuxiliaryAxisValues
                |             List of joint values of the device. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param AnyObject i_auxiliary_dev_mca:
        :return: tuple
        """
        return self.com_object.GetAuxiliaryAxisValues(i_pos_index, i_auxiliary_dev_mca.com_object)

    def get_config(self, i_pos_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetConfig(short iPosIndex) As short
                |     Gets the Robot Configuration for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iConfig
                |             The Robot Configuration 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: int
        """
        return self.com_object.GetConfig(i_pos_index)

    def get_elbow_angle(self, i_pos_index: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetElbowAngle(short iPosIndex) As double
                |     Gets the Elbow angle for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oElbowAngle
                |             The Elbow angle. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: float
        """
        return self.com_object.GetElbowAngle(i_pos_index)

    def get_interpolation_mode(self, i_pos_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInterpolationMode(short iPosIndex) As short
                |     Gets the Interpolation Mode for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
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

        :param int i_pos_index:
        :return: int
        """
        return self.com_object.GetInterpolationMode(i_pos_index)

    def get_motion_type(self, i_pos_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMotionType(short iPosIndex) As short
                |     Gets the Motion Type for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oMotionType
                |             The Motion Type. 0 for JointMOVE, // Interpolated movement of
                |             joints 1 for LINEARMOVE // The TCP moves in a linear fashion 2 for PREDEFINED,
                |             // PREDEFINED MOVE, JOINT Interpolated 3 for CIRCULAR, // The TCP moves in a
                |             circular fashion 4 for CIRCULARVIA // via point in the TCP moves in a circular
                |             fashionon 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: int
        """
        return self.com_object.GetMotionType(i_pos_index)

    def get_tcp_orientation_mode(self, i_pos_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTCPOrientationMode(short iPosIndex) As short
                |     Gets the TCP Orientation Mode for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oOrientationMode
                |             The TCP Orientation Mode 0 for TCPOrientOneAxis 1 for
                |             TCPOrientTwoAxis 2 for TCPOrientThreeAxis 3 for TCPOrientWristAxis
                |             
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: int
        """
        return self.com_object.GetTCPOrientationMode(i_pos_index)

    def get_turn_numbers(self, i_pos_index: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTurnNumbers(short iPosIndex) As CATSafeArrayVariant
                |     Gets the Turn Numbers for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oTurnNumbers
                |             List of Turn Numbers. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: tuple
        """
        return self.com_object.GetTurnNumbers(i_pos_index)

    def get_turn_signs(self, i_pos_index: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTurnSigns(short iPosIndex) As CATSafeArrayVariant
                |     Gets the Turn Signs for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oTurnSigns
                |             List of Turn Signs. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: tuple
        """
        return self.com_object.GetTurnSigns(i_pos_index)

    def get_user_profile_list(self, i_pos_index: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetUserProfileList(short iPosIndex) As
                | CATSafeArrayVariant
                |     Gets the user profiles for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oUserProfileList
                |             The List of User profiles to be used. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: tuple
        """
        return self.com_object.GetUserProfileList(i_pos_index)

    def set_action_prefix_name(self, i_prefix_name_bstr: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetActionPrefixName(CATBSTR iPrefixNameBSTR)
                |     Sets the Prefix for the Actions in the Sequence
                | 
                |     Parameters:
                | 
                |         iPrefixNameBSTR
                |             The prefix to be used for the Actions inside the sequence
                |             
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param str i_prefix_name_bstr:
        :return: None
        """
        return self.com_object.SetActionPrefixName(i_prefix_name_bstr)

    def set_auxiliary_axis_values(self, i_pos_index: int, i_auxiliary_dev_mca: AnyObject, i_auxiliary_axis_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAuxiliaryAxisValues(short iPosIndex,AnyObject
                | iAuxiliaryDevMCA,CATSafeArrayVariant iAuxiliaryAxisValues)
                |     Sets the Auxiliary device Joint values for the specified
                |     index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iAuxiliaryDevMCA
                |             The List of User profiles to be used. 
                |         iAuxiliaryAxisValues
                |             List of joint values of the device. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param AnyObject i_auxiliary_dev_mca:
        :param tuple i_auxiliary_axis_values:
        :return: None
        """
        return self.com_object.SetAuxiliaryAxisValues(i_pos_index, i_auxiliary_dev_mca.com_object, i_auxiliary_axis_values)

    def set_config(self, i_pos_index: int, i_config: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetConfig(short iPosIndex,short iConfig)
                |     Sets the Robot Configuration for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oConfig
                |             The Robot Configuration 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param int i_config:
        :return: None
        """
        return self.com_object.SetConfig(i_pos_index, i_config)

    def set_elbow_angle(self, i_pos_index: int, i_elbow_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetElbowAngle(short iPosIndex,double iElbowAngle)
                |     Sets the Elbow angle for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iElbowAngle
                |             The Elbow angle. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param float i_elbow_angle:
        :return: None
        """
        return self.com_object.SetElbowAngle(i_pos_index, i_elbow_angle)

    def set_interpolation_mode(self, i_pos_index: int, i_interpolation_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInterpolationMode(short iPosIndex,short
                | iInterpolationMode)
                |     Sets the Interpolation Mode for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iInterpolationMode
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

        :param int i_pos_index:
        :param int i_interpolation_mode:
        :return: None
        """
        return self.com_object.SetInterpolationMode(i_pos_index, i_interpolation_mode)

    def set_motion_type(self, i_pos_index: int, i_motion_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionType(short iPosIndex,short iMotionType)
                |     Sets the Motion Type for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iMotionType
                |             The Motion Type. 0 for JointMOVE, // Interpolated movement of
                |             joints 1 for LINEARMOVE // The TCP moves in a linear fashion 2 for PREDEFINED,
                |             // PREDEFINED MOVE, JOINT Interpolated 3 for CIRCULAR, // The TCP moves in a
                |             circular fashion 4 for CIRCULARVIA // via point in the TCP moves in a circular
                |             fashionon 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param int i_motion_type:
        :return: None
        """
        return self.com_object.SetMotionType(i_pos_index, i_motion_type)

    def set_tcp_orientation_mode(self, i_pos_index: int, i_orientation_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPOrientationMode(short iPosIndex,short
                | iOrientationMode)
                |     Sets the TCP Orientation Mode for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iOrientationMode
                |             The TCP Orientation Mode 0 for TCPOrientOneAxis 1 for
                |             TCPOrientTwoAxis 2 for TCPOrientThreeAxis 3 for TCPOrientWristAxis
                |             
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param int i_orientation_mode:
        :return: None
        """
        return self.com_object.SetTCPOrientationMode(i_pos_index, i_orientation_mode)

    def set_turn_numbers(self, i_pos_index: int, i_turn_numbers: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTurnNumbers(short iPosIndex,CATSafeArrayVariant
                | iTurnNumbers)
                |     Sets the Turn Numbers for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iTurnNumbers
                |             List of Turn Numbers. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param tuple i_turn_numbers:
        :return: None
        """
        return self.com_object.SetTurnNumbers(i_pos_index, i_turn_numbers)

    def set_turn_signs(self, i_pos_index: int, i_turn_signs: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTurnSigns(short iPosIndex,CATSafeArrayVariant
                | iTurnSigns)
                |     Sets the Turn Signs for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iTurnSigns
                |             List of Turn Signs. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param tuple i_turn_signs:
        :return: None
        """
        return self.com_object.SetTurnSigns(i_pos_index, i_turn_signs)

    def set_user_profile_list(self, i_pos_index: int, i_user_profile_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUserProfileList(short iPosIndex,CATSafeArrayVariant
                | iUserProfileList)
                |     Sets the user profiles for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iUserProfileList
                |             The List of User profiles to be used. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error 

        :param int i_pos_index:
        :param tuple i_user_profile_list:
        :return: None
        """
        return self.com_object.SetUserProfileList(i_pos_index, i_user_profile_list)

    def __repr__(self):
        return f'SpotDrSequence2(name="{ self.name }")'
