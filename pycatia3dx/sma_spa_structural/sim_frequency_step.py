"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.sma_spa_structural.sim_ams_eigensolver import SimAmsEigensolver
from pycatia3dx.sma_spa_structural.sim_analysis_restart_step_property import SimAnalysisRestartStepProperty
from pycatia3dx.sma_spa_structural.sim_lanczos_eigensolver import SimLanczosEigensolver


class SimFrequencyStep(SimStep):

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
                |                         SimFrequencyStep
                | 
                | Represents the Frequency Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimFrequencyStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyFrequencyStep As SimFrequencyStep
                |      Set MyFrequencyStep = MySteps.Add("SimFrequencyStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimFrequencyStep named
                |     "Frequency Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyFrequencyStep As SimFrequencyStep
                |      Set MyFrequencyStep = MySteps.Item("Frequency Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimFrequencyStep as
                |     following:
                | 
                |      ...
                |      myFrequencyStep = mySteps.Add("SimFrequencyStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimFrequencyStep named
                |     "Frequency Step.1" as following:
                | 
                |      ...
                |      myFrequencyStep = mySteps.Item("Frequency Step.1")
                |      
                | 
                | See also:
                |     SimSteps
                | See also:
                |     SimAnalysisRestartStepProperty
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def ams_solver(self) -> SimAmsEigensolver:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AMSSolver() As SimAMSEigensolver (Read Only)
                |     Returns the AMS solver.

        :return: SimAmsEigensolver
        """

        return SimAmsEigensolver(self.com_object.AMSSolver)

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
    def lanczos_solver(self) -> SimLanczosEigensolver:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LanczosSolver() As SimLanczosEigensolver (Read Only)
                |     Returns the Lanczos solver.

        :return: SimLanczosEigensolver
        """

        return SimLanczosEigensolver(self.com_object.LanczosSolver)

    @property
    def restart_step_property(self) -> SimAnalysisRestartStepProperty:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RestartStepProperty() As SimAnalysisRestartStepProperty (Read
                | Only)
                |     Returns the restart step property for the frequency step.

        :return: SimAnalysisRestartStepProperty
        """

        return SimAnalysisRestartStepProperty(self.com_object.RestartStepProperty)

    @property
    def solver_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SolverType() As SimFrequencyStepSolverType
                |     Returns or sets the solver type. 

        :return: SimFrequencyStepSolverType
        """

        return self.com_object.SolverType

    @solver_type.setter
    def solver_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SolverType = value

    def __repr__(self):
        return f'SimFrequencyStep(name="{ self.name }")'
