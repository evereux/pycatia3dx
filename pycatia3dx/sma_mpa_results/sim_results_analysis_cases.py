"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.sma_mpa_results.sim_results_analysis_case import SimResultsAnalysisCase
from pycatia3dx.types.general import CATVariant


class SimResultsAnalysisCases(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimResultsAnalysisCases
                | 
                | Represents the collection of results analysis cases and can be used to retrieve
                | each results case.
                | Example:
                | 
                |  Given a SimResultsManager object, you can create a SimResultsAnalysisCases
                |  object as following.
                |  
                | 
                |   Dim oResultsAnalysisCases As SimResultsAnalysisCases
                |   Set oResultsAnalysisCases = oResultsManager.ResultsAnalysisCases
                |  
                | 
                | See also:
                |     SimResultsManager
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimResultsAnalysisCase)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SimResultsAnalysisCase:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimResultsAnalysisCase
                |     Returns a Results Analysis Case.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of case to access. The index starts from 1.
                |             
                | 
                |     Returns:
                |         Returns the case for the given index 

        :param CATVariant i_index:
        :return: SimResultsAnalysisCase
        """
        return SimResultsAnalysisCase(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SimResultsAnalysisCases(name="{self.name}")'
