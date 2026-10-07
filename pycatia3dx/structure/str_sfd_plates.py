"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.str_sfd_plate import StrSfdPlate
from pycatia3dx.types.general import CATVariant


class StrSfdPlates(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrSfdPlates
                | 
                | Object for SfdPlates
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrSfdPlate)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> StrSfdPlate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As StrSfdPlate
                |     Returns a SfdPlate from the list of plates
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of SfdPlate 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first plate from the list of
                |              plate.
                |              
                | 
                |               Dim ObjSfdPlateList As SfdPlates
                |               Set ObjSfdPlateList = ObjSfdPlatesMngt.GetPlates
                |               Dim ObjSfdPlate As SfdPlate
                |               Set ObjSfdPlate = ObjSfdPlateList.Item(1)

        :param CATVariant i_index:
        :return: StrSfdPlate
        """
        return StrSfdPlate(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> StrSfdPlate:
        if (n + 1) > self.count:
            raise StopIteration

        return StrSfdPlate(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[StrSfdPlate]:
        for i in range(self.count):
            yield StrSfdPlate(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'StrSfdPlates(name="{self.name}")'
