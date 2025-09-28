"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.mode.reference import Reference


class HybridShapePlaneAngle(Plane):

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
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneAngle
                | 
                | Represents the hybrid shape plane angle feature object.
                | Role: To access the data of the hybrid shape plane angle feature object,
                | created with an angle to another plane. This data includes:
                | 
                |     The rotation axis
                |     The rotation angle
                |     The reference plane
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePlaneAngle
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
                | Property Angle() As Angle (Read Only)
                |     Returns the rotation angle.

        :return: Angle
        """

        return Angle(self.com_object.Angle)

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Returns or sets the plane orientation.
                |     Role: The orientation allows you to invert the plane from the reference
                |     plane.
                |     Legal values: the orientation is 1 if the plane orientation is not
                |     inverted, and -1 otherwise.

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
    def plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Plane() As Reference
                |     Returns or sets the reference plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace.

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
    def projection_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ProjectionMode() As boolean
                |     Gets or sets the projection mode status. ProjectionMode = TRUE : Rotation axis will be projected on to reference plane. = FALSE(default) : Rotation axis will be as it is. This example retrieves in ProjMode the projection mode status for the PlaneAngle hybrid shape feature.
                | 
                |      Dim ProjMode As boolean
                |      ProjMode = PlaneAngle.ProjectionMode

        :return: bool
        """

        return self.com_object.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ProjectionMode = value

    @property
    def revol_axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RevolAxis() As Reference
                |     Returns or sets the rotation axis.
                |     Sub-element(s) supported (see Boundary object): RectilinearTriDimFeatEdge,
                |     RectilinearBiDimFeatEdge or RectilinearMonoDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.RevolAxis)

    @revol_axis.setter
    def revol_axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RevolAxis = value

    def __repr__(self):
        return f'HybridShapePlaneAngle(name="{ self.name }")'
