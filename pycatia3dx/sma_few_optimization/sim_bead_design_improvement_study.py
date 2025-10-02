"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_few_optimization.sim_design_improvement_study_case import SimDesignImprovementStudyCase


class SimBeadDesignImprovementStudy(SimDesignImprovementStudyCase):

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
                |                        SMAFeaOptimizationIDLItf.SimDesignImprovementStudyCase
                |                             SimBeadDesignImprovementStudy
                | 
                | Represents the Bead Design Improvement Study object.
                | 
                | Example:
                |     Given a SimAnalysisCases collection you can retrieve a
                |     SimBeadDesignImprovementStudy object named as "Bead Design Improvement Study.1"
                |     through the following code:
                | 
                |      Dim MyAnalysisCases As SimAnalysisCases
                |      ...
                |      Dim MyDesignImprovementStudy As
                |      SimBeadDesignImprovementStudy
                |      Set MyDesignImprovementStudy = MyAnalysisCases.Item("Bead Design Improvement Study.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAnalysisCases collection you can retrieve a
                |     SimBeadDesignImprovementStudyCase object as following:
                | 
                |      ...
                |      MyDesignImprovementStudy  = MyAnalysisCases.Item("Bead Design Improvement Study.1")
                |      
                | 
                | See also:
                |     SimAnalysisCases
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimBeadDesignImprovementStudy(name="{ self.name }")'
