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
from pycatia3dx.mode.reference import Reference
from pycatia3dx.sketcher.sketch import Sketch
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Sketches(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Sketches
                | 
                | The body's collection of sketches not yet used by any shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Sketch)
        self.com_object = com_object

    def add(self, i_plane: Reference) -> Sketch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Add(Reference iPlane) As Sketch
                |     Creates a new sketch and adds it to the sketch collection. The sketch
                |     creation implies to specify a supporting plane. Once created, the sketch
                |     exists, but is empty. You must use the Sketch.OpenEdition method to begin to
                |     edit it.
                | 
                |     Parameters:
                | 
                |         iPlane
                |             The sketch supporting plane
                |             The following Boundary object is supported: PlanarFace.
                |             
                | 
                |     Returns:
                |         oNewSketch The created sketch 
                |     Example:
                |         This example creates the newSketch sketch on the XY plane of the myPart
                |         part:
                | 
                |          Set XYPlane = myPart.OriginElements.PlaneXY()
                |          Set newSketch = myPart.Sketches.Add(XYPlane)

        :param Reference i_plane:
        :return: Sketch
        """
        return Sketch(self.com_object.Add(i_plane.com_object))

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

    def item(self, i_index: CATVariant) -> Sketch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As Sketch
                |     Returns a sketch using its index or its name from the Sketches
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the sketch to retrieve from the collection
                |             of sketches. As a numerics, this index is the rank of the sketch in the
                |             collection. The index of the first sketch in the collection is 1, and the index
                |             of the last sketch is Count. As a string, it is the name you assigned to the
                |             sketch using the AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved sketch 
                |     Example:
                |         This example retrieves the last item in the collection
                |         sketches.
                | 
                |          Set lastSketch = sketchList.Item(sketchList.Count)

        :param CATVariant i_index:
        :return: Sketch
        """
        return Sketch(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> Sketch:
        if (n + 1) > self.count:
            raise StopIteration

        return Sketch(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Sketch]:
        for i in range(self.count):
            yield Sketch(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Sketches(name="{self.name}")'
