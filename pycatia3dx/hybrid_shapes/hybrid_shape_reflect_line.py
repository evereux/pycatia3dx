"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeReflectLine(HybridShape):

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
                |                         HybridShapeReflectLine
                | 
                | Represents the hybrid shape reflect line feature object.
                | Role: To access the data of the hybrid shape reflect line feature object. This
                | data includes:
                | 
                |     The surface used to create the reflect line
                |     The direction (cylindrical)
                |     The origin (conical)
                |     The angle value
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeReflectLine
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Angle() As Angle
                |     Returns or sets the angle used to create the reflectline.
                | 
                |     Example:
                |         This example retrieves in Ang the angle for the RelectLine hybrid shape
                |         feature.
                | 
                |          Dim Ang As CATIAAngle
                |          Set Ang = ReflectLine.Angle

        :return: Angle
        """

        return Angle(self.com_object.Angle)

    @angle.setter
    def angle(self, value: Angle):
        """
        :param Angle value:
        """

        self.com_object.Angle = value

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Returns or sets the direction used to create the cylindrical
                |     reflectline.
                | 
                |     Example:
                |         This example retrieves in Dir the direction for the cylindrical
                |         RelectLine hybrid shape feature.
                | 
                |          Dim Dir As CATIAHybridShapeDirection
                |          Set Dir = ReflectLine.Direction

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
    def orientation_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property OrientationDirection() As long
                |     Returns or sets the direction orientation used to compute the reflect
                |     line.
                |     Role: The orientation is used to define the angle between the direction and
                |     the normal to the support of the points on the result curve. The orientation is
                |     the same than or the inverse of the result of the cross product:
                |     Normal(support) ^ Tangent(FirstReferenceCurve).
                |     Legal values: 1 for same orientation, and -1 for inverse

        :return: int
        """

        return self.com_object.OrientationDirection

    @orientation_direction.setter
    def orientation_direction(self, value: int):
        """
        :param int value:
        """

        self.com_object.OrientationDirection = value

    @property
    def orientation_support(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property OrientationSupport() As long
                |     Returns or sets the support orientation used to compute the reflect
                |     line.
                |     Role: The orientation is used to define the angle between the direction and
                |     the normal to the support of the points on the result curve. The orientation is
                |     the same than or the inverse of the result of the cross product:
                |     Normal(support) ^ Tangent(FirstReferenceCurve).
                |     Legal values: 1 for same orientation, and -1 for inverse

        :return: int
        """

        return self.com_object.OrientationSupport

    @orientation_support.setter
    def orientation_support(self, value: int):
        """
        :param int value:
        """

        self.com_object.OrientationSupport = value

    @property
    def origin(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Origin() As Reference
                |     Returns or sets the origin point used to create the conical
                |     reflectline.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in Point the origin point for the conical
                |         ReflectLine hybrid shape feature.
                | 
                |          Dim Point As Reference
                |          Set Point = ReflectLine.Origin

        :return: Reference
        """

        return Reference(self.com_object.Origin)

    @origin.setter
    def origin(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Origin = value

    @property
    def source_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SourceType() As long
                |     Returns or sets whether the reflectline curve is or should be created with
                |     infinite light source (cylindrical) or with finite point light source
                |     (conical).
                |     Role: The SourceType indicates whether the created reflectline curve is
                |     compute with infinite light source for cylindrical type or with finite point
                |     light source for conical type.
                |     Legal values: 0 for cylindrical and 1 for conical.

        :return: int
        """

        return self.com_object.SourceType

    @source_type.setter
    def source_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SourceType = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the support surface used to create the
                |     reflectline.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in Surface the support surface for the
                |         RelectLine hybrid shape feature.
                | 
                |          Dim Surface As Reference
                |          Set Surface = ReflectLine.Support

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    @property
    def type_solution(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TypeSolution() As long
                |     Returns or sets whether the reflectline curve is or should be created with
                |     the normal to the support or the tangent plane to the
                |     support.
                |     Role: The TypeSolution indicates whether the created reflectline curve is
                |     compute with the angle between the normale to the support and the direction or
                |     with the angle between the tangent plane to the support and the
                |     direction.
                |     Legal values: 0 for the normal and 1 for the tangent plane.

        :return: int
        """

        return self.com_object.TypeSolution

    @type_solution.setter
    def type_solution(self, value: int):
        """
        :param int value:
        """

        self.com_object.TypeSolution = value

    def invert_orientation_direction(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertOrientationDirection()
                |     Inverts the orientation of direction. This example inverts the direction
                |     orientation of hybRefLine hybrid shape reflect line
                |     object.
                | 
                |      hybRefLine.InvertOrientationDirection

        :return: None
        """
        return self.com_object.InvertOrientationDirection()

    def invert_orientation_support(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertOrientationSupport()
                |     Inverts the orientation of support. This example inverts the support
                |     orientation of hybRefLine hybrid shape reflect line
                |     object.
                | 
                |      hybRefLine.InvertOrientationSupport

        :return: None
        """
        return self.com_object.InvertOrientationSupport()

    def __repr__(self):
        return f'HybridShapeReflectLine(name="{ self.name }")'
