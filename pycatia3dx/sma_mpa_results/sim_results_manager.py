"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch
from pycatia3dx.sma_mpa_results.sim_multi_view import SimMultiView
from pycatia3dx.sma_mpa_results.sim_results_analysis_cases import SimResultsAnalysisCases


class SimResultsManager(CATBaseDispatch):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimResultsManager
                | 
                | Represents the resutls manager and can be used to retrieve the results analysis
                | cases and multi view manager.
                | 
                |  
                | Example:
                | 
                |  Given a SimulationReference object, you can create a SimResultsManager object
                |  as following.
                |  
                | 
                |  Dim oResultsManager As SimResultsManager
                |  Set oResultsManager = oSimulationReference.GetItem("SimResultsManager")
                |  
                | 
                | See also:
                |     SimulationReference
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def multi_view_manager(self) -> SimMultiView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MultiViewManager() As SimMultiView (Read Only)
                |     Returns the MultiViewManager to be used for configuring the viewer and
                |     adding plots in the multi view layout.

        :return: SimMultiView
        """

        return SimMultiView(self.com_object.MultiViewManager)

    @property
    def results_analysis_cases(self) -> SimResultsAnalysisCases:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ResultsAnalysisCases() As SimResultsAnalysisCases (Read
                | Only)
                |     Returns a list of ResultsAnalysisCases created within this
                |     Manager.

        :return: SimResultsAnalysisCases
        """

        return SimResultsAnalysisCases(self.com_object.ResultsAnalysisCases)

    def get_load_case_identifier(self, ocs_load_case_persistent_i_ds: tuple, ocs_load_case_names: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLoadCaseIdentifier(CATSafeArrayVariant
                | ocsLoadCasePersistentIDs,CATSafeArrayVariant ocsLoadCaseNames)
                |     Gets the load case information.
                | 
                |     Parameters:
                | 
                |         ocsLoadCasePersistentIDs
                |             The list of persistent ID's of all the load cases in the model.
                |             
                |         ocsLoadCaseNames
                |             The list of all the load case names present in the model.

        :param tuple ocs_load_case_persistent_i_ds:
        :param tuple ocs_load_case_names:
        :return: None
        """
        return self.com_object.GetLoadCaseIdentifier(ocs_load_case_persistent_i_ds, ocs_load_case_names)

    def __repr__(self):
        return f'SimResultsManager()'
