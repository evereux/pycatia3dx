"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.product_structure_client.shape_3d import Shape3D
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Shape3Ds(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Shape3Ds
                | 
                | A collection of 3DShape Representations.
                | This collection contains all the 3DShape Representations available in the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Shape3D)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> Shape3D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As Shape3D
                |     Returns a 3DShape from its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the 3DShape to retrieve from the collection. As a
                |             numerics, this index is the rank of the 3DShape in the collection. The index of
                |             the first 3DShape in the collection is 1, and the index of the last 3DShape is
                |             returned by Collection.get_Count method. As a String, this index is the name of
                |             the 3DShape. 
                | 
                |     Returns:
                |         The retrieved 3DShape. 
                |     Example:
                | 
                |             This example shows you how to retrieve the third 3DShape beneath a
                |             VPMReference (oOccurrenceToScan)
                |            
                | 
                |            Dim  o3DShapeToRetrieve  As Shape3D
                |            Dim oShape3Ds As Shape3Ds
                |            ...
                |            Set oShape3Ds = oProductSessionService.Shape3Ds
                |            ...
                |            Set  o3DShapeToRetrieve = oShape3Ds.Item(3)

        :param CATVariant i_index:
        :return: Shape3D
        """
        return Shape3D(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> Shape3D:
        if (n + 1) > self.count:
            raise StopIteration

        return Shape3D(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Shape3D]:
        for i in range(self.count):
            yield Shape3D(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Shape3Ds(name="{self.name}")'
