"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_foundation.sim_feature_states import SimFeatureStates


class SimLinearLoadCase(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimLinearLoadCase
                | 
                | Represents the Linear Load Case object.
                | 
                | Example:
                |     Given a SimLinearLoadCases collection you can retrieve a SimLinearLoadCase
                |     object named as "Linear Load Case.1" through the following
                |     code:
                | 
                |      Dim MyLinearLoadCases As SimLinearLoadCases
                |      ...
                |      Dim MyLinearLoadCase As CATBaseDispatch
                |      Set MyLinearLoadCase = MyLinearLoadCases.Item("Linear Load Cases.1")
                |      
                | 
                | Example in Python:
                |     Given a SimLinearLoadCases collection you can retrieve a SimLinearLoadCase
                |     object named as "Linear Load Case.1" through the following
                |     code:
                | 
                |      ...
                |      myLinearLoadCase = myLinearLoadCases.Item("Linear Load Cases.1")
    
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
                |     Retrieves the collection of feature states.

        :return: SimFeatureStates
        """

        return SimFeatureStates(self.com_object.FeatureStates)

    def append_load_case_contents(self, i_source_load_case: 'SimLinearLoadCase') -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AppendLoadCaseContents(SimLinearLoadCase iSourceLoadCase)
                |     This method appends the contents of the source load case into the current
                |     load case. The source load case is not modified. Previous contents of the
                |     destination load case are left unchanged.
                | 
                |     Parameters:
                | 
                |         iSourceLoadCase[in]
                |             The linear load case that should be appended. 

        :param SimLinearLoadCase i_source_load_case:
        :return: None
        """
        return self.com_object.AppendLoadCaseContents(i_source_load_case.com_object)

    def __repr__(self):
        return f'SimLinearLoadCase(name="{ self.name }")'
