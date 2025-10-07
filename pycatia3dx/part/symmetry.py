"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mmr_automation_interfaces.shape import Shape


class Symmetry(Shape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         Symmetry
                | 
                | Represents the shape symmetry feature object.
                | This solid feature is created from an underlying HybridShapeSymmetry aggregated
                | by the Symmetry. Role: To access the data of the symmetry shape feature object.
                | The data includes:
                | 
                |     The element to be transformed
                |     The reference element which can be a point, a line or a
                |     plane
                | 
                | Use the CATIAShapeFactory to create ShapeFeature object.
                | 
                | See also:
                |     ShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def hybrid_shape(self) -> HybridShape:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HybridShape() As HybridShape (Read Only)
                |     Gets the underlying HybridShapeSymmetry.
                | 
                |     Example:
                |         The following example explains how to retrieve the underlying
                |         HybridShape Symmetry
                | 
                |           Dim oHybridShape as AnyObject
                |           Set oHybridShape=oSymmetry.HybridShape
                |           oHybridShape.SectionCoupling = 2

        :return: HybridShape
        """

        return HybridShape(self.com_object.HybridShape)

    def __repr__(self):
        return f'Symmetry(name="{ self.name }")'
