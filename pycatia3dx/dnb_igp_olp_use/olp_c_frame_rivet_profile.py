"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_accuracy_profile import OLPAccuracyProfile
from pycatia3dx.dnb_igp_olp_use.olp_drill_rivet_stage import OLPDrillRivetStage
from pycatia3dx.dnb_igp_olp_use.olp_motion_profile import OLPMotionProfile
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile


class OLPCFrameRivetProfile(OLPProfile):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpProfile
                |                         OlpCFrameRivetProfile
                | 
                | A CFrameRivet profile used for translating a robot program.
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command. If the OlpRobotMotionTarget is
                | part of a OlpDrillRivetAction , it must be of Rivet type. This profile cannot
                | be assigned to targets within Drill or DrillRivet Actions.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def approach_stage(self) -> OLPDrillRivetStage:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApproachStage() As OlpDrillRivetStage
                |     The approach stage object which allows configuration via its methods

        :return: OLPDrillRivetStage
        """

        return OLPDrillRivetStage(self.com_object.ApproachStage)

    @approach_stage.setter
    def approach_stage(self, value: OLPDrillRivetStage):
        """
        :param OLPDrillRivetStage value:
        """

        self.com_object.ApproachStage = value

    @property
    def end_stage(self) -> OLPDrillRivetStage:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndStage() As OlpDrillRivetStage
                |     The end stage object which allows configuration via its methods

        :return: OLPDrillRivetStage
        """

        return OLPDrillRivetStage(self.com_object.EndStage)

    @end_stage.setter
    def end_stage(self, value: OLPDrillRivetStage):
        """
        :param OLPDrillRivetStage value:
        """

        self.com_object.EndStage = value

    @property
    def retract_stage(self) -> OLPDrillRivetStage:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RetractStage() As OlpDrillRivetStage
                |     The retract stage object which allows configuration via its methods

        :return: OLPDrillRivetStage
        """

        return OLPDrillRivetStage(self.com_object.RetractStage)

    @retract_stage.setter
    def retract_stage(self, value: OLPDrillRivetStage):
        """
        :param OLPDrillRivetStage value:
        """

        self.com_object.RetractStage = value

    @property
    def start_stage(self) -> OLPDrillRivetStage:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartStage() As OlpDrillRivetStage
                |     The start stage object which allows configuration via its methods

        :return: OLPDrillRivetStage
        """

        return OLPDrillRivetStage(self.com_object.StartStage)

    @start_stage.setter
    def start_stage(self, value: OLPDrillRivetStage):
        """
        :param OLPDrillRivetStage value:
        """

        self.com_object.StartStage = value

    def get_accuracy_profile(self) -> OLPAccuracyProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAccuracyProfile() As OlpAccuracyProfile
                |     Get the accuracy profile for the rivet stage of this
                |     profile.
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

    def get_approach_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetApproachDirection() As DELOlpAxisDirection
                |     Get the direction the robot approaches the point from.
                | 
                |     Returns:
                |         The TCP axis direction.

        :return: DELOlpAxisDirection
        """
        return self.com_object.GetApproachDirection()

    def get_close_in_positive_direction(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCloseInPositiveDirection() As boolean
                |     This method is only applicable for Rivet and CGun Rivet Profiles Get
                |     whether the direction the tool closes when the joint values go up
                |     (positive).
                | 
                |     Returns:
                |         TRUE if closes in positive direction. FALSE otherwise.

        :return: bool
        """
        return self.com_object.GetCloseInPositiveDirection()

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
                |     Get the joint number assigned to this rivet gun.
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
                |     Get the motion profile for the rivet stage of this
                |     profile.
                | 
                |     Returns:
                |         The motion profile.

        :return: OLPMotionProfile
        """
        return OLPMotionProfile(self.com_object.GetMotionProfile())

    def get_part_thickness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPartThickness() As double
                |     Gets the part thickness assigned to this rivet gun
                | 
                |     Returns:
                |         The thickness in meters

        :return: float
        """
        return self.com_object.GetPartThickness()

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

    def get_push_depth(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPushDepth() As double
                |     Get the rivet push depth.
                | 
                |     Returns:
                |         The value in seconds.

        :return: float
        """
        return self.com_object.GetPushDepth()

    def get_push_depth_link(self, o_profile: OLPProfile, o_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPushDepthLink(OlpProfile oProfile,CATBSTR
                | oControllerParamName)
                |     Get the schedule parameter that is linked to the push depth
                |     parameter.
                | 
                |     Parameters:
                | 
                |         oProfile
                |             The applicative profile. 
                |         oControllerParamName
                |             The name of the linked parameter.

        :param OlpProfile o_profile:
        :param str o_controller_param_name:
        :return: None
        """
        return self.com_object.GetPushDepthLink(o_profile.com_object, o_controller_param_name)

    def get_tool_kin_simulation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetToolKinSimulation() As boolean
                |     Get whether the gun motion is simulated.
                | 
                |     Returns:
                |         TRUE if the motion is simulated. FALSE if not simulated.

        :return: bool
        """
        return self.com_object.GetToolKinSimulation()

    def is_process_schedule_set(self, i_profile_type: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsProcessScheduleSet(CATBSTR iProfileType) As boolean
                |     Get whether this profile has a linked applicative profile schedule for a
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
                |     Set the accuracy profile for the rivet stage of this
                |     profile
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

    def set_approach_direction(self, i_approach_direction: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApproachDirection(DELOlpAxisDirection iApproachDirection,boolean
                | iMatch)
                |     Set the direction the robot approaches the point from.
                | 
                |     Parameters:
                | 
                |         iApproachDirection
                |             The tool axis direction. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_approach_direction:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetApproachDirection(i_approach_direction, i_match)

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
                |     Set the joint number assigned to this rivet gun.
                | 
                |     Parameters:
                | 
                |         iJointNumber
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
                |     Set the motion profile for the rivet stage of this
                |     profile.
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

    def set_part_thickness(self, i_part_thickness: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPartThickness(double iPartThickness,boolean iMatch)
                |     Set the part thickness assigned to this rivet gun
                | 
                |     Parameters:
                | 
                |         iPartThickness
                |             The thickness in meters 
                |         iMatch
                |             If true, the part thickness must match.

        :param float i_part_thickness:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPartThickness(i_part_thickness, i_match)

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
                |             existing spot profile for it to match. However if the default values of the
                |             profile have the same meaning as having the profile unset, then a profile set
                |             with default values will also match.

        :param str i_profile_type:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetProcessSchedulesToNothing(i_profile_type, i_match)

    def set_push_depth(self, i_depth: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPushDepth(double iDepth,boolean iMatch)
                |     Set the rivet push depth.
                | 
                |     Parameters:
                | 
                |         iDepth
                |             The depth in meters 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_depth:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPushDepth(i_depth, i_match)

    def set_push_depth_link(self, i_profile: OLPProfile, i_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPushDepthLink(OlpProfile iProfile,CATBSTR
                | iControllerParamName)
                |     Set the user profile schedule parameter that is linked to the push depth
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
        return self.com_object.SetPushDepthLink(i_profile.com_object, i_controller_param_name)

    def set_tool_kin_simulation(self, i_enabled: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetToolKinSimulation(boolean iEnabled,boolean iMatch)
                |     Set whether the gun motion is simulated.
                | 
                |     Parameters:
                | 
                |         iIsPositiveDirection
                |             TRUE if the motion is simulated. FALSE if not simulated.
                |             
                |         iMatch
                |             If TRUE use value to find existing profile. 

        :param bool i_enabled:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetToolKinSimulation(i_enabled, i_match)

    def __repr__(self):
        return f'OLPCFrameRivetProfile(name="{ self.name }")'
