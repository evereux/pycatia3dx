"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_resource_builder.rsc_accuracy_profile import RscAccuracyProfile
from pycatia3dx.del_resource_builder.rsc_motion_profile import RscMotionProfile
from pycatia3dx.dnb_igp_olp_use.olp_accuracy_profile import OLPAccuracyProfile
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction
from pycatia3dx.dnb_igp_olp_use.olp_motion_group import OLPMotionGroup
from pycatia3dx.dnb_igp_olp_use.olp_motion_profile import OLPMotionProfile
from pycatia3dx.dnb_igp_olp_use.olp_robot_motion_target import OLPRobotMotionTarget


class OLPRobotMotion(OLPInstruction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpInstruction
                |                         OlpRobotMotion
                | 
                | Represents a robot motion instruction in a task.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | Example: (VB.NET)
                | 
                |  Dim Instructions As OlpInstructions
                |  Dim Instruction As OlpInstruction = Instructions.Item(1)
                |  If Instruction.Type=DELOlpInstructionType.delOlpRobotMotion
                |  Then
                |    Dim RobotMotion As OlpRobotMotion = Instruction
                |  End If
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def accuracy_profile(self) -> RscAccuracyProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccuracyProfile() As RscAccuracyProfile (Read Only)
                |     Get the accuracy profile for the primary target.
                | 
                |     This property is obsolete. It is recommended that you use
                |     AccuracyProfileOlp instead of this method. It may be deprecated in the
                |     future.
                | 
                |     This is read only because the accuracy profile for each target must belong
                |     to that motion group's primary device. You can set the accuracy profile
                |     parameters for all targets using the SetAccuracyParams method or you can use
                |     the OlpRobotMotionTarget.AccuracyProfile property to get and set the accuracy
                |     profile for each target individually.

        :return: RscAccuracyProfile
        """

        return RscAccuracyProfile(self.com_object.AccuracyProfile)

    @property
    def accuracy_profile_olp(self) -> OLPAccuracyProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccuracyProfileOlp() As OlpAccuracyProfile
                |     Get/Set the accuracy profile associated with the
                |     instruction.
                | 
                |     This property will return a valid object even for new motions so it can be
                |     used to set accuracy values.
                | 
                |     This object is used to configure the accuracy properties of the motion. The
                |     parameters specified with the iMatch input equal to TRUE will be used to find
                |     an existing profile to reuse for this motion. If no matching profile is found a
                |     new one will be created. To modify a profile directly please use
                |     OlpController.AccuracyProfileList.

        :return: OLPAccuracyProfile
        """

        return OLPAccuracyProfile(self.com_object.AccuracyProfileOlp)

    @accuracy_profile_olp.setter
    def accuracy_profile_olp(self, value: OLPAccuracyProfile):
        """
        :param OLPAccuracyProfile value:
        """

        self.com_object.AccuracyProfileOlp = value

    @property
    def global_position(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GlobalPosition() As boolean
                |     Get/Set this move as a global position.
                |     A global position is one that is referenced by more than one program. In
                |     order to prevent the robot programmer from accidentally modifying a global
                |     position in teach, they are created either as home positions for joint targets
                |     or as a locked tag in a dedicated tag group that includes "GlobalTags" in the
                |     name.

        :return: bool
        """

        return self.com_object.GlobalPosition

    @global_position.setter
    def global_position(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.GlobalPosition = value

    @property
    def motion_profile(self) -> RscMotionProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionProfile() As RscMotionProfile (Read Only)
                | 
                |     Deprecated:
                |         R215 MotionProfileOlp

        :return: RscMotionProfile
        """

        return RscMotionProfile(self.com_object.MotionProfile)

    @property
    def motion_profile_olp(self) -> OLPMotionProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionProfileOlp() As OlpMotionProfile
                |     Get the motion profile associated with the instruction.
                | 
                |     This property will return a valid object even for new motions so it can be
                |     used to set speed values.
                | 
                |     This object is used to configure the speed properties of the motion. The
                |     parameters specified with the iMatch input equal to TRUE will be used to find
                |     an existing profile to reuse for this motion. If no matching profile is found a
                |     new one will be created. To modify a profile directly please use
                |     OlpController.MotionProfileList.

        :return: OLPMotionProfile
        """

        return OLPMotionProfile(self.com_object.MotionProfileOlp)

    @motion_profile_olp.setter
    def motion_profile_olp(self, value: OLPMotionProfile):
        """
        :param OLPMotionProfile value:
        """

        self.com_object.MotionProfileOlp = value

    @property
    def motion_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionType() As DELOlpMotionType
                |     Get/Set the motion type for all targets.
                |     If set, this motion type will be set for all targets. If retrieved and
                |     different motion types are used for each target then an error will occur. You
                |     can use the OlpRobotMotionTarget.MotionType property to get and set the motion
                |     type for each target individually.

        :return: DELOlpMotionType
        """

        return self.com_object.MotionType

    @motion_type.setter
    def motion_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.MotionType = value

    @property
    def orientation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientationMode() As DELOlpOrientationMode
                |     Get/Set the orientation mode for all targets.
                |     If set, this orientation mode will be set for all targets. If retrieved and
                |     different orientation modes are used for each target then an error will occur.
                |     You can use the OlpRobotMotionTarget.OrientationMode property to get and set
                |     the motion type for each target individually.

        :return: DELOlpOrientationMode
        """

        return self.com_object.OrientationMode

    @orientation_mode.setter
    def orientation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.OrientationMode = value

    @property
    def position_comment(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionComment() As CATBSTR
                |     Get/set the position comment associated with the
                |     instruction.
                |     This is a comment associated with the position itself. This may not be used
                |     for all languages. If the value of the position comment is "Move to Pounce", in
                |     some robot languages this may be used inline with the robot motion
                |     instruction
                | 
                |              L P[1:Move to Pounce] 100% CNT100
                |      
                | 
                |     In other languages this may be used when declaring the motion target
                |     variable
                | 
                |              ! Move to Pounce
                |              CONST pounce p50 :=
[[500,500,500],[1,0,0,0],[1,1,0,0],[500,9E9,9E9,9E9,9E9,9E9]];

        :return: str
        """

        return self.com_object.PositionComment

    @position_comment.setter
    def position_comment(self, value: str):
        """
        :param str value:
        """

        self.com_object.PositionComment = value

    @property
    def position_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionName() As CATBSTR
                |     Get/Set the position name associated with the instruction.
                |     This is the name of the position variable in the native robot language
                |     program. This may not be used for all languages. For
                |     example:
                | 
                |             CONST robtarget pounce :=
[[500,500,500],[1,0,0,0],[1,1,0,0],[500,9E9,9E9,9E9,9E9,9E9]];

        :return: str
        """

        return self.com_object.PositionName

    @position_name.setter
    def position_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.PositionName = value

    @property
    def position_number(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionNumber() As CATBSTR
                |     Get/Set the position number associated with the
                |     instruction.
                |     This is the register number where the position is stored in the native
                |     robot language. This is not used for all languages. For example if the position
                |     number is 1:
                | 
                |           L P[1] 100% CNT100

        :return: str
        """

        return self.com_object.PositionNumber

    @position_number.setter
    def position_number(self, value: str):
        """
        :param str value:
        """

        self.com_object.PositionNumber = value

    @property
    def position_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionType() As CATBSTR
                |     Get/Set the position type associated with the instruction.
                |     This is the type of native robot language position. Generally this is used
                |     to indicate where the position is stored or how the position variable is
                |     declared. For example for FANUC this can be P or PR.
                | 
                |            L P[1] 100% CNT100
                |            L PR[1] 100% CNT100
                |      
                | 
                |     For ABB this declares the type of target (robtarget, jointtarget) AND the
                |     variable type (VAR, CONST). For example if OLPPositionType is "CONST robtarget"
                |     the corresponding statement is
                | 
                |            CONST robtarget pounce :=
[[500,500,500],[1,0,0,0],[1,1,0,0],[500,9E9,9E9,9E9,9E9,9E9]];

        :return: str
        """

        return self.com_object.PositionType

    @position_type.setter
    def position_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.PositionType = value

    @property
    def synchronization_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SynchronizationMode() As DELOlpSynchronizationMode
                |     Get/Set the synchronization mode.
                |     This is the synchronization strategy used during motion planning for moves
                |     with multiple motion groups. Moves with a single target are always synchronized
                |     unless there is a workpiece positioner and the tag is attached to the
                |     positioner.

        :return: DELOlpSynchronizationMode
        """

        return self.com_object.SynchronizationMode

    @synchronization_mode.setter
    def synchronization_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.SynchronizationMode = value

    def get_target(self, i_mg: OLPMotionGroup) -> OLPRobotMotionTarget:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTarget(OlpMotionGroup iMG) As OlpRobotMotionTarget
                |     Get the target location for a specific motion group.
                | 
                |     Parameters:
                | 
                |         iMG
                |             The motion group. 
                | 
                |     Returns:
                |         The target location.

        :param OLPMotionGroup i_mg:
        :return: OLPRobotMotionTarget
        """
        return OLPRobotMotionTarget(self.com_object.GetTarget(i_mg.com_object))

    def set_accuracy_params(self, i_fly_by: bool, i_accuracy_type: int, i_accuracy_value: float, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAccuracyParams(boolean iFlyBy,AccuracyType iAccuracyType,double
                | iAccuracyValue,CATBSTR iName)
                |     Set all targets to have these accuracy parameters.
                | 
                |     This method is obsolete. It is recommended that you use AccuracyProfileOlp
                |     instead of this method. It may be deprecated in the
                |     future.
                | 
                |     This function may use an existing profile or create a new one based on
                |     these rules:
                | 
                |         If profile with the name exists, its values will be changed to match
                |         these values.
                |         If a profile with these values exists, its name will be changed. Note:
                |         The Default profile is ignored in this case because their name cannot be
                |         changed.
                |         If neither of the above, it will be created with these
                |         values.
                | 
                |     Parameters:
                | 
                |         iFlyBy
                |             If true, then fly by is on. 
                |         iAccuracyType
                |             The method used for calculating the accuracy. 
                |         iAccuracyValue
                |             The accuracy value: units are in MKS and depend upon the value of
                |             iAccuracyType.
                | 
                |                 ACCURACY_TYPE_SPEED - units are a percentage. 1.0 is
                |                 100%.
                |                 ACCURACY_TYPE_DISTANCE - units are in mm.
                | 
                |         Name
                |             The name of the profile to find/create.

        :param bool i_fly_by:
        :param AccuracyType i_accuracy_type:
        :param float i_accuracy_value:
        :param str i_name:
        :return: None
        """
        return self.com_object.SetAccuracyParams(i_fly_by, i_accuracy_type, i_accuracy_value, i_name)

    def set_motion_params(self, i_basis: int, i_speed: float, i_accel_percent: float, i_angular_speed_percent: float, i_angular_accel_percent: float, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionParams(MotionBasis iBasis,double iSpeed,double
                | iAccelPercent,double iAngularSpeedPercent,double iAngularAccelPercent,CATBSTR
                | iName)
                | 
                |     Deprecated:
                |         R215 MotionProfileOlp 

        :param MotionBasis i_basis:
        :param float i_speed:
        :param float i_accel_percent:
        :param float i_angular_speed_percent:
        :param float i_angular_accel_percent:
        :param str i_name:
        :return: None
        """
        return self.com_object.SetMotionParams(i_basis, i_speed, i_accel_percent, i_angular_speed_percent, i_angular_accel_percent, i_name)

    def __repr__(self):
        return f'OLPRobotMotion(name="{ self.name }")'
