"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimStabilization(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimStabilization
                | 
                | Represents the Stabilization object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def adaptive_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdaptiveFlag() As boolean
                |     Returns or sets the flag that determines if the adaptive automatic
                |     stabilization is applied.
                | 
                |     TRUE: the adaptive automatic stabilization is applied.
                | 
                |     FALSE: the adaptive automatic stabilization is not applied.

        :return: bool
        """

        return self.com_object.AdaptiveFlag

    @adaptive_flag.setter
    def adaptive_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AdaptiveFlag = value

    @property
    def damping_factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DampingFactor() As double
                |     Returns or sets the stabilization damping factor. Quantity: Real, units:
                |     None.

        :return: float
        """

        return self.com_object.DampingFactor

    @damping_factor.setter
    def damping_factor(self, value: float):
        """
        :param float value:
        """

        self.com_object.DampingFactor = value

    @property
    def energy_fraction(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EnergyFraction() As double
                |     Returns or sets the stabilization energy fraction. Quantity: Real, units:
                |     None.

        :return: float
        """

        return self.com_object.EnergyFraction

    @energy_fraction.setter
    def energy_fraction(self, value: float):
        """
        :param float value:
        """

        self.com_object.EnergyFraction = value

    @property
    def energy_ratio_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EnergyRatioTolerance() As double
                |     Returns or sets the stabilization energy ratio tolerance. Quantity: Real,
                |     units: None.

        :return: float
        """

        return self.com_object.EnergyRatioTolerance

    @energy_ratio_tolerance.setter
    def energy_ratio_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.EnergyRatioTolerance = value

    @property
    def stabilization_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StabilizationType() As
                | SimStabilizationStabilizationType
                |     Returns or sets the stabilization type. 

        :return: SimStabilizationStabilizationType
        """

        return self.com_object.StabilizationType

    @stabilization_type.setter
    def stabilization_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.StabilizationType = value

    def __repr__(self):
        return f'SimStabilization(name="{ self.name }")'
