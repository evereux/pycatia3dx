"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotDrProfile(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrProfile
                | 
                | Represents an object that is Spot Drilling-Riveting profile Role: Spot
                | Drilling-Riveting profile contains description of Spot Drilling-Riveting
                | parameters associated with a particular Spot Drilling-Riveting
                | operation.
                | 
                | See also:
                |     SpotDrProfile
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def approach_clearance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApproachClearance() As double
                |     This method gets the Approach Clearance
                | 
                |     Parameters:
                | 
                |         oApproachClearance,
                |             Approach Clearance 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: float
        """

        return self.com_object.ApproachClearance

    @approach_clearance.setter
    def approach_clearance(self, value: float):
        """
        :param float value:
        """

        self.com_object.ApproachClearance = value

    @property
    def approach_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApproachDirection() As DELDRApproachDirection
                |     This method gets the Direction in which the Tool
                |     approaches
                | 
                |     Parameters:
                | 
                |         oApproachDirection,
                |             Tool Approach Direction Valid values: ApproachXPlus,
                |             ApproachXMinus, ApproachYPlus, ApproachYMinus, ApproachZPlus, ApproachZMinus
                |             
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: DELDRApproachDirection
        """

        return self.com_object.ApproachDirection

    @approach_direction.setter
    def approach_direction(self, value: int):
        """
        :param int value:
        """

        self.com_object.ApproachDirection = value

    @property
    def precycle_feature(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PrecycleFeature() As DELDRProfilePrecycle
                |     This method gets the associated PreCycle feature
                | 
                |     Parameters:
                | 
                |         oPreCycle,
                |             Valid Values: None, Hole, Rivet or Bolt 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: DELDRProfilePrecycle
        """

        return self.com_object.PrecycleFeature

    @precycle_feature.setter
    def precycle_feature(self, value: int):
        """
        :param int value:
        """

        self.com_object.PrecycleFeature = value

    @property
    def retract_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RetractDistance() As double
                |     This method gets the Retract Distance
                | 
                |     Parameters:
                | 
                |         oRetractDistance,
                |             Retract Distance 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: float
        """

        return self.com_object.RetractDistance

    @retract_distance.setter
    def retract_distance(self, value: float):
        """
        :param float value:
        """

        self.com_object.RetractDistance = value

    @property
    def tool_kin_simulation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ToolKinSimulation() As boolean
                |     This method gets whether tool kinematic simulation is enabled or
                |     not
                | 
                |     Parameters:
                | 
                |         oEnabled,
                |             TRUE or FALSE 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: bool
        """

        return self.com_object.ToolKinSimulation

    @tool_kin_simulation.setter
    def tool_kin_simulation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ToolKinSimulation = value

    def add_user_cycle(self, i_name: str, o_cycle: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddUserCycle(CATBSTR iName,DELDRProfileCycle oCycle)
                |     This method adds a user specified cycle in the profile
                | 
                |     Parameters:
                | 
                |         iName,
                |             Name of the Cycle 
                |         oCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param str i_name:
        :param int o_cycle:
        :return: None
        """
        return self.com_object.AddUserCycle(i_name, o_cycle)

    def get_accuracy_profile(self, i_move: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAccuracyProfile(DELDRProfileMoves iMove) As AnyObject
                |     This method gets the Accuracy profile associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Retract
                |             
                |         ohAccuracyProfile,
                |             Accuracy profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetAccuracyProfile(i_move))

    def get_approach_clearance_parameter(self, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetApproachClearanceParameter(CATBSTR oParamName,AnyObject
                | oProfile)
                |     This method gets the Approach Clearance applicative profile/parameter and
                |     the attribute name
                | 
                |     Parameters:
                | 
                |         oParamName,
                |             Associated Attribute Name 
                |         oProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetApproachClearanceParameter(o_param_name, o_profile.com_object)

    def get_cycle_accuracy_profile(self, i_cycle: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleAccuracyProfile(DELDRProfileCycle iCycle) As
                | AnyObject
                |     This method gets the Accuracy profile associated with the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         ohAccuracyProfile,
                |             Accuracy profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetCycleAccuracyProfile(i_cycle))

    def get_cycle_depth(self, i_cycle: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleDepth(DELDRProfileCycle iCycle) As double
                |     This method gets the Depth associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oDepth,
                |             Depth 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: float
        """
        return self.com_object.GetCycleDepth(i_cycle)

    def get_cycle_depth_parameter(self, i_cycle: int, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCycleDepthParameter(DELDRProfileCycle iCycle,CATBSTR
                | oParamName,AnyObject oProfile)
                |     This method gets the Cycle Depth applicative profile/parameter and the
                |     attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oParamName,
                |             Associated Attribute Name 
                |         oProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetCycleDepthParameter(i_cycle, o_param_name, o_profile.com_object)

    def get_cycle_distance(self, i_cycle: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleDistance(DELDRProfileCycle iCycle) As double
                |     This method gets the Distance associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oDistance,
                |             Distance 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: float
        """
        return self.com_object.GetCycleDistance(i_cycle)

    def get_cycle_distance_parameter(self, i_cycle: int, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCycleDistanceParameter(DELDRProfileCycle iCycle,CATBSTR
                | oParamName,AnyObject oProfile)
                |     This method gets the Cycle Distance applicative profile/parameter and the
                |     attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oParamName,
                |             Associated Attribute Name 
                |         oProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetCycleDistanceParameter(i_cycle, o_param_name, o_profile.com_object)

    def get_cycle_joint_direction(self, i_cycle: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleJointDirection(DELDRProfileCycle iCycle) As short
                |     This method gets the Direction in which the Joint Moves for the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oJointDir,
                |             Joint Direction - Positive or Negative 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: int
        """
        return self.com_object.GetCycleJointDirection(i_cycle)

    def get_cycle_joint_number(self, i_cycle: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleJointNumber(DELDRProfileCycle iCycle) As short
                |     This method gets the Joint Number associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oJointNum,
                |             Joint Number 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: int
        """
        return self.com_object.GetCycleJointNumber(i_cycle)

    def get_cycle_motion_profile(self, i_cycle: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleMotionProfile(DELDRProfileCycle iCycle) As
                | AnyObject
                |     This method gets the Motion profile associated with the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         ohMotionProfile,
                |             Motion profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetCycleMotionProfile(i_cycle))

    def get_cycle_name(self, i_cycle: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleName(DELDRProfileCycle iCycle) As CATBSTR
                |     This method gets the Cycle name associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oCycleName,
                |             Cycle Name 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: str
        """
        return self.com_object.GetCycleName(i_cycle)

    def get_cycle_simulation_time(self, i_cycle: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleSimulationTime(DELDRProfileCycle iCycle) As
                | double
                |     This method gets the Simulation Time associated to the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oSimulationTime,
                |             Simulation Time 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: float
        """
        return self.com_object.GetCycleSimulationTime(i_cycle)

    def get_cycle_simulation_time_parameter(self, i_cycle: int, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCycleSimulationTimeParameter(DELDRProfileCycle iCycle,CATBSTR
                | oParamName,AnyObject oProfile)
                |     This method gets the Cycle Simulation Time applicative profile/parameter
                |     and the attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oParamName,
                |             Associated Attribute Name 
                |         oProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetCycleSimulationTimeParameter(i_cycle, o_param_name, o_profile.com_object)

    def get_cycle_start_joint_values(self, i_cycle: int, o_tool_joint_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCycleStartJointValues(DELDRProfileCycle iCycle,CATSafeArrayVariant
                | oToolJointValues)
                |     This method gets the Joint Values of the Tool associated to the Tool
                |     Starting Position for the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oToolJointValues,
                |             List of Joint Values 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param tuple o_tool_joint_values:
        :return: None
        """
        return self.com_object.GetCycleStartJointValues(i_cycle, o_tool_joint_values)

    def get_cycle_tcpx_offset(self, i_cycle: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleTCPXOffset(DELDRProfileCycle iCycle) As double
                |     This method gets the TCP X Offset associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oTCPXOffset,
                |             TCP X Offset 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: float
        """
        return self.com_object.GetCycleTCPXOffset(i_cycle)

    def get_cycle_tcpx_offset_parameter(self, i_cycle: int, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCycleTCPXOffsetParameter(DELDRProfileCycle iCycle,CATBSTR
                | oParamName,AnyObject oProfile)
                |     This method gets the Cycle TCP X Offset applicative profile/parameter and
                |     the attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oParamName,
                |             Associated Attribute Name 
                |         oProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetCycleTCPXOffsetParameter(i_cycle, o_param_name, o_profile.com_object)

    def get_cycle_tcpy_offset(self, i_cycle: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleTCPYOffset(DELDRProfileCycle iCycle) As double
                |     This method gets the TCP Y Offset associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oTCPYOffset,
                |             TCP Y Offset 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: float
        """
        return self.com_object.GetCycleTCPYOffset(i_cycle)

    def get_cycle_tcpy_offset_parameter(self, i_cycle: int, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCycleTCPYOffsetParameter(DELDRProfileCycle iCycle,CATBSTR
                | oParamName,AnyObject oProfile)
                |     This method gets the Cycle TCP Y Offset applicative profile/parameter and
                |     the attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oParamName,
                |             Associated Attribute Name 
                |         oProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetCycleTCPYOffsetParameter(i_cycle, o_param_name, o_profile.com_object)

    def get_cycle_tcpz_offset(self, i_cycle: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCycleTCPZOffset(DELDRProfileCycle iCycle) As double
                |     This method gets the TCP Z Offset associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oTCPZOffset,
                |             TCP Z Offset 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: float
        """
        return self.com_object.GetCycleTCPZOffset(i_cycle)

    def get_cycle_tcpz_offset_parameter(self, i_cycle: int, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCycleTCPZOffsetParameter(DELDRProfileCycle iCycle,CATBSTR
                | oParamName,AnyObject oProfile)
                |     This method gets the Cycle TCP Z Offset applicative profile/parameter and
                |     the attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         oParamName,
                |             Associated Attribute Name 
                |         oProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetCycleTCPZOffsetParameter(i_cycle, o_param_name, o_profile.com_object)

    def get_cycle_tool_profile(self, i_cycle: int, oh_tool_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCycleToolProfile(DELDRProfileCycle iCycle,AnyObject
                | ohToolProfile)
                |     This method gets the Tool profile associated with the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         ohToolProfile,
                |             Tool profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param AnyObject oh_tool_profile:
        :return: None
        """
        return self.com_object.GetCycleToolProfile(i_cycle, oh_tool_profile.com_object)

    def get_cycles(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetCycles(CATSafeArrayVariant oCycleValues,CATSafeArrayVariant
                | oEnabledStatus)
                |     This method gets the list of cycles involved in the action
                |
                |     Parameters:
                |
                |         oCycleValues,
                |             List of cycles that have been defined
                |         oEnabledStatus,
                |             List of cycles that are enabled
                |
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: tuple
        """
        return self.com_object.GetCycles()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_cycles'
        # vba_code = """
        # Public Function get_cycles(spot_dr_profile)
        #     Dim oCycleValues (2)
        #     spot_dr_profile.GetCycles oCycleValues
        #     get_cycles = oCycleValues
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_motion_profile(self, i_move: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMotionProfile(DELDRProfileMoves iMove) As AnyObject
                |     This method gets the Motion profile associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Retract
                |             
                |         ohMotionProfile,
                |             Motion profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetMotionProfile(i_move))

    def get_move_status(self, i_move: int, o_enabled: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMoveStatus(DELDRProfileMoves iMove,boolean oEnabled)
                |     This method gets the Move status associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Action, Retract
                |             
                |         oEnabled,
                |             TRUE or FALSE 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param bool o_enabled:
        :return: None
        """
        return self.com_object.GetMoveStatus(i_move, o_enabled)

    def get_profile_type(self, o_profile_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetProfileType(DELDRProfileType oProfileType)
                |     This method gets the profile type
                | 
                |     Parameters:
                | 
                |         oProfileType,
                |             Valid Values : DrillOnly, RivetOnly, DrillRivet 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int o_profile_type:
        :return: None
        """
        return self.com_object.GetProfileType(o_profile_type)

    def get_retract_distance_parameter(self, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRetractDistanceParameter(CATBSTR oParamName,AnyObject
                | oProfile)
                |     This method gets the Retract Distance applicative profile/parameter and the
                |     attribute name
                | 
                |     Parameters:
                | 
                |         oParamName,
                |             Associated Attribute Name 
                |         oProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetRetractDistanceParameter(o_param_name, o_profile.com_object)

    def remove_user_cycle(self, i_cycle: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveUserCycle(DELDRProfileCycle iCycle)
                |     This method removes a user specified cycle from the
                |     profile
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :return: None
        """
        return self.com_object.RemoveUserCycle(i_cycle)

    def set_accuracy_profile(self, i_move: int, ih_accuracy_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAccuracyProfile(DELDRProfileMoves iMove,AnyObject
                | ihAccuracyProfile)
                |     This method sets the Accuracy profile associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Retract
                |             
                |         ihAccuracyProfile,
                |             Accuracy profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param AnyObject ih_accuracy_profile:
        :return: None
        """
        return self.com_object.SetAccuracyProfile(i_move, ih_accuracy_profile.com_object)

    def set_approach_clearance_parameter(self, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApproachClearanceParameter(CATBSTR iParamName,AnyObject
                | iProfile)
                |     This method sets the Approach Clearance applicative profile/parameter and
                |     the attribute name
                | 
                |     Parameters:
                | 
                |         iParamName,
                |             Associated Attribute Name 
                |         iProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetApproachClearanceParameter(i_param_name, i_profile.com_object)

    def set_cycle_accuracy_profile(self, i_cycle: int, ih_accuracy_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleAccuracyProfile(DELDRProfileCycle iCycle,AnyObject
                | ihAccuracyProfile)
                |     This method sets the Accuracy profile associated with the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         ihAccuracyProfile,
                |             Accuracy profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param AnyObject ih_accuracy_profile:
        :return: None
        """
        return self.com_object.SetCycleAccuracyProfile(i_cycle, ih_accuracy_profile.com_object)

    def set_cycle_depth(self, i_cycle: int, i_depth: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleDepth(DELDRProfileCycle iCycle,double iDepth)
                |     This method sets the Depth associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iDepth,
                |             Depth 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param float i_depth:
        :return: None
        """
        return self.com_object.SetCycleDepth(i_cycle, i_depth)

    def set_cycle_depth_parameter(self, i_cycle: int, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleDepthParameter(DELDRProfileCycle iCycle,CATBSTR
                | iParamName,AnyObject iProfile)
                |     This method sets the Cycle Depth applicative profile/parameter and the
                |     attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iParamName,
                |             Associated Attribute Name 
                |         iProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetCycleDepthParameter(i_cycle, i_param_name, i_profile.com_object)

    def set_cycle_distance(self, i_cycle: int, i_distance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleDistance(DELDRProfileCycle iCycle,double
                | iDistance)
                |     This method sets the Distance associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iDistance,
                |             Distance 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param float i_distance:
        :return: None
        """
        return self.com_object.SetCycleDistance(i_cycle, i_distance)

    def set_cycle_distance_parameter(self, i_cycle: int, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleDistanceParameter(DELDRProfileCycle iCycle,CATBSTR
                | iParamName,AnyObject iProfile)
                |     This method sets the Cycle Distance applicative profile/parameter and the
                |     attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iParamName,
                |             Associated Attribute Name 
                |         iProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetCycleDistanceParameter(i_cycle, i_param_name, i_profile.com_object)

    def set_cycle_joint_direction(self, i_cycle: int, i_joint_dir: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleJointDirection(DELDRProfileCycle iCycle,short
                | iJointDir)
                |     This method sets the Direction in which the Joint Moves for the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iJointDir,
                |             Joint Direction - Positive or Negative 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param int i_joint_dir:
        :return: None
        """
        return self.com_object.SetCycleJointDirection(i_cycle, i_joint_dir)

    def set_cycle_joint_number(self, i_cycle: int, i_joint_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleJointNumber(DELDRProfileCycle iCycle,short
                | iJointNum)
                |     This method sets the Joint Number associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iJointNum,
                |             Joint Number 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param int i_joint_num:
        :return: None
        """
        return self.com_object.SetCycleJointNumber(i_cycle, i_joint_num)

    def set_cycle_motion_profile(self, i_cycle: int, ih_motion_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleMotionProfile(DELDRProfileCycle iCycle,AnyObject
                | ihMotionProfile)
                |     This method sets the Motion profile associated with the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         ihMotionProfile,
                |             Motion profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param AnyObject ih_motion_profile:
        :return: None
        """
        return self.com_object.SetCycleMotionProfile(i_cycle, ih_motion_profile.com_object)

    def set_cycle_name(self, i_cycle: int, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleName(DELDRProfileCycle iCycle,CATBSTR iName)
                |     This method sets the cycle name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iCycleName,
                |             Name of the Cycle 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str i_name:
        :return: None
        """
        return self.com_object.SetCycleName(i_cycle, i_name)

    def set_cycle_simulation_time(self, i_cycle: int, i_simulation_time: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleSimulationTime(DELDRProfileCycle iCycle,double
                | iSimulationTime)
                |     This method sets the Simulation Time associated to the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iSimulationTime,
                |             Simulation Time 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param float i_simulation_time:
        :return: None
        """
        return self.com_object.SetCycleSimulationTime(i_cycle, i_simulation_time)

    def set_cycle_simulation_time_parameter(self, i_cycle: int, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleSimulationTimeParameter(DELDRProfileCycle iCycle,CATBSTR
                | iParamName,AnyObject iProfile)
                |     This method sets the Cycle Simulation Time applicative profile/parameter
                |     and the attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iParamName,
                |             Associated Attribute Name 
                |         iProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetCycleSimulationTimeParameter(i_cycle, i_param_name, i_profile.com_object)

    def set_cycle_start_joint_values(self, i_cycle: int, i_tool_joint_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleStartJointValues(DELDRProfileCycle iCycle,CATSafeArrayVariant
                | iToolJointValues)
                |     This method sets the Joint Values of the Tool associated to the Tool
                |     Starting Position for the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iToolJointValues,
                |             List of Joint Values 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param tuple i_tool_joint_values:
        :return: None
        """
        return self.com_object.SetCycleStartJointValues(i_cycle, i_tool_joint_values)

    def set_cycle_status(self, i_cycle: int, i_status: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleStatus(DELDRProfileCycle iCycle,boolean iStatus)
                |     This method Sets the cycle status
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iStatus,
                |             TRUE or FALSE 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param bool i_status:
        :return: None
        """
        return self.com_object.SetCycleStatus(i_cycle, i_status)

    def set_cycle_tcpx_offset(self, i_cycle: int, i_tcpx_offset: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleTCPXOffset(DELDRProfileCycle iCycle,double
                | iTCPXOffset)
                |     This method sets the TCP X Offset associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iTCPXOffset,
                |             TCP X Offset 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param float i_tcpx_offset:
        :return: None
        """
        return self.com_object.SetCycleTCPXOffset(i_cycle, i_tcpx_offset)

    def set_cycle_tcpx_offset_parameter(self, i_cycle: int, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleTCPXOffsetParameter(DELDRProfileCycle iCycle,CATBSTR
                | iParamName,AnyObject iProfile)
                |     This method sets the Cycle TCP X Offset applicative profile/parameter and
                |     the attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iParamName,
                |             Associated Attribute Name 
                |         iProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetCycleTCPXOffsetParameter(i_cycle, i_param_name, i_profile.com_object)

    def set_cycle_tcpy_offset(self, i_cycle: int, i_tcpy_offset: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleTCPYOffset(DELDRProfileCycle iCycle,double
                | iTCPYOffset)
                |     This method sets the TCP Y Offset associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iTCPYOffset,
                |             TCP Y Offset 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param float i_tcpy_offset:
        :return: None
        """
        return self.com_object.SetCycleTCPYOffset(i_cycle, i_tcpy_offset)

    def set_cycle_tcpy_offset_parameter(self, i_cycle: int, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleTCPYOffsetParameter(DELDRProfileCycle iCycle,CATBSTR
                | iParamName,AnyObject iProfile)
                |     This method sets the Cycle TCP Y Offset applicative profile/parameter and
                |     the attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iParamName,
                |             Associated Attribute Name 
                |         iProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetCycleTCPYOffsetParameter(i_cycle, i_param_name, i_profile.com_object)

    def set_cycle_tcpz_offset(self, i_cycle: int, i_tcpz_offset: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleTCPZOffset(DELDRProfileCycle iCycle,double
                | iTCPZOffset)
                |     This method sets the TCP Z Offset associated to the cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iTCPZOffset,
                |             TCP Z Offset 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param float i_tcpz_offset:
        :return: None
        """
        return self.com_object.SetCycleTCPZOffset(i_cycle, i_tcpz_offset)

    def set_cycle_tcpz_offset_parameter(self, i_cycle: int, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleTCPZOffsetParameter(DELDRProfileCycle iCycle,CATBSTR
                | iParamName,AnyObject iProfile)
                |     This method sets the Cycle TCP Z Offset applicative profile/parameter and
                |     the attribute name
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         iParamName,
                |             Associated Attribute Name 
                |         iProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetCycleTCPZOffsetParameter(i_cycle, i_param_name, i_profile.com_object)

    def set_cycle_tool_profile(self, i_cycle: int, ih_tool_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCycleToolProfile(DELDRProfileCycle iCycle,AnyObject
                | ihToolProfile)
                |     This method sets the Tool profile associated with the
                |     cycle
                | 
                |     Parameters:
                | 
                |         iCycle,
                |             Valid Values: Drill, CounterSink, RivetBolt, Sealant, User1 to
                |             User7 
                |         ihToolProfile,
                |             Tool profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_cycle:
        :param AnyObject ih_tool_profile:
        :return: None
        """
        return self.com_object.SetCycleToolProfile(i_cycle, ih_tool_profile.com_object)

    def set_motion_profile(self, i_move: int, ih_motion_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionProfile(DELDRProfileMoves iMove,AnyObject
                | ihMotionProfile)
                |     This method sets the Motion profile associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Retract
                |             
                |         ihMotionProfile,
                |             Motion profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param AnyObject ih_motion_profile:
        :return: None
        """
        return self.com_object.SetMotionProfile(i_move, ih_motion_profile.com_object)

    def set_move_status(self, i_move: int, i_enabled: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMoveStatus(DELDRProfileMoves iMove,boolean iEnabled)
                |     This method sets the Move status associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Action, Retract
                |             
                |         iEnabled,
                |             TRUE or FALSE 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param bool i_enabled:
        :return: None
        """
        return self.com_object.SetMoveStatus(i_move, i_enabled)

    def set_retract_distance_parameter(self, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRetractDistanceParameter(CATBSTR iParamName,AnyObject
                | iProfile)
                |     This method sets the Retract Distance applicative profile/parameter and the
                |     attribute name
                | 
                |     Parameters:
                | 
                |         iParamName,
                |             Associated Attribute Name 
                |         iProfile,
                |             Associated Profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetRetractDistanceParameter(i_param_name, i_profile.com_object)

    def __repr__(self):
        return f'SpotDrProfile(name="{self.name}")'
