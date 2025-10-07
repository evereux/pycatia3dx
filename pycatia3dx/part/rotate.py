"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mmr_automation_interfaces.shape import Shape
from pycatia3dx.mode.reference import Reference


class Rotate(Shape):

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
                |                         Rotate
                | 
                | Represents the shape rotate feature object.
                | This solid feature is created from an underlying HybridShapeRotate aggregated
                | by the Rotate. Role: To access the data of the hybrid shape rotate feature
                | object. This data includes:
                | 
                |     The element to be rotated
                |     The rotation axis
                |     The angle and its value
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
    def angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Angle() As Angle (Read Only)
                |     Returns the rotation angle.

        :return: Angle
        """

        return Angle(self.com_object.Angle)

    @property
    def angle_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngleValue() As double
                |     Returns or sets the rotation angle value.
                | 
                |     Example: This example retrieves in AngleValue the angle value for the
                |     Rotate hybrid shape feature.
                | 
                |      Dim AngleValue As double
                |      Set AngleValue = Rotate.AngleValue

        :return: float
        """

        return self.com_object.AngleValue

    @angle_value.setter
    def angle_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.AngleValue = value

    @property
    def axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Axis() As Reference
                |     Returns or sets the rotation axis.
                |     To set the property, you can use one of the following Boundary objects:
                |     RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge or
                |     RectilinearMonoDimFeatEdge.
                | 
                |     Example: This example retrieves in RotationAxis the rotation axis for the
                |     Rotate hybrid shape feature.
                | 
                |      Dim RotationAxis As Reference
                |      Set RotationAxis = Rotate.Axis

        :return: Reference
        """

        return Reference(self.com_object.Axis)

    @axis.setter
    def axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Axis = value

    @property
    def hybrid_shape(self) -> HybridShape:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HybridShape() As HybridShape (Read Only)
                |     Gets the underlying HybridShapeRotate.
                | 
                |     Example:
                |         The following example explains how to retrieve the underlying
                |         HybridShape Rotate
                | 
                |           Dim oHybridShape as AnyObject
                |           Set oHybridShape=oRotate.HybridShape
                |           oHybridShape.SectionCoupling = 2

        :return: HybridShape
        """

        return HybridShape(self.com_object.HybridShape)

    def __repr__(self):
        return f'Rotate(name="{ self.name }")'
