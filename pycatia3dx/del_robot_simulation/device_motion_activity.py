"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DeviceMotionActivity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DeviceMotionActivity
                | 
                | Interface representing a DeviceMotion.
                | 
                | Role: This interface is used to get and set motion attributes on a device
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
                |     This property returns and sets Accuracy profile used by the device
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
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim oAccuracyProfile
                |         Set oAccuracyProfile = objDeviceMotion.AccuracyProfile

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
    def home_target(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HomeTarget() As CATBSTR
                |     This property returns and sets the Home target of the device
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
                |         Dim objDeviceMotion As DeviceMotionActivity
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
    def joint_target(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property JointTarget() As CATSafeArrayVariant
                |     This property returns and sets the Joint target of the device
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
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim oJointTarget
                |                   ......
                |         Dim oTempDeviceMotion As AnyObject
                |         Set oTempDeviceMotion = objDeviceMotion
                |         oTempDeviceMotion.JointTarget = oJointTarget

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
                |     This property determines whether the Accuracy profile stored in the device
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
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim iKeepAccuracyProfile As Boolean
                |         iKeepAccuracyProfile = False
                |         objDeviceMotion.KeepAccuracyProfile = iKeepAccuracyProfile

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
                |     This property determines whether the Motion profile stored in the device
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
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim iKeepMotionProfile As Boolean
                |         iKeepMotionProfile = False
                |         objDeviceMotion.KeepMotionProfile = iKeepMotionProfile

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
    def motion_groups(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionGroups() As CATSafeArrayVariant (Read Only)
                |     Retreives the list of motion groups managed by the device
                |     motion.
                | 
                |     Returns:
                |         oMotionGroups The list of motion groups. 
                |     Example:
                |
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim oMotionGroups
                |         oMotionGroups = objDeviceMotion.MotionGroups

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
                |     This property returns and sets Motion profile used by the device
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
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim oMotionProfile
                |         Set oMotionProfile = objDeviceMotion.MotionProfile

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
    def target_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TargetList() As CATSafeArrayVariant (Read Only)
                |     This property retrieves the Target List of the device
                |     motion.
                | 
                |     Parameters:
                | 
                |         oTargetList
                |             The List of Targets. 
                | 
                |     Example:
                |
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim oTargetList
                |         oTargetList = objDeviceMotion.TargetList

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
                |     This property retrieves the Target Type of the device motion. Target can be
                |     Joint(index=0) or Home(index=1)
                | 
                |     Parameters:
                | 
                |         oTargetType
                |             Type of the Target. 
                | 
                |     Example:
                |
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim oTargetType
                |         oTargetType = objDeviceMotion.TargetType

        :return: int
        """

        return self.com_object.TargetType

    @property
    def user_profile_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserProfileList() As CATSafeArrayVariant
                |     This property returns and sets the user profiles used by the device
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
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim oUserProfileList
                |         oUserProfileList = objDeviceMotion.UserProfileList

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
                |            Dim objDeviceMotion As DeviceMotionActivity
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
                |            Dim objDeviceMotion As DeviceMotionActivity
                |                   ......

        :param AnyObject i_auxillary_dev_mca:
        :return: tuple
        """
        return self.com_object.GetAuxillaryAxisValues(i_auxillary_dev_mca.com_object)

    def get_target_list_for_motion_group(self, i_motion_group: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTargetListForMotionGroup(AnyObject iMotionGroup) As
                | CATSafeArrayVariant
                |     This property retrieves the Target List for a specific motion
                |     group.
                | 
                |     Parameters:
                | 
                |         oTargetList
                |             The List of Targets. 
                | 
                |     Example:
                |
                |         Dim objDeviceMotion As DeviceMotionActivity
                |                   ......
                |         Dim oTargetListForMG(10)
                |         Call objDeviceMotion.GetTargetListForMotionGroup(iMotionGroup,
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
                |            Dim objDeviceMotion As DeviceMotionActivity
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
                |            Dim objDeviceMotion As DeviceMotionActivity
                |                   ......

        :param AnyObject i_auxillary_dev_mca:
        :param tuple i_auxillary_axis_values:
        :return: None
        """
        return self.com_object.SetAuxillaryAxisValues(i_auxillary_dev_mca.com_object, i_auxillary_axis_values)

    def __repr__(self):
        return f'DeviceMotionActivity(name="{ self.name }")'
