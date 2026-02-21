"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_drill_rivet_cycles import OLPDrillRivetCycles
from pycatia3dx.dnb_igp_olp_use.olp_drill_rivet_stage import OLPDrillRivetStage
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile


class OLPDrillRivetProfile(OLPProfile):
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
                |                         OlpDrillRivetProfile
                | 
                | A DrillRivet profile used for translating a robot program.
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command. When assigning this profile to a
                | OlpRobotMotionTarget, it must be part of a OlpDrillRivetAction
    
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
    def drill_cycles(self) -> OLPDrillRivetCycles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrillCycles() As OlpDrillRivetCycles
                |     Get the Drill cycles collection for this Drill or Drill-Rivet profile.
                |     NOTE: Drill cycles are only applicable for Drill or Drill-Rivet profiles. The
                |     Drill cycles object is a collection of Drill cycles. For a newly created
                |     profile, there will exist at least one cycle. Cycles happen in between the
                |     approach (if enabled) and retract (if enabled) stages.

        :return: OLPDrillRivetCycles
        """

        return OLPDrillRivetCycles(self.com_object.DrillCycles)

    @drill_cycles.setter
    def drill_cycles(self, value: OLPDrillRivetCycles):
        """
        :param OLPDrillRivetCycles value:
        """

        self.com_object.DrillCycles = value

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
    def rivet_cycles(self) -> OLPDrillRivetCycles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RivetCycles() As OlpDrillRivetCycles
                |     Get the Rivet cycles collection for this Rivet or Drill-Rivet profile.
                |     NOTE: Rivet cycles are only applicable for Rivet or Drill-Rivet profiles. The
                |     Rivet cycles object is a collection of Rivet cycles. For a newly created
                |     profile, there will exist at least one cycle. Cycles happen in between the
                |     approach (if enabled) and retract (if enabled) stages.

        :return: OLPDrillRivetCycles
        """

        return OLPDrillRivetCycles(self.com_object.RivetCycles)

    @rivet_cycles.setter
    def rivet_cycles(self, value: OLPDrillRivetCycles):
        """
        :param OLPDrillRivetCycles value:
        """

        self.com_object.RivetCycles = value

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

    def get_precycle_feature(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPrecycleFeature() As CATBSTR
                |     Get the precycle feature. The default value is NONE.
                |     Valid features are: DRILL Process:
                | 
                |         NONE
                |         HOLE
                | 
                |     RIVET Process:
                | 
                |         NONE
                |         RIVET
                |         BOLT
                | 
                |     DRILL-RIVET Process:
                | 
                |         NONE
                |         HOLE
                |         RIVET
                |         BOLT
                | 
                |     Returns:
                |         The currently assigned feature.

        :return: str
        """
        return self.com_object.GetPrecycleFeature()

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
                |     Get the profile process type.
                |     Valid profile process types are:
                | 
                |         DRILL
                |         RIVET
                |         DRILL-RIVET
                | 
                |     Returns:
                |         The profile process type

        :return: str
        """
        return self.com_object.GetProfileProcessType()

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

    def is_tool_fixed(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsToolFixed() As boolean
                |     Get whether this profile has a fixed tool type.
                | 
                |     Returns:
                |         True if the tool is fixed.

        :return: bool
        """
        return self.com_object.IsToolFixed()

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
        # Public Function set_all_process_schedules(olp_drill_rivet_profile)
        #     Dim iProfiles (2)
        #     olp_drill_rivet_profile.SetAllProcessSchedules iProfiles
        #     set_all_process_schedules = iProfiles
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

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

    def set_precycle_feature(self, i_feature: str, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPrecycleFeature(CATBSTR iFeature,boolean iMatch)
                |     Set the precycle feature. The default value is NONE.
                |     Valid features are: DRILL Process:
                | 
                |         NONE
                |         HOLE
                | 
                |     RIVET Process:
                | 
                |         NONE
                |         RIVET
                |         BOLT
                | 
                |     DRILL-RIVET Process:
                | 
                |         NONE
                |         HOLE
                |         RIVET
                |         BOLT
                | 
                |     Parameters:
                | 
                |         iFeature
                |             The feature to be set 
                |         iMatch
                |             Whether this feature should be considered when matching profiles

        :param str i_feature:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPrecycleFeature(i_feature, i_match)

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
        # Public Function set_process_schedules(olp_drill_rivet_profile)
        #     Dim iProfiles (2)
        #     olp_drill_rivet_profile.SetProcessSchedules iProfiles
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
                |             existing spot profile for it to match. However if the default values of the
                |             profile have the same meaning as having the profile unset, then a profile set
                |             with default values will also match.

        :param str i_profile_type:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetProcessSchedulesToNothing(i_profile_type, i_match)

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
        return f'OLPDrillRivetProfile(name="{self.name}")'
