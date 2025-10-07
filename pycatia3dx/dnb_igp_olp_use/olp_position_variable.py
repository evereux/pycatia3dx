"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_controller import OLPController
from pycatia3dx.dnb_igp_olp_use.olp_motion_group import OLPMotionGroup
from pycatia3dx.dnb_igp_olp_use.olp_object_frame_profile import OLPObjectFrameProfile
from pycatia3dx.dnb_igp_olp_use.olp_robot_config_generic import OLPRobotConfigGeneric
from pycatia3dx.dnb_igp_olp_use.olp_tag import OLPTag
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable


class OLPPositionVariable(OLPVariable):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpVariable
                |                         OlpPositionVariable
                | 
                | A variable with data type position used for targets or offset
                | moves.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | Variables are created with OlpVariables. This extension of OlpVariable is for
                | variables with the data type of position that are used as a target of a robot
                | motion, as an offset of a robot motion, or to store temporary position values.
                | The properties and methods here let you get and set the default value of these
                | variables.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def generic_config(self) -> OLPRobotConfigGeneric:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GenericConfig() As OlpRobotConfigGeneric (Read Only)
                |     Get the config data for this variable.
                | 
                |     The config object can only be retrieved for variables of
                |     PositionVariableType equal to "Tag". For new variables, set the
                |     PositionVariableType to "Tag" and the MotionGroup before getting this
                |     object.
                | 
                |     This is the generic DELMIA config which includes the posture and turn
                |     numbers/turn signs used for determining a unique inverse kinematics solution
                |     for a given Cartesian position.
                | 
                |     You can use this object to set the config/turns on an existing or new
                |     variable or subscripted variable.

        :return: OLPRobotConfigGeneric
        """

        return OLPRobotConfigGeneric(self.com_object.GenericConfig)

    @property
    def motion_group(self) -> OLPMotionGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionGroup() As OlpMotionGroup
                |     The motion group associated to this variable.
                |     Ths should be always set for new varialbes. In cases where there is just 1
                |     motion group, the MotionGroup is inferred but variable creation will fail if
                |     not set when there is more than 1 motion group. This must be set before getting
                |     the GenericConfig.

        :return: OLPMotionGroup
        """

        return OLPMotionGroup(self.com_object.MotionGroup)

    @motion_group.setter
    def motion_group(self, value: OLPMotionGroup):
        """
        :param OLPMotionGroup value:
        """

        self.com_object.MotionGroup = value

    @property
    def object_frame_profile(self) -> OLPObjectFrameProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ObjectFrameProfile() As OlpObjectFrameProfile
                |     Get/Set the object frame profile used for this variable.
                | 
                |     The object frame can only be retrieved for variables of
                |     PositionVariableType equal to "Tag". For new variables, set the
                |     PositionVariableType before getting this object.
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
    def position_variable_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionVariableType(CATBSTR iType)
                |     The type of position variariable Can be one of
                | 
                |         Empty: no associated position. All other APIs will
                |         fail.
                |         Tag: a Cartesian type position. All APIs related to Cartesian targets /
                |         Tags can be used.
                |         Joint: a joint type position. Only Get/SetDeviceJoints, MotionGroup,
                |         and GlobalPosition can be used.
                |         Tool: a tool (TCP) position. Use
                |         DELMIAOlpProfileVariable.
                |         ObjectFrame: a object frame position. Use
                |         DELMIAOlpProfileVariable.

        :return: str
        """

        return self.com_object.PositionVariableType

    @position_variable_type.setter
    def position_variable_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.PositionVariableType = value

    @property
    def process_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProcessType() As DELOlpProcessType
                |     Get/Set the type of process operation being done by this
                |     variable.
                | 
                |     Meaningful for variable of PositionVariableType "Tag". Get fails for other
                |     types, Set changes the type to "Tag" unless the translator has set a specific
                |     type.
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
                |     variable.
                | 
                |     Meaningful for variable of PositionVariableType "Tag". Get fails for other
                |     types, Set changes the type to "Tag" unless the translator has set a specific
                |     type.

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
    def tag(self) -> OLPTag:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Tag() As OlpTag (Read Only)
                |     Get the tag.
                | 
                |     The tag object can only be retrieved for variables of PositionVariableType
                |     equal to "Tag". For new variables, set the PositionVariableType before getting
                |     this object.
                | 
                |     The main purpose of this function is to get an object which can be used
                |     with ID fixer to generate a unique position name.

        :return: OLPTag
        """

        return OLPTag(self.com_object.Tag)

    @property
    def tag_group_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TagGroupName(CATBSTR iName)
                |     Get/set the tag group name, meaningful for position variable
                |     only.
                | 
                |     Meaningful for variable of PositionVariableType "Tag". Get fails for other
                |     types, Set changes the type to "Tag" unless the translator has set a specific
                |     type.
                | 
                |     Use the AnyObject.Name property to get/set the tag name for this
                |     variable.

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
                |     Meaningful for variable of PositionVariableType "Tag". Get fails for other
                |     types, Set changes the type to "Tag" unless the translator has set a specific
                |     type.
                | 
                |     Usually the tag group type matches the application type. If the value is
                |     not set then the tag group type for the application will be
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
                |     Meaningful for variable of PositionVariableType "Tag". Get fails for other
                |     types, Set changes the type to "Tag" unless the translator has set a specific
                |     type.
                | 
                |     This property is redundant to ApplicationType but must be used for new
                |     applications where the application has not yet been added to
                |     DELOlpTagGroupType. Usually the tag group type matches the application type. If
                |     the value is not set then the tag group type for the application will be
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

    def get_device_joints(self, i_device: OLPController) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDeviceJoints(OlpController iDevice) As
                | CATSafeArrayVariant
                |     Get the aux joint values for a specific device.
                | 
                |     Meaningful for variable of PositionVariableType "Tag". Fails for other
                |     types.
                | 
                |     The device must be part of the motion group used for this variable and
                |     cannot be the primary device.
                | 
                |     Example: (VB.NET)
                | 
                |      Dim Var As OlpPositionVariable
                |      Dim Device As OlpController
                |      Dim AuxDeviceJointValues() As Object = Var.GetDeviceJoints(Device)
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

    def get_transform(self, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTransform(DELOlpPositionRef iOrigin) As OlpTransform
                |     Get the Cartesian location
                | 
                |     Meaningful for variable of PositionVariableType "Tag". Fails for other
                |     types.
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
                |     Parameters:
                | 
                |         iOrigin
                |             The origin of the coordinate system being used by the translator.
                |             
                | 
                |     Returns:
                |         The location.

        :param int i_origin:
        :return: OLPTransform
        """
        return OLPTransform(self.com_object.GetTransform(i_origin))

    def set_device_joints(self, i_device: OLPController, i_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDeviceJoints(OlpController iDevice,CATSafeArrayVariant
                | iValues)
                |     Set the joint values for a specific device.
                | 
                |     Changes the PositionVariableType to "Tag" unless the translator has set a
                |     specific type.
                | 
                |     The device must be part of the motion group used for this variable and not
                |     be the primary device.
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

    def set_transform(self, i_origin: int, i_target: OLPTransform) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTransform(DELOlpPositionRef iOrigin,OlpTransform
                | iTarget)
                |     Set the Cartesian location
                | 
                |     Changes the PositionVariableType to "Tag" unless the translator has set a
                |     specific type.
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
                |         The location. 

        :param int i_origin:
        :param OLPTransform i_target:
        :return: None
        """
        return self.com_object.SetTransform(i_origin, i_target.com_object)

    def __repr__(self):
        return f'OLPPositionVariable(name="{ self.name }")'
