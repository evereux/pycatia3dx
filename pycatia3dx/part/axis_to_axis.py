"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mmr_automation_interfaces.shape import Shape


class AxisToAxis(Shape):

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
                |                         AxisToAxis
                | 
                | Represents the hybrid shape AxisToAxis feature object.
                | This solid feature is created from an underlying HybridShapeAxisToAxis
                | aggregated by the AxisToAxis. Role: To access the data of the hybrid shape
                | AxisToAxis feature object. This data includes:
                | 
                |     The element to AxisToAxis
                |     Origin for the AxisToAxis
                |     Plane for the AxisToAxis
                |     Direction for the AxisToAxis
                |     XRatio Value for the AxisToAxis
                |     YRatio Value for the AxisToAxis
                |     ZRatio Value for the AxisToAxis
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
                |     Gets the underlying HybridShapeAxisToAxis.
                | 
                |     Example:
                |         The following example explains how to retrieve the underlying
                |         HybridShape AxisToAxis
                | 
                |           Dim oHybridShape as AnyObject
                |           Set oHybridShape=oAxisToAxis.HybridShape
                |           oHybridShape.ElemToAxisToAxis = reference1

        :return: HybridShape
        """

        return HybridShape(self.com_object.HybridShape)

    def __repr__(self):
        return f'AxisToAxis(name="{ self.name }")'
