"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_accuracy_profile import OLPAccuracyProfile
from pycatia3dx.dnb_igp_olp_use.olp_gun import OLPGun
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile


class OLPSpotProfile(OLPProfile):

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
                |                         OlpSpotProfile
                | 
                | A spot profile used for translating a robot program.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | The behavior of this object depends on where it was retrieved from. If the
                | object was retrieved from an OlpRobotMotionTarget then this object is used to
                | configure the spot properties of that motion. The parameters specified with the
                | iMatch input equal to TRUE will be used to find an existing profile to reuse
                | for this motion. If no matching profile is found, a new one will be created. If
                | the object was retrieved from OlpController.SpotProfileList then any
                | modifications to this object will change an existing or new profile's values
                | directly.
                | 
                | There are 2 types of controller specific parameters on the spot profile:
                | parameters on linked spot schedules and parameters directly stored on the spot
                | profile. Parameters stored directly on the spot profile apply to all guns and
                | are accessed using OlpProfile.GetParameter and OlpProfile.SetParameter. Linked
                | spot schedules are gun dependent and are accessed using GetGunParameter and
                | SetGunParameter. When setting linked spot schedule parameters, existing
                | schedule profiles will be searched for based on the iMatch flag and a matching
                | profile will be linked to the spot profile if found, otherwise a new schedule
                | will be created with the specified parameters and linked.
                | 
                | When spot schedules are linked to the spot profiles some of the spot profile
                | parameters will be overridden by the values from the spot schedule. The linking
                | is predefined by DELMIA logic and cannot be configured by the translator. On
                | download, if you get the value of an overridden parameter, you will get the
                | corresponding value from the spot schedule. WARNING: If a profile has been
                | created or modified, such as during upload, the value retrieved for an
                | overridden parameter may not be the value in the spot
                | schedule.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_approach_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetApproachDirection() As DELOlpAxisDirection
                |     Get the direction the robot approaches the weld point
                |     from.
                | 
                |     Returns:
                |         The value.

        :return: DELOlpAxisDirection
        """
        return self.com_object.GetApproachDirection()

    def get_approach_enabled(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetApproachEnabled() As boolean
                |     Get whether the approach move is enabled.
                | 
                |     Returns:
                |         TRUE if enabled.

        :return: bool
        """
        return self.com_object.GetApproachEnabled()

    def get_approach_gun_joint_value(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetApproachGunJointValue(short iGunNumber) As double
                |     Get the gun's position at the end of the approach move.
                |     This is calculated from the stationary tip clearance, the moving tip
                |     clearance, the part thickness, the gun closed joint value, and the gun close
                |     direction.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The joint values are in meters. Only linear joints are currently
                |         supported.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetApproachGunJointValue(i_gun_number)

    def get_approach_moving_tip_clearance(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetApproachMovingTipClearance(short iGunNumber) As double
                |     Get the distance from the part for the movable tip at the end of the
                |     approach move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value in meters.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetApproachMovingTipClearance(i_gun_number)

    def get_approach_stationary_tip_clearance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetApproachStationaryTipClearance() As double
                |     Get the distance from the part for the stationary tip at the end of the
                |     approach move.
                | 
                |     Returns:
                |         The value in meters.

        :return: float
        """
        return self.com_object.GetApproachStationaryTipClearance()

    def get_backup_accel(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBackupAccel() As double
                |     Get acceleration for the backup move.
                | 
                |     Returns:
                |         The value as a percentage (1.0 is 100%).

        :return: float
        """
        return self.com_object.GetBackupAccel()

    def get_backup_accuracy_profile(self) -> OLPAccuracyProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBackupAccuracyProfile() As OlpAccuracyProfile
                |     Get the accuracy profile for the backup move.
                |     In general you should not modify the profile retrieved from this property
                |     because the behavior is not intuitive. If the profile is modified, the spot
                |     profile will be updated with an accuracy profile that was matched based on the
                |     parameters set. The accuracy profile will be ignored when trying to find a
                |     matching spot profile.
                | 
                |     Returns:
                |         The profile.

        :return: OLPAccuracyProfile
        """
        return OLPAccuracyProfile(self.com_object.GetBackupAccuracyProfile())

    def get_backup_enabled(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBackupEnabled() As boolean
                |     Get whether the backup move is enabled.
                | 
                |     Returns:
                |         TRUE if enabled.

        :return: bool
        """
        return self.com_object.GetBackupEnabled()

    def get_backup_stroke(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBackupStroke(short iGunNumber) As double
                |     Get the servo gun backup position.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value in meters.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetBackupStroke(i_gun_number)

    def get_gun(self, i_gun_number: int) -> OLPGun:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGun(short iGunNumber) As OlpGun
                |     Get the OLP gun object used with this spot profile.
                |     The gun corresponds to a specific joint of a tool device.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) - a spot profile can control up to 2 guns.
                |             This is not the mapped gun ID. 
                | 
                |     Returns:
                |         The value.

        :param int i_gun_number:
        :return: OLPGun
        """
        return OLPGun(self.com_object.GetGun(i_gun_number))

    def get_gun_close_in_positive_direction(self, i_gun_number: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGunCloseInPositiveDirection(short iGunNumber) As
                | boolean
                |     Get whether the direction the gun closes when the servo joint values go up
                |     (positive).
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value.

        :param int i_gun_number:
        :return: bool
        """
        return self.com_object.GetGunCloseInPositiveDirection(i_gun_number)

    def get_gun_closed_joint_value(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGunClosedJointValue(short iGunNumber) As double
                |     Get the joint value of the servo gun when the gun is
                |     closed.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The joint values are in meters. Only linear joints are currently
                |         supported.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetGunClosedJointValue(i_gun_number)

    def get_gun_enabled(self, i_gun_number: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGunEnabled(short iGunNumber) As boolean
                |     Get whether the specified gun is enabled.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value.

        :param int i_gun_number:
        :return: bool
        """
        return self.com_object.GetGunEnabled(i_gun_number)

    def get_gun_schedule(self, i_gun_number: int, i_profile_type: str) -> OLPProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGunSchedule(short iGunNumber,CATBSTR iProfileType) As
                | OlpProfile
                |     Get a linked applicative profile weld schedule for a specific
                |     gun.
                |     This will always return a profile which can be configured using
                |     SetParameter methods to match an existing profile or create a new one if
                |     needed.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iProfileType
                |             The applicative profile type 
                | 
                |     Returns:
                |         The profile.

        :param int i_gun_number:
        :param str i_profile_type:
        :return: OLPProfile
        """
        return OLPProfile(self.com_object.GetGunSchedule(i_gun_number, i_profile_type))

    def get_joint_number(self, i_gun_number: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetJointNumber(short iGunNumber) As short
                |     Get the joint number of the servo gun.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value.

        :param int i_gun_number:
        :return: int
        """
        return self.com_object.GetJointNumber(i_gun_number)

    def get_part_thickness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPartThickness() As double
                |     Get the part thickness.
                | 
                |     Returns:
                |         The value in meters.

        :return: float
        """
        return self.com_object.GetPartThickness()

    def get_press_end_accel(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressEndAccel() As double
                |     Get acceleration for the pressure end move.
                | 
                |     Returns:
                |         The value as a percentage (1.0 is 100%).

        :return: float
        """
        return self.com_object.GetPressEndAccel()

    def get_press_end_accuracy_profile(self) -> OLPAccuracyProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressEndAccuracyProfile() As OlpAccuracyProfile
                |     Get the accuracy profile for the pressure end move.
                |     In general you should not modify the profile retrieved from this property
                |     because the behavior is not intuitive. If the profile is modified, the spot
                |     profile will be updated with an accuracy profile that was matched based on the
                |     parameters set. The accuracy profile will be ignored when trying to find a
                |     matching spot profile.
                | 
                |     Returns:
                |         The profile.

        :return: OLPAccuracyProfile
        """
        return OLPAccuracyProfile(self.com_object.GetPressEndAccuracyProfile())

    def get_press_end_enabled(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressEndEnabled() As boolean
                |     Get whether the pressure end move is enabled.
                | 
                |     Returns:
                |         TRUE if enabled.

        :return: bool
        """
        return self.com_object.GetPressEndEnabled()

    def get_press_end_gun_joint_value(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressEndGunJointValue(short iGunNumber) As double
                |     Get the gun's position at the end of the pressure end
                |     move.
                |     This is calculated from the stationary tip clearance, the moving tip
                |     clearance, the part thickness, the gun closed joint value, and the gun close
                |     direction.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The joint values are in meters. Only linear joints are currently
                |         supported.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetPressEndGunJointValue(i_gun_number)

    def get_press_end_moving_tip_clearance(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressEndMovingTipClearance(short iGunNumber) As double
                |     Get the distance from the part for the movable tip at the end of the
                |     pressure end move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value in meters.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetPressEndMovingTipClearance(i_gun_number)

    def get_press_end_stationary_tip_clearance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressEndStationaryTipClearance() As double
                |     Get the distance from the part for the stationary tip at the end of the
                |     pressure end move.
                | 
                |     Returns:
                |         The value in meters.

        :return: float
        """
        return self.com_object.GetPressEndStationaryTipClearance()

    def get_press_start_accel(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressStartAccel() As double
                |     Get acceleration for the pressure start move.
                | 
                |     Returns:
                |         The value as a percentage (1.0 is 100%).

        :return: float
        """
        return self.com_object.GetPressStartAccel()

    def get_press_start_accuracy_profile(self) -> OLPAccuracyProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressStartAccuracyProfile() As OlpAccuracyProfile
                |     Get the accuracy profile for the pressure start move.
                |     In general you should not modify the profile retrieved from this property
                |     because the behavior is not intuitive. If the profile is modified, the spot
                |     profile will be updated with an accuracy profile that was matched based on the
                |     parameters set. The accuracy profile will be ignored when trying to find a
                |     matching spot profile.
                | 
                |     Returns:
                |         The profile.

        :return: OLPAccuracyProfile
        """
        return OLPAccuracyProfile(self.com_object.GetPressStartAccuracyProfile())

    def get_press_start_enabled(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressStartEnabled() As boolean
                |     Get whether the pressure start move is enabled.
                | 
                |     Returns:
                |         TRUE if enabled.

        :return: bool
        """
        return self.com_object.GetPressStartEnabled()

    def get_press_start_gun_joint_value(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressStartGunJointValue(short iGunNumber) As double
                |     Get the gun's position at the end of the pressure start
                |     move.
                |     This is calculated from the stationary tip clearance, the moving tip
                |     clearance, the part thickness, the gun closed joint value, and the gun close
                |     direction.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The joint values are in meters. Only linear joints are currently
                |         supported.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetPressStartGunJointValue(i_gun_number)

    def get_press_start_moving_tip_clearance(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressStartMovingTipClearance(short iGunNumber) As
                | double
                |     Get the distance from the part for the movable tip at the end of the
                |     pressure start move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value in meters.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetPressStartMovingTipClearance(i_gun_number)

    def get_press_start_stationary_tip_clearance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressStartStationaryTipClearance() As double
                |     Get the distance from the part for the stationary tip at the end of the
                |     pressure start move.
                | 
                |     Returns:
                |         The value in meters.

        :return: float
        """
        return self.com_object.GetPressStartStationaryTipClearance()

    def get_pressure_accel(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressureAccel() As double
                |     Get acceleration for the pressure move.
                | 
                |     Returns:
                |         The value as a percentage (1.0 is 100%).

        :return: float
        """
        return self.com_object.GetPressureAccel()

    def get_pressure_accuracy_profile(self) -> OLPAccuracyProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressureAccuracyProfile() As OlpAccuracyProfile
                |     Get the accuracy profile for the pressure move.
                |     In general you should not modify the profile retrieved from this property
                |     because the behavior is not intuitive. If the profile is modified, the spot
                |     profile will be updated with an accuracy profile that was matched based on the
                |     parameters set. The accuracy profile will be ignored when trying to find a
                |     matching spot profile.
                | 
                |     Returns:
                |         The profile.

        :return: OLPAccuracyProfile
        """
        return OLPAccuracyProfile(self.com_object.GetPressureAccuracyProfile())

    def get_pressure_push_depth(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressurePushDepth(short iGunNumber) As double
                |     Get the push depth for the pressure move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value in meters.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetPressurePushDepth(i_gun_number)

    def get_pressure_speed_factor(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPressureSpeedFactor(short iGunNumber) As double
                |     Get the speed factor for the pressure move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value as a percentage (1.0 is 100%).

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetPressureSpeedFactor(i_gun_number)

    def get_weld_delay(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetWeldDelay(short iGunNumber) As double
                |     Get welding time.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value in seconds.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetWeldDelay(i_gun_number)

    def get_weld_pressure_stabilization_time(self, i_gun_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetWeldPressureStabilizationTime(short iGunNumber) As
                | double
                |     Get welding pressure stabilization time.
                |     This is additional time needed before welding can begin and is added to the
                |     weld delay during simulation.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                | 
                |     Returns:
                |         The value in seconds.

        :param int i_gun_number:
        :return: float
        """
        return self.com_object.GetWeldPressureStabilizationTime(i_gun_number)

    def is_gun_schedule_set(self, i_gun_number: int, i_profile_type: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsGunScheduleSet(short iGunNumber,CATBSTR iProfileType) As
                | boolean
                |     Get whether this spot profile has a linked applicative profile weld
                |     schedule for a specific gun.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iProfileType
                |             The applicative profile type 
                | 
                |     Returns:
                |         True if the schedule is set.

        :param int i_gun_number:
        :param str i_profile_type:
        :return: bool
        """
        return self.com_object.IsGunScheduleSet(i_gun_number, i_profile_type)

    def set_approach_direction(self, i_approach_direction: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApproachDirection(DELOlpAxisDirection iApproachDirection,boolean
                | iMatch)
                |     Set the direction the robot approaches the weld point
                |     from.
                | 
                |     Parameters:
                | 
                |         iApproachDirection
                |             The value. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_approach_direction:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetApproachDirection(i_approach_direction, i_match)

    def set_approach_enabled(self, i_enabled: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApproachEnabled(boolean iEnabled,boolean iMatch)
                |     Set whether the approach move is enabled.
                | 
                |     Parameters:
                | 
                |         iEnabled
                |             TRUE if enabled. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param bool i_enabled:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetApproachEnabled(i_enabled, i_match)

    def set_approach_gun_joint_value(self, i_gun_number: int, i_joint_value: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApproachGunJointValue(short iGunNumber,double iJointValue,boolean
                | iMatch)
                |     Set the gun's position at the end of the approach move.
                |     You should call either SetApproachMovingTipClearance or this method.
                |     Specifying both would over constrain the gun position. For example specify this
                |     value if the gun's position is known but the moving tip clearance is unknown.
                |     The moving tip clearance will be calculated from the stationary tip clearance,
                |     the gun position, the part thickness, the gun closed joint value, and the gun
                |     close direction.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iDistance
                |             The joint values are in meters. Only linear joints are currently
                |             supported. 
                |         iMatch
                |             If TRUE use value to find existing profile. If TRUE the moving tip
                |             clearance will be calculated based on the values set on this profile. The value
                |             from the candidate matching profile will be used for any parameter required for
                |             this calculation which has not been set. A profile will match if its moving tip
                |             clearance and other parameters would result in the correct gun joint position.

        :param int i_gun_number:
        :param float i_joint_value:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetApproachGunJointValue(i_gun_number, i_joint_value, i_match)

    def set_approach_moving_tip_clearance(self, i_gun_number: int, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApproachMovingTipClearance(short iGunNumber,double iDistance,boolean
                | iMatch)
                |     Set the distance from the part for the movable tip at the end of the
                |     approach move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iDistance
                |             The value in meters. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param float i_distance:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetApproachMovingTipClearance(i_gun_number, i_distance, i_match)

    def set_approach_stationary_tip_clearance(self, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApproachStationaryTipClearance(double iDistance,boolean
                | iMatch)
                |     Set the distance from the part for the stationary tip at the end of the
                |     approach move.
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
        return self.com_object.SetApproachStationaryTipClearance(i_distance, i_match)

    def set_backup_accel(self, i_accel: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBackupAccel(double iAccel,boolean iMatch)
                |     Set acceleration for the backup move.
                | 
                |     Parameters:
                | 
                |         iAccel
                |             The value as a percentage (1.0 is 100%). 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_accel:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetBackupAccel(i_accel, i_match)

    def set_backup_accuracy_profile(self, i_profile: OLPAccuracyProfile, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBackupAccuracyProfile(OlpAccuracyProfile iProfile,boolean
                | iMatch)
                |     Set the accuracy profile for the backup move.
                |     You should retrieve the accuracy profile to set on this property from the
                |     OlpController.AccuracyProfileList.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The profile. 
                |         iMatch
                |             If TRUE use value to find existing spot profile.

        :param OLPAccuracyProfile i_profile:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetBackupAccuracyProfile(i_profile.com_object, i_match)

    def set_backup_enabled(self, i_enabled: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBackupEnabled(boolean iEnabled,boolean iMatch)
                |     Set whether the backup move is enabled.
                | 
                |     Parameters:
                | 
                |         iEnabled
                |             TRUE if enabled. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param bool i_enabled:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetBackupEnabled(i_enabled, i_match)

    def set_backup_stroke(self, i_gun_number: int, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBackupStroke(short iGunNumber,double iDistance,boolean
                | iMatch)
                |     Set the servo gun backup position.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iDistance
                |             The value in meters. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param float i_distance:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetBackupStroke(i_gun_number, i_distance, i_match)

    def set_gun(self, i_gun_number: int, i_gun: OLPGun, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGun(short iGunNumber,OlpGun iGun,boolean iMatch)
                |     Set the OLP gun object used with this spot profile.
                |     The gun corresponds to a specific joint of a tool device. If you set the
                |     Gun, you don't need to set the Joint Number - the joint number comes from the
                |     mapping the user specified in the UI.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) - a spot profile can control up to 2 guns.
                |             This is not the mapped gun ID. 
                |         iGun
                |             The value. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param OLPGun i_gun:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetGun(i_gun_number, i_gun.com_object, i_match)

    def set_gun_close_in_positive_direction(self, i_gun_number: int, i_is_positive_direction: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGunCloseInPositiveDirection(short iGunNumber,boolean
                | iIsPositiveDirection,boolean iMatch)
                |     Set whether the direction the gun closes when the servo joint values go up
                |     (positive).
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iIsPositiveDirection
                |             The value. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param bool i_is_positive_direction:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetGunCloseInPositiveDirection(i_gun_number, i_is_positive_direction, i_match)

    def set_gun_closed_joint_value(self, i_gun_number: int, i_gun_closed_joint_value: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGunClosedJointValue(short iGunNumber,double iGunClosedJointValue,boolean
                | iMatch)
                |     Set the joint value of the servo gun when the gun is
                |     closed.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iGunClosedJointValue
                |             The joint values are in meters. Only linear joints are currently
                |             supported. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param float i_gun_closed_joint_value:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetGunClosedJointValue(i_gun_number, i_gun_closed_joint_value, i_match)

    def set_gun_enabled(self, i_gun_number: int, i_enabled: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGunEnabled(short iGunNumber,boolean iEnabled,boolean
                | iMatch)
                |     Set whether the specified gun is enabled.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iEnabled
                |             The value. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param bool i_enabled:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetGunEnabled(i_gun_number, i_enabled, i_match)

    def set_gun_schedule(self, i_gun_number: int, i_profile: OLPProfile, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGunSchedule(short iGunNumber,OlpProfile iProfile,boolean
                | iMatch)
                |     Set a linked applicative profile weld schedule for a specific
                |     gun.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iProfile
                |             The profile. 
                |         iMatch
                |             If TRUE then this profile must be linked to an existing spot
                |             profile for it to match. If the profile is Nothing and iMatch is TRUE then this
                |             profile must not be linked to an existing spot profile for it to match. However,
                |             if the profile is mandatory or the default values of the profile have the same
                |             meaning as having the profile unset, then a profile set with default values
                |             will also match.

        :param int i_gun_number:
        :param OLPProfile i_profile:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetGunSchedule(i_gun_number, i_profile.com_object, i_match)

    def set_gun_schedule_to_nothing(self, i_gun_number: int, i_profile_type: str, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGunScheduleToNothing(short iGunNumber,CATBSTR iProfileType,boolean
                | iMatch)
                |     Clear a linked applicative profile weld schedule for a specific
                |     gun.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iProfileType
                |             The applicative profile type 
                |         iMatch
                |             If iMatch is TRUE then this profile must not be linked to an
                |             existing spot profile for it to match. However, if the default values of the
                |             profile have the same meaning as having the profile unset, then a profile set
                |             with default values will also match.

        :param int i_gun_number:
        :param str i_profile_type:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetGunScheduleToNothing(i_gun_number, i_profile_type, i_match)

    def set_joint_number(self, i_gun_number: int, i_joint_number: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetJointNumber(short iGunNumber,short iJointNumber,boolean
                | iMatch)
                |     Set the joint number of the servo gun.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iJointNumber
                |             The value. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param int i_joint_number:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetJointNumber(i_gun_number, i_joint_number, i_match)

    def set_part_thickness(self, i_part_thickness: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPartThickness(double iPartThickness,boolean iMatch)
                |     Set the part thickness.
                | 
                |     Parameters:
                | 
                |         iPartThickness
                |             The value in meters. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_part_thickness:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPartThickness(i_part_thickness, i_match)

    def set_press_end_accel(self, i_accel: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressEndAccel(double iAccel,boolean iMatch)
                |     Set acceleration for the pressure end move.
                | 
                |     Parameters:
                | 
                |         iAccel
                |             The value as a percentage (1.0 is 100%). 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_accel:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressEndAccel(i_accel, i_match)

    def set_press_end_accuracy_profile(self, i_profile: OLPAccuracyProfile, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressEndAccuracyProfile(OlpAccuracyProfile iProfile,boolean
                | iMatch)
                |     Set the accuracy profile for the pressure end move.
                |     You should retrieve the accuracy profile to set on this property from the
                |     OlpController.AccuracyProfileList.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The profile. 
                |         iMatch
                |             If TRUE use value to find existing spot profile.

        :param OLPAccuracyProfile i_profile:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressEndAccuracyProfile(i_profile.com_object, i_match)

    def set_press_end_enabled(self, i_enabled: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressEndEnabled(boolean iEnabled,boolean iMatch)
                |     Set whether the pressure end move is enabled.
                | 
                |     Parameters:
                | 
                |         iEnabled
                |             TRUE if enabled. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param bool i_enabled:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressEndEnabled(i_enabled, i_match)

    def set_press_end_gun_joint_value(self, i_gun_number: int, i_joint_value: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressEndGunJointValue(short iGunNumber,double iJointValue,boolean
                | iMatch)
                |     Set the gun's position at the end of the pressure end
                |     move.
                |     You should call either SetPressEndMovingTipClearance or this method.
                |     Specifying both would over constrain the gun position. For example specify this
                |     value if the gun's position is known but the moving tip clearance is unknown.
                |     The moving tip clearance will be calculated from the stationary tip clearance,
                |     the gun position, the part thickness, the gun closed joint value, and the gun
                |     close direction.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iDistance
                |             The joint values are in meters. Only linear joints are currently
                |             supported. 
                |         iMatch
                |             If TRUE use value to find existing profile. If TRUE the moving tip
                |             clearance will be calculated based on the values set on this profile. The value
                |             from the candidate matching profile will be used for any parameter required for
                |             this calculation which has not been set. A profile will match if its moving tip
                |             clearance and other parameters would result in the correct gun joint position.

        :param int i_gun_number:
        :param float i_joint_value:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressEndGunJointValue(i_gun_number, i_joint_value, i_match)

    def set_press_end_moving_tip_clearance(self, i_gun_number: int, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressEndMovingTipClearance(short iGunNumber,double iDistance,boolean
                | iMatch)
                |     Set the distance from the part for the movable tip at the end of the
                |     pressure end move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iDistance
                |             The value in meters. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param float i_distance:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressEndMovingTipClearance(i_gun_number, i_distance, i_match)

    def set_press_end_stationary_tip_clearance(self, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressEndStationaryTipClearance(double iDistance,boolean
                | iMatch)
                |     Set the distance from the part for the stationary tip at the end of the
                |     pressure end move.
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
        return self.com_object.SetPressEndStationaryTipClearance(i_distance, i_match)

    def set_press_start_accel(self, i_accel: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressStartAccel(double iAccel,boolean iMatch)
                |     Set acceleration for the pressure start move.
                | 
                |     Parameters:
                | 
                |         iAccel
                |             The value as a percentage (1.0 is 100%). 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_accel:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressStartAccel(i_accel, i_match)

    def set_press_start_accuracy_profile(self, i_profile: OLPAccuracyProfile, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressStartAccuracyProfile(OlpAccuracyProfile iProfile,boolean
                | iMatch)
                |     Set the accuracy profile for the pressure start move.
                |     You should retrieve the accuracy profile to set on this property from the
                |     OlpController.AccuracyProfileList.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The profile. 
                |         iMatch
                |             If TRUE use value to find existing spot profile.

        :param OLPAccuracyProfile i_profile:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressStartAccuracyProfile(i_profile.com_object, i_match)

    def set_press_start_enabled(self, i_enabled: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressStartEnabled(boolean iEnabled,boolean iMatch)
                |     Set whether the pressure start move is enabled.
                | 
                |     Parameters:
                | 
                |         iEnabled
                |             TRUE if enabled. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param bool i_enabled:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressStartEnabled(i_enabled, i_match)

    def set_press_start_gun_joint_value(self, i_gun_number: int, i_joint_value: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressStartGunJointValue(short iGunNumber,double iJointValue,boolean
                | iMatch)
                |     Set the gun's position at the end of the pressure start
                |     move.
                |     You should call either SetPressStartMovingTipClearance or this method.
                |     Specifying both would over constrain the gun position. For example specify this
                |     value if the gun's position is known but the moving tip clearance is unknown.
                |     The moving tip clearance will be calculated from the stationary tip clearance,
                |     the gun position, the part thickness, the gun closed joint value, and the gun
                |     close direction.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iDistance
                |             The joint values are in meters. Only linear joints are currently
                |             supported. 
                |         iMatch
                |             If TRUE use value to find existing profile. If TRUE the moving tip
                |             clearance will be calculated based on the values set on this profile. The value
                |             from the candidate matching profile will be used for any parameter required for
                |             this calculation which has not been set. A profile will match if its moving tip
                |             clearance and other parameters would result in the correct gun joint position.

        :param int i_gun_number:
        :param float i_joint_value:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressStartGunJointValue(i_gun_number, i_joint_value, i_match)

    def set_press_start_moving_tip_clearance(self, i_gun_number: int, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressStartMovingTipClearance(short iGunNumber,double iDistance,boolean
                | iMatch)
                |     Set the distance from the part for the movable tip at the end of the
                |     pressure start move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iDistance
                |             The value in meters. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param float i_distance:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressStartMovingTipClearance(i_gun_number, i_distance, i_match)

    def set_press_start_stationary_tip_clearance(self, i_distance: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressStartStationaryTipClearance(double iDistance,boolean
                | iMatch)
                |     Set the distance from the part for the stationary tip at the end of the
                |     pressure start move.
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
        return self.com_object.SetPressStartStationaryTipClearance(i_distance, i_match)

    def set_pressure_accel(self, i_accel: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressureAccel(double iAccel,boolean iMatch)
                |     Set acceleration for the pressure move.
                | 
                |     Parameters:
                | 
                |         iAccel
                |             The value as a percentage (1.0 is 100%). 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_accel:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressureAccel(i_accel, i_match)

    def set_pressure_accuracy_profile(self, i_profile: OLPAccuracyProfile, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressureAccuracyProfile(OlpAccuracyProfile iProfile,boolean
                | iMatch)
                |     Set the accuracy profile for the pressure move.
                |     You should retrieve the accuracy profile to set on this property from the
                |     OlpController.AccuracyProfileList.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The profile. 
                |         iMatch
                |             If TRUE use value to find existing spot profile.

        :param OLPAccuracyProfile i_profile:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressureAccuracyProfile(i_profile.com_object, i_match)

    def set_pressure_push_depth(self, i_gun_number: int, i_push_depth: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressurePushDepth(short iGunNumber,double iPushDepth,boolean
                | iMatch)
                |     Set the push depth for the pressure move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iSpeedFactor
                |             The value as a percentage (1.0 is 100%). 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param float i_push_depth:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressurePushDepth(i_gun_number, i_push_depth, i_match)

    def set_pressure_speed_factor(self, i_gun_number: int, i_speed_factor: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPressureSpeedFactor(short iGunNumber,double iSpeedFactor,boolean
                | iMatch)
                |     Set the speed factor for the pressure move.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iSpeedFactor
                |             The value as a percentage (1.0 is 100%). 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param float i_speed_factor:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPressureSpeedFactor(i_gun_number, i_speed_factor, i_match)

    def set_weld_delay(self, i_gun_number: int, i_weld_delay: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetWeldDelay(short iGunNumber,double iWeldDelay,boolean
                | iMatch)
                |     Set the welding time.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iWeldDelay
                |             The value in seconds. 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param int i_gun_number:
        :param float i_weld_delay:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetWeldDelay(i_gun_number, i_weld_delay, i_match)

    def set_weld_pressure_stabilization_time(self, i_gun_number: int, i_weld_pressure_stabilization_time: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetWeldPressureStabilizationTime(short iGunNumber,double
                | iWeldPressureStabilizationTime,boolean iMatch)
                |     Set welding pressure stabilization time.
                |     This is additional time needed before welding can begin and is added to the
                |     weld delay during simulation.
                | 
                |     Parameters:
                | 
                |         iGunNumber
                |             The gun number (1 or 2) 
                |         iWeldPressureStabilizationTime
                |             The value in seconds. 
                |         iMatch
                |             If TRUE use value to find existing profile. 

        :param int i_gun_number:
        :param float i_weld_pressure_stabilization_time:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetWeldPressureStabilizationTime(i_gun_number, i_weld_pressure_stabilization_time, i_match)

    def __repr__(self):
        return f'OLPSpotProfile(name="{ self.name }")'
