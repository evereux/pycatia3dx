"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep


class SimTransientHeatTransferStep(SimStep):

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
                |                         SimTransientHeatTransferStep
                | 
                | Represents the Transient Heat Transfer Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimTransientHeatTransferStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyTransientHeatTransferStep As
                |      SimTransientHeatTransferStep
                |      Set MyTransientHeatTransferStep = MySteps.Add("SimTransientHeatTransferStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimTransientHeatTransferStep
                |     named "Transient Heat Transfer Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyTransientHeatTransferStep As
                |      SimTransientHeatTransferStep
                |      Set MyTransientHeatTransferStep = MySteps.Item("Transient Heat Transfer Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a
                |     SimTransientHeatTransferStep as following:
                | 
                |      ...
                |      myTransientHeatTransferStep = mySteps.Add("SimTransientHeatTransferStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a
                |     SimTransientHeatTransferStep named "Transient Heat Transfer Step.1" as
                |     following:
                | 
                |      ...
                |      myTransientHeatTransferStep = mySteps.Item("Transient Heat Transfer Step.1")
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
    def end_at_steady_state_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndAtSteadyStateFlag() As boolean
                |     Returns or sets the flag that determines if the step ends when steady state
                |     is reached.
                |     TRUE: the step ends when steady state is reached.
                |     FALSE: the step does not end when steady state is reached.

        :return: bool
        """

        return self.com_object.EndAtSteadyStateFlag

    @end_at_steady_state_flag.setter
    def end_at_steady_state_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.EndAtSteadyStateFlag = value

    @property
    def initial_time_step(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialTimeStep() As double
                |     Returns or sets the initial time step. Quantity: TIME, units: s

        :return: float
        """

        return self.com_object.InitialTimeStep

    @initial_time_step.setter
    def initial_time_step(self, value: float):
        """
        :param float value:
        """

        self.com_object.InitialTimeStep = value

    @property
    def maximum_emissivity_change(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumEmissivityChange() As double
                |     Maximum emissivity change value. Quantity: Real, units: None

        :return: float
        """

        return self.com_object.MaximumEmissivityChange

    @maximum_emissivity_change.setter
    def maximum_emissivity_change(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumEmissivityChange = value

    @property
    def maximum_number_of_increments(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumNumberOfIncrements() As long
                |     Returns or sets the maximum number of increments. Quantity: Integer, units:
                |     None

        :return: int
        """

        return self.com_object.MaximumNumberOfIncrements

    @maximum_number_of_increments.setter
    def maximum_number_of_increments(self, value: int):
        """
        :param int value:
        """

        self.com_object.MaximumNumberOfIncrements = value

    @property
    def maximum_temperature_change(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumTemperatureChange() As double
                |     Maximum temperature change per increments value. Quantity:
                |     TEMPERATUREDIFFERENCE, units: Kdeg

        :return: float
        """

        return self.com_object.MaximumTemperatureChange

    @maximum_temperature_change.setter
    def maximum_temperature_change(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumTemperatureChange = value

    @property
    def maximum_time_step(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumTimeStep() As double
                |     Returns or sets the maximum time step. Quantity: TIME, units: s

        :return: float
        """

        return self.com_object.MaximumTimeStep

    @maximum_time_step.setter
    def maximum_time_step(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumTimeStep = value

    @property
    def minimum_time_step(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumTimeStep() As double
                |     Returns or sets the minimum time step. Quantity: TIME, units: s

        :return: float
        """

        return self.com_object.MinimumTimeStep

    @minimum_time_step.setter
    def minimum_time_step(self, value: float):
        """
        :param float value:
        """

        self.com_object.MinimumTimeStep = value

    @property
    def steady_state_temperature_change_rate(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SteadyStateTemperatureChangeRate() As double
                |     Maximum temperature change rate for steady state value. Quantity:
                |     TEMPERATURESLOPE, units: Kdeg_s

        :return: float
        """

        return self.com_object.SteadyStateTemperatureChangeRate

    @steady_state_temperature_change_rate.setter
    def steady_state_temperature_change_rate(self, value: float):
        """
        :param float value:
        """

        self.com_object.SteadyStateTemperatureChangeRate = value

    @property
    def time_incrementation_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeIncrementationScheme() As
                | SimTimeIncrementationScheme
                |     Returns or sets the incrementation scheme.

        :return: SimTimeIncrementationScheme
        """

        return self.com_object.TimeIncrementationScheme

    @time_incrementation_scheme.setter
    def time_incrementation_scheme(self, value: int):
        """
        :param int value:
        """

        self.com_object.TimeIncrementationScheme = value

    @property
    def total_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TotalTime() As double
                |     Returns or sets the total time. Quantity: TIME, units: s 

        :return: float
        """

        return self.com_object.TotalTime

    @total_time.setter
    def total_time(self, value: float):
        """
        :param float value:
        """

        self.com_object.TotalTime = value

    def __repr__(self):
        return f'SimTransientHeatTransferStep(name="{ self.name }")'
