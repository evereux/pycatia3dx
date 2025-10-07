"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_resource_builder.rsc_accuracy_profile import RscAccuracyProfile
from pycatia3dx.del_resource_builder.rsc_applicative_profile import RscApplicativeProfile
from pycatia3dx.del_resource_builder.rsc_motion_profile import RscMotionProfile
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_accuracy_profile import OLPAccuracyProfile
from pycatia3dx.dnb_igp_olp_use.olp_c_frame_rivet_profile import OLPCFrameRivetProfile
from pycatia3dx.dnb_igp_olp_use.olp_choreography_events import OLPChoreographyEvents
from pycatia3dx.dnb_igp_olp_use.olp_controller import OLPController
from pycatia3dx.dnb_igp_olp_use.olp_conveyor_tracking_profile import OLPConveyorTrackingProfile
from pycatia3dx.dnb_igp_olp_use.olp_drill_rivet_profile import OLPDrillRivetProfile
from pycatia3dx.dnb_igp_olp_use.olp_motion_profile import OLPMotionProfile
from pycatia3dx.dnb_igp_olp_use.olp_object_frame_profile import OLPObjectFrameProfile
from pycatia3dx.dnb_igp_olp_use.olp_position_variable import OLPPositionVariable
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile
from pycatia3dx.dnb_igp_olp_use.olp_robot_config_generic import OLPRobotConfigGeneric
from pycatia3dx.dnb_igp_olp_use.olp_spot_profile import OLPSpotProfile
from pycatia3dx.dnb_igp_olp_use.olp_tag import OLPTag
from pycatia3dx.dnb_igp_olp_use.olp_tool_profile import OLPToolProfile
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform
from pycatia3dx.types.general import CATVariant


class OLPRobotMotionTarget(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpRobotMotionTarget
                | 
                | Represents a target position of a robot motion.
                | 
                | Each motion group has a target position. This interface can only be used by a
                | translator within the Robotics Off-line Programming (OLP) Download or Upload
                | command.
                | 
                | The name of a robot motion target is the tag name. For targets which are not of
                | type tag target, you should not get or set the name.
                | 
                | Example: (VB.NET)
                | 
                |  Dim Motion As OlpRobotMotion
                |  Dim Group As OlpMotionGroup
                |  Dim Target As OlpRobotMotionTarget = Motion.GetTarget(Group)
                |  If Target.TargetType = delOlpTagTarget Then
                |     MsgBox Target.Name
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
                | Property AccuracyProfile() As RscAccuracyProfile
                | 
                |     Deprecated:
                |         R425 AccuracyProfileOlp

        :return: RscAccuracyProfile
        """

        return RscAccuracyProfile(self.com_object.AccuracyProfile)

    @accuracy_profile.setter
    def accuracy_profile(self, value: RscAccuracyProfile):
        """
        :param RscAccuracyProfile value:
        """

        self.com_object.AccuracyProfile = value

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
    def application_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApplicationType() As DELOlpInstructionType
                |     Get/Set the application type being done at this target (spot welding, arc
                |     welding, etc).
                | 
                |     Setting this value is mandatory for robot tasks which control multiple
                |     motion groups, otherwise all targets will be assumed to be robot motions. The
                |     specific motion instruction type used to create the robot motion is ignored in
                |     these cases until OlpRobotMotionTarget.ApplicationType is
                |     set.

        :return: DELOlpInstructionType
        """

        return self.com_object.ApplicationType

    @application_type.setter
    def application_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ApplicationType = value

    @property
    def application_type_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApplicationTypeString() As CATBSTR
                |     Get/Set the application type as a string being done at this target (spot
                |     welding, arc welding, etc).
                | 
                |     This property is redundant to ApplicationType but must be used for new
                |     applications where the application has not yet been added to
                |     DELOlpInstructionType.

        :return: str
        """

        return self.com_object.ApplicationTypeString

    @application_type_string.setter
    def application_type_string(self, value: str):
        """
        :param str value:
        """

        self.com_object.ApplicationTypeString = value

    @property
    def applicative_profiles(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApplicativeProfiles() As CATSafeArrayVariant (Read
                | Only)
                | 
                |     Deprecated:
                |         R425 GetParameter GetProfileName IsProfileSet

        :return: tuple
        """

        return self.com_object.ApplicativeProfiles

    @property
    def c_frame_rivet_profile(self) -> OLPCFrameRivetProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CFrameRivetProfile() As OlpCFrameRivetProfile
                |     Get/Set the CFrameRivet profile associated with the
                |     instruction.
                | 
                |     This property will return a valid object even for new targets so it can be
                |     used to set accuracy values.
                | 
                |     This object is used to configure the rivet parameters. The parameters
                |     specified with the iMatch input equal to TRUE will be used to find an existing
                |     profile to reuse for this motion. If no matching profile is found a new one
                |     will be created. To modify a profile directly please use
                |     OlpController.CFrameRivetProfileList.

        :return: OLPCFrameRivetProfile
        """

        return OLPCFrameRivetProfile(self.com_object.CFrameRivetProfile)

    @c_frame_rivet_profile.setter
    def c_frame_rivet_profile(self, value: OLPCFrameRivetProfile):
        """
        :param OLPCFrameRivetProfile value:
        """

        self.com_object.CFrameRivetProfile = value

    @property
    def choreography(self) -> OLPChoreographyEvents:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Choreography() As OlpChoreographyEvents (Read Only)
                |     Get choreography manager to access and create choregraphy for this
                |     motion.

        :return: OLPChoreographyEvents
        """

        return OLPChoreographyEvents(self.com_object.Choreography)

    @property
    def conveyor_taught_position(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConveyorTaughtPosition() As double
                |     Get/Set the conveyor taught position in meters.

        :return: float
        """

        return self.com_object.ConveyorTaughtPosition

    @conveyor_taught_position.setter
    def conveyor_taught_position(self, value: float):
        """
        :param float value:
        """

        self.com_object.ConveyorTaughtPosition = value

    @property
    def conveyor_tracking(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConveyorTracking() As boolean
                |     Get/Set whether this target is tracking a conveyor.

        :return: bool
        """

        return self.com_object.ConveyorTracking

    @conveyor_tracking.setter
    def conveyor_tracking(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ConveyorTracking = value

    @property
    def conveyor_tracking_profile(self) -> OLPConveyorTrackingProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConveyorTrackingProfile() As
                | OlpConveyorTrackingProfile
                |     Get/Set the conveyor tracking profile.
                | 
                |     This property will return a valid object without being set even for new
                |     motions so it can be used to set tracking parameters.
                | 
                |     This object is used to configure the tracking parameters. The parameters
                |     specified with the iMatch input equal to TRUE will be used to find an existing
                |     profile to reuse for this motion. If no matching profile is found, a new one
                |     will be created. To modify a profile directly please use
                |     OlpController.ConveyorTrackingProfileList.

        :return: OLPConveyorTrackingProfile
        """

        return OLPConveyorTrackingProfile(self.com_object.ConveyorTrackingProfile)

    @conveyor_tracking_profile.setter
    def conveyor_tracking_profile(self, value: OLPConveyorTrackingProfile):
        """
        :param OLPConveyorTrackingProfile value:
        """

        self.com_object.ConveyorTrackingProfile = value

    @property
    def drill_profile(self) -> OLPDrillRivetProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrillProfile() As OlpDrillRivetProfile
                |     Get/Set the drill profile associated with the instruction.
                | 
                |     This property will return a valid object even for new targets so it can be
                |     used to set accuracy values.
                | 
                |     This object is used to configure the drill parameters. The parameters
                |     specified with the iMatch input equal to TRUE will be used to find an existing
                |     profile to reuse for this motion. If no matching profile is found a new one
                |     will be created. To modify a profile directly please use
                |     OlpController.DrillProfileList.

        :return: OLPDrillRivetProfile
        """

        return OLPDrillRivetProfile(self.com_object.DrillProfile)

    @drill_profile.setter
    def drill_profile(self, value: OLPDrillRivetProfile):
        """
        :param OLPDrillRivetProfile value:
        """

        self.com_object.DrillProfile = value

    @property
    def drill_rivet_profile(self) -> OLPDrillRivetProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrillRivetProfile() As OlpDrillRivetProfile
                |     Get/Set the drill-rivet profile associated with the
                |     instruction.
                | 
                |     This property will return a valid object even for new targets so it can be
                |     used to set accuracy values.
                | 
                |     This object is used to configure the drill-rivet parameters. The parameters
                |     specified with the iMatch input equal to TRUE will be used to find an existing
                |     profile to reuse for this motion. If no matching profile is found a new one
                |     will be created. To modify a profile directly please use
                |     OlpController.DrillRivetProfileList.

        :return: OLPDrillRivetProfile
        """

        return OLPDrillRivetProfile(self.com_object.DrillRivetProfile)

    @drill_rivet_profile.setter
    def drill_rivet_profile(self, value: OLPDrillRivetProfile):
        """
        :param OLPDrillRivetProfile value:
        """

        self.com_object.DrillRivetProfile = value

    @property
    def generic_config(self) -> OLPRobotConfigGeneric:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GenericConfig() As OlpRobotConfigGeneric (Read Only)
                |     Get the config used for this target.
                | 
                |     This is the generic DELMIA config which includes the posture and turn
                |     numbers/turn signs used for determining a unique inverse kinematics solution
                |     for a given Cartesian position.

        :return: OLPRobotConfigGeneric
        """

        return OLPRobotConfigGeneric(self.com_object.GenericConfig)

    @property
    def global_position(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GlobalPosition() As boolean
                |     Get/Set whether this target uses a global position (not just local to this
                |     task).
                | 
                |     Global positions are treated specially during upload. Global cartesian
                |     positions are uploaded as tag targets in a dedicated tag group and their
                |     position is locked against accidental modification. This is to prevent
                |     accidental modification of a position that is used in other tasks so that the
                |     behavior of the other tasks is not affected. Global joint targets are uploaded
                |     as home positions. Home positions cannot be modified directly in teach eacher,
                |     which also prevents accidental modification.

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
    def home(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Home() As CATBSTR
                |     Get/Set the home name used for the primary device in this
                |     target.
                | 
                |     An empty string means that no home is used for this position. The target
                |     type will be assumed to be a home target if a home position is set. See
                |     TargetType for how to override this.
                | 
                |     Both device joint values and a home name can be specified.
                | 
                |         If the home name exists and device joints are set then the joint values
                |         should match the existing home name or a warning will be
                |         issued.
                |         If the home name exists and device joints are not set, then the home
                |         name is used as is.
                |         If the home name does not exist and device joints are set then the home
                |         name will be created using the specified joint values.
                |         If the home name does not exist and device joints are not set then the
                |         home name will be created with joint values of all zero and a warning will be
                |         issued.

        :return: str
        """

        return self.com_object.Home

    @home.setter
    def home(self, value: str):
        """
        :param str value:
        """

        self.com_object.Home = value

    @property
    def home_set(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HomeSet() As CATBSTR
                |     Get/Set the home set name.
                |     Home sets are used to group home positions during upload for re-use. Any
                |     home positions with the same name in the same set can be re-used for multiple
                |     moves. For a home position to be re-used it must also have the same joint
                |     values. There is also a special "Global" home set that includes all existing
                |     home positions. If a home position is in the "Global" homeset, a home position
                |     that existed before the upload that has te same name will be reused and if the
                |     uploaded joint values are different, the existing home position will be updated
                |     with the new joint values. By default, when the HomeSet name has not been set,
                |     any GlobalPosition homes are in the "Global" home set. All other homes are in a
                |     set for their task. Home set names are not stored so during download this
                |     proprty is unset.

        :return: str
        """

        return self.com_object.HomeSet

    @home_set.setter
    def home_set(self, value: str):
        """
        :param str value:
        """

        self.com_object.HomeSet = value

    @property
    def keep_tag_position(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KeepTagPosition() As boolean
                |     Do not update the tag position.
                |     In NRLTeach, modification of other properties, like the object frame, aux
                |     axis values, etc could impact the tag position even if SetTransform has not
                |     been called. The APIs are designed to work in robot coordinates (not simulation
                |     coordinates). This means the target transform is relative to the object frame.
                |     For example, if the tag is attached to the part and the part is attached to an
                |     aux positioner, and the object frame is stationary (not attached to the
                |     positioner), updating the positioner angle on the move and keeping the same
                |     x,y,z,w,p,r of the target, the target is kept in the same position relative to
                |     the object frame but has moved relative to the part so the tag position
                |     changes. This is effective only for the current macro call and will be reset to
                |     FALSE after the macro finishes. This cannot be set to TRUE for new moves, moves
                |     that are not tag targets, and you cannot set the target (e.g. SetTransform,
                |     SetDeviceJoints for the robot, Home) before or after setting this to True.

        :return: bool
        """

        return self.com_object.KeepTagPosition

    @keep_tag_position.setter
    def keep_tag_position(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.KeepTagPosition = value

    @property
    def motion_profile(self) -> RscMotionProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionProfile() As RscMotionProfile
                | 
                |     Deprecated:
                |         R215 MotionProfileOlp

        :return: RscMotionProfile
        """

        return RscMotionProfile(self.com_object.MotionProfile)

    @motion_profile.setter
    def motion_profile(self, value: RscMotionProfile):
        """
        :param RscMotionProfile value:
        """

        self.com_object.MotionProfile = value

    @property
    def motion_profile_olp(self) -> OLPMotionProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionProfileOlp() As OlpMotionProfile
                |     Get/Set the motion profile associated with the
                |     instruction.
                | 
                |     This property will return a valid object without being set even for new
                |     motions so it can be used to set speed values.
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
                |     Get/Set the motion type used for this target.

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
    def object_frame_profile(self) -> OLPObjectFrameProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ObjectFrameProfile() As OlpObjectFrameProfile
                |     Get/Set the object frame profile used for this target.
                | 
                |     The object frame profile must be from the primary device's
                |     controller.

        :return: OLPObjectFrameProfile
        """

        return OLPObjectFrameProfile(self.com_object.ObjectFrameProfile)

    @object_frame_profile.setter
    def object_frame_profile(self, value: OLPObjectFrameProfile):
        """
        :param OLPObjectFrameProfile value:
        """

        self.com_object.ObjectFrameProfile = value

    @property
    def offset_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OffsetType() As DELOlpOffsetType
                |     Get/Set the type of offset.
                | 
                |     An Offset adjusts the primary taget of the robot. The offset can be a joint
                |     offset or a Cartesian offset. Cartesian offsets can be relative to the TCP
                |     (tool frame), the object frame used by this target, or the station (task
                |     context frame). Station frames are not used unless the translator calls
                |     OlpTranslatorHelper.SetSupportedFeature with the input "StationOffset" (see
                |     DELOlpOffsetType for more details). All types of offsets can include joint
                |     value offsets for the aux devices. delOlpNoOffset is returned if the target
                |     does not have an offset. Setting a different OffsetType after setting a
                |     Cartesian offset using SetCartesianOffset or after setting a joint offset for
                |     the robot with SetJointOffset will clear the offset values. It will not clear
                |     the joint offsets for the aux devices. The default value if not set during
                |     upload is delOlpNoOffset. The delOlpJointOffset type is NOT supported for
                |     upload.
                | 
                |     To use offsets, you must call OlpTranslatorHelper.SetSupportedFeature with
                |     the input "OffsetMotion" otherwise this function will fail and the offset will
                |     be directly included in the normal target.

        :return: DELOlpOffsetType
        """

        return self.com_object.OffsetType

    @offset_type.setter
    def offset_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.OffsetType = value

    @property
    def orientation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientationMode() As DELOlpOrientationMode
                |     Get/Set the orientation mode used for this target.
                |     This is not available if MotionType set to joint.

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
    def position_variable(self) -> OLPPositionVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionVariable() As OlpPositionVariable
                |     Get/Set position variable.
                | 
                |     A target can be specified with a position variable, in place of Cartesian
                |     or joint values. The DELMIAOlpVariable in this case will be of type "Position"
                |     as its DataTypeInString property.

        :return: OLPPositionVariable
        """

        return OLPPositionVariable(self.com_object.PositionVariable)

    @position_variable.setter
    def position_variable(self, value: OLPPositionVariable):
        """
        :param OLPPositionVariable value:
        """

        self.com_object.PositionVariable = value

    @property
    def process_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProcessType() As DELOlpProcessType
                |     Get/Set the type of process operation being done at this
                |     target.
                | 
                |     This is used with tags in specialized trajectories. On upload, the value
                |     can only be set to a limited number of options based on the type of robot
                |     motion being created.
                | 
                |         Robot Motions: only delOlpUndefinedProcess can be set.
                |         Spot Operations: only delOlpUndefinedProcess can be
                |         set.
                |         Point Operations: only delOlpUndefinedProcess can be
                |         set.
                |         Arc Operations: can be set to delOlpStartWeld, delOlpWeld, or
                |         delOlpEndWeld.
                |         Sealant Operations: can be set to delOlpStartProcess, delOlpMidProcess,
                |         or delOlpEndProcess.
                |         Path Adhesive Operations: can be set to delOlpStartProcess,
                |         delOlpMidProcess, or delOlpEndProcess.
                |         Seam Search Operations: can be set to delOlpViaPoint or
                |         delOlpTouchPoint.

        :return: DELOlpProcessType
        """

        return self.com_object.ProcessType

    @process_type.setter
    def process_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ProcessType = value

    @property
    def redundant_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RedundantAngle() As double
                |     Get/Set the reduntant angle value for a 7 degree of freedom robot's
                |     cartesian target.

        :return: float
        """

        return self.com_object.RedundantAngle

    @redundant_angle.setter
    def redundant_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.RedundantAngle = value

    @property
    def relative_move_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RelativeMoveType() As DELOlpRelativeMoveType
                |     Get/Set whether this is a relative move.
                | 
                |     A relative move, moves the robot the specified distance or joint values
                |     relative to the current position of the robot. A relative move can be a joint
                |     move or a Cartesian move. In both cases, the relative move coordinates are
                |     stored and retrieved from the robot using the usual methods. GetTransform and
                |     SetTranform for Cartesian relative moves or or GetDeviceJoints and
                |     SetDeviceJoints for joint relative moves. The TargetType will match the
                |     relative move type. The default value if not set during upload is
                |     delOlpNoRelative.
                | 
                |     To use relative moves, you must call
                |     OlpTranslatorHelper.SetSupportedFeature with the input "RelativeMotion"
                |     otherwise this function will fail and the target retreived from GetTransform
                |     and GetDeviceJoints will be the resulting target motion of the relative motion
                |     instead of the relative values stored on the move. This result may not be
                |     correct depending on the complexity of the program, in which case a warning
                |     will be issued.

        :return: DELOlpRelativeMoveType
        """

        return self.com_object.RelativeMoveType

    @relative_move_type.setter
    def relative_move_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.RelativeMoveType = value

    @property
    def rivet_profile(self) -> OLPDrillRivetProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RivetProfile() As OlpDrillRivetProfile
                |     Get/Set the rivet profile associated with the instruction.
                | 
                |     This property will return a valid object even for new targets so it can be
                |     used to set accuracy values.
                | 
                |     This object is used to configure the rivet parameters. The parameters
                |     specified with the iMatch input equal to TRUE will be used to find an existing
                |     profile to reuse for this motion. If no matching profile is found a new one
                |     will be created. To modify a profile directly please use
                |     OlpController.RivetProfileList.

        :return: OLPDrillRivetProfile
        """

        return OLPDrillRivetProfile(self.com_object.RivetProfile)

    @rivet_profile.setter
    def rivet_profile(self, value: OLPDrillRivetProfile):
        """
        :param OLPDrillRivetProfile value:
        """

        self.com_object.RivetProfile = value

    @property
    def spot_profile(self) -> OLPSpotProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpotProfile() As OlpSpotProfile
                |     Get/Set the spot profile associated with the instruction.
                | 
                |     This property will return a valid object without being set even for new
                |     motions so it can be used to set spot parameters. This property is only valid
                |     for spot operations.
                | 
                |     This object is used to configure the spot parameters. The parameters
                |     specified with the iMatch input equal to TRUE will be used to find an existing
                |     profile to reuse for this motion. If no matching profile is found, a new one
                |     will be created. To modify a profile directly please use
                |     OlpController.SpotProfileList.

        :return: OLPSpotProfile
        """

        return OLPSpotProfile(self.com_object.SpotProfile)

    @spot_profile.setter
    def spot_profile(self, value: OLPSpotProfile):
        """
        :param OLPSpotProfile value:
        """

        self.com_object.SpotProfile = value

    @property
    def tag(self) -> OLPTag:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Tag() As OlpTag (Read Only)
                |     Get the tag.
                | 
                |     Getting the tag will fail if the target is not a tag target. For a new
                |     motion target, getting the tag will fail until after the macro has finished.
                |     The main purpose of this function is to get an object which can be used with ID
                |     fixer to generate a unique position name.

        :return: OLPTag
        """

        return OLPTag(self.com_object.Tag)

    @property
    def tag_group_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TagGroupName() As CATBSTR
                |     Get/Set the tag group name.
                | 
                |     Use the AnyObject.Name property to get/set the tag name for this
                |     target.

        :return: str
        """

        return self.com_object.TagGroupName

    @tag_group_name.setter
    def tag_group_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.TagGroupName = value

    @property
    def tag_group_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TagGroupType() As DELOlpTagGroupType
                |     Get/Set the tag group type (spot welding, arc welding,
                |     etc).
                | 
                |     Usually the tag group type matches the ApplicationType. If the value is not
                |     set then the tag group type for the application will be
                |     used.

        :return: DELOlpTagGroupType
        """

        return self.com_object.TagGroupType

    @tag_group_type.setter
    def tag_group_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.TagGroupType = value

    @property
    def tag_group_type_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TagGroupTypeString() As CATBSTR
                |     Get/Set the tag group type as a string (spot welding, arc welding,
                |     etc).
                | 
                |     This property is redundant to TagGroupType but must be used for new
                |     applications where the application has not yet been added to
                |     DELOlpTagGroupType. Usually the tag group type matches the ApplicationType. If
                |     this value is not set then the tag group type for the application will be
                |     used.

        :return: str
        """

        return self.com_object.TagGroupTypeString

    @tag_group_type_string.setter
    def tag_group_type_string(self, value: str):
        """
        :param str value:
        """

        self.com_object.TagGroupTypeString = value

    @property
    def target_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TargetType() As DELOlpTargetType
                |     Get/Set the target type used for this target.
                | 
                |     The target type does not need to be specified. It will be automatically
                |     inferred from the type of robot motion and how the target position has been
                |     set.
                | 
                |     This property can be set to override the inferred target type. For example
                |     if SetDeviceJoints has been called, you can have a tag target created by
                |     setting this property to delOlpTagTarget.
                | 
                |         Spot Operations: a tag target will always be created and cannot be
                |         overridden.
                |         Point Operations: a tag target will always be created and cannot be
                |         overridden.
                |         Arc Operations: a tag target will always be created and cannot be
                |         overridden.
                |         Seam Search Operations: a tag target will always be created and cannot
                |         be overridden.
                |         If SetTransform is called, a tag target will be created. This can be
                |         overridden.
                |         If SetDeviceJoints is called for the primary device and Home is not
                |         set, a joint target will be created. This can be
                |         overridden.
                |         If Home is set, a home target will be created. This can be
                |         overridden.

        :return: DELOlpTargetType
        """

        return self.com_object.TargetType

    @target_type.setter
    def target_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.TargetType = value

    @property
    def tool_profile(self) -> OLPToolProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ToolProfile() As OlpToolProfile
                |     Get/Set the tool profile used for this target.
                | 
                |     The tool profile must be from the primary device's
                |     controller.

        :return: OLPToolProfile
        """

        return OLPToolProfile(self.com_object.ToolProfile)

    @tool_profile.setter
    def tool_profile(self, value: OLPToolProfile):
        """
        :param OLPToolProfile value:
        """

        self.com_object.ToolProfile = value

    @property
    def waypoint_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WaypointID() As CATBSTR
                |     Get/Set the waypoint ID.
                |     The waypoint ID is defined on waypoint motions and also on motions that
                |     declare the closest waypoint. For actions, the WaypointID can be retrieved from
                |     the target or from the OlpTemplate that represents the action.

        :return: str
        """

        return self.com_object.WaypointID

    @waypoint_id.setter
    def waypoint_id(self, value: str):
        """
        :param str value:
        """

        self.com_object.WaypointID = value

    @property
    def waypoint_parent_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WaypointParentID() As CATBSTR
                |     Get/Set the waypoint parent ID.
                |     The waypoint parent ID is only defined on waypoint motions.

        :return: str
        """

        return self.com_object.WaypointParentID

    @waypoint_parent_id.setter
    def waypoint_parent_id(self, value: str):
        """
        :param str value:
        """

        self.com_object.WaypointParentID = value

    def add_applicative_profile(self, i_profile: RscApplicativeProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddApplicativeProfile(RscApplicativeProfile iProfile)
                | 
                |     Deprecated:
                |         R425 SetParameter SetProfileName

        :param RscApplicativeProfile i_profile:
        :return: None
        """
        return self.com_object.AddApplicativeProfile(i_profile.com_object)

    def get_applicative_profile(self, i_profile_type: str) -> RscApplicativeProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetApplicativeProfile(CATBSTR iProfileType) As
                | RscApplicativeProfile
                | 
                |     Deprecated:
                |         R425 GetParameter GetProfileName IsProfileSet

        :param str i_profile_type:
        :return: RscApplicativeProfile
        """
        return RscApplicativeProfile(self.com_object.GetApplicativeProfile(i_profile_type))

    def get_aux_home(self, i_device: OLPController) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAuxHome(OlpController iDevice) As CATBSTR
                |     Get the home position for a specific aux device.
                | 
                |     The device must be part of the motion group used for this
                |     target.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to get the home position for. 
                | 
                |     Returns:
                |         The home name.

        :param OLPController i_device:
        :return: str
        """
        return self.com_object.GetAuxHome(i_device.com_object)

    def get_cartesian_offset(self) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCartesianOffset() As OlpTransform
                |     Get the Cartesian offset.
                | 
                |     The offest is in the frame of reference retrieved by OffsetType. This
                |     function will fail if the OffsetType is delOlpNoOffset or
                |     delOlpJointOffset.
                | 
                |     To use offsets, you must call OlpTranslatorHelper.SetSupportedFeature with
                |     the input "OffsetMotion" otherwise this function will fail and the offset will
                |     be directly included in the normal target.
                | 
                |     Returns:
                |         The offset.

        :return: OLPTransform
        """
        return OLPTransform(self.com_object.GetCartesianOffset())

    def get_device_joints(self, i_device: OLPController) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDeviceJoints(OlpController iDevice) As
                | CATSafeArrayVariant
                |     Get the joint values for a specific device.
                | 
                |     The device must be part of the motion group used for this
                |     target.
                | 
                |     Example: (VB.NET)
                | 
                |      Dim Group As OlpMotionGroup
                |      Dim Target As OlpRobotMotionTarget
                |      Dim Device As OlpController = Group.PrimaryDevice
                |      Dim AuxDeviceJointValues() As Object = Target.GetDeviceJoints(Device)
                |      
                |      ' get the 1st joint value - arrays in VB.NET are 0 based.
                |      Dim Joint1 As Double = AuxDeviceJointValues(0)
                |      
                |      ' display as a string with units - joint indexes are 1
                |      based
                |      If Device.GetJointType(1) = DELOlpJointType.delOlpLinearJoint Then
                |          MsgBox("Joint 1 : " & Joint1.ToString & "mm")
                |      Else
                |          MsgBox("Joint 1 : " & Joint1.ToString & "rad")
                |      End If
                |      
                | 
                |     In the case of an offset motion when a translator supports offsets,
                |     GetDeviceJoints for the robot returns the robot's joint values at the main
                |     target (without the offset).
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to get the joint values for. 
                | 
                |     Returns:
                |         The array of joint values. Each value in the array is a double. The
                |         joint values are in MKS units. The units depend on the joint
                |         type.
                | 
                |             Linear joints - units are in m.
                |             Rotational joints - units are in rad.

        :param OLPController i_device:
        :return: tuple
        """
        return self.com_object.GetDeviceJoints(i_device.com_object)

    def get_joint_offset(self, i_device: OLPController) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetJointOffset(OlpController iDevice) As
                | CATSafeArrayVariant
                |     Get the joint offset for a device.
                | 
                |     This function will return the joint offsets for any device in the motion
                |     group controlled by this target. This function will fail for the primary device
                |     of the motion group if the OffsetType is not delOlpJointOffset. This function
                |     can be called for aux devices for all types of offsets except
                |     delOlpNoOffset.
                | 
                |     To use offsets, you must call OlpTranslatorHelper.SetSupportedFeature with
                |     the input "OffsetMotion" otherwise this function will fail and the offset will
                |     be directly included in the normal target.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to get the joint offset values for. 
                | 
                |     Returns:
                |         The offset.

        :param OLPController i_device:
        :return: tuple
        """
        return self.com_object.GetJointOffset(i_device.com_object)

    def get_parameter(self, i_profile_type: str, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameter(CATBSTR iProfileType,CATBSTR iParameterName) As
                | CATVariant
                |     Get applicative profile parameter value.
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

    def get_parameter_from_parent(self, i_profile_type: str, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameterFromParent(CATBSTR iProfileType,CATBSTR iParameterName) As
                | CATVariant
                |     Get a parameter from a profile set on the multi-move sequence that contains
                |     this motion.
                | 
                |     This function will return the value of a specified parameter on a profile
                |     set on the multi-move sequence this motion instruction is contained within. If
                |     no profile type is specified, this function will fail. If no parameter is
                |     specified, this function will fail.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The type of profile to check for this parameter. 
                |         iParameterName
                |             The the parameter to get the value of. 
                | 
                |     Returns:
                |         The value.

        :param str i_profile_type:
        :param str i_parameter_name:
        :return: CATVariant
        """
        return CATVariant(self.com_object.GetParameterFromParent(i_profile_type, i_parameter_name))

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

    def get_position_variable_offset(self, o_offset: OLPPositionVariable, o_reference_frame: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPositionVariableOffset(OlpPositionVariable oOffset,DELOlpOffsetType
                | oReferenceFrame)
                |     Get the position variable offset.
                | 
                |     The offest is in the frame of reference retrieved by OffsetType. This
                |     function will fail if the OffsetType is delOlpNoOffset or delOlpJointOffset. It
                |     also fails if the offset is not a position variable.
                | 
                |     To use offsets, you must call OlpTranslatorHelper.SetSupportedFeature with
                |     the input "OffsetMotion" otherwise this function will fail and the offset will
                |     be directly included in the normal target.
                | 
                |     Returns:
                |         The offset as position variable.

        :param OLPPositionVariable o_offset:
        :param int o_reference_frame:
        :return: None
        """
        return self.com_object.GetPositionVariableOffset(o_offset.com_object, o_reference_frame)

    def get_profile_name(self, i_profile_type: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfileName(CATBSTR iProfileType) As CATBSTR
                |     Get applicative profile instance name.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                | 
                |     Returns:
                |         The profile instance name

        :param str i_profile_type:
        :return: str
        """
        return self.com_object.GetProfileName(i_profile_type)

    def get_profile_name_from_parent(self, i_profile_type: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfileNameFromParent(CATBSTR iProfileType) As CATBSTR
                |     Get the name of the profile of a specified type on the multi-move sequence
                |     that contains this motion.
                | 
                |     This function will return the name of the profile of a specified type on
                |     the multi-move sequence that contains this motion. If there is no profile of
                |     the specified type set on the sequence, or if there is no sequence associated
                |     with the target, it will return "".
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The type of profile to find the name of. 
                | 
                |     Returns:
                |         The name of the profile set on the parent sequence.

        :param str i_profile_type:
        :return: str
        """
        return self.com_object.GetProfileNameFromParent(i_profile_type)

    def get_profile_olp(self, i_profile_type: str) -> OLPProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfileOlp(CATBSTR iProfileType) As OlpProfile
                |     Get a applicative or user profile.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The type of profile to return. 
                | 
                |     Returns:
                |         The profile. Only 1 instance of a profile can be assigned to a motion.

        :param str i_profile_type:
        :return: OLPProfile
        """
        return OLPProfile(self.com_object.GetProfileOlp(i_profile_type))

    def get_transform(self, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTransform(DELOlpPositionRef iOrigin) As OlpTransform
                |     Get the target location as a Cartesian position.
                | 
                |     Translators should always treat the Cartesian position as being relative to
                |     the object frame. The object frame is relative to iOrigin (the origin of the
                |     coordinate system used by the translator).
                | 
                |     The same origin reference must be used when getting the object frame
                |     location and the Cartesian position. See
                |     OlpObjectFrameProfile.GetTransform.
                | 
                |     If an object frame's position has not been set then the Cartesian position
                |     is relative to iOrigin. This is because the object frame is assumed to be zero
                |     (an Identity transform) relative to any specified origin. The object frame is
                |     not set if X, Y, Z, Yaw, Pitch, and Roll components are internally stored as
                |     zero. The object frame is stored relative to the station in most
                |     cases.
                | 
                |     For Fixed TCP motions, the origin must be delOlpMount. The object frame is
                |     always relative to the mount plate for fixed TCP motions.
                | 
                |     If the user has selected the part coordinates option, then for tag targets
                |     which are attached (or owned by) a part other than the station, the transform
                |     will be relative to the part's origin and the object frame is ignored.
                |     Translators should not modify their behavior when the customer has selected
                |     part coordinates.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The origin of the coordinate system being used by the translator.
                |             
                | 
                |     Returns:
                |         The target location.

        :param int i_origin:
        :return: OLPTransform
        """
        return OLPTransform(self.com_object.GetTransform(i_origin))

    def is_offset_position_variable(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsOffsetPositionVariable() As boolean
                |     Query if there is position variable offset.
                | 
                |     This will return true only if there is an offset AND the offset is a
                |     position variable.
                | 
                |     Returns:
                |         True if there is an offset as position variable, False otherwise.

        :return: bool
        """
        return self.com_object.IsOffsetPositionVariable()

    def is_profile_set(self, i_profile_type: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsProfileSet(CATBSTR iProfileType) As boolean
                |     Identify if profile type is set.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                | 
                |     Returns:
                |         TRUE if profile has be set.

        :param str i_profile_type:
        :return: bool
        """
        return self.com_object.IsProfileSet(i_profile_type)

    def is_profile_set_on_parent(self, i_profile_type: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsProfileSetOnParent(CATBSTR iProfileType) As boolean
                |     Check whether a profile is active on the multi-move sequence that contains
                |     this motion.
                | 
                |     This function will return True if the profile type specified is set on the
                |     multi-move sequence this motion instruction is contained within. It will return
                |     False if the profile type is not set or if there is no multi-move sequence
                |     associated with the motion.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The type of profile to check for. 
                | 
                |     Returns:
                |         the boolean for whether or not the profile is set.

        :param str i_profile_type:
        :return: bool
        """
        return self.com_object.IsProfileSetOnParent(i_profile_type)

    def set_accuracy_params(self, i_fly_by: bool, i_accuracy_type: int, i_accuracy_value: float, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAccuracyParams(boolean iFlyBy,AccuracyType iAccuracyType,double
                | iAccuracyValue,CATBSTR iName)
                |     Set the accuracy profile for this target using the
                |     parameters.
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

    def set_aux_home(self, i_device: OLPController, i_home_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAuxHome(OlpController iDevice,CATBSTR iHomeName)
                |     Set the home position for a specific aux device.
                | 
                |     The device must be part of the motion group used for this
                |     target.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to set the home position for. 
                |         iHomeName
                |             The home name.

        :param OLPController i_device:
        :param str i_home_name:
        :return: None
        """
        return self.com_object.SetAuxHome(i_device.com_object, i_home_name)

    def set_cartesian_offset(self, i_offset: OLPTransform, i_reference_frame: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCartesianOffset(OlpTransform iOffset,DELOlpOffsetType
                | iReferenceFrame)
                |     Set the Cartesian offset.
                | 
                |     You must specify both the offset and the reference frame as an offset type.
                |     The function will fail if you specify delOlpNoOffset or delOlpJointOffset. This
                |     function will also change the value of OffsetType. Cartesian offsets can only
                |     be set if a robot is in the motion group.
                | 
                |     To use offsets, you must call OlpTranslatorHelper.SetSupportedFeature with
                |     the input "OffsetMotion" otherwise this function will fail and the offset will
                |     be directly included in the normal target.
                | 
                |     Parameters:
                | 
                |         iOffset
                |             The joint offset values. 
                |         iReferenceFrame
                |             The reference frame the offset values are defined in.

        :param OLPTransform i_offset:
        :param int i_reference_frame:
        :return: None
        """
        return self.com_object.SetCartesianOffset(i_offset.com_object, i_reference_frame)

    def set_device_joints(self, i_device: OLPController, i_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDeviceJoints(OlpController iDevice,CATSafeArrayVariant
                | iValues)
                |     Set the joint values for a specific device.
                | 
                |     The device must be part of the motion group used for this
                |     target.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to set the joint values for. 
                |         iValues
                |             The array of joint values. Each value in the array is a double. The
                |             joint values are in MKS units. The units depend on the joint type. The number
                |             of values must be the same as the number of joints for the
                |             device.
                | 
                |                 Linear joints - units are in m.
                |                 Rotational joints - units are in rad.

        :param OLPController i_device:
        :param tuple i_values:
        :return: None
        """
        return self.com_object.SetDeviceJoints(i_device.com_object, i_values)

    def set_joint_offset(self, i_device: OLPController, i_offset: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetJointOffset(OlpController iDevice,CATSafeArrayVariant
                | iOffset)
                |     Set the joint offset for a device.
                | 
                |     This function will set the joint offsets for any device in the motion group
                |     controlled by this target. This function will set the offset type to
                |     delOlpJointOffset if called for the primary device. When called for an aux
                |     device, if the offset type is currently delOlpNoOffset, it will be change dto
                |     delOlpJointOffset but it will not be changed if the offset type is
                |     Cartesian.
                | 
                |     To use offsets, you must call OlpTranslatorHelper.SetSupportedFeature with
                |     the input "OffsetMotion" otherwise this function will fail and the offset will
                |     be directly included in the normal target.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to set the joint offset values for. 
                |         iOffset
                |             The joint offset values.

        :param OLPController i_device:
        :param tuple i_offset:
        :return: None
        """
        return self.com_object.SetJointOffset(i_device.com_object, i_offset)

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

    # todo:
    def set_offset_base_target(self, i_base_target: OLPRobotMotionTarget) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOffsetBaseTarget(OlpRobotMotionTarget iBaseTarget)
                |     Set the base target / tag for this offset motion.
                | 
                |     To calculate offset amount for uploading a motion, its base target is
                |     needed in addition to offset type, where delOlpJointOffset is not supported
                |     yet.
                | 
                |     To use offsets, you must call OlpTranslatorHelper.SetSupportedFeature with
                |     the input "OffsetMotion" otherwise this function will fail and the motion will
                |     be uploaded as the normal target.
                | 
                |     Parameters:
                | 
                |         iBaseTarget
                |             The base target to set.

        :param OLPRobotMotionTarget i_base_target:
        :return: None
        """
        return self.com_object.SetOffsetBaseTarget(i_base_target.com_object)

    def set_parameter(self, i_profile_type: str, i_parameter_name: str, i_value: CATVariant, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParameter(CATBSTR iProfileType,CATBSTR iParameterName,CATVariant
                | iValue,boolean iMatch)
                |     Set applicative profile parameter value.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iParameterName
                |             The parameter name 
                |         iValue
                |             The parameter value. 
                |         iMatch
                |             If TRUE use parameter to find existing applicative profile

        :param str i_profile_type:
        :param str i_parameter_name:
        :param CATVariant i_value:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetParameter(i_profile_type, i_parameter_name, i_value, i_match)

    def set_position_variable_offset(self, i_offse: OLPPositionVariable, i_reference_frame: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPositionVariableOffset(OlpPositionVariable iOffse,DELOlpOffsetType
                | iReferenceFrame)
                |     Set the Cartesian offset using the position variable.
                | 
                |     You must specify both the offset as a position variable and the reference
                |     frame as an offset type. The function will fail if you specify delOlpNoOffset
                |     or delOlpJointOffset. This function will also change the value of OffsetType.
                |     Cartesian offsets can only be set if a robot is in the motion
                |     group.
                | 
                |     To use offsets, you must call OlpTranslatorHelper.SetSupportedFeature with
                |     the input "OffsetMotion" otherwise this function will fail and the offset will
                |     be directly included in the normal target.
                | 
                |     Parameters:
                | 
                |         iOffset
                |             The offset as position variable. 
                |         iReferenceFrame
                |             The reference frame the offset values are defined in.

        :param OLPPositionVariable i_offse:
        :param int i_reference_frame:
        :return: None
        """
        return self.com_object.SetPositionVariableOffset(i_offse.com_object, i_reference_frame)

    def set_profile_name(self, i_profile_type: str, i_profile_name: str, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProfileName(CATBSTR iProfileType,CATBSTR iProfileName,boolean
                | iMatch)
                |     Get applicative profile instance name.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iProfileName
                |             The profile instance name 
                |         iMatch
                |             If TRUE use name to find existing applicative profile

        :param str i_profile_type:
        :param str i_profile_name:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetProfileName(i_profile_type, i_profile_name, i_match)

    def set_profile_olp(self, i_profile: OLPProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProfileOlp(OlpProfile iProfile)
                |     Set a applicative or user profile.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The profile.

        :param OLPProfile i_profile:
        :return: None
        """
        return self.com_object.SetProfileOlp(i_profile.com_object)

    def set_transform(self, i_origin: int, i_target: OLPTransform) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTransform(DELOlpPositionRef iOrigin,OlpTransform
                | iTarget)
                |     Set the target location as a Cartesian position.
                | 
                |     See GetTransform for details.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The origin of the coordinate system being used by the translator.
                |             
                | 
                |     Returns:
                |         The target location.

        :param int i_origin:
        :param OLPTransform i_target:
        :return: None
        """
        return self.com_object.SetTransform(i_origin, i_target.com_object)

    def set_wrist_joints(self, i_j4: float, i_j5: float, i_j6: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetWristJoints(double iJ4,double iJ5,double iJ6)
                |     Method sets orientation of the transform using wrist
                |     joints
                |     When using this method, you need to set both the Cartesian posision with
                |     SetTransform and call SetWristJoints. The Orientation from SetTransform will be
                |     ignored when calculating the target location. Role: Used in robot programming
                |     languages such as Kobelco.
                | 
                |     Parameters:
                | 
                |         iJ4
                |             joint 4 value in radians 
                |         iJ5
                |             joint 5 value in radians 
                |         iJ6
                |             joint 6 value in radians

        :param float i_j4:
        :param float i_j5:
        :param float i_j6:
        :return: None
        """
        return self.com_object.SetWristJoints(i_j4, i_j5, i_j6)

    def try_get_device_joints(self, i_device: OLPController, o_values: tuple) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TryGetDeviceJoints(OlpController iDevice,CATSafeArrayVariant oValues) As
                | boolean
                |     Try to get the joint values for a specific device.
                | 
                |     This works the same as GetDeviceJoints, but it also returns the
                |     reachability status. It does not log any errors if the position is not
                |     reachable.
                | 
                |     Parameters:
                | 
                |         iDevice
                |             The device to get the joint values for. 
                |         oValues
                |             The array of joint values. Each value in the array is a double. The
                |             joint values are in MKS units. The units depend on the joint type. see
                |             GetDeviceJoints 
                | 
                |     Returns:
                |         TRUE if the position is reachable, FALSE if not reachable.

        :param OLPController i_device:
        :param tuple o_values:
        :return: bool
        """
        return self.com_object.TryGetDeviceJoints(i_device.com_object, o_values)

    def __repr__(self):
        return f'OLPRobotMotionTarget(name="{ self.name }")'
