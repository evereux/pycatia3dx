"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_circle import HybridShapeCircle
from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapeCircleCtrRad(HybridShapeCircle):

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
                |                             HybridShapeCircleCtrRad
                | 
                | Represents the hybrid shape circle object defined using a center and a
                | radius.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The circle center
                |     The circle radius
                |     The surface that supports the circle
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircleCtrRad
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
    def diameter(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Diameter() As Length (Read Only)
                |     Returns the circle diameter.
                |     It is expressed as a Length literal. Succeeds only if DiameterMode is set
                |     to True. 
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
    def first_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstDirection() As HybridShapeDirection
                |     Returns or sets the first direction used to set the angles reference.
                |     
                | Example:
                |     This example retrieves in myHybridShapeDirection the first direction of the
                |     HybShpCircle hybrid shape circle feature
                | 
                |      Dim myHybridShapeDirection As CATIAHybridShapeDirection 
                |      myHybridShapeDirection = HybShpCircle.FirstDirection
                |      
                | 
                |     See also:
                |         HybridShapeDirection

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.FirstDirection)

    @first_direction.setter
    def first_direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.FirstDirection = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Radius() As Length (Read Only)
                |     Returns the circle radius. It is expressed as a Length literal. Succeeds
                |     only if DiameterMode is set to False. 
                | Example:
                |     This example retrieves in HybShpCircleRadius the radius of the HybShpCircle
                |     hybrid shape circle.
                | 
                |      Dim HybShpCircleRadius As Length
                |      HybShpCircleRadius = HybShpCircle.Radius

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

    def get_second_direction(self, o_dir_x: float, o_dir_y: float, o_dir_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetSecondDirection(double oDirX,double oDirY,double oDirZ)
                |     Gets the second direction on the plane to compute the point (for
                |     stability).
                |     This direction has to be kept perpendicular to the first
                |     direction
                | 
                |     Parameters:
                | 
                |         oDirX,
                |             oDirY, oDirZ. second direction 
                | 
                |     See also:
                |         HybridShapeDirection

        :param float o_dir_x:
        :param float o_dir_y:
        :param float o_dir_z:
        :return: None
        """
        return self.com_object.GetSecondDirection(o_dir_x, o_dir_y, o_dir_z)

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

    def set_second_direction(self, i_dir_x: float, i_dir_y: float, i_dir_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSecondDirection(double iDirX,double iDirY,double iDirZ)
                |     Sets the second direction on the plane to compute the point (for
                |     stability).
                |     This direction has to be kept perpendicular to the first
                |     direction
                | 
                |     Parameters:
                | 
                |         iDirX,
                |             iDirY, iDirZ. second direction 
                | 
                |     See also:
                |         HybridShapeDirection

        :param float i_dir_x:
        :param float i_dir_y:
        :param float i_dir_z:
        :return: None
        """
        return self.com_object.SetSecondDirection(i_dir_x, i_dir_y, i_dir_z)

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
        return f'HybridShapeCircleCtrRad(name="{ self.name }")'
