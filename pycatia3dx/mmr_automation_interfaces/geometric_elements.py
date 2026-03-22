#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.geometric_element import GeometricElement
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class GeometricElements(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     GeometricElements
                | 
                | A collection of all geometric elements contained in a part or a
                | sketch.
                | Geometric elements are created with the 2D factory for the sketch and with the
                | 3D factory for the part. Geometric elements thus created are then aggregated
                | either in the sketch or as part of the geometric element
                | collection.
                | 
                | See also:
                |     Factory2D, HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=GeometricElement)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> GeometricElement:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As GeometricElement
                |     Returns a geometric element using its index or its name from the
                |     GeometricElements collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the geometric element to retrieve from the
                |             collection of geometric elements. As a numerics, this index is the rank of the
                |             geometric element in the collection. The index of the first geometric element
                |             in the collection is 1, and the index of the last geometric element is Count.
                |             As a string, it is the name you assigned to the geometric element using the
                |             AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved geometric element 
                |     Example:
                |         This example retrieves the last item in the geometric element
                |         collection.
                | 
                |          Set lastCst = cstList.Item(cstList.Count)

        :param CATVariant i_index:
        :return: GeometricElement
        """
        return GeometricElement(self.com_object.Item(i_index))

    def __repr__(self):
        return f'GeometricElements(name="{self.name}")'
