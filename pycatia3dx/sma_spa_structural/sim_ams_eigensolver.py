"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimAmsEigensolver(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAMSEigensolver
                | 
                | Represents the A M S Eigensolver object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def acoustic_coupling_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AcousticCouplingType() As
                | SimAMSEigensolverAcousticCouplingType
                |     Returns or sets the acoustic coupling type.

        :return: int
        """

        return self.com_object.AcousticCouplingType

    @acoustic_coupling_type.setter
    def acoustic_coupling_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.AcousticCouplingType = value

    @property
    def damping_projection_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DampingProjectionFlag() As boolean
                |     Returns or sets the flag that determines if the damping projection option
                |     is used.
                |     TRUE : the damping projection option is used.
                |     FALSE : the damping projection option is not used.

        :return: bool
        """

        return self.com_object.DampingProjectionFlag

    @damping_projection_flag.setter
    def damping_projection_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DampingProjectionFlag = value

    @property
    def maximum_frequency(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumFrequency() As double
                |     Returns or sets the maximum frequency. Quantity: FREQUENCY, units: Hz.

        :return: float
        """

        return self.com_object.MaximumFrequency

    @maximum_frequency.setter
    def maximum_frequency(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumFrequency = value

    @property
    def minimum_frequency(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumFrequency() As double
                |     Returns or sets the minimum frequency. Quantity: FREQUENCY, units: Hz.

        :return: float
        """

        return self.com_object.MinimumFrequency

    @minimum_frequency.setter
    def minimum_frequency(self, value: float):
        """
        :param float value:
        """

        self.com_object.MinimumFrequency = value

    @property
    def minimum_frequency_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumFrequencyFlag() As boolean
                |     Returns or sets the flag that determines if the minimum frequency is
                |     specified.
                |     TRUE : the minimum frequency is specified.
                |     FALSE : the minimum frequency is not specified.

        :return: bool
        """

        return self.com_object.MinimumFrequencyFlag

    @minimum_frequency_flag.setter
    def minimum_frequency_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MinimumFrequencyFlag = value

    @property
    def number_of_modes(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfModes() As long
                |     Returns or sets the number of modes.

        :return: int
        """

        return self.com_object.NumberOfModes

    @number_of_modes.setter
    def number_of_modes(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfModes = value

    @property
    def residual_modes_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ResidualModesFlag() As boolean
                |     Returns or sets the flag that determines if the residual modes option is
                |     used.
                |     TRUE : the residual modes option is used.
                |     FALSE : the residual modes option is not used.

        :return: bool
        """

        return self.com_object.ResidualModesFlag

    @residual_modes_flag.setter
    def residual_modes_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ResidualModesFlag = value

    @property
    def specified_modes_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecifiedModesFlag() As boolean
                |     Returns or sets the flag that determines if the number of eigenvalues to be
                |     calculated is specified.
                |     TRUE : the number of eigenvalues to be calculated is specified.
                |     FALSE : all the eigenvalues from the minimum frequency of interest up to the maximum frequency of interest will be calculated. 

        :return: bool
        """

        return self.com_object.SpecifiedModesFlag

    @specified_modes_flag.setter
    def specified_modes_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SpecifiedModesFlag = value

    def __repr__(self):
        return f'SimAmsEigensolver(name="{ self.name }")'
