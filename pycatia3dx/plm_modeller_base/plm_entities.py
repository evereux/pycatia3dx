"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class PLMEntities(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMEntities
                | 
                | A collection of PLM Entity objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=PLMEntity)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> PLMEntity:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As PLMEntity
                |     Returns a PLM Entity object from its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of the PLMEntity to retrieve from the collection of
                |             PLMEntities. As a numerics, this index is the rank of the PLMEntity in the
                |             collection. The index of the first PLMEntity in the collection is 1, and the
                |             index of the last PLMEntity is returned by Collection.get_Count method.
                |             
                | 
                |     Returns:
                |         Retrieved PLMEntity.

        :param CATVariant i_index:
        :return: PLMEntity
        """
        return PLMEntity(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> PLMEntity:
        if (n + 1) > self.count:
            raise StopIteration

        return PLMEntity(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[PLMEntity]:
        for i in range(self.count):
            yield PLMEntity(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'PlmEntities(name="{self.name}")'
