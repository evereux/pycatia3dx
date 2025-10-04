"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_results.sim_frames_selection import SimFramesSelection


class SimSensorBase(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSensorBase
                | 
                | Represents the Base Sensor.
                | All the sensors are derived from this sensor.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def frame_selector(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrameSelector(SimFramesSelection ispFrameSelector) (Write
                | Only)
                |     Sets the frame selector.

        :return: False
        """

        return SimFramesSelection(self.com_object.SimFramesSe)

    @frame_selector.setter
    def frame_selector(self, value: False):
        """
        :param False value:
        """

        self.com_object.FrameSelector = value

    @property
    def sim_support(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SimSupport(CATSafeArrayVariant icusSupport) (Write
                | Only)
                |     Sets the support for orphan results. The name of the support such as node
                |     set.

        :return: False
        """

        return None

    @sim_support.setter
    def sim_support(self, value: False):
        """
        :param False value:
        """

        self.com_object.SimSupport = value

    @property
    def support(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Support(CATSafeArrayVariant ilsSupport) (Write Only)
                |     Sets the support for native results. Support can be features such as loads,
                |     restraints.

        :return: False
        """

        return None

    @support.setter
    def support(self, value: False):
        """
        :param False value:
        """

        self.com_object.Support = value

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Updates the sensor. It should be called at the end after setting all the
                |     sensor properties and the frame selector.

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'SimSensorBase(name="{ self.name }")'
