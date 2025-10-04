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


class SimFeatureHistory(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimFeatureHistory
                | 
                | Represents the Feature History Collection.
                | 
                | Example:
                |     You can retrieve a SimFeatureHistory collection from a propagating feature,
                |     for example: SimPressure as following:
                | 
                |      Dim MyPressure As SimPressure
                |      ...
                |      Dim MyFeatureHistory As SimFeatureHistory
                |      Set MyFeatureHistory = MyPressure.FeatureHistory
                |      
                | 
                |     Given a SimFeatureHistory object, you can loop through the SimFeatureState
                |     objects as following:
                | 
                |      Dim MyFeatureHistory As SimFeatureHistory
                |      ...
                |      Dim MyFeatureState As SimFeatureState
                |      For Each MyFeatureState In MyFeatureHistory
                |          Dim MyScaleFactorFlag As Boolean
                |          MyScaleFactorFlag = MyFeatureState.ScaleFactorFlag
                |      Next
                |      
                | 
                | Example in Python:
                |     You can retrieve a SimFeatureHistory collection from a propagating feature,
                |     for example: SimPressure as following:
                | 
                |      ...
                |      myFeatureHistory = myPressure.FeatureHistory
                |      
                | 
                |     Given a SimFeatureHistory object, you can loop through the SimFeatureState
                |     objects as following:
                | 
                |      ...
                |      for myFeatureState in myFeatureHistory:
                |          myScaleFactorFlag = myFeatureState.ScaleFactorFlag
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_to_step(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddToStep(CATVariant iIndex)
                |     Adds the Feature State in a step and any dependent steps. Dependent steps
                |     are:
                | 
                |         For General steps - All subsequent steps
                |         For Frequency/Buckle steps - All subsequent Linear Dynamic
                |         steps
                |         For Linear Dynamic steps - None
                |         For any other Perturbation steps - None
                | 
                |     Parameters:
                | 
                |         iIndex[in]
                |             The index or name of the Step.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.AddToStep(i_index)

    def can_add_to_step(self, i_index: CATVariant) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CanAddToStep(CATVariant iIndex) As boolean
                |     Returns whether the Feature State can be added in a step.
                | 
                |     Parameters:
                | 
                |         iIndex[in]
                |             The index or name of the Step. 
                | 
                |     Returns:
                |         TRUE: the Feature State can be added in the specified
                |         step.
                |         FALSE: the Feature State cannot be added in the specified step.

        :param CATVariant i_index:
        :return: bool
        """
        return self.com_object.CanAddToStep(i_index)

    def can_remove_from_step(self, i_index: CATVariant) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CanRemoveFromStep(CATVariant iIndex) As boolean
                |     Returns whether the Feature State can be removed from a
                |     step.
                | 
                |     Parameters:
                | 
                |         iIndex[in]
                |             The index or name of the Step. 
                | 
                |     Returns:
                |         TRUE: the Feature State can be removed from the specified
                |         step.
                |         FALSE: the Feature State cannot be removed from the specified step.

        :param CATVariant i_index:
        :return: bool
        """
        return self.com_object.CanRemoveFromStep(i_index)

    def can_start_in_step(self, i_index: CATVariant) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CanStartInStep(CATVariant iIndex) As boolean
                |     Returns whether the Feature State can start in a step.
                | 
                |     Parameters:
                | 
                |         iIndex[in]
                |             The index or name of the Step. 
                | 
                |     Returns:
                |         TRUE: the Feature State can start in the specified
                |         step.
                |         FALSE: the Feature State cannot start in the specified step.

        :param CATVariant i_index:
        :return: bool
        """
        return self.com_object.CanStartInStep(i_index)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns the Feature State from a step.
                | 
                |     Parameters:
                | 
                |         iIndex[in]
                |             The index or name of the Step. 
                | 
                |     Returns:
                |         The retrieved SimFeatureState object.

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove_from_step(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveFromStep(CATVariant iIndex)
                |     Removes the Feature State from a step and any dependent steps. Dependent
                |     steps are:
                | 
                |         For General steps - All subsequent steps
                |         For Frequency/Buckle steps - All subsequent Linear Dynamic
                |         steps
                |         For Linear Dynamic steps - None
                |         For any other Perturbation steps - None
                | 
                |     Parameters:
                | 
                |         iIndex[in]
                |             The index or name of the Step.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.RemoveFromStep(i_index)

    def start_in_step(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub StartInStep(CATVariant iIndex)
                |     Starts the Feature State in a step.
                | 
                |     Parameters:
                | 
                |         iIndex[in]
                |             The index or name of the Step. 

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.StartInStep(i_index)

    def __repr__(self):
        return f'SimFeatureHistory(name="{ self.name }")'
