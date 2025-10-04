"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_analysis_case import SimAnalysisCase


class SimThermalAnalysisCase(SimAnalysisCase):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaFoundationIDLItf.SimAnalysisCase
                |                         SimThermalAnalysisCase
                | 
                | Represents the Thermal Analysis Case object.
                | 
                | Example:
                |     Given a SimAnalysisCases collection you can retrieve a
                |     SimThermalAnalysisCase object named as "Thermal Analysis Case.1" through the
                |     following code:
                | 
                |      Dim MyAnalysisCases As SimAnalysisCases
                |      ...
                |      Dim MyAnalysisCase As SimThermalAnalysisCase
                |      Set MyAnalysisCase = MyAnalysisCases.Item("Thermal Analysis Case.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAnalysisCases collection you can retrieve a
                |     SimThermalAnalysisCase object named as "Thermal Analysis Case.1" through the
                |     following code:
                | 
                |      ...
                |      myAnalysisCase = myAnalysisCases.Item("Thermal Analysis Case.1")
                |      
                | 
                | See also:
                |     SimAnalysisCases

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimThermalAnalysisCase(name="{ self.name }")'
