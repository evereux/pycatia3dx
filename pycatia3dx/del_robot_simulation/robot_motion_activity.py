"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_robot_simulation.tag_point import TagPoint


class RobotMotionActivity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RobotMotionActivity
                | 
                | Interface representing a RobotMotion.
                | 
                | Role: This interface is used to get and set motion attributes on a robot
                | motion
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def accuracy_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccuracyProfile() As AnyObject
                |     This property returns and sets Accuracy profile used by the robot
                |     Motion.
                | 
                |     Returns:
                |         oAccuracyProfile The Accuracy profile used. 
                |     Parameters:
                | 
                |         iAccuracyProfile
                |             The Accuracy profile to use. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oAccuracyProfile
                |         Set oAccuracyProfile = objRobotMotion.AccuracyProfile

        :return: AnyObject
        """

        return AnyObject(self.com_object.AccuracyProfile)

    @accuracy_profile.setter
    def accuracy_profile(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.AccuracyProfile = value

    @property
    def cartesian_target(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CartesianTarget() As CATSafeArrayVariant
                |     This property returns and sets the cartesian target of the robot
                |     motion.
                | 
                |     Returns:
                |         oCartesianTarget The cartesian target. 
                |     Parameters:
                | 
                |         iCartesianTarget
                |             The cartesian target. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oCartesianTarget
                |                   ......
                |         Dim oTempRobotMotion As AnyObject
                |         Set oTempRobotMotion = objRobotMotion
                |         oTempRobotMotion.CartesianTarget = oCartesianTarget

        :return: tuple
        """

        return self.com_object.CartesianTarget

    @cartesian_target.setter
    def cartesian_target(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.CartesianTarget = value

    @property
    def config(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Config() As short
                |     This property returns and sets the robot posture used by the robot
                |     motion.
                | 
                |     Returns:
                |         oConfig The robot posture used. 
                |     Parameters:
                | 
                |         iConfig
                |             The robot posture to use. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oConfig
                |         oConfig = objRobotMotion.Config

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
                |     This property returns and sets the Elbow angle used by the robot
                |     motion.
                | 
                |     Returns:
                |         oElbowAngle The elbow angle used. 
                |     Parameters:
                | 
                |         iElbowAngle
                |             The elbow angle to use. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim iElbowAngle
                |                   ......
                |         objRobotMotion.ElbowAngle = iElbowAngle

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
    def home_target(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HomeTarget() As CATBSTR
                |     This property returns and sets the Home target of the robot
                |     motion.
                | 
                |     Returns:
                |         oHomeTarget The Home Target Name. 
                |     Parameters:
                | 
                |         iHomeTarget
                |             The Home Target Name. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......

        :return: str
        """

        return self.com_object.HomeTarget

    @home_target.setter
    def home_target(self, value: str):
        """
        :param str value:
        """

        self.com_object.HomeTarget = value

    @property
    def interpolation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterpolationMode() As short
                |     This property returns and sets the interpolation mode of the robot motion.
                |     The Interpolation Mode. 0 for NEARMODE, // Shortest Angle Strategy 1 for
                |     KEEPCFG_KEEPTURN // The posture and the turn values are unchanged at the end of
                |     move 2 for KEEPCFG_SETTURN, // The turn values in the robot motion is applied
                |     at the end of move 3 for SETCFG_KEEPTURN, // The posture set in the robot
                |     motion is applied at the end of move 4 for SETCFG_SETTURN // The posture and
                |     the turn values in the robot motion is applied at the end of
                |     move
                | 
                |     Returns:
                |         oInterpolationMode The interpolation mode used. 
                |     Parameters:
                | 
                |         iInterpolationMode
                |             The interpolation mode to use. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oInterpolationMode
                |         oInterpolationMode = objRobotMotion.InterpolationMode

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
    def joint_target(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property JointTarget() As CATSafeArrayVariant
                |     This property returns and sets the Joint target of the robot
                |     motion.
                | 
                |     Returns:
                |         oJointTarget The List of Joint DOF values. 
                |     Parameters:
                | 
                |         iJointTarget
                |             The List of Joint DOF values. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oJointTarget
                |                   ......
                |         Dim oTempRobotMotion As AnyObject
                |         Set oTempRobotMotion = objRobotMotion
                |         oTempRobotMotion.JointTarget = oJointTarget

        :return: tuple
        """

        return self.com_object.JointTarget

    @joint_target.setter
    def joint_target(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.JointTarget = value

    @property
    def keep_accuracy_profile(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KeepAccuracyProfile() As boolean
                |     This property determines whether the Accuracy profile stored in the robot
                |     motion is to used during simulation. Keep Accuracy Profile TRUE is profile
                |     stored is not to be used. FALSE is profile stored is to be
                |     used.
                | 
                |     Returns:
                |         oKeepAccuracyProfile The Keep Accuracy Profile mode. 
                |     Parameters:
                | 
                |         iKeepAccuracyProfile
                |             The Keep Accuracy Profile mode. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim iKeepAccuracyProfile As Boolean
                |         iKeepAccuracyProfile = False
                |         objRobotMotion.KeepAccuracyProfile = iKeepAccuracyProfile

        :return: bool
        """

        return self.com_object.KeepAccuracyProfile

    @keep_accuracy_profile.setter
    def keep_accuracy_profile(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.KeepAccuracyProfile = value

    @property
    def keep_motion_profile(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KeepMotionProfile() As boolean
                |     This property determines whether the Motion profile stored in the robot
                |     motion is to used during simulation. Keep Motion Profile TRUE is profile stored
                |     is not to be used. FALSE is profile stored is to be used.
                | 
                |     Returns:
                |         oKeepMotionProfile The Keep Motion Profile mode. 
                |     Parameters:
                | 
                |         iKeepMotionProfile
                |             The Keep Motion Profile mode. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim iKeepMotionProfile As Boolean
                |         iKeepMotionProfile = False
                |         objRobotMotion.KeepMotionProfile = iKeepMotionProfile

        :return: bool
        """

        return self.com_object.KeepMotionProfile

    @keep_motion_profile.setter
    def keep_motion_profile(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.KeepMotionProfile = value

    @property
    def keep_object_profile(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KeepObjectProfile() As boolean
                |     This property determines whether the Object profile stored in the robot
                |     motion is to used during simulation. Keep Object Profile TRUE is profile stored
                |     is not to be used. FALSE is profile stored is to be used.
                | 
                |     Returns:
                |         oKeepObjectProfile The Keep Object Profile mode. 
                |     Parameters:
                | 
                |         iKeepObjectProfile
                |             The Keep Object Profile mode. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim iKeepObjectProfile As Boolean
                |         iKeepObjectProfile = False
                |         objRobotMotion.KeepObjectProfile = iKeepObjectProfile

        :return: bool
        """

        return self.com_object.KeepObjectProfile

    @keep_object_profile.setter
    def keep_object_profile(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.KeepObjectProfile = value

    @property
    def keep_tool_profile(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KeepToolProfile() As boolean
                |     This property determines whether the tool profile stored in the robot
                |     motion is to used during simulation. Keep Tool Profile TRUE is profile stored
                |     is not to be used. FALSE is profile stored is to be used.
                | 
                |     Returns:
                |         oKeepToolProfile The Keep Tool Profile mode. 
                |     Parameters:
                | 
                |         iKeepToolProfile
                |             The Keep Tool Profile mode. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim iKeepToolProfile As Boolean
                |         iKeepToolProfile = False
                |         objRobotMotion.KeepToolProfile = iKeepToolProfile

        :return: bool
        """

        return self.com_object.KeepToolProfile

    @keep_tool_profile.setter
    def keep_tool_profile(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.KeepToolProfile = value

    @property
    def motion_groups(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionGroups() As CATSafeArrayVariant (Read Only)
                |     Retreives the list of motion groups managed by the robot
                |     motion.
                | 
                |     Returns:
                |         oMotionGroups The list of motion groups. 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oMotionGroups
                |         oMotionGroups = objRobotMotion.MotionGroups

        :return: tuple
        """

        return self.com_object.MotionGroups

    @property
    def motion_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionProfile() As AnyObject
                |     This property returns and sets Motion profile used by the robot
                |     motion.
                | 
                |     Returns:
                |         oMotionProfile The Motion profile used. 
                |     Parameters:
                | 
                |         iMotionProfile
                |             The Motion profile to use. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oMotionProfile
                |         Set oMotionProfile = objRobotMotion.MotionProfile

        :return: AnyObject
        """

        return AnyObject(self.com_object.MotionProfile)

    @motion_profile.setter
    def motion_profile(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.MotionProfile = value

    @property
    def motion_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionType() As short
                |     This property returns and sets the motion type of the robot motion. The
                |     Motion Type. 0 for JointMOVE, // Interpolated movement of joints 1 for
                |     LINEARMOVE // The TCP moves in a linear fashion 2 for PREDEFINED, // PREDEFINED
                |     MOVE, JOINT Interpolated 3 for CIRCULAR, // The TCP moves in a circular fashion
                |     4 for CIRCULARVIA // via point in the TCP moves in a circular
                |     fashionon
                | 
                |     Returns:
                |         oMotionType The motion type used. 
                |     Parameters:
                | 
                |         iMotionType
                |             The motion type to use. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oMotionType
                |         oMotionType = objRobotMotion.MotionType

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
    def object_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ObjectProfile() As AnyObject
                |     This property returns and sets Object profile used by the robot
                |     Motion.
                | 
                |     Returns:
                |         oObjectProfile The Object profile used. 
                |     Parameters:
                | 
                |         iObjectProfile
                |             The Object profile to use. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oObjectProfile
                |         Set oObjectProfile = objRobotMotion.ObjectProfile

        :return: AnyObject
        """

        return AnyObject(self.com_object.ObjectProfile)

    @object_profile.setter
    def object_profile(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.ObjectProfile = value

    @property
    def orientation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientationMode() As short
                |     This property returns and sets the Orientation Mode of the robot motion.
                |     The Orientaion Mode 0 for TCPOrientOneAxis 1 for TCPOrientTwoAxis 2 for
                |     TCPOrientThreeAxis 3 for TCPOrientWristAxis
                | 
                |     Returns:
                |         oOrientationMode The Orientation Mode used. 
                |     Parameters:
                | 
                |         iOrientationMode
                |             The Orientation Mode to use. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oOrientationMode
                |         oOrientationMode = objRobotMotion.OrientationMode

        :return: int
        """

        return self.com_object.OrientationMode

    @orientation_mode.setter
    def orientation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.OrientationMode = value

    @property
    def tag_target(self) -> TagPoint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TagTarget() As TagPoint (Read Only)
                |     This property returns the Tag target of the robot motion.
                | 
                |     Returns:
                |         oTag The underlying Tag. 
                |     Parameters:
                | 
                |         iJointTarget
                |             The List of Joint DOF values. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oTag As Tag
                |         Set oTag = objRobotMotion.TagTarget

        :return: TagPoint
        """

        return TagPoint(self.com_object.TagTarget)

    @property
    def target_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TargetList() As CATSafeArrayVariant (Read Only)
                |     This property retrieves the Target List of the robot
                |     motion.
                | 
                |     Parameters:
                | 
                |         oTargetList
                |             The List of Targets. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oTargetList
                |         oTargetList = objRobotMotion.TargetList

        :return: tuple
        """

        return self.com_object.TargetList

    @property
    def target_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TargetType() As short (Read Only)
                |     This property retrieves the Target Type of the robot motion. Target can be
                |     Cartesian(index=0),Joint(index=1), Tag(index=2) or
                |     Home(index=3)
                | 
                |     Parameters:
                | 
                |         oTargetType
                |             Type of the Target. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oTargetType
                |         oTargetType = objRobotMotion.TargetType

        :return: int
        """

        return self.com_object.TargetType

    @property
    def tool_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ToolProfile() As AnyObject
                |     This property returns and sets tool profile used by the robot
                |     motion.
                | 
                |     Returns:
                |         oToolProfile The tool profile used. 
                |     Parameters:
                | 
                |         iToolProfile
                |             The tool profile to use. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oToolProfile
                |         Set oToolProfile = objRobotMotion.ToolProfile

        :return: AnyObject
        """

        return AnyObject(self.com_object.ToolProfile)

    @tool_profile.setter
    def tool_profile(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.ToolProfile = value

    @property
    def turn_numbers(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TurnNumbers() As CATSafeArrayVariant
                |     This property returns and sets the turn numbers of the robot
                |     motion.
                | 
                |     Returns:
                |         oTurnNumbers The underlying List of Turn Numbers. 
                |     Parameters:
                | 
                |         iTurnNumbers
                |             The List of Turn numbers to be set. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oTurnNumbers
                |         oTurnNumbers = objRobotMotion.TurnNumbers

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
                |     This property returns and sets the turn signs of the robot
                |     motion.
                | 
                |     Returns:
                |         oTurnSigns The underlying List of Turn Signs. 
                |     Parameters:
                | 
                |         iTurnSigns
                |             The List of Turn signs to be set. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oTurnSigns
                |         oTurnSigns = objRobotMotion.TurnSigns

        :return: tuple
        """

        return self.com_object.TurnSigns

    @turn_signs.setter
    def turn_signs(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.TurnSigns = value

    @property
    def user_profile_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserProfileList() As CATSafeArrayVariant
                |     This property returns and sets the user profiles used by the robot
                |     motion.
                | 
                |     Returns:
                |         oUserProfileList The List of User profiles used. 
                |     Parameters:
                | 
                |         iUserProfileList
                |             The List of User profiles to be used. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oUserProfileList
                |         oUserProfileList = objRobotMotion.UserProfileList

        :return: tuple
        """

        return self.com_object.UserProfileList

    @user_profile_list.setter
    def user_profile_list(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.UserProfileList = value

    def get_auxillary_axis_home(self, i_auxillary_dev_mca: AnyObject) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAuxillaryAxisHome(AnyObject iAuxillaryDevMCA) As
                | CATBSTR
                |     Retrieves the underlying Auxillary device Home.
                | 
                |     Parameters:
                | 
                |         iAuxillaryDevMCA
                |             The MCA for the auxiliary device 
                |         oHomeName
                |             Home name used for the given Auxillary device. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......

        :param AnyObject i_auxillary_dev_mca:
        :return: str
        """
        return self.com_object.GetAuxillaryAxisHome(i_auxillary_dev_mca.com_object)

    def get_auxillary_axis_values(self, i_auxillary_dev_mca: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAuxillaryAxisValues(AnyObject iAuxillaryDevMCA) As
                | CATSafeArrayVariant
                |     Retrieves the Auxillary device Joint values.
                | 
                |     Parameters:
                | 
                |         iAuxillaryDevMCA
                |             The MCA for the auxiliary device 
                |         oAuxillaryAxisValues
                |             List of joint values of the device. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......

        :param AnyObject i_auxillary_dev_mca:
        :return: tuple
        """
        return self.com_object.GetAuxillaryAxisValues(i_auxillary_dev_mca.com_object)

    def get_tag_target(self, o_tag: TagPoint, o_tag_owner: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTagTarget(TagPoint oTag,AnyObject oTagOwner)
                |     Retreives Tag target of the robot motion.
                | 
                |     Returns:
                |         oTag The underlying Tag. 
                |     Returns:
                |         oTagOwner The product occurrence which aggregates the Tag (in case the
                |         Tag is in PRODUCT DAG). In case the trajectory is not in PRODUCT DAG then Root
                |         Product is returned. 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......

        :param TagPoint o_tag:
        :param AnyObject o_tag_owner:
        :return: None
        """
        return self.com_object.GetTagTarget(o_tag.com_object, o_tag_owner.com_object)

    def get_target_list_for_motion_group(self, i_motion_group: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTargetListForMotionGroup(AnyObject iMotionGroup) As
                | CATSafeArrayVariant
                |     Retrieves the targets listfor a specific motion group.
                | 
                |     Parameters:
                | 
                |         oTargetList
                |             The List of Targets. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim oTargetListForMG(10)
                |         Call objRobotMotion.GetTargetListForMotionGroup(iMotionGroup,
                |         oTargetListForMG)

        :param AnyObject i_motion_group:
        :return: tuple
        """
        return self.com_object.GetTargetListForMotionGroup(i_motion_group.com_object)

    def set_auxillary_axis_home(self, i_auxillary_dev_mca: AnyObject, i_home_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAuxillaryAxisHome(AnyObject iAuxillaryDevMCA,CATBSTR
                | iHomeName)
                |     Sets the underlying Auxillary device Home.
                | 
                |     Parameters:
                | 
                |         iAuxillaryDevMCA
                |             The MCA for the auxiliary device 
                |         iHomeName
                |             Home name set for the given Auxillary device. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......

        :param AnyObject i_auxillary_dev_mca:
        :param str i_home_name:
        :return: None
        """
        return self.com_object.SetAuxillaryAxisHome(i_auxillary_dev_mca.com_object, i_home_name)

    def set_auxillary_axis_values(self, i_auxillary_dev_mca: AnyObject, i_auxillary_axis_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAuxillaryAxisValues(AnyObject iAuxillaryDevMCA,CATSafeArrayVariant
                | iAuxillaryAxisValues)
                |     Sets the Auxillary device Joint values.
                | 
                |     Parameters:
                | 
                |         iAuxillaryDevMCA
                |             The MCA for the auxiliary device 
                |         iAuxillaryAxisValues
                |             List of joint values of the device. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......

        :param AnyObject i_auxillary_dev_mca:
        :param tuple i_auxillary_axis_values:
        :return: None
        """
        return self.com_object.SetAuxillaryAxisValues(i_auxillary_dev_mca.com_object, i_auxillary_axis_values)

    def set_tag_target(self, i_tag: TagPoint, i_tag_owner: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTagTarget(TagPoint iTag,AnyObject iTagOwner)
                |     Sets the Tag target of the robot motion.
                | 
                |     Parameters:
                | 
                |         iTrajectory
                |             The underlying Tag. 
                |         iTrajectoryOwner
                |             The product occurrence which aggregates the Tag (in case the Tag is
                |             in PRODUCT DAG). 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objRobotMotion As RobotMotionActivity
                |                   ......
                |         Dim iTag As AnyObject
                |         Dim iTagOwner As AnyObject
                |                   ......
                |         Call oRobotMotion3.SetTagTarget(oTag, iTagOwner)

        :param TagPoint i_tag:
        :param AnyObject i_tag_owner:
        :return: None
        """
        return self.com_object.SetTagTarget(i_tag.com_object, i_tag_owner.com_object)

    def __repr__(self):
        return f'RobotMotionActivity(name="{ self.name }")'
