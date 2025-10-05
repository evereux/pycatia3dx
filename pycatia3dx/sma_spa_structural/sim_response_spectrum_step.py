"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.sma_spa_structural.sim_spectrum import SimSpectrum


class SimResponseSpectrumStep(SimStep):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaFoundationIDLItf.SimStep
                |                         SimResponseSpectrumStep
                | 
                | Represents the Response Spectrum Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimResponseSpectrumStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyResponseSpectrumStep As SimResponseSpectrumStep
                |      Set MyResponseSpectrumStep = MySteps.Add("SimResponseSpectrumStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimResponseSpectrumStep named
                |     "Response Spectrum Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyResponseSpectrumStep As SimResponseSpectrumStep
                |      Set MyResponseSpectrumStep = MySteps.Item("Response Spectrum Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimResponseSpectrumStep
                |     as following:
                | 
                |      ...
                |      myResponseSpectrumStep = mySteps.Add("SimResponseSpectrumStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimResponseSpectrumStep
                |     named "Response Spectrum Step.1" as following:
                | 
                |      ...
                |      myResponseSpectrumStep = mySteps.Item("Response Spectrum Step.1")
                |      
                | 
                | See also:
                |     SimSteps
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activated() As boolean
                |     Returns or sets the activation status.

        :return: bool
        """

        return self.com_object.Activated

    @activated.setter
    def activated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activated = value

    @property
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def damping_definition(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DampingDefinition() As
                | SimResponseSpectrumStepDampingDefinition
                |     Returns or sets the damping definition.

        :return: SimResponseSpectrumStepDampingDefinition
        """

        return self.com_object.DampingDefinition

    @damping_definition.setter
    def damping_definition(self, value: int):
        """
        :param int value:
        """

        self.com_object.DampingDefinition = value

    @property
    def directional_summation_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DirectionalSummationMethod() As
                | SimResponseSpectrumStepDirectionalSummationMethod
                |     Returns or sets the directional summation method.

        :return: SimResponseSpectrumStepDirectionalSummationMethod
        """

        return self.com_object.DirectionalSummationMethod

    @directional_summation_method.setter
    def directional_summation_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.DirectionalSummationMethod = value

    @property
    def missing_mass_method_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MissingMassMethodFlag() As boolean
                |     Returns or sets the missing mass method flag.
                |     TRUE: the missing mass method is used.
                |     FALSE: the missing mass method is not used.

        :return: bool
        """

        return self.com_object.MissingMassMethodFlag

    @missing_mass_method_flag.setter
    def missing_mass_method_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MissingMassMethodFlag = value

    @property
    def modal_summation_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ModalSummationMethod() As
                | SimResponseSpectrumStepModalSummationMethod
                |     Returns or sets the modal summation method.

        :return: SimResponseSpectrumStepModalSummationMethod
        """

        return self.com_object.ModalSummationMethod

    @modal_summation_method.setter
    def modal_summation_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.ModalSummationMethod = value

    @property
    def rigid_response_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RigidResponseMethod() As
                | SimResponseSpectrumStepRigidResponseMethod
                |     Returns or sets the rigid response method.

        :return: SimResponseSpectrumStepRigidResponseMethod
        """

        return self.com_object.RigidResponseMethod

    @rigid_response_method.setter
    def rigid_response_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.RigidResponseMethod = value

    def get_align_axis(self, i_direction_type: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAlignAxis(SimResponseSpectrumStepDirectionType iDirectionType) As
                | SimResponseSpectrumStepAlignAxisType
                |     Retrieves the axis used to align the data of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                | 
                |     Returns:
                |         The axis to align with.

        :param int i_direction_type:
        :return: int
        """
        return self.com_object.GetAlignAxis(i_direction_type)

    def get_apply_directional_spectrum_flag(self, i_direction_type: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetApplyDirectionalSpectrumFlag(SimResponseSpectrumStepDirectionType
                | iDirectionType) As boolean
                |     Retrieves the flag used to determine if spectrum data is applied in a given
                |     direction. Only applicable for second and third direction.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                | 
                |     Returns:
                |         TRUE: the spectrum data is applied.
                |         FALSE: the spectrum data is not applied.

        :param int i_direction_type:
        :return: bool
        """
        return self.com_object.GetApplyDirectionalSpectrumFlag(i_direction_type)

    def get_cut_off_frequency(self, i_direction_type: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCutOffFrequency(SimResponseSpectrumStepDirectionType iDirectionType) As
                | double
                |     Retrieves the cut-off frequency of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                | 
                |     Returns:
                |         Frequency value. Quantity: FREQUENCY, Units: Hz.

        :param int i_direction_type:
        :return: float
        """
        return self.com_object.GetCutOffFrequency(i_direction_type)

    def get_periodic_region_frequency(self, i_direction_type: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPeriodicRegionFrequency(SimResponseSpectrumStepDirectionType
                | iDirectionType) As double
                |     Retrieves the periodic region frequency of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                | 
                |     Returns:
                |         Frequency value. Quantity: FREQUENCY, Units: Hz.

        :param int i_direction_type:
        :return: float
        """
        return self.com_object.GetPeriodicRegionFrequency(i_direction_type)

    def get_rigid_region_frequency(self, i_direction_type: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRigidRegionFrequency(SimResponseSpectrumStepDirectionType
                | iDirectionType) As double
                |     Retrieves the rigid region frequency of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                | 
                |     Returns:
                |         Frequency value. Quantity: FREQUENCY, Units: Hz.

        :param int i_direction_type:
        :return: float
        """
        return self.com_object.GetRigidRegionFrequency(i_direction_type)

    def get_scale_factor(self, i_direction_type: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetScaleFactor(SimResponseSpectrumStepDirectionType iDirectionType) As
                | double
                |     Retrieves the scale factor of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                | 
                |     Returns:
                |         Scale factor value. Quantity: DIMENSIONLESS, Units: None.

        :param int i_direction_type:
        :return: float
        """
        return self.com_object.GetScaleFactor(i_direction_type)

    def get_spectrum(self, i_direction_type: int) -> SimSpectrum:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSpectrum(SimResponseSpectrumStepDirectionType iDirectionType) As
                | SimSpectrum
                |     Retrieves the response spectrum in a specific direction.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                | 
                |     Returns:
                |         The spectrum.

        :param int i_direction_type:
        :return: SimSpectrum
        """
        return SimSpectrum(self.com_object.GetSpectrum(i_direction_type))

    def get_time_duration(self, i_direction_type: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTimeDuration(SimResponseSpectrumStepDirectionType iDirectionType) As
                | double
                |     Retrieves the time duration of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                | 
                |     Returns:
                |         Time duration value. Quantity: TIME, Units: s.

        :param int i_direction_type:
        :return: float
        """
        return self.com_object.GetTimeDuration(i_direction_type)

    def set_align_axis(self, i_direction_type: int, i_align_axis: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAlignAxis(SimResponseSpectrumStepDirectionType
                | iDirectionType,SimResponseSpectrumStepAlignAxisType
                | iAlignAxis)
                |     Sets the axis used to align the data of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                |         iAlignAxis[in]
                |             The axis to align with.

        :param int i_direction_type:
        :param int i_align_axis:
        :return: None
        """
        return self.com_object.SetAlignAxis(i_direction_type, i_align_axis)

    def set_apply_directional_spectrum_flag(self, i_direction_type: int, i_apply_spectrum: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApplyDirectionalSpectrumFlag(SimResponseSpectrumStepDirectionType
                | iDirectionType,boolean iApplySpectrum)
                |     Sets the flag used to determine if spectrum data is applied in a given
                |     direction. Only applicable for second and third direction.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                |         iApplySpectrum[in]
                |             TRUE: the spectrum data is applied.
                |             FALSE: the spectrum data is not applied.

        :param int i_direction_type:
        :param bool i_apply_spectrum:
        :return: None
        """
        return self.com_object.SetApplyDirectionalSpectrumFlag(i_direction_type, i_apply_spectrum)

    def set_cut_off_frequency(self, i_direction_type: int, i_frequency: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCutOffFrequency(SimResponseSpectrumStepDirectionType
                | iDirectionType,double iFrequency)
                |     Sets the cut-off frequency of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                |         iFrequency[in]
                |             Frequency value. Quantity: FREQUENCY, Units: Hz.

        :param int i_direction_type:
        :param float i_frequency:
        :return: None
        """
        return self.com_object.SetCutOffFrequency(i_direction_type, i_frequency)

    def set_periodic_region_frequency(self, i_direction_type: int, i_frequency: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPeriodicRegionFrequency(SimResponseSpectrumStepDirectionType
                | iDirectionType,double iFrequency)
                |     Sets the periodic region frequency of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                |         iFrequency[in]
                |             Frequency value. Quantity: FREQUENCY, Units: Hz.

        :param int i_direction_type:
        :param float i_frequency:
        :return: None
        """
        return self.com_object.SetPeriodicRegionFrequency(i_direction_type, i_frequency)

    def set_rigid_region_frequency(self, i_direction_type: int, i_frequency: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRigidRegionFrequency(SimResponseSpectrumStepDirectionType
                | iDirectionType,double iFrequency)
                |     Sets the rigid region frequency of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                |         iFrequency[in]
                |             Frequency value. Quantity: FREQUENCY, Units: Hz.

        :param int i_direction_type:
        :param float i_frequency:
        :return: None
        """
        return self.com_object.SetRigidRegionFrequency(i_direction_type, i_frequency)

    def set_scale_factor(self, i_direction_type: int, i_scale_factor: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetScaleFactor(SimResponseSpectrumStepDirectionType iDirectionType,double
                | iScaleFactor)
                |     Sets the scale factor of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                |         iScaleFactor[in]
                |             Scale factor value. Quantity: DIMENSIONLESS, Units: None.

        :param int i_direction_type:
        :param float i_scale_factor:
        :return: None
        """
        return self.com_object.SetScaleFactor(i_direction_type, i_scale_factor)

    def set_spectrum(self, i_direction_type: int, i_spectrum: SimSpectrum) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSpectrum(SimResponseSpectrumStepDirectionType iDirectionType,SimSpectrum
                | iSpectrum)
                |     Sets the response spectrum in a specific direction.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                |         ispSpectrum[in]
                |             The spectrum.

        :param int i_direction_type:
        :param SimSpectrum i_spectrum:
        :return: None
        """
        return self.com_object.SetSpectrum(i_direction_type, i_spectrum.com_object)

    def set_time_duration(self, i_direction_type: int, i_time_duration: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTimeDuration(SimResponseSpectrumStepDirectionType iDirectionType,double
                | iTimeDuration)
                |     Sets the time duration of a spectrum.
                | 
                |     Parameters:
                | 
                |         iDirectionType[in]
                |             The spectrum direction. 
                |         iTimeDuration[in]
                |             Time duration value. Quantity: TIME, Units: s. 

        :param int i_direction_type:
        :param float i_time_duration:
        :return: None
        """
        return self.com_object.SetTimeDuration(i_direction_type, i_time_duration)

    def __repr__(self):
        return f'SimResponseSpectrumStep(name="{ self.name }")'
