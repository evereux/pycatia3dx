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


class HybridShapePointOnPlane(Point):

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
                |                             HybridShapePointOnPlane
                | 
                | Point on a plane.
                | Role: Allows to access data of the point feature created on a plane with a
                | reference point or not.
                | 
                | See also:
                |     Length, Reference, HybridShapeDirection,
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstDirection() As HybridShapeDirection
                |     Returns or sets the first direction on the plane to compute the point (for
                |     stability).
                | 
                |     Example
                |     :
                |         This example retrieves in oDirection the direction of the PointOnPlane
                |         feature.
                | 
                |          Dim oDirection As CATIAHybridShapeDirection
                |          Set oDirection = PointOnPlane.FirstDirection

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
    def plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Plane() As Reference
                |     Returns or sets the support plane.
                |     Sub-element(s) supported (see Boundary object):
                |     PlanarFace.
                | 
                |     Example
                |     :
                |         This example retrieves in oPlane the supporting Plane for PointOnPlane
                |         feature.
                | 
                |          Dim oPlane As CATIAReference
                |          Set oPlane  = PointOnPlane.Plane

        :return: Reference
        """

        return Reference(self.com_object.Plane)

    @plane.setter
    def plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Plane = value

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Point() As Reference
                |     Returns or sets the reference point.
                |     This data is not mandatory, if Point is
                |     null, the projection of the origin point on the plane is
                |     taken.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example
                |     :
                |         This example retrieves in oPoint the reference point for PointOnPlane
                |         feature.
                | 
                |          Dim oPoint As CATIAReference
                |          Set oPoint  = PointOnPlane.Point

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
    def projection_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ProjectionSurface() As Reference
                |     Returns or sets the projection surface to compute the
                |     point.
                | 
                |     Example
                |     :
                |         This example retrieves in oProjSur the projection surface of the
                |         PointOnPlane feature.
                | 
                |          Dim oProjSur As CATIAReference
                |          Set oProjSur = PointOnPlane.ProjectionSurface

        :return: Reference
        """

        return Reference(self.com_object.ProjectionSurface)

    @projection_surface.setter
    def projection_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ProjectionSurface = value

    @property
    def x_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property XOffset() As Length (Read Only)
                |     Returns the X cartesian coordinate in the plane.
                | 
                |     Example
                |     :
                |         This example retrieves in oX the X coordinate for PointOnPlane
                |         feature.
                | 
                |          Dim oX As  CATIALength
                |          Set oX  = PointOnPlane.XOffset

        :return: Length
        """

        return Length(self.com_object.XOffset)

    @property
    def y_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property YOffset() As Length (Read Only)
                |     Returns the Y cartesian coordinate in the plane.
                | 
                |     Example
                |     :
                |         This example retrieves in oY the Y coordinate for PointOnPlane
                |         feature.
                | 
                |          Dim oY As  CATIALength
                |          Set oY  = PointOnPlane.YOffset

        :return: Length
        """

        return Length(self.com_object.YOffset)

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
                |         oDir
                |             second direction 
                | 
                |     See also:
                |         HybridShapeDirection

        :param float o_dir_x:
        :param float o_dir_y:
        :param float o_dir_z:
        :return: None
        """
        return self.com_object.GetSecondDirection(o_dir_x, o_dir_y, o_dir_z)

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
                |         iDir
                |             second direction 
                | 
                |     See also:
                |         HybridShapeDirection

        :param float i_dir_x:
        :param float i_dir_y:
        :param float i_dir_z:
        :return: None
        """
        return self.com_object.SetSecondDirection(i_dir_x, i_dir_y, i_dir_z)

    def __repr__(self):
        return f'HybridShapePointOnPlane(name="{ self.name }")'
