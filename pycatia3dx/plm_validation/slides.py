"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.plm_validation.slide import Slide
from pycatia3dx.types.general import CATVariant


class Slides(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Slides
                | 
                | A collection of Slides.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Slide)
        self.com_object = com_object

    def add(self) -> Slide:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As Slide
                |     Creates a Slide and adds it to the Slide collection.
                | 
                |     Parameters:
                | 
                |         iSlide
                |             The Slide 
                | 
                |     Example:
                | 
                |             This example creates a new Slide in the cSlides
                |             collection.
                |             
                | 
                |             Dim oNewSlideText As Slide
                |             Set oNewSlideText = cSlides.Add

        :return: Slide
        """
        return Slide(self.com_object.Add())

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Slide using its index from the Slides
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Slide to retrieve from the collection
                |             of Slides. As a numerics, this index is the rank of the Slide in the
                |             collection. The index of the first Slide in the collection is 1, and the index
                |             of the last Slide is Count. As a string, it is the name you assigned to the
                |             Slide. 
                | 
                |     Returns:
                |         The retrieved Slide 
                |     Example:
                | 
                |             This example retrieves in oSlide1 the ninth Slide,
                |             and in oSlide2 the Slide named
                |             Slide3 from the cSlides collection. 
                |             
                | 
                |             Dim oSlide1 As Slide
                |             Set oSlide1 = cSlides.Item(9)
                |             Dim oSlide2 As Slide
                |             Set oSlide2 = cSlides.Item("Slide3")

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
                |     Removes a Slide from the Slides collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Slide to retrieve from the collection
                |             of Slides. As a numerics, this index is the rank of the Slide in the
                |             collection. The index of the first Slide in the collection is 1, and the index
                |             of the last Slide is Count. As a string, it is the name you assigned to the
                |             Slide. 
                | 
                |     Example:
                | 
                |             The following example removes the tenth Slide and the Slide
                |             named
                |             Slide2 from the cSlides collection.
                |             
                | 
                |             cSlides.Remove(10)
                |             cSlides.Remove("Slide2")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __getitem__(self, n: int) -> Slide:
        if (n + 1) > self.count:
            raise StopIteration

        return Slide(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Slide]:
        for i in range(self.count):
            yield Slide(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Slides(name="{self.name}")'
