"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_controller import OLPController


class OLPMotionGroup(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpMotionGroup
                |
                | A motion group.
                |
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | A motion group is a list of devices that have a single Cartesian or joint
                | target in a robot motion.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def has_robot(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HasRobot() As boolean (Read Only)
                |     Indicates if this motion group contains a robot.

        :return: bool
        """

        return self.com_object.HasRobot

    @property
    def index(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Index() As long (Read Only)
                |     Get the motion group index.
                |     In some robot languages an index is used to identify the motion group. If
                |     the Index property is not set (IndexIsSet returns FALSE), then getting the
                |     Index will fail.

        :return: int
        """

        return self.com_object.Index

    @property
    def index_set(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IndexSet() As boolean (Read Only)
                |     Get whether an index is set for the motion group.
                |     If not set, then getting the Index property will fail.

        :return: bool
        """

        return self.com_object.IndexSet

    @property
    def primary_device(self) -> OLPController:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PrimaryDevice() As OlpController (Read Only)
                |     The main devices in the motion group.
                |     If there is a robot in the motion group, this is the robot.

        :return: OLPController
        """

        return OLPController(self.com_object.PrimaryDevice)

    def get_devices(self, i_type: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDevices(DELOlpDeviceType iType) As CATSafeArrayVariant
                |     Retrieve devices from the motion group.
                |
                |     Parameters:
                |
                |         iType
                |             This filters the list of devices returned.
                |
                |     Returns:
                |         The list of devices. Each object in this array implements
                |         OlpController.

        :param int i_type:
        :return: tuple
        """
        return self.com_object.GetDevices(i_type)

    def __repr__(self):
        return f'OLPMotionGroup(name="{ self.name }")'
