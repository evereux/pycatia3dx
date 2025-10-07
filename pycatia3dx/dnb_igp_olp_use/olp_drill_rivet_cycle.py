"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_accuracy_profile import OLPAccuracyProfile
from pycatia3dx.dnb_igp_olp_use.olp_motion_profile import OLPMotionProfile
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile
from pycatia3dx.dnb_igp_olp_use.olp_tool_profile import OLPToolProfile
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform


class OLPDrillRivetCycle(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpDrillRivetCycle
                | 
                | Interface representing a cycle within a
                | OlpDrillRivetProfile This interface can only be used by a translator within the
                | Robotics Off-line Programming (OLP) Download or Upload command. A cycle in
                | itself does not exist, as it is part of its containing
                | DELMIAOlpDrillRivetProfile Use this interface to modify data related to a cycle
                | within a profile.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_accuracy_profile(self) -> OLPAccuracyProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAccuracyProfile() As OlpAccuracyProfile
                |     Get the accuracy profile which controls the motion planning for this
                |     cycle.
                | 
                |     Returns:
                |         The accuracy profile.

        :return: OLPAccuracyProfile
        """
        return OLPAccuracyProfile(self.com_object.GetAccuracyProfile())

    def get_all_process_schedules(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAllProcessSchedules() As CATSafeArrayVariant
                |     Get all linked applicative profile schedules.
                | 
                |     Returns:
                |         A list of profiles. Empty if none.

        :return: tuple
        """
        return self.com_object.GetAllProcessSchedules()

    def get_close_in_positive_direction(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCloseInPositiveDirection() As boolean
                |     Get whether the direction the tool closes when the joint values go up
                |     (positive).
                | 
                |     Returns:
                |         TRUE if closes in positive direction. FALSE otherwise.

        :return: bool
        """
        return self.com_object.GetCloseInPositiveDirection()

    def get_cycle_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleType() As CATBSTR
                |     Get the cycle type.
                |     Valid cycle types are:
                | 
                |         DRILL
                |         RIVET
                | 
                |     Returns:
                |         The cycle type

        :return: str
        """
        return self.com_object.GetCycleType()

    def get_dimension(self, i_dimension_name: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDimension(CATBSTR iDimensionName) As double
                |     Get a dimension of the process.
                | 
                |     Parameters:
                | 
                |         iDimensionName
                |             Valid dimensions are:
                | 
                |                 DRILL
                |                     DRILLDEPTH
                |                     BREAKTHROUGH
                |                 RIVET
                |                     DISTANCE
                | 
                | Returns:
                |     The value in meters.

        :param str i_dimension_name:
        :return: float
        """
        return self.com_object.GetDimension(i_dimension_name)

    def get_dimension_link(self, i_dimension_name: str, o_profile: OLPProfile, o_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDimensionLink(CATBSTR iDimensionName,OlpProfile oProfile,CATBSTR
                | oControllerParamName)
                |     Get the schedule parameter that is linked to a dimension
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iDimensionName
                |             Valid dimensions are:
                | 
                |                 DRILL
                |                     DEPTH
                |                     BREAKTHROUGH
                |                 RIVET
                |                     DISTANCE
                | 
                |         oProfile
                |             The applicative profile. 
                |         oControllerParamName
                |             The name of the linked parameter.

        :param str i_dimension_name:
        :param OLPProfile o_profile:
        :param str o_controller_param_name:
        :return: None
        """
        return self.com_object.GetDimensionLink(i_dimension_name, o_profile.com_object, o_controller_param_name)

    def get_enabled(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEnabled() As boolean
                |     Get the cycle enabled state
                | 
                |     Returns:
                |         oEnabled The cycle enabled state

        :return: bool
        """
        return self.com_object.GetEnabled()

    def get_enabled_dynamic_drilling_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEnabledDynamicDrillingMode() As boolean
                |     This method is only valid for Drill Profiles Get the enabled state of the
                |     dynamic drilling mode
                | 
                |     Returns:
                |         iEnabled The enabled state of the dynamic drilling mode

        :return: bool
        """
        return self.com_object.GetEnabledDynamicDrillingMode()

    def get_hold_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetHoldTime() As double
                |     Get the hold time parameter of the process.
                | 
                |     Returns:
                |         The value in seconds.

        :return: float
        """
        return self.com_object.GetHoldTime()

    def get_hold_time_link(self, o_profile: OLPProfile, o_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetHoldTimeLink(OlpProfile oProfile,CATBSTR
                | oControllerParamName)
                |     Get the schedule parameter that is linked to the hold time
                |     parameter.
                | 
                |     Parameters:
                | 
                |         oProfile
                |             The applicative profile. 
                |         oControllerParamName
                |             The name of the linked parameter.

        :param OLPProfile o_profile:
        :param str o_controller_param_name:
        :return: None
        """
        return self.com_object.GetHoldTimeLink(o_profile.com_object, o_controller_param_name)

    def get_home_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetHomeName() As CATBSTR
                |     Get the home name for the gun's closed position.
                | 
                |     Returns:
                |         The home name. This is blank if the joint values don't correspond to a
                |         home name.

        :return: str
        """
        return self.com_object.GetHomeName()

    def get_joint_number(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetJointNumber() As short
                |     Get the joint number manipulated by this cycle.
                | 
                |     Returns:
                |         The joint number

        :return: int
        """
        return self.com_object.GetJointNumber()

    def get_joint_value(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetJointValue() As CATSafeArrayVariant
                |     Get the tool joint values for the closed position.
                | 
                |     Returns:
                |         The value in meters. Rotational joints are not supported.

        :return: tuple
        """
        return self.com_object.GetJointValue()

    def get_motion_profile(self) -> OLPMotionProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMotionProfile() As OlpMotionProfile
                |     Get the motion profile which controls the motion planning for this
                |     cycle.
                | 
                |     Returns:
                |         The motion profile.

        :return: OLPMotionProfile
        """
        return OLPMotionProfile(self.com_object.GetMotionProfile())

    def get_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetName() As CATBSTR
                |     Get the cycle name.
                | 
                |     Returns:
                |         The cycle name

        :return: str
        """
        return self.com_object.GetName()

    def get_process_schedules(self, i_profile_type: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProcessSchedules(CATBSTR iProfileType) As
                | CATSafeArrayVariant
                |     Get linked applicative profile schedules by type.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                | 
                |     Returns:
                |         A list of profiles. Empty if none.

        :param str i_profile_type:
        :return: tuple
        """
        return self.com_object.GetProcessSchedules(i_profile_type)

    def get_profile_process_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfileProcessType() As CATBSTR
                |     Get the cycle's parent profile process type.
                |     Valid profile process types are:
                | 
                |         DRILL
                |         RIVET
                |         DRILL-RIVET
                | 
                |     Returns:
                |         The cycle's parent profile process type

        :return: str
        """
        return self.com_object.GetProfileProcessType()

    def get_tcp_offset(self) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTCPOffset() As OlpTransform
                |     Get the TCP offset for this cycle.
                | 
                |     The offest is applied to the TCP during simulation for of this
                |     cycle.
                | 
                |     Returns:
                |         The offset.

        :return: OLPTransform
        """
        return OLPTransform(self.com_object.GetTCPOffset())

    def get_tcp_offset_link(self, i_coordinate_name: str, o_profile: OLPProfile, o_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPOffsetLink(CATBSTR iCoordinateName,OlpProfile oProfile,CATBSTR
                | oControllerParamName)
                |     Get the parameter that is linked to 1 coordinate of the TCP offset for this
                |     cycle.
                |     The parameter can be linked to a parameter in a user profile or a parameter
                |     of the manufacturing fastener.
                | 
                |     Parameters:
                | 
                |         iCoordinateName
                |             Valid cooridnate names are:
                | 
                |                 x
                |                 y
                |                 z
                |                 yaw
                |                 pitch
                |                 roll
                | 
                |         oProfile
                |             The applicative profile. In case of a parameter linked to the
                |             manufacturing fastener the profile is Nothing. 
                |         oControllerParamName
                |             The name of the linked parameter. It must be a parameter with the
                |             dimension length or angle.

        :param str i_coordinate_name:
        :param OLPProfile o_profile:
        :param str o_controller_param_name:
        :return: None
        """
        return self.com_object.GetTCPOffsetLink(i_coordinate_name, o_profile.com_object, o_controller_param_name)

    def get_tool_profile(self) -> OLPToolProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetToolProfile() As OlpToolProfile
                |     Get the tool profile which controls the motion planning for this
                |     cycle.
                | 
                |     Returns:
                |         The tool profile.

        :return: OLPToolProfile
        """
        return OLPToolProfile(self.com_object.GetToolProfile())

    def is_process_schedule_set(self, i_profile_type: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsProcessScheduleSet(CATBSTR iProfileType) As boolean
                |     Get whether this cycle has a linked applicative profile schedule for a
                |     type.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                | 
                |     Returns:
                |         True if the schedule is set.

        :param str i_profile_type:
        :return: bool
        """
        return self.com_object.IsProcessScheduleSet(i_profile_type)

    def set_accuracy_profile(self, i_profile: OLPAccuracyProfile, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAccuracyProfile(OlpAccuracyProfile iProfile,boolean
                | iMatch)
                |     This method is only valid for cycles within a profile of type of DRILL or
                |     RIVET only. Not valid for DRILL-RIVET.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The accuracy profile. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPAccuracyProfile i_profile:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetAccuracyProfile(i_profile.com_object, i_match)

    def set_all_process_schedules(self, i_profiles: tuple, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAllProcessSchedules(CATSafeArrayVariant iProfiles,boolean
                | iMatch)
                |     Set all linked applicative profile schedules.
                |     This will remove all currently linked profiles if they are not also in this
                |     list.
                | 
                |     Returns:
                |         A list of profiles. Empty if none.

        :param tuple i_profiles:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetAllProcessSchedules(i_profiles, i_match)

    def set_close_in_positive_direction(self, i_is_positive_direction: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCloseInPositiveDirection(boolean iIsPositiveDirection,boolean
                | iMatch)
                |     Set whether the direction the tool closes when the joint values go up
                |     (positive).
                | 
                |     Parameters:
                | 
                |         iIsPositiveDirection
                |             TRUE if closes in positive direction. FALSE otherwise.
                |             
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param bool i_is_positive_direction:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetCloseInPositiveDirection(i_is_positive_direction, i_match)

    def set_dimension(self, i_dimension_name: str, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDimension(CATBSTR iDimensionName,double iDistance,boolean
                | iMatch)
                |     Set a dimension of the process.
                | 
                |     Parameters:
                | 
                |         iDimensionName
                |             Valid dimensions are:
                | 
                |                 DRILL
                |                     DEPTH
                |                     BREAKTHROUGH
                |                 RIVET
                |                     DISTANCE
                | 
                |         iDistance
                |             The value in meterrs.

        :param str i_dimension_name:
        :param float i_distance:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetDimension(i_dimension_name, i_distance, i_match)

    def set_dimension_link(self, i_dimension_name: str, i_profile: OLPProfile, i_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDimensionLink(CATBSTR iDimensionName,OlpProfile iProfile,CATBSTR
                | iControllerParamName)
                |     Set the schedule parameter that is linked to a dimension
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iDimensionName
                |             Valid dimensions are:
                | 
                |                 DRILL
                |                     DEPTH
                |                     BREAKTHROUGH
                |                 RIVET
                |                     DISTANCE
                | 
                |         iProfile
                |             The applicative profile. 
                |         iControllerParamName
                |             The name of the linked parameter. It must be a parameter with the
                |             dimension length.

        :param str i_dimension_name:
        :param OLPProfile i_profile:
        :param str i_controller_param_name:
        :return: None
        """
        return self.com_object.SetDimensionLink(i_dimension_name, i_profile.com_object, i_controller_param_name)

    def set_enabled(self, i_enabled: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetEnabled(boolean iEnabled,boolean iMatch)
                |     Set the cycle enabled state
                | 
                |     Parameters:
                | 
                |         iEnabled
                |             The enabled state

        :param bool i_enabled:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetEnabled(i_enabled, i_match)

    def set_enabled_dynamic_drilling_mode(self, i_enabled: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetEnabledDynamicDrillingMode(boolean iEnabled,boolean
                | iMatch)
                |     This method is only valid for Drill Profiles Set the enabled state of the
                |     dynamic drilling mode
                | 
                |     Parameters:
                | 
                |         iEnabled
                |             The enabled state of the dynamic drilling mode 
                |         iMatch
                |             If true enabled state must match

        :param bool i_enabled:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetEnabledDynamicDrillingMode(i_enabled, i_match)

    def set_hold_time(self, i_time: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetHoldTime(double iTime,boolean iMatch)
                |     Set the hold time parameter of the process.
                | 
                |     Parameters:
                | 
                |         iTime
                |             The value in seconds. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_time:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetHoldTime(i_time, i_match)

    def set_hold_time_link(self, i_profile: OLPProfile, i_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetHoldTimeLink(OlpProfile iProfile,CATBSTR
                | iControllerParamName)
                |     Set the user profile schedule parameter that is linked to the hold time
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The applicative profile. 
                |         iControllerParamName
                |             The name of the linked parameter. It must be a parameter with the
                |             dimension time.

        :param OLPProfile i_profile:
        :param str i_controller_param_name:
        :return: None
        """
        return self.com_object.SetHoldTimeLink(i_profile.com_object, i_controller_param_name)

    def set_home_name(self, i_home: str, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetHomeName(CATBSTR iHome,boolean iMatch)
                |     Set the home name for the gun's closed position.
                |     You may set any combination of joint values, home names, and dimensions to
                |     set the tool position for each phase. Any missing values will be calculated. If
                |     a home name is specified and does not exist but no joint values are specified,
                |     0's will be assumed and a warning displayed. If a home name is not specified
                |     but is needed (e.g. for the closed position) a name will be generated. If a
                |     missing value cannot be calculated because not enough information was specified
                |     a warning will be issued. For some tools or applications, the tool position is
                |     not supported. A warning will be generated that the DELMIA simulation does not
                |     support this if a value is set if this is the case. For example, breakthrough
                |     only applies to drilling.
                | 
                |     Parameters:
                | 
                |         iHome
                |             The home name 
                |         iMatch
                |             if true the home name will be used in the matching process

        :param str i_home:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetHomeName(i_home, i_match)

    def set_joint_number(self, i_joint_number: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetJointNumber(short iJointNumber,boolean iMatch)
                |     Set the joint number manipulated by this cycle.
                | 
                |     Parameters:
                | 
                |         iPartThickness
                |             The joint number. 
                |         iMatch
                |             If true, the joint number must match.

        :param int i_joint_number:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetJointNumber(i_joint_number, i_match)

    def set_joint_value(self, i_values: tuple, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetJointValue(CATSafeArrayVariant iValues,boolean iMatch)
                |     Set the tool joint values for the closed position.
                | 
                |     Parameters:
                | 
                |         iValues
                |             An array of joint values in meters. Rotational joints are not
                |             supported. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param tuple i_values:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetJointValue(i_values, i_match)

    def set_motion_profile(self, i_profile: OLPMotionProfile, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionProfile(OlpMotionProfile iProfile,boolean iMatch)
                |     This method is only valid for cycles within a profile of type of DRILL or
                |     RIVET only. Not valid for DRILL-RIVET. Set the motion profile which controls
                |     the motion planning for this cycle.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The motion profile. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPMotionProfile i_profile:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetMotionProfile(i_profile.com_object, i_match)

    def set_name(self, i_name: str, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetName(CATBSTR iName,boolean iMatch)
                |     Set the cycle name.
                | 
                |     Parameters:
                | 
                |         iName
                |             The cycle name 
                |         iMatch
                |             If true, the cycle name will be considered when matching
                |             drill-rivet profiles.

        :param str i_name:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetName(i_name, i_match)

    def set_process_schedules(self, i_profiles: tuple, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProcessSchedules(CATSafeArrayVariant iProfiles,boolean
                | iMatch)
                |     Set linked applicative profile schedules by type.
                |     You must also call a SetXLink method to link at least 1 parameter of a user
                |     profile to this profile.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type. 
                | 
                |     Returns:
                |         A list of profiles. Empty if none.

        :param tuple i_profiles:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetProcessSchedules(i_profiles, i_match)

    def set_process_schedules_to_nothing(self, i_profile_type: str, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProcessSchedulesToNothing(CATBSTR iProfileType,boolean
                | iMatch)
                |     Clear a linked applicative profile schedule for a type.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iMatch
                |             If iMatch is TRUE then this profile must not be linked to an
                |             existing drill-rivet profile for it to match. However if the default values of
                |             the profile have the same meaning as having the profile unset, then a profile
                |             set with default values will also match.

        :param str i_profile_type:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetProcessSchedulesToNothing(i_profile_type, i_match)

    def set_tcp_offset(self, i_offset: OLPTransform, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPOffset(OlpTransform iOffset,boolean iMatch)
                |     Set the TCP offset for this cycle.
                | 
                |     The offest is applied to the TCP during simulation for of this
                |     cycle.
                | 
                |     Parameters:
                | 
                |         iOffset
                |             The offset values. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OlpTransform i_offset:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPOffset(i_offset.com_object, i_match)

    def set_tcp_offset_link(self, i_coordinate_name: str, i_profile: OLPProfile, i_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPOffsetLink(CATBSTR iCoordinateName,OlpProfile iProfile,CATBSTR
                | iControllerParamName)
                |     Set the parameter that is linked to 1 coordinate of the TCP offset for this
                |     cycle.
                |     The parameter can be linked to a parameter in a user profile or a parameter
                |     of the manufacturing fastener.
                | 
                |     Parameters:
                | 
                |         iCoordinateName
                |             Valid cooridnate names are:
                | 
                |                 x
                |                 y
                |                 z
                |                 yaw
                |                 pitch
                |                 roll
                | 
                |         iProfile
                |             The applicative profile. In case of a parameter linked to the
                |             manufacturing fastener set the profile to Nothing.
                |             
                |         iControllerParamName
                |             The name of the linked parameter. It must be a parameter with the
                |             dimension length or angle.

        :param str i_coordinate_name:
        :param OLPProfile i_profile:
        :param str i_controller_param_name:
        :return: None
        """
        return self.com_object.SetTCPOffsetLink(i_coordinate_name, i_profile.com_object, i_controller_param_name)

    def set_tool_profile(self, i_profile: OLPToolProfile, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetToolProfile(OlpToolProfile iProfile,boolean iMatch)
                |     Set the tool profile which controls the motion planning for this
                |     cycle.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The tool profile. 
                |         iMatch
                |             If TRUE use value to find existing profile. 

        :param OLPToolProfile i_profile:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetToolProfile(i_profile.com_object, i_match)

    def __repr__(self):
        return f'OLPDrillRivetCycle(name="{ self.name }")'
