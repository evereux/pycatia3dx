"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_few_optimization.sim_design_exploration_study_case import SimDesignExplorationStudyCase
from pycatia3dx.sma_few_optimization.sim_design_improvement_features import SimDesignImprovementFeatures


class SimDesignImprovementStudyCase(SimDesignExplorationStudyCase):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    SMAFeaOptimizationIDLItf.SimDesignExplorationStudyCase
                |                         SimDesignImprovementStudyCase
                | 
                | Represents the Optimization Case object.
                | Base class for topology, shape and bead design improvement study
                | objects.
                | 
                | Example:
                |     Given a SimAnalysisCases collection you can retrieve a
                |     SimDesignImprovementStudyCase object named as "Topology Optimization Case.1"
                |     through the following code:
                | 
                |      Dim MyAnalysisCases As SimAnalysisCases
                |      ...
                |      Dim MyOptimizationCase As SimDesignImprovementStudyCase
                |      Set MyOptimizationCase = MyAnalysisCases.Item("Topology Optimization Case.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAnalysisCases collection you can retrieve a
                |     SimDesignImprovementStudyCase object as following:
                | 
                |      ...
                |      MyOptimizationCase  = MyAnalysisCases.Item("Topology Design Improvement Study.1")
                |      
                | 
                | See also:
                |     SimAnalysisCases
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def analysis_case(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnalysisCase() As CATBaseDispatch
                |     Retrieves the analysis case associated to the design improvement study
                |     case. Retrieved value will be empty in case no analysis case is associated with
                |     the design improvement study case.

        :return: AnyObject
        """

        return AnyObject(self.com_object.AnalysisCase)

    @analysis_case.setter
    def analysis_case(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.AnalysisCase = value

    @property
    def fem_rep(self) -> False:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FEMRep(CATBaseDispatch ispFEMRep) (Write Only)
                |     Associates the FEM representation to the design improvement study case.

        :return: False
        """

        return None

    @fem_rep.setter
    def fem_rep(self, value: False):
        """
        :param False value:
        """

        self.com_object.FEMRep = value

    @property
    def features(self) -> SimDesignImprovementFeatures:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Features() As SimDesignImprovementFeatures (Read
                | Only)
                |     Retrieves the collection of available design improvement study features.

        :return: SimDesignImprovementFeatures
        """

        return SimDesignImprovementFeatures(self.com_object.Features)

    def __repr__(self):
        return f'SimDesignImprovementStudyCase(name="{ self.name }")'
