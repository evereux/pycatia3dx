"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_local_element_type_assignment import SimLocalElementTypeAssignment
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimLocalElementTypeAssignments(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimLocalElementTypeAssignments
                | 
                | Represents the Local Element Type Assignments collection
                | object.
                | 
                | Example:
                |     This example demonstrates how to retrieve the
                |     SimLocalElementTypeAssignments object from a SimAnalysisCase, and use the Add,
                |     Item, and Remove methods.
                | 
                |      Dim MyAnalysisCase As SimAnalysisCase
                |      ...
                |      Dim MyLocalElementTypeAssignments As
                |      SimLocalElementTypeAssignments
                |      Set MyLocalElementTypeAssignments = MyAnalysisCase.LocalElementTypeAssignments
                |      Dim MyLocalElementTypeAssignment As
                |      SimLocalElementTypeAssignment
                |      Set MyLocalElementTypeAssignment = MyLocalElementTypeAssignments.Add
                |      Set MyLocalElementTypeAssignment = MyLocalElementTypeAssignments.Item("Local Element Type Assignment.1")
                |      MyLocalElementTypeAssignments.Remove "Local Element Type
                |      Assignment.1"
                |      
                | 
                | Example in Python:
                | 
                |      MyLocalElementTypeAssignments = MyAnalysisCase.LocalElementTypeAssignments
                |      MyLocalElementTypeAssignment = MyLocalElementTypeAssignments.Add()
                |      MyLocalElementTypeAssignment = MyLocalElementTypeAssignments.Item("Local Element Type Assignment.1")
                |      MyLocalElementTypeAssignments.Remove( )"Local Element Type
                |      Assignment.1")
                |      
                | 
                | See also:
                |     SimLocalElementTypeAssignment
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimLocalElementTypeAssignment)
        self.com_object = com_object

    def add(self) -> SimLocalElementTypeAssignment:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As CATBaseDispatch
                |     Creates an Local Element Type Assignment object and returns
                |     it.
                | 
                |     Returns:
                |         A SimLocalElementTypeAssignment object

        :return: SimLocalElementTypeAssignment
        """
        return SimLocalElementTypeAssignment(self.com_object.Add())

    def item(self, i_index: CATVariant) -> SimLocalElementTypeAssignment:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Local Element Type Assignment from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or name of the Local Element Type Assignment.
                |             
                | 
                |     Returns:
                |         The SimLocalElementTypeAssignment object

        :param CATVariant i_index:
        :return: SimLocalElementTypeAssignment
        """
        return SimLocalElementTypeAssignment(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes an Local Element Type Assignment object from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Local Element Type Assignment. 

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimLocalElementTypeAssignments(name="{self.name}")'
