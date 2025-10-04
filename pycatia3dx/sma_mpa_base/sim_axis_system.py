"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_base.sim_math_axis import SimMathAxis


class SimAxisSystem(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAxisSystem
                | 
                | Represents the Axis System object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis_system(self) -> SimMathAxis:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimMathAxis
                |     Returns or sets the axis system.

        :return: SimMathAxis
        """

        return SimMathAxis(self.com_object.AxisSystem)

    @axis_system.setter
    def axis_system(self, value: SimMathAxis):
        """
        :param SimMathAxis value:
        """

        self.com_object.AxisSystem = value

    @property
    def coordinate_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CoordinateType() As SimAxisSystemCoordinateType
                |     Returns or sets the type of axis being used.

        :return: int
        """

        return self.com_object.CoordinateType

    @coordinate_type.setter
    def coordinate_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.CoordinateType = value

    @property
    def definition_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DefinitionMode() As SimAxisSystemDefinitionMode
                |     Returns or sets the axis definition mode.

        :return: int
        """

        return self.com_object.DefinitionMode

    @definition_mode.setter
    def definition_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.DefinitionMode = value

    @property
    def local_axis_system(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LocalAxisSystem(AnyObject iAxis) (Write Only)
                |     Sets the axis system. This method will fail in case the axis system
                |     definition mode is not SimAxisSystemLocal. 

        :return: bool
        """

        return self.com_object.LocalAxisSystem

    @local_axis_system.setter
    def local_axis_system(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.LocalAxisSystem = value

    def __repr__(self):
        return f'SimAxisSystem(name="{ self.name }")'
