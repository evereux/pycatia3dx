"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_controller import OLPController
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction
from pycatia3dx.dnb_igp_olp_use.olp_object_frame_profile import OLPObjectFrameProfile
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform
from pycatia3dx.dnb_igp_olp_use.olp_trigger_action import OLPTriggerAction


class OLPTrigger(OLPInstruction):

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
                |                         OlpTrigger
                | 
                | A trigger instruction.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def condition_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConditionType() As DELOlpTriggerConditionType
                |     Get/Set the type of condition used to determine when the trigger fires.

        :return: DELOlpTriggerConditionType
        """

        return self.com_object.ConditionType

    @condition_type.setter
    def condition_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ConditionType = value

    @property
    def distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Distance() As double
                |     Get/Set the distance before/after for a distance based
                |     trigger.
                |     Value is in meters. If the value is positive, the trigger fires when the
                |     robot has moved the specified distance past the target of the next move. If the
                |     value is negative, the triger fires when the robot arrives within the specified
                |     distance of the target of the next move. If the robot is already within that
                |     distance, the trigger fires immediately when the next move starts. Method fails
                |     if not a distance trigger.

        :return: float
        """

        return self.com_object.Distance

    @distance.setter
    def distance(self, value: float):
        """
        :param float value:
        """

        self.com_object.Distance = value

    @property
    def monitored_device(self) -> OLPController:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MonitoredDevice() As OlpController
                |     Get/Set the device that is monitored for the triggering
                |     condition.
                |     Generally this is the primary device of the motion group controlled by the
                |     task.

        :return: OLPController
        """

        return OLPController(self.com_object.MonitoredDevice)

    @monitored_device.setter
    def monitored_device(self, value: OLPController):
        """
        :param OLPController value:
        """

        self.com_object.MonitoredDevice = value

    @property
    def num_actions(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumActions() As long (Read Only)
                |     Get the number of actions.
                |     Generally there should be just 1, but the model allows multiple.

        :return: int
        """

        return self.com_object.NumActions

    @property
    def plane_attached_device(self) -> OLPController:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlaneAttachedDevice() As OlpController
                |     Get/Set the device moving the trigger plane.
                |     Returns Nothing if not attached to a device. Method fails if not a plane
                |     trigger.

        :return: OLPController
        """

        return OLPController(self.com_object.PlaneAttachedDevice)

    @plane_attached_device.setter
    def plane_attached_device(self, value: OLPController):
        """
        :param OLPController value:
        """

        self.com_object.PlaneAttachedDevice = value

    @property
    def plane_object_frame(self) -> OLPObjectFrameProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlaneObjectFrame() As OlpObjectFrameProfile
                |     Get/Set the object frame for the trigger plane.
                |     Does not need to be set on upload. It should be the same as the object
                |     frame on the next move. Method fails if not a plane trigger.

        :return: OLPObjectFrameProfile
        """

        return OLPObjectFrameProfile(self.com_object.PlaneObjectFrame)

    @plane_object_frame.setter
    def plane_object_frame(self, value: OLPObjectFrameProfile):
        """
        :param OLPObjectFrameProfile value:
        """

        self.com_object.PlaneObjectFrame = value

    @property
    def time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Time() As double
                |     Get/Set the time before/after for a time based trigger.
                |     Value is in seconds. If the value is positive, the trigger fires the
                |     specified time after the robot completes its next move. If the value is
                |     negative, the triger fires the specified number of seconds before the robot
                |     completes its next move. If the move will take less time than specified, the
                |     trigger fires immediately when the next move starts. Method fails if not a time
                |     trigger.

        :return: float
        """

        return self.com_object.Time

    @time.setter
    def time(self, value: float):
        """
        :param float value:
        """

        self.com_object.Time = value

    @property
    def triggered_moves(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TriggeredMoves() As CATSafeArrayVariant (Read Only)
                |     Get the list of moves that this trigger could apply to.
                |     Will be empty during upload until MacroSetConfigs.

        :return: tuple
        """

        return self.com_object.TriggeredMoves

    def create_and_append_action(self, i_type: str) -> OLPTriggerAction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateAndAppendAction(CATBSTR iType) As OlpTriggerAction
                |     Create a new acction.
                |     The new action is returned and is appended to the list of actions. It is
                |     recommended to use CreateUniqueAction to prevent accidental creation of
                |     multiple actions. Valid types are "GunActivate", "SetParam", "SetVar", and
                |     "PRun".

        :param str i_type:
        :return: OLPTriggerAction
        """
        return OLPTriggerAction(self.com_object.CreateAndAppendAction(i_type))

    def create_unique_action(self, i_type: str) -> OLPTriggerAction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateUniqueAction(CATBSTR iType) As OlpTriggerAction
                |     Get the action for triggers with a single action.
                |     This is the recommended and simplest way to access the action during
                |     upload. If no action of this type exists, a new one is created. If an action of
                |     this type already exists, it returns the 1st one. If other actions exists, they
                |     are all deleted. Valid types are "GunActivate", "SetParam", "SetVar", and
                |     "PRun".

        :param str i_type:
        :return: OLPTriggerAction
        """
        return OLPTriggerAction(self.com_object.CreateUniqueAction(i_type))

    def delete_action(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteAction(long iIndex)
                |     Delete a new acction.
                |     Delete an action and removes it from the list.

        :param int i_index:
        :return: None
        """
        return self.com_object.DeleteAction(i_index)

    def get_action(self, i_index: int) -> OLPTriggerAction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAction(long iIndex) As OlpTriggerAction
                |     Get the action.
                |     Generally, there is just 1 action. Index is 1 based.

        :param int i_index:
        :return: OLPTriggerAction
        """
        return OLPTriggerAction(self.com_object.GetAction(i_index))

    def get_plane(self, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPlane(DELOlpPositionRef iOrigin) As OlpTransform
                |     Get the plane for a plane based trigger.
                |     After starting the next move, this trigger will fire when the robot crosses
                |     that plane. The Y-Z plane of the transform is used as the trigger plane. (X+ is
                |     the normal to the plane) The transform is relative to the object frame. If the
                |     object frame is zero, the plane is relative to the specified origin.
                |     delOlpMount origin is not allowed. Method fails if not a plane trigger.

        :param int i_origin:
        :return: OLPTransform
        """
        return OLPTransform(self.com_object.GetPlane(i_origin))

    def set_plane(self, i_origin: int, i_plane: OLPTransform) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPlane(DELOlpPositionRef iOrigin,OlpTransform iPlane)
                |     Set the plane for a plane based trigger.
                |     After starting the next move, this trigger will fire when the robot crosses
                |     that plane. The Y-Z plane of the transform is used as the trigger plane. (X+ is
                |     the normal to the plane) The transform is relative to the object frame. If the
                |     object frame is zero, the plane is relative to the specified origin.
                |     delOlpMount origin is not allowed. Method fails if not a plane trigger.

        :param int i_origin:
        :param OLPTransform i_plane:
        :return: None
        """
        return self.com_object.SetPlane(i_origin.com_object, i_plane.com_object)

    def __repr__(self):
        return f'OLPTrigger(name="{ self.name }")'
