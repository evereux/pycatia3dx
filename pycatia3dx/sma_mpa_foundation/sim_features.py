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


class SimFeatures(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimFeatures
                | 
                | Represents the Feature Set Collection.
                | 
                | Example:
                |     Given a feature SimAnalysisCase object you can retrieve a SimFeatures
                |     object as following:
                | 
                |      Dim MyAnalysisCase As SimStructuralAnalysisCase
                |      ...
                |      Dim MyFeatures As SimFeatures
                |      Set MyFeatures = MyAnalysisCase.Features
                |      
                | 
                | Example in Python:
                |     Given a feature SimAnalysisCase object you can retrieve a SimFeatures
                |     object as following:
                | 
                |      ...
                |      myFeatures = myAnalysisCase.Features
                |      
                | 
                | See also:
                |     SimAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As CATBaseDispatch
                |     Creates a Feature object of the argument type and returns it. The type must
                |     be the feature type in string format. For example "SimClamp" to create a
                |     SimClamp.
                | 
                |     Parameters:
                | 
                |         iType
                |             The Feature Type to be created. 
                | 
                |     Returns:
                |         The created feature object.

        :param str i_type:
        :return: AnyObject
        """
        return self.com_object.Add(i_type)

    def get_spec_tree_category(self, i_feature: AnyObject) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSpecTreeCategory(CATBaseDispatch iFeature) As CATBSTR
                |     Returns a string representing the specification tree category of the
                |     argument feature. Possible values are:
                | 
                |         Abstractions
                |         Amplitudes
                |         Controls
                |         Connections
                |         Damping
                |         ElementTypeAssignments
                |         Envelopes
                |         FieldPlots
                |         FlowConditions
                |         HistoryPlots
                |         InitialConditions
                |         Interactions
                |         KeywordEdits
                |         LinearLoadCases
                |         Loads
                |         LoadSets
                |         OutputRequests
                |         PredefinedFields
                |         Properties
                |         Restraints
                |         Sensors
                |         Streams
                |         ThermalConditions
                |         UserSubroutines
                |         NotDefined
                | 
                |     Parameters:
                | 
                |         iFeature
                |             The feature object.

        :param AnyObject i_feature:
        :return: str
        """
        return self.com_object.GetSpecTreeCategory(i_feature.com_object)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Feature from the collection of Features.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Feature Set. 
                | 
                |     Returns:
                |         The retrieved feature object.

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
                |     Removes a Feature from the collection of Features.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or name of the feature object. 

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimFeatures(name="{ self.name }")'
