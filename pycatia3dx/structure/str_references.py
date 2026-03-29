"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class StrReferences(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrReferences
                | 
                | Object to Add cutting elements to the collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Reference)
        self.com_object = com_object

    def add(self, i_reference: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(Reference iReference)
                |     Adds a reference in the collection.
                | 
                |     Parameters:
                | 
                |         iReference
                |             Reference. 
                | 
                |     Example:
                | 
                | 
                |              This example Adds refernces to the list of
                |              StrRefernces.
                |              
                | 
                |               Dim ListOfCuttingRefs As StrReferences
                |               Set ListOfCuttingRefs = ObjSfdPlatesMngt.CuttingElements
                |               'add the references of cutting elements in the
                |               list
                |               ListOfCuttingRefs.Add CuttingElemRef

        :param Reference i_reference:
        :return: None
        """
        return self.com_object.Add(i_reference.com_object)

    def item(self, i_index: CATVariant) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As Reference
                |     Returns a reference from the collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of the Reference to be retrieved. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first plate from the list of
                |              plate.
                |              
                | 
                |               Dim ObjReference As Reference
                |               Set ObjReference = ListOfCuttingRefs.Item(1)

        :param CATVariant i_index:
        :return: Reference
        """
        return Reference(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> Reference:
        if (n + 1) > self.count:
            raise StopIteration

        return Reference(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Reference]:
        for i in range(self.count):
            yield Reference(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'StrReferences(name="{self.name}")'
