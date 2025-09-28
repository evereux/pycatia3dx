"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_circle import HybridShapeCircle
from pycatia3dx.mode.reference import Reference


class HybridShapeCircleCtrPt(HybridShapeCircle):

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
                |                             HybridShapeCircleCtrPt
                | 
                | Represents the hybrid shape circle object defined using a center and a point on
                | the circle.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The circle center
                |     The point on the circle
                |     The surface that supports the circle
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircleCtrPt
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def center(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Center() As Reference
                |     Returns or sets the circle center.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleCenter the center of the
                |         HybShpCircle hybrid shape circle.
                | 
                |          Dim HybShpCircleCenter As Reference
                |          HybShpCircleCenter = HybShpCircle.Center

        :return: Reference
        """

        return Reference(self.com_object.Center)

    @center.setter
    def center(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Center = value

    @property
    def crossing_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CrossingPoint() As Reference
                |     Returns or sets the circle passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the passing point of the HybShpCircle hybrid
                |         shape circle in HybShpCirclePassingPoint point.
                | 
                |          Dim HybShpCirclePassingPoint As Reference
                |          Set HybShpCirclePassingPoint = HybShpCircle.CrossingPoint

        :return: Reference
        """

        return Reference(self.com_object.CrossingPoint)

    @crossing_point.setter
    def crossing_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.CrossingPoint = value

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
                |     It puts the circle on the surface.

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
        return f'HybridShapeCircleCtrPt(name="{ self.name }")'
