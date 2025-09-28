"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.hybrid_shapes.point import Point
from pycatia3dx.mode.reference import Reference


class HybridShapePointTangent(Point):

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
                |                         CATGSMIDLItf.Point
                |                             HybridShapePointTangent
                | 
                | Point Tangent.
                | Role: Allows to access data of the point feature created as follow
                | :
                | The tangent to the curve at this point is colinear to a given
                | direction.
                | Note: The resulting feature can contain several points.
                | 
                | See also:
                |     Length
                | See also:
                |     Reference
                | See also:
                |     HybridShapeDirection
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Curve() As Reference
                |     Returns or Gets the supporting curve.
                |     Sub-element(s) supported (see Boundary object): Edge.
                | 
                |     Example
                |     :
                |         This example retrieves in oCurve the supporting Curve for the
                |         PointTangent feature.
                | 
                |          Dim oCurve As CATIAReference   
                |          Set oCurve  = PointTangent.Curve

        :return: Reference
        """

        return Reference(self.com_object.Curve)

    @curve.setter
    def curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Curve = value

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Returns or Sets the direction.
                | 
                |     Example
                |     :
                |         This example retrieves in oDirection the tangent direction use to
                |         compute on supporting curve the PointTangent feature.
                | 
                |          Dim oDirection As CATIAHybridShapeDirection
                |          Set oDirection  = PointTangent.Direction

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Direction)

    @direction.setter
    def direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Direction = value

    def __repr__(self):
        return f'HybridShapePointTangent(name="{ self.name }")'
