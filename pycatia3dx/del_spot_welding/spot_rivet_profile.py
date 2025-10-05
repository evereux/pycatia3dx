"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotRivetProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotRivetProfile
                | 
                | Represents an object that is Spot-Rivet profile Role: Spot-Rivet profile
                | contains description of Spot-Rivet parameters associated with a particular
                | Rivet operation.
                | 
                | See also:
                |     SpotRivetProfile
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def approach_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApproachDirection() As DELSpotRivetApproachDirection
                |     This method gets the Approach Direction
                | 
                |     Parameters:
                | 
                |         oApproachDirection,
                |             Approach Direction 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: DELSpotRivetApproachDirection
        """

        return self.com_object.ApproachDirection

    @approach_direction.setter
    def approach_direction(self, value: int):
        """
        :param int value:
        """

        self.com_object.ApproachDirection = value

    @property
    def hold_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HoldTime() As double
                |     This method gets the Hold Time
                | 
                |     Parameters:
                | 
                |         oHoldTime,
                |             Hold Time 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: float
        """

        return self.com_object.HoldTime

    @hold_time.setter
    def hold_time(self, value: float):
        """
        :param float value:
        """

        self.com_object.HoldTime = value

    @property
    def joint_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property JointDirection() As short
                |     This method gets the Joint Direction
                | 
                |     Parameters:
                | 
                |         oJointDirection,
                |             Joint Direction 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: int
        """

        return self.com_object.JointDirection

    @joint_direction.setter
    def joint_direction(self, value: int):
        """
        :param int value:
        """

        self.com_object.JointDirection = value

    @property
    def joint_number(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property JointNumber() As short
                |     This method gets the Joint Number
                | 
                |     Parameters:
                | 
                |         oJointNumber,
                |             Joint Number 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: int
        """

        return self.com_object.JointNumber

    @joint_number.setter
    def joint_number(self, value: int):
        """
        :param int value:
        """

        self.com_object.JointNumber = value

    @property
    def part_thickness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PartThickness() As double
                |     This method gets the Part Thickness
                | 
                |     Parameters:
                | 
                |         oPartThickness,
                |             Part Thickness 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: float
        """

        return self.com_object.PartThickness

    @part_thickness.setter
    def part_thickness(self, value: float):
        """
        :param float value:
        """

        self.com_object.PartThickness = value

    @property
    def push_depth(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PushDepth() As double
                |     This method gets the Push Depth
                | 
                |     Parameters:
                | 
                |         oPushDepth,
                |             Push Depth 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: float
        """

        return self.com_object.PushDepth

    @push_depth.setter
    def push_depth(self, value: float):
        """
        :param float value:
        """

        self.com_object.PushDepth = value

    @property
    def tool_close_position(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ToolClosePosition() As double
                |     This method gets the Tool Close Position
                | 
                |     Parameters:
                | 
                |         oToolClosePosition,
                |             Tool Close Position 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: float
        """

        return self.com_object.ToolClosePosition

    @tool_close_position.setter
    def tool_close_position(self, value: float):
        """
        :param float value:
        """

        self.com_object.ToolClosePosition = value

    def get_accuracy_profile(self, i_move: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAccuracyProfile(DELSpotRivetProfileMoves iMove) As
                | AnyObject
                |     This method gets the Accuracy profile associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Action, Retract
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

    def get_hold_time_parameter(self, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetHoldTimeParameter(CATBSTR oParamName,AnyObject
                | oProfile)
                |     This method gets the Hold Time applicative profile and the attribute
                |     name
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
        return self.com_object.GetHoldTimeParameter(o_param_name, o_profile.com_object)

    def get_motion_profile(self, i_move: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMotionProfile(DELSpotRivetProfileMoves iMove) As
                | AnyObject
                |     This method gets the Motion profile associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Action, Retract
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
                | Sub GetMoveStatus(DELSpotRivetProfileMoves iMove,boolean
                | oEnabled)
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

    def get_moving_tip_clearance_parameter(self, i_move: int, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMovingTipClearanceParameter(DELSpotRivetProfileMoves iMove,CATBSTR
                | oParamName,AnyObject oProfile)
                |     This method gets the Moving Tip Clearance parameter associated with the
                |     given Spot-Rivet Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Valid Moves : Approach, Start, Action, Complete, Retract 
                |         oParamName,
                |             Input parameter name. 
                |         oProfile,
                |             Output Moving Tip Clearance profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetMovingTipClearanceParameter(i_move, o_param_name, o_profile.com_object)

    def get_moving_tip_clearance_value(self, i_move: int, o_tip_clearance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMovingTipClearanceValue(DELSpotRivetProfileMoves iMove,double
                | oTipClearance)
                |     This method gets the Moving Tip Clearance value
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Valid Moves : Approach, Start, Action, Complete, Retract 
                |         oTipClearance,
                |             Moving Tip Clearance value 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param float o_tip_clearance:
        :return: None
        """
        return self.com_object.GetMovingTipClearanceValue(i_move, o_tip_clearance)

    def get_push_depth_parameter(self, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPushDepthParameter(CATBSTR oParamName,AnyObject
                | oProfile)
                |     This method gets the Push Depth applicative profile and the attribute
                |     name
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
        return self.com_object.GetPushDepthParameter(o_param_name, o_profile.com_object)

    def get_stationary_tip_clearance_parameter(self, i_move: int, o_param_name: str, o_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetStationaryTipClearanceParameter(DELSpotRivetProfileMoves iMove,CATBSTR
                | oParamName,AnyObject oProfile)
                |     This method gets the Stationary Tip Clearance parameter associated with the
                |     given Spot-Rivet Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Valid Moves : Approach, Start, Action, Complete, Retract 
                |         oParamName,
                |             Input parameter name. 
                |         oProfile,
                |             Output Stationary Tip Clearance profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param str o_param_name:
        :param AnyObject o_profile:
        :return: None
        """
        return self.com_object.GetStationaryTipClearanceParameter(i_move, o_param_name, o_profile.com_object)

    def get_stationary_tip_clearance_value(self, i_move: int, o_tip_clearance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetStationaryTipClearanceValue(DELSpotRivetProfileMoves iMove,double
                | oTipClearance)
                |     This method gets the Stationary Tip Clearance value
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Valid Moves : Approach, Start, Action, Complete, Retract 
                |         oTipClearance,
                |             Stationary Tip Clearance value 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param float o_tip_clearance:
        :return: None
        """
        return self.com_object.GetStationaryTipClearanceValue(i_move, o_tip_clearance)

    def set_accuracy_profile(self, i_move: int, ih_accuracy_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAccuracyProfile(DELSpotRivetProfileMoves iMove,AnyObject
                | ihAccuracyProfile)
                |     This method sets the Accuracy profile associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Action, Retract
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

    def set_hold_time_parameter(self, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetHoldTimeParameter(CATBSTR iParamName,AnyObject
                | iProfile)
                |     This method sets the Hold Time applicative profile and the attribute
                |     name
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
        return self.com_object.SetHoldTimeParameter(i_param_name, i_profile.com_object)

    def set_motion_profile(self, i_move: int, ih_motion_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionProfile(DELSpotRivetProfileMoves iMove,AnyObject
                | ihMotionProfile)
                |     This method sets the Motion profile associated with the given Drill-Rivet
                |     Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Drill-Rivet Move type. Valid values: Approach, Action, Retract
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
                | Sub SetMoveStatus(DELSpotRivetProfileMoves iMove,boolean
                | iEnabled)
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

    def set_moving_tip_clearance_parameter(self, i_move: int, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMovingTipClearanceParameter(DELSpotRivetProfileMoves iMove,CATBSTR
                | iParamName,AnyObject iProfile)
                |     This method sets the Moving Tip Clearance parameter associated with the
                |     given Spot-Rivet Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Spot-Rivet Move type. Valid values: Approach, Start, Action,
                |             Complete, Retract 
                |         iParamName,
                |             parameter name 
                |         iProfile,
                |             Moving Tip Clearance profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetMovingTipClearanceParameter(i_move, i_param_name, i_profile.com_object)

    def set_moving_tip_clearance_value(self, i_move: int, i_tip_clearance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMovingTipClearanceValue(DELSpotRivetProfileMoves iMove,double
                | iTipClearance)
                |     This method sets the Moving Tip Clearance value associated with the given
                |     Spot-Rivet Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Spot-Rivet Move type. Valid values: Approach, Start, Action,
                |             Complete, Retract 
                |         iTipClearance,
                |             Moving Tip Clearance Value. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param float i_tip_clearance:
        :return: None
        """
        return self.com_object.SetMovingTipClearanceValue(i_move, i_tip_clearance)

    def set_push_depth_parameter(self, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPushDepthParameter(CATBSTR iParamName,AnyObject
                | iProfile)
                |     This method sets the Push Depth applicative profile and the attribute
                |     name
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
        return self.com_object.SetPushDepthParameter(i_param_name, i_profile.com_object)

    def set_stationary_tip_clearance_parameter(self, i_move: int, i_param_name: str, i_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStationaryTipClearanceParameter(DELSpotRivetProfileMoves iMove,CATBSTR
                | iParamName,AnyObject iProfile)
                |     This method sets the Stationary Tip Clearance profile associated with the
                |     given Spot-Rivet Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Spot-Rivet Move type. Valid values: Approach, Start, Action,
                |             Complete, Retract 
                |         iParamName,
                |             parameter name 
                |         iProfile,
                |             Stationary Tip Clearance profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_move:
        :param str i_param_name:
        :param AnyObject i_profile:
        :return: None
        """
        return self.com_object.SetStationaryTipClearanceParameter(i_move, i_param_name, i_profile.com_object)

    def set_stationary_tip_clearance_value(self, i_move: int, i_tip_clearance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStationaryTipClearanceValue(DELSpotRivetProfileMoves iMove,double
                | iTipClearance)
                |     This method sets the Stationary Tip Clearance value associated with the
                |     given Spot-Rivet Move
                | 
                |     Parameters:
                | 
                |         iMove,
                |             Spot-Rivet Move type. Valid values: Approach, Start, Action,
                |             Complete, Retract 
                |         iTipClearance,
                |             Stationary Tip Clearance Value. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param int i_move:
        :param float i_tip_clearance:
        :return: None
        """
        return self.com_object.SetStationaryTipClearanceValue(i_move, i_tip_clearance)

    def __repr__(self):
        return f'SpotRivetProfile(name="{ self.name }")'
