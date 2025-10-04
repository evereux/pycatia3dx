"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_foundation.sim_feature_states import SimFeatureStates


class SimLoadSet(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimLoadSet
                | 
                | Represents the Load Set object.
                | 
                | Example:
                |     Given a SimFeatures collection you can retrieve a SimLoadSet object named
                |     as "Load Set.1" through the following code:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyLoadSet As CATBaseDispatch
                |      Set MyLoadSet = MyFeatures.Item("Load Set.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures collection you can retrieve a SimLoadSet object named
                |     as "Load Set.1" through the following code:
                | 
                |      ...
                |      myLoadSet = myFeatures.Item("Load Set.1")
    
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
                |     Retrieves the collection of available feature states. 

        :return: SimFeatureStates
        """

        return SimFeatureStates(self.com_object.FeatureStates)

    def __repr__(self):
        return f'SimLoadSet(name="{ self.name }")'
