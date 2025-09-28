"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShape3DCurveOffset(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShape3DCurveOffset
                | 
                | Represents the hybrid shape 3DCurve Offset operation feature.
                | Role: Allows you to access data of the 3D Curve Offset feature created by using
                | a curve, a direction and three literal parameters
                | 
                | Use the HybridShapeFactory.AddNew3DCurveOffset to create a
                | HybridShape3DCurveOffset object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def corner_radius_value(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CornerRadiusValue() As Length
                |     Returns or sets the Corner Radius Value.

        :return: Length
        """

        return Length(self.com_object.CornerRadiusValue)

    @corner_radius_value.setter
    def corner_radius_value(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.CornerRadiusValue = value

    @property
    def corner_tension_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CornerTensionValue() As double
                |     Returns or sets the Corner Tension Value.

        :return: float
        """

        return self.com_object.CornerTensionValue

    @corner_tension_value.setter
    def corner_tension_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.CornerTensionValue = value

    @property
    def curve_to_offset(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CurveToOffset() As Reference
                |     Returns or sets the curve to offset.

        :return: Reference
        """

        return Reference(self.com_object.CurveToOffset)

    @curve_to_offset.setter
    def curve_to_offset(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.CurveToOffset = value

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Returns or sets the direction.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Direction)

    @direction.setter
    def direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Direction = value

    @property
    def invert_direction(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property InvertDirection() As boolean
                |     Returns or sets the direction orientation.

        :return: bool
        """

        return self.com_object.InvertDirection

    @invert_direction.setter
    def invert_direction(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.InvertDirection = value

    @property
    def offset_value(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property OffsetValue() As Length
                |     Returns or sets the OffsetValue.

        :return: Length
        """

        return Length(self.com_object.OffsetValue)

    @offset_value.setter
    def offset_value(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.OffsetValue = value

    def __repr__(self):
        return f'HybridShape3DCurveOffset(name="{ self.name }")'
