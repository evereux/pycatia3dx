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


class SimSteps(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimSteps
                | 
                | Represents the Steps Collection.
                | Possible types that can be created are:
                | 
                |     SimStaticStep : Creates a static step. It is of type SimStaticStep.
                |     SimBuckleStep : Creates a buckle step. It is of type SimBuckleStep.
                |     SimFrequencyStep : Creates a frequency step. It is of type SimFrequencyStep.
                |     SimComplexFrequencyStep : Creates a complex frequency step. It is of type SimComplexFrequencyStep.
                |     SimHarmonicResponseStep : Creates an harmonic response step. It is of type SimHarmonicResponseStep.
                |     SimModalDynamicStep : Creates an modal dynamic step. It is of type SimModalDynamicStep.
                |     SimStaticPerturbationStep : Creates a static perturbation step. It is of type SimStaticPerturbationStep.
                |     SimSteadyStateHeatTransferStep : Creates a steady state heat transfer step. It is of type SimSteadyStateHeatTransferStep.
                |     SimTransientHeatTransferStep : Creates a transient heat transfer step. It is of type SimTransientHeatTransferStep.
                |     SimExplicitDynamicStep : Creates an explicit dynamic step. It is of type SimExplicitDynamicStep.
                |     SimImplicitDynamicStep : Creates an implicit dynamic step. It is of type SimImplicitDynamicStep.
                |     SimQuasiStaticStep : Creates a quasi-static step. It is of type SimQuasiStaticStep.
                | 
                | Example:
                |     Given a SimAnalysisCase object you can retrieve a SimSteps collection as
                |     following:
                | 
                |      Dim MyAnalysisCase As SimStructuralAnalysisCase
                |      ...
                |      Dim MySteps As SimSteps
                |      Set MySteps = MyAnalysisCase.Steps
                |      
                | 
                | Example in Python:
                |     Given a SimAnalysisCase object you can retrieve a SimSteps collection as
                |     following:
                | 
                |      ...
                |      mySteps = myAnalysisCase.Steps
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
                |     Creates a Step object and returns it.
                | 
                |     Parameters:
                | 
                |         iType
                |             The Step Type to be created. 
                | 
                |     Returns:
                |         A SimStep object

        :param str i_type:
        :return: AnyObject
        """
        return self.com_object.Add(i_type)

    def add_after(self, i_type: str, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddAfter(CATBSTR iType,CATVariant iIndex) As
                | CATBaseDispatch
                |     Creates a Step object, after the specified step in the analysis case and
                |     returns it.
                | 
                |     Parameters:
                | 
                |         iType
                |             The Step Type to be created. 
                |         iIndex
                |             The newly create step will be added after the step specified at
                |             index. 
                | 
                |     Returns:
                |         A SimStep object

        :param str i_type:
        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.AddAfter(i_type, i_index)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Step from the collection of Steps.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or name of the Step 
                | 
                |     Returns:
                |         A SimStep object

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
                |     Removes a Step from the collection of Steps. 

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimSteps(name="{ self.name }")'
