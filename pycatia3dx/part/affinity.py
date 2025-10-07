"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mmr_automation_interfaces.shape import Shape


class Affinity(Shape):

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
                |                         Affinity
                | 
                | Represents the hybrid shape Affinity feature object.
                | This solid feature is created from an underlying HybridShapeAffinity aggregated
                | by the Affinity. Role: To access the data of the hybrid shape Affinity feature
                | object. This data includes:
                | 
                |     The element to Affinity
                |     Origin for the Affinity
                |     Plane for the Affinity
                |     Direction for the Affinity
                |     XRatio Value for the Affinity
                |     YRatio Value for the Affinity
                |     ZRatio Value for the Affinity
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
                |     Gets the underlying HybridShapeAffinity.
                | 
                |     Example:
                |         The following example explains how to retrieve the underlying
                |         HybridShape Affinity
                | 
                |           Dim oHybridShape as AnyObject
                |           Set oHybridShape=oAffinity.HybridShape
                |           oHybridShape.ElemToAffinity = reference1

        :return: HybridShape
        """

        return HybridShape(self.com_object.HybridShape)

    def __repr__(self):
        return f'Affinity(name="{ self.name }")'
