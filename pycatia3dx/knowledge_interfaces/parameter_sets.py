"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.parameter_set import ParameterSet
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class ParameterSets(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ParameterSets
                | 
                | Represents a collection of parameter sets.
                | The ParameterSet object is a neutral object that contains parameters, like the
                | Parameters node in the specification tree.
                | 
                | The following example shows how to retrieve it on a part:
                | 
                |  Dim part1 As Part
                |  Set part1 = ...
                |  Dim parameters1 As Parameters
                |  Set parameters1 = part1.Parameters
                |  Dim ParameterSet1 As ParameterSet
                |  Set ParameterSet1 = parameters1.RootParameterSet
                |  Dim parameterSets1 As ParameterSets
                |  Set parameterSets1 = parameterSet1.ParameterSets
                |  
                | 
                | This collection is not a collection of all parameter sets of a representation
                | reference, but a collection of all parameter sets in the current parameter
                | set.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ParameterSet)
        self.com_object = com_object

    def create_set(self, i_name: str) -> ParameterSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateSet(CATBSTR iName) As ParameterSet
                |     Creates a set of parameters and appends it to the parameter set which
                |     corresponds to this collection.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the set of parameters 
                | 
                |     Returns:
                |         Parameter set created

        :param str i_name:
        :return: ParameterSet
        """
        return ParameterSet(self.com_object.CreateSet(i_name))

    def item(self, i_index: CATVariant) -> ParameterSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As ParameterSet
                |     Returns a parameter set using its index or its name from the ParameterSets
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the parameter set to retrieve from the
                |             collection of parameter sets. As a numerics, this index is the rank of the
                |             parameter set in the collection. The index of the first parameter set in the
                |             collection is 1, and the index of the last parameter set is Count. As a string,
                |             it is the name you assigned to the parameter set using the AnyObject.Name
                |             property . 
                | 
                |     Returns:
                |         Parameter set retrieved 
                |     Example:
                |         This example retrieves the parameter set named "Parameters.1" in the
                |         parameterSets collection:
                | 
                |          Set theSet = parameterSets.Item("Parameters.1")

        :param CATVariant i_index:
        :return: ParameterSet
        """
        return ParameterSet(self.com_object.Item(i_index))

    def __repr__(self):
        return f'ParameterSets(name="{self.name}")'
