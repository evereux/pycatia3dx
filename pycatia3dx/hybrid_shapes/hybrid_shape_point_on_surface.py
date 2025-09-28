"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.hybrid_shapes.point import Point
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapePointOnSurface(Point):

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
                |                             HybridShapePointOnSurface
                | 
                | Represents the Point on Surface feature objects.
                | Role: Allows to access data of the point feature created with a geodesic
                | distance in a direction to a reference point on a surface
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
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Returns or Sets the direction from the reference point in which the point
                |     is computed.
                | 
                |     Example
                |     :
                |         This example retrieves in oDirection the direction from the reference
                |         point for PointOnSurface feature.
                | 
                |          Dim oDirection As CATIAHybridShapeDirection
                |          Set oDirection  = PointOnSurface.Direction

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
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Offset() As Length (Read Only)
                |     Returns the geodesic length.
                | 
                |     Example
                |     :
                |         This example retrieves in oGeodesicOffset the offset (Geodesic Length)
                |         from the reference point for PointOnSurface feature.
                | 
                |          Dim oGeodesicOffset As CATIAReference
                |          Set oGeodesicOffset  = PointOnSurface.GeodesicOffset

        :return: Length
        """

        return Length(self.com_object.Offset)

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Point() As Reference
                |     Returns or Sets the reference point.
                |     This data is not mandatory.
                |     If no point is given, the middle point on the surface is
                |     taken.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example
                |     :
                |         This example retrieves in oPointRef the reference point for
                |         PointOnSurface feature.
                | 
                |          Dim oPointRef As CATIAReference
                |          Set oPointRef  = PointOnSurface.PointRef

        :return: Reference
        """

        return Reference(self.com_object.Point)

    @point.setter
    def point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Point = value

    @property
    def surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Surface() As Reference
                |     Returns or Sets the surface.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example
                |     :
                |         This example retrieves in oSurface the supporting surface for
                |         PointOnSurface feature.
                | 
                |          Dim oSurface As CATIAReference
                |          Set oSurface  = PointOnSurface.Surface

        :return: Reference
        """

        return Reference(self.com_object.Surface)

    @surface.setter
    def surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Surface = value

    def __repr__(self):
        return f'HybridShapePointOnSurface(name="{ self.name }")'
