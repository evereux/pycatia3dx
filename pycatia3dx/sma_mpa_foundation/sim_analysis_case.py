"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_foundation.sim_features import SimFeatures
from pycatia3dx.sma_mpa_foundation.sim_global_element_type_assignment import SimGlobalElementTypeAssignment
from pycatia3dx.sma_mpa_foundation.sim_local_element_type_assignments import SimLocalElementTypeAssignments
from pycatia3dx.sma_mpa_foundation.sim_steps import SimSteps


class SimAnalysisCase(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAnalysisCase
                | 
                | Represents the Analysis Case object.
                | Base class for structural and thermal analysis case objects.
                | 
                | Example:
                |     Given a SimAnalysisCases collection you can retrieve a SimAnalysisCase
                |     object named as "Structural Analysis Case.1" through the following
                |     code:
                | 
                |      Dim MyAnalysisCases As SimAnalysisCases
                |      ...
                |      Dim MyAnalysisCase As CATBaseDispatch
                |      Set MyAnalysisCase = MyAnalysisCases.Item("Structural Analysis Case.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAnalysisCases collection you can retrieve a SimAnalysisCase
                |     object named as "Structural Analysis Case.1" through the following
                |     code:
                | 
                |      ...
                |      myAnalysisCase = myAnalysisCases.Item("Structural Analysis Case.1")
                |      
                | 
                | See also:
                |     SimAnalysisCases
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def fem_rep(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FEMRep() As CATBaseDispatch
                |     Retrieves the FEM representation associated to the analysis case. Retrieved
                |     value will be empty in case no FEMRep is associated with the analysis case.

        :return: AnyObject
        """

        return AnyObject(self.com_object.FEMRep)

    @fem_rep.setter
    def fem_rep(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.FEMRep = value

    @property
    def features(self) -> SimFeatures:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Features() As SimFeatures (Read Only)
                |     Retrieves the collection of available features.

        :return: SimFeatures
        """

        return SimFeatures(self.com_object.Features)

    @property
    def global_element_type_assignment(self) -> SimGlobalElementTypeAssignment:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GlobalElementTypeAssignment() As SimGlobalElementTypeAssignment (Read
                | Only)
                |     Retrieves the Global Element Type Assignment.

        :return: SimGlobalElementTypeAssignment
        """

        return SimGlobalElementTypeAssignment(self.com_object.GlobalElementTypeAssignment)

    @property
    def local_element_type_assignments(self) -> SimLocalElementTypeAssignments:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LocalElementTypeAssignments() As SimLocalElementTypeAssignments (Read
                | Only)
                |     Retrieves the Local Element Type Assignments collection.

        :return: SimLocalElementTypeAssignments
        """

        return SimLocalElementTypeAssignments(self.com_object.LocalElementTypeAssignments)

    @property
    def results_analysis_case(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ResultsAnalysisCase() As CATBaseDispatch (Read Only)
                |     Retrieves the corresponding analysis case result. Retireved value will be
                |     empty in case on results analysis case is associated with the analysis case.

        :return: AnyObject
        """

        return AnyObject(self.com_object.ResultsAnalysisCase)

    @property
    def steps(self) -> SimSteps:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Steps() As SimSteps (Read Only)
                |     Retrieves the collection of steps.

        :return: SimSteps
        """

        return SimSteps(self.com_object.Steps)

    @property
    def update_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UpdateFlag() As boolean (Read Only)
                |     Returns the flag that specificies if the analysis case is
                |     up-to-date.
                |     TRUE : the analysis case is up-to-date.
                |     FALSE : the analysis case is out of date and needs to be updated.

        :return: bool
        """

        return self.com_object.UpdateFlag

    def create_default_element_type_assignment(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateDefaultElementTypeAssignment()
                |     Creates default element type assignment for the analysis case. The analysis
                |     case must have a step underneath it for this method to be successful.

        :return: None
        """
        return self.com_object.CreateDefaultElementTypeAssignment()

    def delete_solver_restart_result(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteSolverRestartResult()
                |     Deletes the restart data of the analysis case.

        :return: None
        """
        return self.com_object.DeleteSolverRestartResult()

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Performs an update on the analysis case. The analysis case will visit all
                |     contained features and perform update on each. A failure of any feature to
                |     update properly will stop the update cycle and return. 

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'SimAnalysisCase(name="{ self.name }")'
