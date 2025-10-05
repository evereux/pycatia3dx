"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import Variant


class SpotWeldProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotWeldProfile
                | 
                | Represents an object that is Spot Welding profile Role: Spot Welding profile
                | contains description of Spot welding parameters associated with a particular
                | Spot welding operation.
                | 
                | See also:
                |     SpotWeldProfiles
    
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
                | Property ApproachDirection(DELSpotProfileApproachDir
                | iSpotProfileApproachDir)
                |     This method sets the Approach direction
                | 
                |     Parameters:
                | 
                |         iSpotProfileApproachDir,
                |             approach direction. Valid values : X axis = 0, Y axis = 1, Z axis =2, -ve X Axis =3, -ve Y Axis =4, -ve Z Axis =5 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.ApproachDirection = Neg_Z_Axis
                |            End If

        :return: int
        """

        return self.com_object.ApproachDirection

    @approach_direction.setter
    def approach_direction(self, value: int):
        """
        :param int value:
        """

        self.com_object.ApproachDirection = value

    @property
    def controller_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ControllerName() As CATBSTR (Read Only)
                |     Returns the name of robot controller that the profile is associated
                |     with
                | 
                |     Parameters:
                | 
                |         CATBSTR
                |             The name of the robot controller 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim  oName  As  CATBSTR  =  MySWProfile.ControllerName
                |            End If

        :return: str
        """

        return self.com_object.ControllerName

    @property
    def part_thickness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PartThickness(double iThickness)
                |     This method sets the Part Thickness
                | 
                |     Parameters:
                | 
                |         iThickness,
                |             Part thickness. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.PartThickness = 10.5
                |            End If

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
    def pressure_move_push_depth(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PressureMovePushDepth(double iPushDepth)
                |     This method sets the push depth for Pressure Move
                | 
                |     Parameters:
                | 
                |         iPushDepth,
                |             Push Depth. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.PressureMovePushDepth = 10.0
                |            End If

        :return: float
        """

        return self.com_object.PressureMovePushDepth

    @pressure_move_push_depth.setter
    def pressure_move_push_depth(self, value: float):
        """
        :param float value:
        """

        self.com_object.PressureMovePushDepth = value

    @property
    def pressure_speed_factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PressureSpeedFactor(double iSpeedFactor)
                |     This method sets the speed factor for Pressure Move
                | 
                |     Parameters:
                | 
                |         iSpeedFactor,
                |             Speed factor 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.PressureSpeedFactor = 10.0
                |            End  If

        :return: float
        """

        return self.com_object.PressureSpeedFactor

    @pressure_speed_factor.setter
    def pressure_speed_factor(self, value: float):
        """
        :param float value:
        """

        self.com_object.PressureSpeedFactor = value

    @property
    def spot_moves(self) -> Variant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpotMoves(CATSafeArrayVariant iSpotMoves)
                |     This method sets the different spot moves in the spot profile By default
                |     "Pressure move" and "Weld" spot moves are set by default when the spot profile
                |     is created.
                | 
                |     Parameters:
                | 
                |         iSpotMoves,
                |             list of spot moves to be set in the spot profile. Each item in the
                |             list is a DELSpotProfileMoves. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim iSpotMoves As CATSafeArrayVariant
                |            .....
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.SpotMoves = iSpotMoves
                |            End If

        :return: Variant
        """

        return self.com_object.SpotMoves

    @spot_moves.setter
    def spot_moves(self, value: Variant):
        """
        :param Variant value:
        """

        self.com_object.SpotMoves = value

    @property
    def weld_delay(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WeldDelay(double iWeldDelay)
                |     This method sets the weld delay
                | 
                |     Parameters:
                | 
                |         iWeldDelay,
                |             Weld delay 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.WeldDelay = 10.0
                |            End If

        :return: float
        """

        return self.com_object.WeldDelay

    @weld_delay.setter
    def weld_delay(self, value: float):
        """
        :param float value:
        """

        self.com_object.WeldDelay = value

    @property
    def weld_pressure_stabilization_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WeldPressureStabilizationTime(double
                | iWeldPressureStabilizationTime)
                |     This method sets the weld pressure stabilization time
                | 
                |     Parameters:
                | 
                |         iWeldPressureStabilizationTime,
                |             Weld pressure stabilization time 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.WeldPressureStabilizationTime = 10.0
                |            End If

        :return: float
        """

        return self.com_object.WeldPressureStabilizationTime

    @weld_pressure_stabilization_time.setter
    def weld_pressure_stabilization_time(self, value: float):
        """
        :param float value:
        """

        self.com_object.WeldPressureStabilizationTime = value

    @property
    def weld_time_table(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WeldTimeTable(AnyObject ispWeldTimeTable)
                |     This method gets the WeldTime Table
                | 
                |     Parameters:
                | 
                |         ispWeldTimeTable,
                |             WeldTime Table 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.WeldTimeTable = MyApplicativeFanucProfile;
                |            End If

        :return: AnyObject
        """

        return AnyObject(self.com_object.WeldTimeTable)

    @weld_time_table.setter
    def weld_time_table(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.WeldTimeTable = value

    def get_accuracy_profile(self, i_accuracy_profile_spot_moves: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAccuracyProfile(DELSpotAccuracyProfileAndAccelerationMoves
                | iAccuracyProfileSpotMoves) As AnyObject
                |     This method gets the Accuracy value associated with the given spot
                |     move
                | 
                |     Parameters:
                | 
                |         iAccuracyProfileSpotMoves,
                |             Move type. It is one of the value in
                |             DELSpotAccuracyProfileAndAccelerationMoves 
                |         ospAccProfile,
                |             Accuracy profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim  AccuracyProfile  As  CATIABase = MySWProfile.GetAccuracyProfile(AccuracyProfilePressureStartMove)
                |            End If

        :param int i_accuracy_profile_spot_moves:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetAccuracyProfile(i_accuracy_profile_spot_moves))

    def get_backup_move_stroke(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBackupMoveStroke(short iGunNumber) As double
                |     This method gets the Backup move stroke
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             gun number. Valid value: 1 or 2 
                |         iBackupMoveStroke,
                |             backup move stroke 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim oBackupMoveStroke As Double = MySWProfile.GetBackupMoveStroke(1)
                |            End If

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetBackupMoveStroke(i_gun_number)

    def get_closed_joint_value(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetClosedJointValue(short iGunNumber) As double
                |     This method gets the gun close joint value
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             Gun Number. Valid values : 1 or 2. 
                |         oJointValue,
                |             gun close joint value. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim oJointValue As double = MySWProfile.GetClosedJointValue(1)
                |            End If

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetClosedJointValue(i_gun_number)

    def get_gun_status(self, i_gun_number: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGunStatus(short iGunNumber) As boolean
                |     This method gets the status of the gun (used or not used)
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             Gun Number. Valid values : 1 or 2. 
                |         oGunStatus,
                |             Gun Status. FALSE - Gun is not used, TRUE - Gun is used
                |             
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim oGunStatus As boolean
                |            oGunStatus = MySWProfile.GetGunStatus(1)
                |            End If

        :param int i_gun_number:
        :return: bool
        """
        return self.com_object.GetGunStatus(i_gun_number)

    def get_gun_tip_close_direction(self, i_gun_number: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGunTipCloseDirection(short iGunNumber) As boolean
                |     This method gets the Gun Tip Close direction
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             gun number. Valid value: 1 or 2 
                |         oDirection,
                |             gun tip close direction. could be either: TRUE or FALSE. FALSE = decreasing or -ve gun axis value TRUE = increasing or +ve gun axis value 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            Dim oDirection As boolean = MySWProfile.GetGunTipCloseDirection(1)
                |            End If

        :param int i_gun_number:
        :return: bool
        """
        return self.com_object.GetGunTipCloseDirection(i_gun_number)

    def get_joint_number(self, i_gun_number: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetJointNumber(short iGunNumber) As short
                |     This method gets the Joint Number
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             Gun Number. Valid values : 1 or 2. 
                |         oJointNum,
                |             Joint Number. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim oJointNum As short
                |            oJointNum = MySWProfile.GetJointNumber(1)
                |            End If

        :param int i_gun_number:
        :return: int
        """
        return self.com_object.GetJointNumber(i_gun_number)

    def get_move_acceleration(self, i_accuracy_profile_spot_moves: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMoveAcceleration(DELSpotAccuracyProfileAndAccelerationMoves
                | iAccuracyProfileSpotMoves) As double
                |     This method gets the Acceleration to the given spot move
                | 
                |     Parameters:
                | 
                |         iAccuracyProfileSpotMoves,
                |             Move type. It is one of the value in
                |             DELSpotAccuracyProfileAndAccelerationMoves 
                |         oAcceleration,
                |             Acceleration 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim oPushDepth As Double = MySWProfile.GetMoveAcceleration(AccuracyProfilePressureStartMove)
                |            End If

        :param int i_accuracy_profile_spot_moves:
        :return: float
        """
        return self.com_object.GetMoveAcceleration(i_accuracy_profile_spot_moves)

    def get_moving_tip_clearance(self, i_gun_number: int, i_moving_tip_spot_moves: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMovingTipClearance(short iGunNumber,DELSpotMovingTipClearanceMoves
                | iMovingTipSpotMoves) As double
                |     This method gets the Moving Tip Clearance value
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             gun number. Valid value: 1 or 2 
                |         iMovingTipSpotMoves,
                |             Move type. It is one of the value in
                |             DELSpotMovingTipClearanceMoves. 
                |         oMovingTipClearance,
                |             Moving tip clearance. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim oMovingTipClearance As Double = MySWProfile.GetMovingTipClearance(MovingTipApproachMove)
                |            End If

        :param int i_gun_number:
        :param int i_moving_tip_spot_moves:
        :return: float
        """
        return self.com_object.GetMovingTipClearance(i_gun_number, i_moving_tip_spot_moves)

    def get_stationary_tip_clearance(self, i_stationary_tip_spot_moves: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetStationaryTipClearance(DELSpotStationaryTipClearanceMoves
                | iStationaryTipSpotMoves) As double
                |     This method gets the Moving Tip Clearance value
                | 
                |     Parameters:
                | 
                |         iStationaryTipSpotMoves,
                |             Move type. It is one of the value in
                |             DELSpotStationaryTipClearanceMoves 
                |         oTipClearance,
                |             Stationary tip clearance. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim oTipClearance As Double = MySWProfile.GetStationaryTipClearance(StationaryTipApproachAndBackupMove)
                |            End If

        :param int i_stationary_tip_spot_moves:
        :return: float
        """
        return self.com_object.GetStationaryTipClearance(i_stationary_tip_spot_moves)

    def set_accuracy_profile(self, i_accuracy_profile_spot_moves: int, isp_acc_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAccuracyProfile(DELSpotAccuracyProfileAndAccelerationMoves
                | iAccuracyProfileSpotMoves,AnyObject ispAccProfile)
                |     This method sets the Accuracy value to given spot move
                | 
                |     Parameters:
                | 
                |         iAccuracyProfileSpotMoves,
                |             Move type. It is one of the value in
                |             DELSpotAccuracyProfileAndAccelerationMoves 
                |         ispAccProfile,
                |             Accuracy profile. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.SetAccuracyProfile(AccuracyProfilePressureStartMove,
                |            MyAccuracyProfile)
                |            End If

        :param int i_accuracy_profile_spot_moves:
        :param AnyObject isp_acc_profile:
        :return: None
        """
        return self.com_object.SetAccuracyProfile(i_accuracy_profile_spot_moves, isp_acc_profile.com_object)

    def set_backup_move_stroke(self, i_gun_number: int, i_backup_move_stroke: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBackupMoveStroke(short iGunNumber,double
                | iBackupMoveStroke)
                |     This method sets the Backup move stroke
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             gun number. Valid value: 1 or 2 
                |         iBackupMoveStroke,
                |             backup move stroke 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.SetBackupMoveStroke(1, 0.75)
                |            End If

        :param int i_gun_number:
        :param float i_backup_move_stroke:
        :return: None
        """
        return self.com_object.SetBackupMoveStroke(i_gun_number, i_backup_move_stroke)

    def set_closed_joint_value(self, i_gun_number: int, i_joint_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetClosedJointValue(short iGunNumber,double iJointValue)
                |     This method sets the gun close joint value
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             Gun Number. Valid values : 1 or 2. 
                |         iJointValue,
                |             gun close joint value. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim iJointValue As double = 7.5;
                |            MySWProfile.SetClosedJointValue(1,iJointValue)
                |            End If

        :param int i_gun_number:
        :param float i_joint_value:
        :return: None
        """
        return self.com_object.SetClosedJointValue(i_gun_number, i_joint_value)

    def set_gun_status(self, i_gun_number: int, i_gun_status: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGunStatus(short iGunNumber,boolean iGunStatus)
                |     This method sets the status of the gun (used or not used)
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             Gun Number. Valid values : 1 or 2. 
                |         iGunStatus,
                |             Gun Status. FALSE - Gun is not used, TRUE - Gun is used
                |             
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim iGunStatus As boolean = True
                |            MySWProfile.SetGunStatus(1,iGunStatus)
                |            End If

        :param int i_gun_number:
        :param bool i_gun_status:
        :return: None
        """
        return self.com_object.SetGunStatus(i_gun_number, i_gun_status)

    def set_gun_tip_close_direction(self, i_gun_number: int, i_direction: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGunTipCloseDirection(short iGunNumber,boolean
                | iDirection)
                |     This method sets the Gun Tip Close direction
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             gun number. Valid value: 1 or 2 
                |         iDirection,
                |             gun tip close direction. Valid values: TRUE or FALSE. FALSE = decreasing or -ve gun axis value TRUE = increasing or +ve gun axis value 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.SetGunTipCloseDirection(1, TRUE)
                |            End If

        :param int i_gun_number:
        :param bool i_direction:
        :return: None
        """
        return self.com_object.SetGunTipCloseDirection(i_gun_number, i_direction)

    def set_joint_number(self, i_gun_number: int, i_joint_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetJointNumber(short iGunNumber,short iJointNum)
                |     This method sets the Joint Number
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             Gun Number. Valid values : 1 or 2. 
                |         iJointNum,
                |             Joint Number. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            Dim iJointNum As short = 7;
                |            MySWProfile.SetJointNumber(1,iJointNum)
                |            End If

        :param int i_gun_number:
        :param int i_joint_num:
        :return: None
        """
        return self.com_object.SetJointNumber(i_gun_number, i_joint_num)

    def set_move_acceleration(self, i_accuracy_profile_spot_moves: int, i_acceleration: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMoveAcceleration(DELSpotAccuracyProfileAndAccelerationMoves
                | iAccuracyProfileSpotMoves,double iAccelaration)
                |     This method sets the Acceleration to the given spot move
                | 
                |     Parameters:
                | 
                |         iAccuracyProfileSpotMoves,
                |             Move type. It is one of the value in
                |             DELSpotAccuracyProfileAndAccelerationMoves 
                |         iAccelaration,
                |             Acceleration 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |           MySWProfile.SetMoveAcceleration(AccuracyProfilePressureStartMove,10.5)
                |            End If

        :param int i_accuracy_profile_spot_moves:
        :param float i_acceleration:
        :return: None
        """
        return self.com_object.SetMoveAcceleration(i_accuracy_profile_spot_moves, i_acceleration)

    def set_moving_tip_clearance(self, i_gun_number: int, i_moving_tip_spot_moves: int, i_moving_tip_clearance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMovingTipClearance(short iGunNumber,DELSpotMovingTipClearanceMoves
                | iMovingTipSpotMoves,double iMovingTipClearance)
                |     This method sets the Moving Tip Clearance value
                | 
                |     Parameters:
                | 
                |         iGunNumber,
                |             gun number. Valid value: 1 or 2 
                |         iMovingTipSpotMoves,
                |             Move type. It is one of the value in
                |             DELSpotMovingTipClearanceMoves. 
                |         iMovingTipClearance,
                |             Moving tip clearance. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |            MySWProfile.SetMovingTipClearance(MovingTipApproachMove,
                |            10.5)
                |            End If

        :param int i_gun_number:
        :param int i_moving_tip_spot_moves:
        :param float i_moving_tip_clearance:
        :return: None
        """
        return self.com_object.SetMovingTipClearance(i_gun_number, i_moving_tip_spot_moves, i_moving_tip_clearance)

    def set_stationary_tip_clearance(self, i_stationary_tip_spot_moves: int, i_tip_clearance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStationaryTipClearance(DELSpotStationaryTipClearanceMoves
                | iStationaryTipSpotMoves,double iTipClearance)
                |     This method sets the Moving Tip Clearance value
                | 
                |     Parameters:
                | 
                |         iStationaryTipSpotMoves,
                |             Move type. It is one of the value in
                |             DELSpotStationaryTipClearanceMoves 
                |         iTipClearance,
                |             Stationary tip clearance. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |            
                | 
                |            Dim MySWProfile As SpotWeldProfile = MySWProfileFactory.CreateProfile(MyProfileName)
                |            If  MySWProfile  IsNot  Nothing  Then 
                |           
                |           MySWProfile.SetStationaryTipClearance(StationaryTipApproachAndBackupMove,
                |           10.5)
                |            End If

        :param int i_stationary_tip_spot_moves:
        :param float i_tip_clearance:
        :return: None
        """
        return self.com_object.SetStationaryTipClearance(i_stationary_tip_spot_moves, i_tip_clearance)

    def __repr__(self):
        return f'SpotWeldProfile(name="{ self.name }")'
