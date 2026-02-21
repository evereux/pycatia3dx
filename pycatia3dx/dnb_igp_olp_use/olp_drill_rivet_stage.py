"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.dnb_igp_olp_use.olp_accuracy_profile import OLPAccuracyProfile
from pycatia3dx.dnb_igp_olp_use.olp_motion_profile import OLPMotionProfile
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile
from pycatia3dx.system.any_object import AnyObject


class OLPDrillRivetStage(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpDrillRivetStage
                | 
                | Interface representing a stage within a
                | OlpDrillRivetProfile or within a OlpCFrameRivetProfile This interface can only
                | be used by a translator within the Robotics Off-line Programming (OLP) Download
                | or Upload command. A stage in itself does not exist, as it is part of its
                | containing OlpDrillRivetProfile or its containing DELMIAOlpCFrameRivetProfile
                | Use this interface to modify data related to a stage within a
                | profile.
    
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
                |     stage.
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

    def get_enabled(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEnabled() As boolean
                |     Get the stage enabled state
                | 
                |     Returns:
                |         oEnabled The stage enabled state

        :return: bool
        """
        return self.com_object.GetEnabled()

    def get_motion_profile(self) -> OLPMotionProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMotionProfile() As OlpMotionProfile
                |     Get the motion profile which controls the motion planning for this
                |     stage.
                | 
                |     Returns:
                |         The motion profile.

        :return: OLPMotionProfile
        """
        return OLPMotionProfile(self.com_object.GetMotionProfile())

    def get_moving_tcp_clearance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMovingTCPClearance() As double
                |     Get the moving distance the TCP is from at the end of the move for this
                |     stage.
                |     This method is only valid for stages within a CFrameRivet profile. This
                |     method is not valid for any stage within a Drill, Rivet or DrillRivet
                |     profile.
                | 
                |     Returns:
                |         The value in meters.

        :return: float
        """
        return self.com_object.GetMovingTCPClearance()

    def get_moving_tcp_clearance_link(self, o_profile: OLPProfile, o_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMovingTCPClearanceLink(OlpProfile oProfile,CATBSTR
                | oControllerParamName)
                |     Get the schedule parameter that is linked to a moving TCP clearance
                |     parameter.
                |     This method is only valid for stages within a CFrameRivet profile. This
                |     method is not valid for any stage within a Drill, Rivet or DrillRivet
                |     profile.
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
        return self.com_object.GetMovingTCPClearanceLink(o_profile.com_object, o_controller_param_name)

    def get_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetName() As CATBSTR
                |     Get the stage name.
                | 
                |     Returns:
                |         The stage name

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

    def get_stationary_tcp_clearance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetStationaryTCPClearance() As double
                |     Get the stationary distance the TCP is from at the end of the move for this
                |     stage.
                |     This method gets the approach distance for the approach stage in a Drill or
                |     a Rivet profile. This method gets the retract clearance for the retract stage
                |     in a DrillRivet profile. This method gets the stationary distance for any stage
                |     within a CFrameRivet profile. Any specific combination not listed here is not
                |     supported.
                | 
                |     Returns:
                |         The value in meters.

        :return: float
        """
        return self.com_object.GetStationaryTCPClearance()

    def get_stationary_tcp_clearance_link(self, o_profile: OLPProfile, o_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetStationaryTCPClearanceLink(OlpProfile oProfile,CATBSTR
                | oControllerParamName)
                |     Get the schedule parameter that is linked to a stationary TCP clearance
                |     parameter.
                |     This method gets the approach distance profile for the approach stage in a
                |     Drill or a Rivet profile. This method gets the retract clearance profile for
                |     the retract stage in a DrillRivet profile. This method gets the stationary
                |     distance profile for any stage within a CFrameRivet profile. Any specific
                |     combination not listed here is not supported.
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
        return self.com_object.GetStationaryTCPClearanceLink(o_profile.com_object, o_controller_param_name)

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
                |     Set the accuracy profile which controls the motion planning for this
                |     stage.
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

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
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
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_all_process_schedules'
        # vba_code = """
        # Public Function set_all_process_schedules(olp_drill_rivet_stage)
        #     Dim iProfiles (2)
        #     olp_drill_rivet_stage.SetAllProcessSchedules iProfiles
        #     set_all_process_schedules = iProfiles
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_enabled(self, i_enabled: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetEnabled(boolean iEnabled,boolean iMatch)
                |     Set the stage enabled state
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

    def set_motion_profile(self, o_profile: OLPMotionProfile, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionProfile(OlpMotionProfile oProfile,boolean iMatch)
                |     Set the motion profile which controls the motion planning for this
                |     stage.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The motion profile. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPMotionProfile o_profile:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetMotionProfile(o_profile.com_object, i_match)

    def set_moving_tcp_clearance(self, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMovingTCPClearance(double iDistance,boolean iMatch)
                |     Set the moving distance the TCP is from at the end of the move for this
                |     stage.
                |     This method is only valid for stages within a CFrameRivet profile. This
                |     method is not valid for any stage within a Drill, Rivet or DrillRivet
                |     profile.
                | 
                |     Parameters:
                | 
                |         iDistance
                |             The value in meters. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_distance:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetMovingTCPClearance(i_distance, i_match)

    def set_moving_tcp_clearance_link(self, i_profile: OLPProfile, i_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMovingTCPClearanceLink(OlpProfile iProfile,CATBSTR
                | iControllerParamName)
                |     Set the user profile schedule parameter that is linked to a moving TCP
                |     clearance parameter.
                |     This method is only valid for stages within a CFrameRivet profile. This
                |     method is not valid for any stage within a Drill, Rivet or DrillRivet
                |     profile.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The applicative profile. 
                |         iControllerParamName
                |             The name of the linked parameter. It must be a parameter with the
                |             dimension length.

        :param OLPProfile i_profile:
        :param str i_controller_param_name:
        :return: None
        """
        return self.com_object.SetMovingTCPClearanceLink(i_profile.com_object, i_controller_param_name)

    def set_process_schedules(self, i_profiles: tuple, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
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
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_process_schedules'
        # vba_code = """
        # Public Function set_process_schedules(olp_drill_rivet_stage)
        #     Dim iProfiles (2)
        #     olp_drill_rivet_stage.SetProcessSchedules iProfiles
        #     set_process_schedules = iProfiles
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

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

    def set_stationary_tcp_clearance(self, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStationaryTCPClearance(double iDistance,boolean iMatch)
                |     Set the stationary distance the TCP is from at the end of the move for this
                |     stage.
                |     This method sets the approach distance for the approach stage in a Drill or
                |     a Rivet profile. This method sets the retract clearance for the retract stage
                |     in a DrillRivet profile. This method sets the stationary distance for any stage
                |     within a CFrameRivet profile. Any specific combination not listed here is not
                |     supported.
                | 
                |     Parameters:
                | 
                |         iDistance
                |             The value in meters. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_distance:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetStationaryTCPClearance(i_distance, i_match)

    def set_stationary_tcp_clearance_link(self, i_profile: OLPProfile, i_controller_param_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStationaryTCPClearanceLink(OlpProfile iProfile,CATBSTR
                | iControllerParamName)
                |     Set the user profile schedule parameter that is linked to a stationary TCP
                |     clearance parameter.
                |     This method sets the approach distance profile for the approach stage in a
                |     Drill or a Rivet profile. This method sets the retract clearance profile for
                |     the retract stage in a DrillRivet profile. This method sets the stationary
                |     distance profile for any stage within a CFrameRivet profile. Any specific
                |     combination not listed here is not supported.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The applicative profile. 
                |         iControllerParamName
                |             The name of the linked parameter. It must be a parameter with the
                |             dimension length. 

        :param OLPProfile i_profile:
        :param str i_controller_param_name:
        :return: None
        """
        return self.com_object.SetStationaryTCPClearanceLink(i_profile.com_object, i_controller_param_name)

    def __repr__(self):
        return f'OLPDrillRivetStage(name="{self.name}")'
