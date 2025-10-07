"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mmr_automation_interfaces.shape import Shape


class Translate(Shape):

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
                |                         Translate
                | 
                | Represents the hybrid shape translate feature object.
                | This solid feature is created from an underlying HybridShapeTranslate
                | aggregated by the Translate. Role: To access the data of the hybrid shape
                | translate feature object. This data includes:
                | 
                |     The element to translate
                |     The translation direction
                |     The translation distance and its value
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
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
                |     Gets the underlying HybridShapeTranslate.
                | 
                |     Example:
                |         The following example explains how to retrieve the underlying
                |         HybridShape Translate
                | 
                |           Dim oHybridShape as AnyObject
                |           Set oHybridShape=oTranslate.HybridShape
                |           oHybridShape.ElemToTranslate = reference1

        :return: HybridShape
        """

        return HybridShape(self.com_object.HybridShape)

    def __repr__(self):
        return f'Translate(name="{ self.name }")'
