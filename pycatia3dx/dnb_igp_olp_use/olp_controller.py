"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_resource_builder.rsc_applicative_profiles_mgr import RscApplicativeProfilesMgr
from pycatia3dx.del_resource_builder.rsc_user_profiles_mgr import RscUserProfilesMgr
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_cartesian_safety_zones import OLPCartesianSafetyZones
from pycatia3dx.dnb_igp_olp_use.olp_profiles import OLPProfiles
from pycatia3dx.dnb_igp_olp_use.olp_tool_volumes import OLPToolVolumes
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform
from pycatia3dx.types.general import CATVariant


class OLPController(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpController
                | 
                | Interface for accessing a device (or controller's) properties.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved from a OlpMotionGroup.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def acceleration_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccelerationMode() As DELOlpAccelerationMode
                |     The property AccelerationMode.

        :return: DELOlpAccelerationMode
        """

        return self.com_object.AccelerationMode

    @acceleration_mode.setter
    def acceleration_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.AccelerationMode = value

    @property
    def accuracy_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccuracyProfileList() As OlpProfiles (Read Only)
                |     The list of all accuracy profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.AccuracyProfileList)

    @property
    def application_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApplicationType() As CATBSTR
                |     The property ApplicationType.

        :return: str
        """

        return self.com_object.ApplicationType

    @application_type.setter
    def application_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.ApplicationType = value

    @property
    def applicative_profiles_mgr(self) -> RscApplicativeProfilesMgr:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApplicativeProfilesMgr() As RscApplicativeProfilesMgr (Read
                | Only)
                |     The applicative profiles manager for this device.

        :return: RscApplicativeProfilesMgr
        """

        return RscApplicativeProfilesMgr(self.com_object.ApplicativeProfilesMgr)

    @property
    def c_frame_rivet_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CFrameRivetProfileList() As OlpProfiles (Read Only)
                |     The list of all CFrameRivet profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.CFrameRivetProfileList)

    @property
    def cartesian_safety_zones(self) -> OLPCartesianSafetyZones:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CartesianSafetyZones() As OlpCartesianSafetyZones (Read
                | Only)
                |     The list of all Cartesian safety zones.

        :return: OLPCartesianSafetyZones
        """

        return OLPCartesianSafetyZones(self.com_object.CartesianSafetyZones)

    @property
    def conveyor_tracking_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConveyorTrackingProfileList() As OlpProfiles (Read
                | Only)
                |     The list of all conveyor tracking profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.ConveyorTrackingProfileList)

    @property
    def device_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DeviceID() As CATBSTR (Read Only)
                |     The native robot language ID of this device set in the device mapping tab.

        :return: str
        """

        return self.com_object.DeviceID

    @property
    def device_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DeviceType() As DELOlpDeviceType (Read Only)
                |     The type of this device (robot, rail, etc.)

        :return: DELOlpDeviceType
        """

        return self.com_object.DeviceType

    @property
    def device_type_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DeviceTypeString() As CATBSTR (Read Only)
                |     The type of this device as a string ("Robot", "Rail", "Tool",
                |     "WorkpiecePositioner" or "Conveyor").

        :return: str
        """

        return self.com_object.DeviceTypeString

    @property
    def drill_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrillProfileList() As OlpProfiles (Read Only)
                |     The list of all Drill profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.DrillProfileList)

    @property
    def drill_rivet_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrillRivetProfileList() As OlpProfiles (Read Only)
                |     The list of all Drill-Rivet profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.DrillRivetProfileList)

    @property
    def heart_beat(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HeartBeat() As double
                |     Get the heart beat for a device.
                | 
                |     Returns:
                |         The heart beat of the current device.

        :return: float
        """

        return self.com_object.HeartBeat

    @heart_beat.setter
    def heart_beat(self, value: float):
        """
        :param float value:
        """

        self.com_object.HeartBeat = value

    @property
    def home_positions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HomePositions() As CATSafeArrayVariant (Read Only)
                |     The list of home position names for this device.
                |     Each item in the list is a string.

        :return: tuple
        """

        return self.com_object.HomePositions

    @property
    def max_linear_accel(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaxLinearAccel() As double
                |     The property MaxLinearAccel.

        :return: float
        """

        return self.com_object.MaxLinearAccel

    @max_linear_accel.setter
    def max_linear_accel(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaxLinearAccel = value

    @property
    def max_linear_speed(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaxLinearSpeed() As double
                |     Maximum linear speed of a robot.
                |     Value is in m/s. This will fail if this is not the controller for a robot.
                |     Use DeviceType to determine if this is a robot.

        :return: float
        """

        return self.com_object.MaxLinearSpeed

    @max_linear_speed.setter
    def max_linear_speed(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaxLinearSpeed = value

    @property
    def model_number(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ModelNumber() As CATBSTR (Read Only)
                |     The robot model number as assigned by manufacturer. For example: SK16,
                |     R2000iA-165F, KR125-2, SH133-01, ...

        :return: str
        """

        return self.com_object.ModelNumber

    @property
    def motion_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionProfileList() As OlpProfiles (Read Only)
                |     The list of all motion profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.MotionProfileList)

    @property
    def num_joints(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumJoints() As long (Read Only)
                |     Number of joints in this device.

        :return: int
        """

        return self.com_object.NumJoints

    @property
    def object_frame_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ObjectFrameProfileList() As OlpProfiles (Read Only)
                |     The list of all object frame profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.ObjectFrameProfileList)

    @property
    def paint_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PaintProfileList() As OlpProfiles (Read Only)
                |     The list of all paint profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.PaintProfileList)

    @property
    def postures(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Postures() As CATSafeArrayVariant (Read Only)
                |     The list of valid postures for this robot.
                |     Each item in the list is a string. This will fail if this is not the
                |     controller for a robot. Use DeviceType to determine if this is a robot.

        :return: tuple
        """

        return self.com_object.Postures

    @property
    def rail_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RailDirection() As DELOlpAxisDirection (Read Only)
                |     Get the rail direction for a rail device.
                | 
                |     Returns:
                |         The axis direction of the movement of the rail device. It doesn't make
                |         sense for devices of any other types.

        :return: DELOlpAxisDirection
        """

        return self.com_object.RailDirection

    @property
    def rivet_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RivetProfileList() As OlpProfiles (Read Only)
                |     The list of all Rivet profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.RivetProfileList)

    @property
    def singularity_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SingularityTolerance() As double
                |     The property SingularityTolerance.

        :return: float
        """

        return self.com_object.SingularityTolerance

    @singularity_tolerance.setter
    def singularity_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.SingularityTolerance = value

    @property
    def spot_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpotProfileList() As OlpProfiles (Read Only)
                |     The list of all spot profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.SpotProfileList)

    @property
    def tool_profile_list(self) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ToolProfileList() As OlpProfiles (Read Only)
                |     The list of all tool profiles for this robot.

        :return: OLPProfiles
        """

        return OLPProfiles(self.com_object.ToolProfileList)

    @property
    def tool_volumes(self) -> OLPToolVolumes:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ToolVolumes() As OlpToolVolumes (Read Only)
                |     The list of all safety zone tool volumes for this robot.

        :return: OLPToolVolumes
        """

        return OLPToolVolumes(self.com_object.ToolVolumes)

    @property
    def turn_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TurnMode() As DELOlpTurnMode
                |     Indicates whether this robot uses turn numbers, turn signs,
                |     etc.
                |     This will fail if this is not the controller for a robot. Use DeviceType to
                |     determine if this is a robot.

        :return: DELOlpTurnMode
        """

        return self.com_object.TurnMode

    @turn_mode.setter
    def turn_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.TurnMode = value

    @property
    def user_profiles_mgr(self) -> RscUserProfilesMgr:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserProfilesMgr() As RscUserProfilesMgr (Read Only)
                |     The user profiles manager for this device.

        :return: RscUserProfilesMgr
        """

        return RscUserProfilesMgr(self.com_object.UserProfilesMgr)

    def get_applicative_profile_list(self, i_profile_type: str) -> OLPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetApplicativeProfileList(CATBSTR iProfileType) As
                | OlpProfiles
                |     Get a specific type of applicative profile or user
                |     profile.
                |     The user profile does not need to exist yet. Setting a parameter on a new
                |     user profile group, will automatically create the
                |     parameters."
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The profile type 
                | 
                |     Returns:
                |         The collection of profiles.

        :param str i_profile_type:
        :return: OLPProfiles
        """
        return OLPProfiles(self.com_object.GetApplicativeProfileList(i_profile_type))

    def get_base_location(self, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBaseLocation(DELOlpPositionRef iOrigin) As
                | OlpTransform
                |     The location of the device's base.
                |     The device base location may be different from the device's product origin.
                |     This location was set when the device model was created. If the device is
                |     mounted on a rail, the base location is taken at the rail
                |     origin.
                |     This will fail if this is not the controller for a robot. Use DeviceType to
                |     determine if this is a robot.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The reference coordinate frame for the base
                |             location.
                |             delOlpMount and delOlpRobotBase are not a valid origins.
                |             
                | 
                |     Returns:
                |         The location of the device's base relative to the specified origin.

        :param int i_origin:
        :return: OLPTransform
        """
        return OLPTransform(self.com_object.GetBaseLocation(i_origin))

    def get_conveyor_direction(self, i_robot: 'OLPController') -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetConveyorDirection(OlpController iRobot) As
                | DELOlpAxisDirection
                |     Get the conveyor direction.
                | 
                |     Parameters:
                | 
                |         iRobot
                |             The robot of interest. If the controller has only one robot,
                |             "Nothing" can be used alternatively in place of the name of robot.
                |             
                | 
                |     Returns:
                |         The robot base coordinate axis that the conveyor travels along. If the
                |         conveyor is out of alignment with the robot base coordinates by more than 2
                |         degrees, this call will fail.

        :param OLPController i_robot:
        :return: DELOlpAxisDirection
        """
        return self.com_object.GetConveyorDirection(i_robot.com_object)

    def get_dof_parameter(self, i_dof_index: int, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDOFParameter(long iDOFIndex,CATBSTR iParameterName) As
                | CATVariant
                |     Get a mapped DOF parameter by name for the current
                |     controller.
                | 
                |     Parameters:
                | 
                |         iDOFIndex
                |             The DOF's index. 
                |         iParameterName
                |             The parameter name to find 
                | 
                |     Returns:
                |         oValue the mapped parameter value for the current controller and DOF
                |         index

        :param int i_dof_index:
        :param str i_parameter_name:
        :return: CATVariant
        """
        return CATVariant(self.com_object.GetDOFParameter(i_dof_index, i_parameter_name))

    def get_hard_limit(self, i_joint_index: int, o_upper_limit: float, o_lower_limit: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetHardLimit(long iJointIndex,double oUpperLimit,double
                | oLowerLimit)
                |     Get the upper and lower hard limits for the given joint.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint's index. The 1st joint is 1 the last joint is NumJoints
                |             
                | 
                |     Returns:
                |         oUpperLimit the joint's upper hard limit oLowerLimit the joint's lower
                |         hard limit

        :param int i_joint_index:
        :param float o_upper_limit:
        :param float o_lower_limit:
        :return: None
        """
        return self.com_object.GetHardLimit(i_joint_index, o_upper_limit, o_lower_limit)

    def get_home_position(self, i_home_name: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetHomePosition(CATBSTR iHomeName) As CATSafeArrayVariant
                |     Get the joint values for a home position.
                | 
                |     Parameters:
                | 
                |         iHomeName
                |             The name of the home position. 
                | 
                |     Returns:
                |         The array of joint values. Each value in the array is a double. The
                |         joint values are in MKS units. The units depend on the joint type. The number
                |         of values must be the same as the number of joints for the device.

        :param str i_home_name:
        :return: tuple
        """
        return self.com_object.GetHomePosition(i_home_name)

    def get_joint_accel_time(self, i_joint_index: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetJointAccelTime(long iJointIndex) As double
                |     Get the acceleration time of a joint in this device.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint index. The 1st joint is 1 the last joint is NumJoints
                |             
                | 
                |     Returns:
                |         The accel time in seconds

        :param int i_joint_index:
        :return: float
        """
        return self.com_object.GetJointAccelTime(i_joint_index)

    def get_joint_type(self, i_joint_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetJointType(long iJointIndex) As DELOlpJointType
                |     Get the type of a joint (linear, rotational) in this
                |     device.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint index. The 1st joint is 1 the last joint is NumJoints
                |             
                | 
                |     Returns:
                |         The type of joint.

        :param int i_joint_index:
        :return: DELOlpJointType
        """
        return self.com_object.GetJointType(i_joint_index)

    def get_max_joint_accel(self, i_joint_index: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaxJointAccel(long iJointIndex) As double
                |     Get the max acceleration of a joint in this device.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint index. The 1st joint is 1 the last joint is NumJoints
                |             
                | 
                |     Returns:
                |         The acceleration units are m/s^2 for linear joints and rad/s^2 for
                |         rotational joints

        :param int i_joint_index:
        :return: float
        """
        return self.com_object.GetMaxJointAccel(i_joint_index)

    def get_max_joint_speed(self, i_joint_index: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaxJointSpeed(long iJointIndex) As double
                |     Get the max speed of a joint in this device.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint index. The 1st joint is 1 the last joint is NumJoints
                |             
                | 
                |     Returns:
                |         The speed units are m/s for linear joints and rad/s for rotational
                |         joints

        :param int i_joint_index:
        :return: float
        """
        return self.com_object.GetMaxJointSpeed(i_joint_index)

    def get_parameter(self, i_profile_type: str, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameter(CATBSTR iProfileType,CATBSTR iParameterName) As
                | CATVariant
                |     Get applicative profile parameter value directly on the motion controller
                |     (MCA).
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iParameterName
                |             The parameter name 
                | 
                |     Returns:
                |         The parameter value.

        :param str i_profile_type:
        :param str i_parameter_name:
        :return: CATVariant
        """
        return CATVariant(self.com_object.GetParameter(i_profile_type, i_parameter_name))

    def get_parameter_names(self, i_profile_type: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameterNames(CATBSTR iProfileType) As
                | CATSafeArrayVariant
                |     Get all applicative and user profile parameter names for a profile
                |     type.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type. 
                | 
                |     Returns:
                |         The list of parameter names as strings.

        :param str i_profile_type:
        :return: tuple
        """
        return self.com_object.GetParameterNames(i_profile_type)

    def get_soft_limit(self, i_joint_index: int, o_upper_limit: float, o_lower_limit: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSoftLimit(long iJointIndex,double oUpperLimit,double
                | oLowerLimit)
                |     Get the upper and lower soft limits for the given joint.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint's index. The 1st joint is 1 the last joint is NumJoints
                |             
                | 
                |     Returns:
                |         oUpperLimit the joint's upper soft limit oLowerLimit the joint's lower
                |         soft limit

        :param int i_joint_index:
        :param float o_upper_limit:
        :param float o_lower_limit:
        :return: None
        """
        return self.com_object.GetSoftLimit(i_joint_index, o_upper_limit, o_lower_limit)

    def set_base_location(self, i_origin: int, i_location: OLPTransform) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBaseLocation(DELOlpPositionRef iOrigin,OlpTransform
                | iLocation)
                |     Set the base location of the resource. It does not move the
                |     resource.
                |     The behavior is different depending on the type of device. Use DeviceType
                |     to determine if this is a robot or a conveyor. SetBaseLocation is ignored if
                |     update device parameters has been unchecked by the user.
                | 
                |     For robots, this sets the robot origin by specifying the robot base
                |     location relative to it. If the device is mounted on an aux device rail, the
                |     base location is taken at the rail origin. This will fail if this is not the
                |     controller for a robot.
                | 
                |     For conveyors, this sets the base frame of the conveyor that is the
                |     tracking frame origin.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             Valid values for robots are
                | 
                |                 delOlpUserDefined - The origin type will be set to user defined
                |                 regardless of the position set.
                |                 delOlpRobotOrigin - The origin type will be computed
                |                 automatically based on the location. If the transform is 0, delOlpRailOrigin
                |                 will be used, if the transform matches the robot's location in the cell
                |                 delOlpStation will be used.
                | 
                |             Valid values for conveyors are
                | 
                |                 delOlpWorld
                |                 delOlpStation
                |                 delOlpRailOrigin
                |                 delOlpRobotBase
                |                 delOlpUserDefined
                |                 delOlpRobotOrigin
                | 
                |         iLocation
                |             The location of the device's base relative to the robot origin.

        :param int i_origin:
        :param OLPTransform i_location:
        :return: None
        """
        return self.com_object.SetBaseLocation(i_origin, i_location.com_object)

    def set_dof_parameter(self, i_dof_index: int, i_parameter_name: str, i_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDOFParameter(long iDOFIndex,CATBSTR iParameterName,CATVariant
                | iValue)
                |     Set a DOF mapped parameter by name for the current
                |     controller.
                | 
                |     Parameters:
                | 
                |         iDOFIndex
                |             The DOF's index. 
                |         iParameterName
                |             The parameter name to find 
                |         iValue
                |             The value to set for the parameter and DOF index

        :param int i_dof_index:
        :param str i_parameter_name:
        :param CATVariant i_value:
        :return: None
        """
        return self.com_object.SetDOFParameter(i_dof_index, i_parameter_name, i_value)

    def set_hard_limit(self, i_joint_index: int, i_upper_limit: float, i_lower_limit: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetHardLimit(long iJointIndex,double iUpperLimit,double
                | iLowerLimit)
                |     Set the upper and lower hard limits for the given joint.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint's index. The 1st joint is 1 the last joint is NumJoints
                |             
                |         iUpperLimit
                |             the joint's upper hard limit to set 
                |         iLowerLimit
                |             the joint's lower hard limit to set

        :param int i_joint_index:
        :param float i_upper_limit:
        :param float i_lower_limit:
        :return: None
        """
        return self.com_object.SetHardLimit(i_joint_index, i_upper_limit, i_lower_limit)

    def set_home_position(self, i_home_name: str, i_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetHomePosition(CATBSTR iHomeName,CATSafeArrayVariant
                | iValues)
                |     Set the joint values for a home position.
                | 
                |     Parameters:
                | 
                |         iHomeName
                |             The name of the home position. 
                |         iValues
                |             The array of joint values. Each value in the array is a double. The
                |             joint values are in MKS units. The units depend on the joint type. The number
                |             of values must be the same as the number of joints for the device.

        :param str i_home_name:
        :param tuple i_values:
        :return: None
        """
        return self.com_object.SetHomePosition(i_home_name, i_values)

    def set_joint_accel_time(self, i_joint_index: int, i_accel: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetJointAccelTime(long iJointIndex,double iAccel)
                |     Set the acceleration time of a joint in this device.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint index. The 1st joint is 1 the last joint is NumJoints
                |             
                |         iAccel
                |             The accel time in seconds

        :param int i_joint_index:
        :param float i_accel:
        :return: None
        """
        return self.com_object.SetJointAccelTime(i_joint_index, i_accel)

    def set_max_joint_accel(self, i_joint_index: int, i_accel: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaxJointAccel(long iJointIndex,double iAccel)
                |     Get the max acceleration of a joint in this device.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint index. The 1st joint is 1 the last joint is NumJoints
                |             
                |         iAccel
                |             The acceleration units are m/s^2 for linear joints and rad/s^2 for
                |             rotational joints

        :param int i_joint_index:
        :param float i_accel:
        :return: None
        """
        return self.com_object.SetMaxJointAccel(i_joint_index, i_accel)

    def set_max_joint_speed(self, i_joint_index: int, i_speed: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaxJointSpeed(long iJointIndex,double iSpeed)
                |     Set the max speed of a joint in this device.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint index. The 1st joint is 1 the last joint is NumJoints
                |             
                |         iSpeed
                |             The speed units are m/s for linear joints and rad/s for rotational
                |             joints

        :param int i_joint_index:
        :param float i_speed:
        :return: None
        """
        return self.com_object.SetMaxJointSpeed(i_joint_index, i_speed)

    def set_parameter(self, i_profile_type: str, i_parameter_name: str, i_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParameter(CATBSTR iProfileType,CATBSTR iParameterName,CATVariant
                | iValue)
                |     Set applicative profile parameter value directly on the motion controller
                |     (MCA).
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iParameterName
                |             The parameter name 
                |         iValue
                |             The parameter value.

        :param str i_profile_type:
        :param str i_parameter_name:
        :param CATVariant i_value:
        :return: None
        """
        return self.com_object.SetParameter(i_profile_type, i_parameter_name, i_value)

    def set_soft_limit(self, i_joint_index: int, i_upper_limit: float, i_lower_limit: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSoftLimit(long iJointIndex,double iUpperLimit,double
                | iLowerLimit)
                |     Set the upper and lower soft limits for the given joint.
                | 
                |     Parameters:
                | 
                |         iJointIndex
                |             The joint's index. The 1st joint is 1 the last joint is NumJoints
                |             
                |         iUpperLimit
                |             the joint's upper soft limit to set 
                |         iLowerLimit
                |             the joint's lower soft limit to set 

        :param int i_joint_index:
        :param float i_upper_limit:
        :param float i_lower_limit:
        :return: None
        """
        return self.com_object.SetSoftLimit(i_joint_index, i_upper_limit, i_lower_limit)

    def __repr__(self):
        return f'OLPController(name="{ self.name }")'
