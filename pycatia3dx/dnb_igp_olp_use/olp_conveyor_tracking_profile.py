"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_controller import OLPController
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable


class OLPConveyorTrackingProfile(OLPProfile):

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
                |                         OlpConveyorTrackingProfile
                | 
                | A conveyor tracking profile used for translating a robot
                | program.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | This object contains the parameters for controlling the conveyor tracking.
                | Tracking is turned on and off with a property of the
                | OlpRobotMotionTarget.
                | 
                | To get the profile from the motion you need to use the temporary interface
                | OlpObjectAccess. The profile is the 1st object (index 0) in the returned
                | array.
                | Dim move As OlpRobotMotion
                | Dim target As OlpRobotMotionTarget = move.GetTarget(motiongroup)
                | Dim TargetTemp As OlpObjectAccess = Target
                | Dim returnarray() As Object = TargetTemp.GetProperty("ConveyorTrackingProfile", Nothing)
                | Dim profile as OlpConveyorTrackingProfile = returnarray(0)
                | 
                | The behavior of this object depends on where it was retrieved from. If the
                | object was retrieved from an OlpRobotMotionTarget then this object is used to
                | configure the properties of that motion. The parameters specified with the
                | iMatch input equal to TRUE will be used to find an existing profile to reuse
                | for this motion. If no matching profile is found, a new one will be created. If
                | the object was retrieved from OlpController.GetApplicativeProfileList then any
                | modifications to this object will change an existing or new profile's values
                | directly.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def conveyor(self) -> OLPController:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Conveyor() As OlpController
                |     The conveyor to track.
                | 
                |     The conveyor is always matched. To set the conveyor, retrieve it from the
                |     OlpResourceControlDevice temporary interface
                |     OlpObjectAccess.
                |     Dim ControlDev As OlpResourceControlDevice = TranslatorHelper.ResourceControlDevice
                |     Dim ControlDevTmp as OlpObjectAccess = ControlDev
                |     Dim ID As Object() = {"CNV1","Conveyor"}
                |     Dim returnarray() As Object = ControlDev.GetProperty("DeviceByID", params)(0)
                |     Dim conveyor As OlpController = returnarray(0)
                |     profile.Conveyor = conveyor

        :return: OLPController
        """

        return OLPController(self.com_object.Conveyor)

    @conveyor.setter
    def conveyor(self, value: OLPController):
        """
        :param OLPController value:
        """

        self.com_object.Conveyor = value

    @property
    def inbound_offset_constant(self) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InboundOffsetConstant() As OlpVariable (Read Only)
                |     The constant that can be used in expressions in the task.

        :return: OLPVariable
        """

        return OLPVariable(self.com_object.InboundOffsetConstant)

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mode() As DELOlpConveyorTrackingMode
                |     The tracking mode.
                | 
                |     The mode is always matched. If not set, rail tracking will be used if the
                |     robot is on a rail. Otherwise, line tracking will be used.

        :return: DELOlpConveyorTrackingMode
        """

        return self.com_object.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mode = value

    @property
    def rail_device(self) -> OLPController:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RailDevice() As OlpController
                |     Get/Set the rail device that is tracking the conveyor.
                |     This is NULL if not rail tracking.

        :return: OLPController
        """

        return OLPController(self.com_object.RailDevice)

    @rail_device.setter
    def rail_device(self, value: OLPController):
        """
        :param OLPController value:
        """

        self.com_object.RailDevice = value

    @property
    def rail_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RailDirection() As short (Read Only)
                |     Get the rail direction relative to the conveyor for rail tracking
                |     scenarios.
                | 
                |     Returns:
                |         1 if same as conveyor -1 if opposite of conveyor

        :return: int
        """

        return self.com_object.RailDirection

    def get_inbound_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInboundOffset() As double
                |     Get the inbound conveyor position.
                |     This is the conveyor position that the robot will wait for before starting
                |     the next move. A conveyor wait instruction will reference this value as a
                |     variable.
                | 
                |     Returns:
                |         The conveyor position (in meters) relative to the conveyor zero
                |         position (referential).

        :return: float
        """
        return self.com_object.GetInboundOffset()

    def get_outbound_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOutboundOffset() As double
                |     Get the outbound conveyor position.
                |     This is the conveyor position that will cause the robot to stop tracking
                |     because the part has moved too far down the conveyor. (not currently used in
                |     simulation)
                | 
                |     Returns:
                |         The conveyor position (in meters) relative to the conveyor zero
                |         position (referential).

        :return: float
        """
        return self.com_object.GetOutboundOffset()

    def get_rail_joint_number(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRailJointNumber() As short
                |     Get the joint number of the rail used to track the
                |     conveyor.
                |     This is the joint number of the rail device, not the joint number in the
                |     motion group. For example if a rail has 2 command joints and is an aux device
                |     of the robot in the same motion group as the robot, 1 or 2 are valid values of
                |     the joint number (NOT 7 or 8). This value is only valid if mode is set to rail
                |     tracking.
                | 
                |     Returns:
                |         The joint number.

        :return: int
        """
        return self.com_object.GetRailJointNumber()

    def set_inbound_offset(self, i_offset: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInboundOffset(double iOffset,boolean iMatch)
                |     Set the inbound conveyor position.
                |     This is the conveyor position that the robot will wait for before starting
                |     the next move. A conveyor wait instruction will reference this value as a
                |     variable.
                | 
                |     Parameters:
                | 
                |         iOffset
                |             The conveyor position (in meters) relative to the conveyor zero
                |             position (referential). 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_offset:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetInboundOffset(i_offset, i_match)

    def set_outbound_offset(self, i_offset: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOutboundOffset(double iOffset,boolean iMatch)
                |     Set the outbound conveyor position.
                |     This is the conveyor position that will cause the robot to stop tracking
                |     because the part has moved too far down the conveyor. (not currently used in
                |     simulation)
                | 
                |     Parameters:
                | 
                |         iOffset
                |             The conveyor position (in meters) relative to the conveyor zero
                |             position (referential). 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param float i_offset:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetOutboundOffset(i_offset, i_match)

    def set_rail_joint_number(self, i_joint_number: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRailJointNumber(short iJointNumber,boolean iMatch)
                |     Set the joint number of the rail used to track the
                |     conveyor.
                |     This is the joint number of the rail device, not the joint number in the
                |     motion group. For example if a rail has 2 command joints and is an aux device
                |     of the robot in the same motion group as the robot, 1 or 2 are valid values of
                |     the joint number (NOT 7 or 8). This value is only valid if mode is set to rail
                |     tracking.
                | 
                |     Parameters:
                | 
                |         iJointNumber
                |             The value. 
                |         iMatch
                |             If TRUE use value to find existing profile. 

        :param int i_joint_number:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetRailJointNumber(i_joint_number, i_match)

    def __repr__(self):
        return f'OLPConveyorTrackingProfile(name="{ self.name }")'
