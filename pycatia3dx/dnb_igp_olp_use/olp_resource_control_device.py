"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_controller import OLPController
from pycatia3dx.dnb_igp_olp_use.olp_gun import OLPGun
from pycatia3dx.dnb_igp_olp_use.olp_motion_groups import OLPMotionGroups
from pycatia3dx.types.general import CATVariant


class OLPResourceControlDevice(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpResourceControlDevice
                | 
                | Interface for accessing a resource control device properties.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved from a OlpTranslatorHelper.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def controller_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ControllerType() As CATBSTR
                |     The controller type. (e.g. MOTOMAN DX100)

        :return: str
        """

        return self.com_object.ControllerType

    @controller_type.setter
    def controller_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.ControllerType = value

    @property
    def guns(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Guns() As CATSafeArrayVariant (Read Only)
                |     All Guns.
                |     Each item in the list is a OlpGun.

        :return: tuple
        """

        return self.com_object.Guns

    @property
    def motion_groups(self) -> OLPMotionGroups:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionGroups() As OlpMotionGroups (Read Only)
                |     The motion groups.

        :return: OLPMotionGroups
        """

        return OLPMotionGroups(self.com_object.MotionGroups)

    @property
    def origin_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OriginType() As DELOlpPositionRef
                |     Get/Set the robot's origin type.
                | 
                |     The origin is the reference frame used for stationary object frames and
                |     tool profiles. Valid values are
                | 
                |         delOlpStation - World Cell origin.
                |         delOlpRailOrigin - Robot Base when all Rail axes are at 0. This is for
                |         integrated rail scenarios.
                |         delOlpRobotBase - Robot Base, wherever it is currently located. This is
                |         for a non-integrated rail, external rail, AGV scenarios
                |         etc..
                |         delOlpUserDefined - Any other location, the origin can be attached to
                |         something if the device is being moved by an AGV for
                |         example.
                | 
                |     If the robot is stationary and has no rail axis, delOlpRobotBase and
                |     delOlpRailOrigin are equivalent. In case of delOlpUserOrigin you can get/set
                |     location of the origin by using OlpController.GetBaseLocation and
                |     OlpController.SetBaseLocation. When setting this value, the same origin type
                |     will apply to all robots in the control device. delOlpWorld, delOlpMount, and
                |     delOlpUnknown are not valid origins. During upload, the OriginType set is
                |     ignored if update device parameters has been unchecked by the
                |     user.

        :return: DELOlpPositionRef
        """

        return self.com_object.OriginType

    @origin_type.setter
    def origin_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.OriginType = value

    def get_device_by_id(self, i_id: str, i_type: str) -> OLPController:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDeviceByID(CATBSTR iID,CATBSTR iType) As OlpController
                |     Get a device using its ID.
                | 
                |     Parameters:
                | 
                |         iID
                |             The native robot language ID from OlpController.DeviceID of this
                |             device set in the device mapping tab. 
                |         iType
                |             The type of this device (robot, rail, etc.) 
                | 
                |     Returns:
                |         The device

        :param str i_id:
        :param str i_type:
        :return: OLPController
        """
        return OLPController(self.com_object.GetDeviceByID(i_id, i_type))

    def get_gun_by_id(self, i_id: str, i_type: str) -> OLPGun:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGunByID(CATBSTR iID,CATBSTR iType) As OlpGun
                |     Get a gun using its ID.
                | 
                |     Parameters:
                | 
                |         iID
                |             The gun ID from OlpGun.Index of this gun set in the device mapping
                |             tab. 
                |         iType
                |             The OlpGun.Type of this gun (e.g. "SpotWeld", "Paint", etc).
                |             
                | 
                |     Returns:
                |         The device

        :param str i_id:
        :param str i_type:
        :return: OLPGun
        """
        return OLPGun(self.com_object.GetGunByID(i_id, i_type))

    def get_parameter(self, i_profile_type: str, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameter(CATBSTR iProfileType,CATBSTR iParameterName) As
                | CATVariant
                |     Get applicative profile parameter value directly on the control
                |     device.
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
        return self.com_object.GetParameter(i_profile_type, i_parameter_name)

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

    #todo: what is DELMIAOlpRobotTeam?
    def get_robot_team(self) -> DELMIAOlpRobotTeam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRobotTeam() As DELMIAOlpRobotTeam
                |     Get the robot team.
                | 
                |     Returns:
                |         The robot team retrieved.

        :return: DELMIAOlpRobotTeam
        """
        return DELMIAOlpRobotTeam(self.com_object.GetRobotTeam())

    def set_parameter(self, i_profile_type: str, i_parameter_name: str, i_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParameter(CATBSTR iProfileType,CATBSTR iParameterName,CATVariant
                | iValue)
                |     Set applicative profile parameter value directly on the control
                |     device.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iParameterName
                |             The parameter name 
                |         iValue
                |             The parameter value. 

        :param str i_profile_type:
        :param str i_parameter_name:
        :param CATVariant i_value:
        :return: None
        """
        return self.com_object.SetParameter(i_profile_type, i_parameter_name, i_value)

    def __repr__(self):
        return f'OLPResourceControlDevice(name="{ self.name }")'
