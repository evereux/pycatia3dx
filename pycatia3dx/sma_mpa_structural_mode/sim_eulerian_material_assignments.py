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


class SimEulerianMaterialAssignments(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimEulerianMaterialAssignments
                | 
                | Represents the Eulerian Material Assignments collection.
                | 
                | Example:
                |     Given a SimEulerianProperty object you can retrieve a
                |     SimEulerianMaterialAssignments collection as following:
                | 
                |      Dim MyEulerianProperty As SimEulerianProperty
                |      ...
                |      Dim MyMaterialAssignments As
                |      SimEulerianMaterialAssignments
                |      Set MyMaterialAssignments = MyEulerianProperty.MaterialAssignments
                |      
                | 
                | Example in Python:
                |     Given a SimEulerianProperty object you can retrieve a
                |     SimEulerianMaterialAssignments collection as following:
                | 
                |      ...
                |      myMaterialAssignments = myEulerianProperty.MaterialAssignments
                |      
                | 
                | See also:
                |     SimEulerianProperty
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As CATBaseDispatch
                |     Creates an Eulerian Material Assignment object and returns
                |     it.
                | 
                |     Parameters:
                | 
                |         oMaterialInstance[out]
                |             The created Eulerian Material Assignment.

        :return: AnyObject
        """
        return self.com_object.Add()

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns an Eulerian Material Assignment from the collection of Eulerian
                |     Material Assignments.
                | 
                |     Parameters:
                | 
                |         iIndex[in]
                |             The index of the Eulerian Material Assignment. 
                |         oMaterialInstance[out]
                |             The created Eulerian Material Assignment.

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
                |     Removes the specified Eulerian Material Assignment.
                | 
                |     Parameters:
                | 
                |         iIndex[in]
                |             The index of the Eulerian Material Assignment that will be removed.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAll()
                |     Removes all Eulerian Material Assignments. 

        :return: None
        """
        return self.com_object.RemoveAll()

    def __repr__(self):
        return f'SimEulerianMaterialAssignments(name="{ self.name }")'
