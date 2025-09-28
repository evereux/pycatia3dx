"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.point import Point
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mode.reference import Reference


class HybridShapePointBetween(Point):

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
                |                             HybridShapePointBetween
                | 
                | Represents the hybrid shape PointBetween feature object.
                | Role: To access the data of the hybrid shape PointBetween feature
                | object.
                | This data includes:
                | 
                |     The first reference point
                |     The second reference point 
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstPoint() As Reference
                |     Returns or sets the first reference point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in RefPoint1 the first reference point for the
                |         PointBetween hybrid shape feature.
                | 
                |          Dim RefPoint1 As Reference
                |          Set RefPoint1 = PointBetween.FirstPoint

        :return: Reference
        """

        return Reference(self.com_object.FirstPoint)

    @first_point.setter
    def first_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstPoint = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Returns or sets the orientation. Role:
                |     Orientation = 1 means that distance is measured from the second point
                | 
                |     Example:
                |         This example retrieves in Orient the orientation for the PointBetween
                |         hybrid shape feature.
                | 
                |          Dim Orient As long
                |          Set Orient = PointBetween.Orientation

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
    def ratio(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Ratio() As RealParam (Read Only)
                |     Get the ratio. Role:
                |     if d1 is the distance between the first point and the created point, and d2 is the distance between the first point and the second point, then ratio = d1/d2.
                | 
                |     Example:
                |         This example retrieves in ratio the orientation for the PointBetween
                |         hybrid shape feature.
                | 
                |          Dim ratio  As CATIARealParam
                |          Get ratio = PointBetween.Ratio

        :return: RealParam
        """

        return RealParam(self.com_object.Ratio)

    @property
    def second_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondPoint() As Reference
                |     Returns or sets the second reference point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in RefPoint2 the second reference point for the
                |         PointBetween hybrid shape feature.
                | 
                |          Dim RefPoint2 As Reference
                |          Set RefPoint2 = PointBetween.SecondPoint

        :return: Reference
        """

        return Reference(self.com_object.SecondPoint)

    @second_point.setter
    def second_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondPoint = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or Sets the support.
                |     Note: the support can be surface or curve. It is not
                |     mandatory
                | 
                |     Sub-element(s) supported (see Boundary object): Face and TriDimFeatEdge and
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in oSupport the support(if it exist) for the
                |         PointBetween hybrid shape feature.
                | 
                |          Dim oSupport As Reference 
                |          Set oSupport = PointBetween.Support

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    def __repr__(self):
        return f'HybridShapePointBetween(name="{ self.name }")'
