"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.system.any_object import AnyObject


class SimOrientation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimOrientation
                | 
                | Represents the Orientation object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle_of_rotation(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngleOfRotation() As double
                |     Returns or sets the angle of rotation. Quantity: ANGLE, units: Degree

        :return: float
        """

        return self.com_object.AngleOfRotation

    @angle_of_rotation.setter
    def angle_of_rotation(self, value: float):
        """
        :param float value:
        """

        self.com_object.AngleOfRotation = value

    @property
    def axis_of_rotation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisOfRotation() As SimOrientationAxisOfRotation
                |     Returns or sets the axis of rotation.

        :return: int
        """

        return self.com_object.AxisOfRotation

    @axis_of_rotation.setter
    def axis_of_rotation(self, value: int):
        """
        :param int value:
        """

        self.com_object.AxisOfRotation = value

    @property
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system used for the mass.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def orientation_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientationFlag() As boolean
                |     Returns or sets the flag that determines if the orientation is
                |     enabled.
                | 
                |     TRUE: the orientation is enabled.
                | 
                |     FALSE: the orientation is not enabled. 

        :return: bool
        """

        return self.com_object.OrientationFlag

    @orientation_flag.setter
    def orientation_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.OrientationFlag = value

    def __repr__(self):
        return f'SimOrientation(name="{ self.name }")'
