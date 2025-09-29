"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.kin_mechanism.kin_mechanism import KinMechanism
from pycatia3dx.kin_simulation.kin_recorded_excitation import KinRecordedExcitation
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class KinScenarioSpec(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 KinScenarioSpec
                | 
                | Interface representing a kinematics scenario.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def end_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndTime() As double (Read Only)
                |     Returns the end time of the kinematics scenario.
                | 
                |     Example:
                | 
                |      Dim KinScenario As KinScenarioSpec
                |      ...
                |      Dim EndTime As Double
                |      EndTime = KinScenario.EndTime

        :return: float
        """

        return self.com_object.EndTime

    @property
    def mechanism(self) -> KinMechanism:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mechanism() As KinMechanism (Read Only)
                |     Returns the mechanism of the kinematics scenario.
                | 
                |     Example:
                |         The following example returns the mechanism of a kinematics scenario
                |         :
                | 
                |          Dim KinScenario As KinScenarioSpec
                |          ...
                |          Dim Mechanism  As KinMechanism
                |          Set MyMechanism = KinScenario.Mechanism()

        :return: KinMechanism
        """

        return KinMechanism(self.com_object.Mechanism)

    @property
    def start_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartTime() As double (Read Only)
                |     Returns the start time of the kinematics scenario.
                | 
                |     Example:
                | 
                |      Dim KinScenario As KinScenarioSpec
                |      ...
                |      Dim StartTime As Double
                |      StartTime = KinScenario.StartTime

        :return: float
        """

        return self.com_object.StartTime

    @property
    def time_step(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeStep() As double (Read Only)
                |     Returns the time step of the kinematics scenario.
                | 
                |     Example:
                | 
                |      Dim KinScenario As KinScenarioSpec
                |      ...
                |      Dim TimeStep As Double
                |      TimeStep = KinScenario.TimeStep

        :return: float
        """

        return self.com_object.TimeStep

    def add_recorded_excitation(self) -> KinRecordedExcitation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddRecordedExcitation() As KinRecordedExcitation
                |     Creates and adds a recorded excitation under the kinematics
                |     scenario.
                |     Only one recorded excitation can be created per kinematics scenario. A
                |     second call will return an empty object.
                | 
                |     Example:
                | 
                |      Dim KinScenario As KinScenarioSpec
                |      ...
                |      Dim KinExcitation As KinRecordedExcitation
                |      Set KinExcitation = KinScenario.AddRecordedExcitation

        :return: KinRecordedExcitation
        """
        return KinRecordedExcitation(self.com_object.AddRecordedExcitation())

    def get_recorded_excitation(self) -> KinRecordedExcitation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRecordedExcitation() As KinRecordedExcitation
                |     Gets the recorded Excitation.
                | 
                |     Example:
                | 
                |      Dim KinScenario As KinScenarioSpec
                |      ...
                |      Dim KinExcitation As KinRecordedExcitation
                |      Set KinExcitation = KinScenario.GetRecordedExcitation

        :return: KinRecordedExcitation
        """
        return KinRecordedExcitation(self.com_object.GetRecordedExcitation())

    def remove_recorded_excitation(self, i_recorded_excitation: KinRecordedExcitation) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveRecordedExcitation(KinRecordedExcitation
                | iRecordedExcitation)
                |     Removes the recorded Excitation.
                | 
                |     Example:
                | 
                |      Dim KinScenario As KinScenarioSpec
                |      ...
                |      Dim KinExcitation As KinRecordedExcitation
                |      ...
                |      KinScenario.RemoveRecordedExcitation (KinExcitation)

        :param KinRecordedExcitation i_recorded_excitation:
        :return: None
        """
        return self.com_object.RemoveRecordedExcitation(i_recorded_excitation.com_object)

    def set_time_parameters(self, i_start_time: float, i_end_time: float, i_time_step: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTimeParameters(double iStartTime,double iEndTime,double
                | iTimeStep)
                |     Sets the time parameters of the kinematics scenario. The time parameters
                |     should satisfy the following conditions:
                |     0s <= iStartTime <= iEndTime
                |     0s <= iTimeStep <= (iEndTime - iStartTime)
                | 
                |     Parameters:
                | 
                |         iStartTime
                |             The start time of the scenario 
                |         iEndTime
                |             The end time of the scenario 
                |         iTimeStep
                |             The time step of the scenario
                | 
                |             Example:
                |                 Set the scenario to start at 0s, end at 100s with a time step
                |                 equal to 1s.
                | 
                |                  Dim KinScenario As KinScenarioSpec
                |                  ...
                |                  Call KinScenario.SetTimeParameters(0,100,1)

        :param float i_start_time:
        :param float i_end_time:
        :param float i_time_step:
        :return: None
        """
        return self.com_object.SetTimeParameters(i_start_time, i_end_time, i_time_step)

    def __repr__(self):
        return f'KinScenarioSpec()'
