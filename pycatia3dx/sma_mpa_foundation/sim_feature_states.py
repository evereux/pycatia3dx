"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimFeatureStates(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimFeatureStates
                | 
                | Represents the Feature States Collection.
                | 
                | Example:
                |     Given a SimStep object you can retrieve a SimFeatureStates collection as
                |     following:
                | 
                |      Dim MyStaticStep As SimStaticStep
                |      ...
                |      Dim MyFeatureStates As SimFeatureStates
                |      Set MyFeatureStates = MyStaticStep.FeatureStates
                |      
                | 
                | Example in Python:
                |     Given a SimStep object you can retrieve a SimFeatureStates collection as
                |     following:
                | 
                |      ...
                |      myFeatureStates = myStaticStep.FeatureStates
                |      
                | 
                | See also:
                |     SimStep
    
    """

    def __init__(self, com_object):
        # todo: What is the child_object for this Collection?
        super().__init__(com_object)
        self.com_object = com_object

    def create_feature_state(self, i_feature: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateFeatureState(CATBaseDispatch iFeature)
                |     Creates a Feature State object and returns it. The Feature State is created
                |     in the context of a SimStep, SimLoadSet, or SimLoadCase. When created in a
                |     SimStep, corresponding Feature States are created in the downstream Steps. When
                |     created in a SimLoadSet or SimLoadCase, a single Feature State is
                |     created.
                | 
                |     Parameters:
                | 
                |         iFeature
                |             The Feature for which feature state object has to be created.

        :param AnyObject i_feature:
        :return: None
        """
        return self.com_object.CreateFeatureState(i_feature.com_object)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Feature State from the collection of Feature
                |     States.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Feature State. 
                | 
                |     Returns:
                |         The retrieved SimFeatureState object

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Feature State from the collection of Feature States. The Feature
                |     State is removed in the context of a SimStep, SimLoadSet, or SimLoadCase. When
                |     removed from a SimStep, all Feature States referencing the same Feature are
                |     removed in the upstream and downstream Steps. When removed from a SimLoadSet or
                |     SimLoadCase, a single Feature State is removed.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Feature State. 

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimFeatureStates(name="{self.name}")'
