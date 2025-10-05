"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_linear_load_cases import SimLinearLoadCases
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep


class SimStaticPerturbationStep(SimStep):

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
                |                         SimStaticPerturbationStep
                | 
                | Represents the Static Perturbation Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimStaticPerturbationStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyStaticPerturbationStep As SimStaticPerturbationStep
                |      Set MyStaticPerturbationStep = MySteps.Add("SimStaticPerturbationStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimStaticPerturbationStep named
                |     "Static Perturbation Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyStaticPerturbationStep As SimStaticPerturbationStep
                |      Set MyStaticPerturbationStep = MySteps.Item("Static Perturbation Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimStaticPerturbationStep
                |     as following:
                | 
                |      ...
                |      myStaticPerturbationStep = mySteps.Add("SimStaticPerturbationStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a
                |     SimStaticPerturbationStep named "Static Perturbation Step.1" as
                |     following:
                | 
                |      ...
                |      myStaticPerturbationStep = mySteps.Item("Static Perturbation Step.1")
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
    def linear_load_cases(self) -> SimLinearLoadCases:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LinearLoadCases() As SimLinearLoadCases (Read Only)
                |     Returns the list of all linear load cases.

        :return: SimLinearLoadCases
        """

        return SimLinearLoadCases(self.com_object.LinearLoadCases)

    @property
    def matrix_storage_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MatrixStorageScheme() As SimMatrixStorageScheme
                |     Returns or sets the matrix storage scheme.

        :return: SimMatrixStorageScheme
        """

        return self.com_object.MatrixStorageScheme

    @matrix_storage_scheme.setter
    def matrix_storage_scheme(self, value: int):
        """
        :param int value:
        """

        self.com_object.MatrixStorageScheme = value

    @property
    def solution_technique(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SolutionTechnique() As
                | SimStaticPerturbationStepSolutionTechnique
                |     Returns or sets the solution technique. 

        :return: SimStaticPerturbationStepSolutionTechnique
        """

        return self.com_object.SolutionTechnique

    @solution_technique.setter
    def solution_technique(self, value: int):
        """
        :param int value:
        """

        self.com_object.SolutionTechnique = value

    def __repr__(self):
        return f'SimStaticPerturbationStep(name="{ self.name }")'
