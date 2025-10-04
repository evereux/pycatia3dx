"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_foundation.sim_feature_states import SimFeatureStates


class SimStep(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimStep
                | 
                | Represents the Step object.
                | 
                | Example:
                |     Given a SimSteps collection you can retrieve a SimStep object named as
                |     "Static Step.1" through the following code:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyStep As CATBaseDispatch
                |      Set MyStep = MyAnalysisCases.Item("Static Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps collection you can retrieve a SimStep object named as
                |     "Static Step.1" through the following code:
                | 
                |      ...
                |      myStep = myAnalysisCases.Item("Static Step.1")
                |      
                | 
                | See also:
                |     SimSteps
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def feature_states(self) -> SimFeatureStates:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FeatureStates() As SimFeatureStates (Read Only)
                |     Retrieves the collection of all available feature sets.

        :return: SimFeatureStates
        """

        return SimFeatureStates(self.com_object.FeatureStates)

    def create_analysis_default_output_requests(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateAnalysisDefaultOutputRequests()
                |     Creates default output requests for the step. 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :return: None
        """
        return self.com_object.CreateAnalysisDefaultOutputRequests()

    def __repr__(self):
        return f'SimStep(name="{ self.name }")'
