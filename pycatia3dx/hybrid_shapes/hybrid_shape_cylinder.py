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


class HybridShapeCylinder(HybridShape):

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
                |                         HybridShapeCylinder
                | 
                | Represents the hybrid shape Cylinder feature object.
                | Role: To access the data of the hybrid shape Cylinder feature object. This data
                | includes:
                | 
                |     The center of the Cylinder
                |     The Radius of the Cylinder
                |     Length of Cylinder in the given extrusion direction
                |     Length of Cylinder opposite to extrusion direction
                |     Direction of extrusion for cylinder.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCylinder
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
                |     Returns or sets the center of the cylinder object.
                | 
                |     Example:
                |         This example retrieves in CylinderCenter the center of the Cylinder,
                |         for the Cylinder hybrid shape feature.
                | 
                |          Dim CylinderCenter As Reference 
                |          Set CylinderCenter = Cylinder.Center

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
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Returns or sets the direction of the cylinder object.
                | 
                |     Example:
                |         This example retrieves in CylinderDirection the direction of extrusion
                |         of the Cylinder, for the Cylinder hybrid shape
                |         feature.
                | 
                |          Dim CylinderDirection As HybridShapeDirection 
                |          Set CylinderDirection = Cylinder.Direction

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
    def length1(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Length1() As Length
                |     Returns or sets the length of the cylinder object in the given extrusion
                |     direction.
                | 
                |     Example:
                |         This example retrieves in CylinderLength1 the length of the Cylinder in
                |         the given extrusion direction, for the Cylinder hybrid shape
                |         feature.
                | 
                |          Dim CylinderLength1 As Length
                |          Set CylinderLength1 = Cylinder.Length1

        :return: Length
        """

        return Length(self.com_object.Length1)

    @length1.setter
    def length1(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.Length1 = value

    @property
    def length2(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Length2() As Length
                |     Returns or sets the length of the cylinder object in the opposite direction
                |     of given extrusion direction.
                | 
                |     Example:
                |         This example retrieves in CylinderLength2 the length of the Cylinder in
                |         the opposite direction of the given extrusion direction, for the Cylinder
                |         hybrid shape feature.
                | 
                |          Dim CylinderLength2 As Length
                |          Set CylinderLength2 = Cylinder.Length2

        :return: Length
        """

        return Length(self.com_object.Length2)

    @length2.setter
    def length2(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.Length2 = value

    @property
    def orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation(boolean iOrientation)
                |     Returns or sets the the inversion of extrusion direction.
                | 
                |     Example:
                |         This example retrieves in IsInverted the inversion status of extrusion
                |         direction for the Cylinder hybrid shape feature.
                | 
                |          Dim IsInverted As boolean
                |          Set IsInverted = Cylinder.Orientation

        :return: bool
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Orientation = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Radius() As Length
                |     Returns or sets the radius of the cylinder object.
                | 
                |     Example:
                |         This example retrieves in CylinderRadius the radius of the Cylinder,
                |         for the Cylinder hybrid shape feature.
                | 
                |          Dim CylinderRadius As Length
                |          Set CylinderRadius = Cylinder.Radius

        :return: Length
        """

        return Length(self.com_object.Radius)

    @radius.setter
    def radius(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.Radius = value

    @property
    def symmetrical_extension(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SymmetricalExtension() As boolean
                |     Gets or Sets the symmetrical extension of Cylinder (Length 2 = -Length 1).
                | 
                |     Parameters:
                | 
                |         iSym
                |             Symetry flag

        :return: bool
        """

        return self.com_object.SymmetricalExtension

    @symmetrical_extension.setter
    def symmetrical_extension(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SymmetricalExtension = value

    def invert_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertOrientation()
                |     Inverts the Orientation of Cylinder object.
                | 
                |     Example:
                |         This example inverts the orientation for the Cylinder hybrid shape
                |         feature.
                | 
                |          Cylinder.InvertOrientation

        :return: None
        """
        return self.com_object.InvertOrientation()

    def __repr__(self):
        return f'HybridShapeCylinder(name="{ self.name }")'
