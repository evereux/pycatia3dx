"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.point import Point
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapePointCoord(Point):

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
                |                             HybridShapePointCoord
                | 
                | Point defined by coordinates.
                | Role: To access data of the point feature created with its cartesian
                | coordinates.
                | 
                | See also:
                |     Length
                | See also:
                |     Reference
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def pt_ref(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PtRef() As Reference
                |     Returns or Sets the reference point for PointCoord
                |     feature.
                |     This data is not mandatory, if element is null, the origin point is
                |     taken.
                |     When an element is given, X, Y and Z are measured starting from this
                |     point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example
                |     :
                |         This example retrieves in oPtRef the reference point for PointCoord
                |         feature.
                | 
                |          Dim oPtRef As CATIAReference
                |          Set oPtRef  = PointCoord.PtRef

        :return: Reference
        """

        return Reference(self.com_object.PtRef)

    @pt_ref.setter
    def pt_ref(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PtRef = value

    @property
    def ref_axis_system(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RefAxisSystem() As Reference
                |     Returns or Sets the reference Axis System for PointCoord
                |     feature.
                |     This data is not mandatory, if element is null, the absolute axis system is
                |     taken.
                |     When an element is given, X, Y and Z are considered in this Axis
                |     system.
                |     If reference point is not specified, X,Y and Z are measured from origin of
                |     this axis system. *
                | 
                |     Example
                |     :
                |         This example retrieves in oRefAxis the reference Axis System for
                |         PointCoord feature.
                | 
                |          Dim oRefAxis As CATIAReference
                |          Set oRefAxis  = PointCoord.RefAxisSystem

        :return: Reference
        """

        return Reference(self.com_object.RefAxisSystem)

    @ref_axis_system.setter
    def ref_axis_system(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RefAxisSystem = value

    @property
    def x(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property X() As Length (Read Only)
                |     Returns X coordinate of the point.
                | 
                |     Example
                |     :
                |         This example retrieves in oX the X coordinate for the PointCoord hybrid
                |         shape feature.
                | 
                |          Dim oX As CATIALength
                |          Set oX = PointCoord.X

        :return: Length
        """

        return Length(self.com_object.X)

    @property
    def y(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Y() As Length (Read Only)
                |     Returns Y coordinate of the point.
                | 
                |     Example
                |     :
                |         This example retrieves in oY the Y coordinate for the PointCoord hybrid
                |         shape feature.
                | 
                |          Dim oY As CATIALength
                |          Set oY = PointCoord.Y

        :return: Length
        """

        return Length(self.com_object.Y)

    @property
    def z(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Z() As Length (Read Only)
                |     Returns Z coordinate of the point.
                | 
                |     Example
                |     :
                |         This example retrieves in oZ the Z coordinate for the PointCoord hybrid
                |         shape feature.
                | 
                |          Dim oZ As CATIALength
                |          Set oZ = PointCoord.Z

        :return: Length
        """

        return Length(self.com_object.Z)

    def __repr__(self):
        return f'HybridShapePointCoord(name="{ self.name }")'
