"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_circle import HybridShapeCircle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapeCircle2PointsRad(HybridShapeCircle):

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
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircle2PointsRad
                | 
                | Represents the hybrid shape circle object defined using two points and a
                | radius.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The circle two passing points
                |     The circle radius
                |     The surface that supports the circle
                |     The circle orientation
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircle2PointsRad
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def diameter(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Diameter() As Length (Read Only)
                |     Returns the circle diameter. It is expressed as a Length literal. Succeeds
                |     only if DiameterMode is set to True. 
                | 
                | Example:
                |     This example retrieves in HybShpCircleDiameter the diameter of the
                |     HybShpCircle hybrid shape circle feature
                | 
                |      Dim HybShpCircleDiameter As Length
                |      HybShpCircleDiameter = HybShpCircle.Diameter

        :return: Length
        """

        return Length(self.com_object.Diameter)

    @property
    def diameter_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DiameterMode() As boolean
                |     Returns or sets the DiameterMode.
                |     Legal values: True implies diameter False implies radius (default). When
                |     DiameterMode is changed, Radius/Diameter value, which is stored will not be
                |     modified.
                | 
                |     Example:
                | 
                |           This example sets that the DiameterMode of
                |           the HybShpCircle hybrid shape circle feature
                |           
                | 
                |           HybShpCircle.DiameterMode = True

        :return: bool
        """

        return self.com_object.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DiameterMode = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Returns or sets the circle orientation.
                |     Role: The circle orientation indicates which side of the line made up using
                |     the two passing points is used to create the major part of the circle. It is
                |     determined using the cross product of the normal to the suppport and the vector
                |     made up using the two passing points (Pt1-Pt2).
                |     Legal values: 1 to state that the major part of the circle is or should be
                |     created on the side of the line shown by the vector resulting from this cross
                |     product, and -1 otherwise.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleOrientation the orientation of
                |         the HybShpCircle hybrid shape circle.
                | 
                |          HybShpCircleOrientation = HybShpCircle.Orientation

        :return: int
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation = value

    @property
    def pt1(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Pt1() As Reference
                |     Returns or sets the circle first passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the first passing point of the HybShpCircle
                |         hybrid shape circle in HybShpCircleFirstPassingPoint
                |         point.
                | 
                |          Dim HybShpCircleFirstPassingPoint As Reference
                |          Set HybShpCircleFirstPassingPoint = HybShpCircle.Pt1

        :return: Reference
        """

        return Reference(self.com_object.Pt1)

    @pt1.setter
    def pt1(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Pt1 = value

    @property
    def pt2(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Pt2() As Reference
                |     Returns or sets the circle second passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example sets the second passing point of the HybShpCircle hybrid
                |         shape circle as the Point12 point.
                | 
                |          HybShpCircle.Pt2 Point12

        :return: Reference
        """

        return Reference(self.com_object.Pt2)

    @pt2.setter
    def pt2(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Pt2 = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Radius() As Length (Read Only)
                |     Returns the circle radius.
                | 
                |     Parameters:
                | 
                |         Radius
                |             The circle radius, expressed as a Length literal. Succeeds only if
                |             DiameterMode is set to False. 
                | 
                |     Example:
                |         This example retrieves in HybShpCircleRadius the radius of the
                |         HybShpCircle hybrid shape circle.
                | 
                |          Dim HybShpCircleRadius As Length
                |          HybShpCircleRadius = HybShpCircle.Radius

        :return: Length
        """

        return Length(self.com_object.Radius)

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the circle support surface.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleSupportSurf the support surface
                |         of the HybShpCircle hybrid shape circle.
                | 
                |          Dim HybShpCircleSupportSurf As Reference 
                |          HybShpCircleSupportSurf = HybShpCircle.Support

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    def is_geodesic(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func IsGeodesic() As boolean
                |     Queries whether the circle is geodesic or not.
                | 
                |     Parameters:
                | 
                |         oGeod
                |             geodesic type : when TRUE, the circle is geodesic.

        :return: bool
        """
        return self.com_object.IsGeodesic()

    def set_geometry_on_support(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetGeometryOnSupport()
                |     Sets GeometryOnSupport of circle.
                |     It puts the circle on the surface. S_OK if OK, E_FAIL if fail

        :return: None
        """
        return self.com_object.SetGeometryOnSupport()

    def unset_geometry_on_support(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub UnsetGeometryOnSupport()
                |     Inactivates GeometryOnSupport of circle.
                |     Note: The circle becomes euclidean.

        :return: None
        """
        return self.com_object.UnsetGeometryOnSupport()

    def __repr__(self):
        return f'HybridShapeCircle2PointsRad(name="{ self.name }")'
