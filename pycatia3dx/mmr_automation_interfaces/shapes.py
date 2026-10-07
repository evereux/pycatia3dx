#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.mmr_automation_interfaces.boundary import Boundary
from pycatia3dx.mmr_automation_interfaces.shape import Shape
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Shapes(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Shapes
                | 
                | The collection of the shapes making up a body.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Shape)
        self.com_object = com_object

    def get_boundary(self, i_label: str) -> Boundary:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetBoundary(CATBSTR iLabel) As Boundary
                |     Returns a boundary using its label.
                | 
                |     Parameters:
                | 
                |         iLabel
                |             Identification of the Boundary object. See Reference.DisplayName.
                |             
                | 
                |     Returns:
                |         The retrieved boundary

        :param str i_label:
        :return: Boundary
        """
        return Boundary(self.com_object.GetBoundary(i_label))

    def item(self, i_index: CATVariant) -> Shape:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As Shape
                |     Returns a shape using its index or its name from the Shapes
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the shape to retrieve from the collection
                |             of shapes. As a numerics, this index is the rank of the shape in the
                |             collection. The index of the first shape in the collection is 1, and the index
                |             of the last shape is Collection.Count. As a string, it is the name you assigned
                |             to the shape using the AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved shape 
                |     Example:
                |         This example retrieves in ThisShape the third shape, and in ThatShape
                |         the shape named MyShape in the shape collection of the active 3D
                |         shape.
                | 
                |          Set Editor = CATIA.ActiveEditor
                |          Set Part = Editor.ActiveObject
                |          Set ThisShape = Part.Shapes.Item(3)
                |          Set ThatShape = Part.Shapes.Item("MyShape")

        :param CATVariant i_index:
        :return: Shape
        """
        return Shape(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> Shape:
        if (n + 1) > self.count:
            raise StopIteration

        return Shape(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Shape]:
        for i in range(self.count):
            yield Shape(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Shapes(name="{self.name}")'
