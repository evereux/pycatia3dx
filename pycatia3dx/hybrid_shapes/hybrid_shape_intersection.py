"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeIntersection(HybridShape):

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
                |                         HybridShapeIntersection
                | 
                | Represents the hybrid shape intersection feature object.
                | Role: To access the data of the hybrid shape intersection object. This data
                | includes:
                | 
                |     The first element to intersect
                |     The second element to intersect
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def element1(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Element1() As Reference
                |     Returns or sets the first element to intersect.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in FirstElem the first element to intersect for
                |         the Intersection hybrid shape feature.
                | 
                |          Dim FirstElem As Reference
                |          Set FirstElem = Intersection.Element1

        :return: Reference
        """

        return Reference(self.com_object.Element1)

    @element1.setter
    def element1(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Element1 = value

    @property
    def element2(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Element2() As Reference
                |     Returns or sets the second element to intersect.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in SecondElem the second element to intersect
                |         for the Intersection hybrid shape feature.
                | 
                |          Dim SecondElem As Reference
                |          Set SecondElem = Intersection.Element2

        :return: Reference
        """

        return Reference(self.com_object.Element2)

    @element2.setter
    def element2(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Element2 = value

    @property
    def extend_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtendMode() As long
                |     Returns or sets the ExtendMode flag for intersect.
                | 
                |     Example:
                |         This example retrieves in ExtendMode the ExtendMode to intersect for
                |         the Intersection hybrid shape feature.
                | 
                |          Dim ExtendMode As Reference
                |          Set ExtendMode = Intersection.ExtendMode
                |          ExtendMode is 0 when both "Extend Linear Supposr for intersection" are
                |          unchecked
                |          ExtendMode is 1 when "Extend Linear Supposr for intersection" for
                |          First Element is checked and for Second Element is
                |          unchecked
                |          ExtendMode is 2 when "Extend Linear Supposr for intersection" for
                |          First Element is unchecked and for Second Element is
                |          checked
                |          ExtendMode is 3 when both "Extend Linear Supposr for intersection" are
                |          checked

        :return: int
        """

        return self.com_object.ExtendMode

    @extend_mode.setter
    def extend_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ExtendMode = value

    @property
    def extrapolate_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtrapolateMode() As boolean
                |     Returns or sets the ExtrapolateMode flag for intersect.
                | 
                |     Example:
                |         This example retrieves in ExtrapolateMode the ExtrapolateMode to
                |         intersect for the Intersection hybrid shape feature.
                | 
                |          Dim ExtrapolateMode As Reference
                |          Set ExtrapolateMode = Intersection.ExtrapolateMode

        :return: bool
        """

        return self.com_object.ExtrapolateMode

    @extrapolate_mode.setter
    def extrapolate_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ExtrapolateMode = value

    @property
    def intersect_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property IntersectMode() As boolean
                |     Returns or sets the IntersectMode flag for intersect.
                | 
                |     Example:
                |         This example retrieves in IntersectMode the IntersectMode to intersect
                |         for the Intersection hybrid shape feature.
                | 
                |          Dim IntersectMode As Reference
                |          Set IntersectMode = Intersection.IntersectMode

        :return: bool
        """

        return self.com_object.IntersectMode

    @intersect_mode.setter
    def intersect_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IntersectMode = value

    @property
    def point_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PointType() As long
                |     Returns or sets the PointType flag for intersect.
                | 
                |     Example:
                |         This example retrieves in PointType the PointType to intersect for the
                |         Intersection hybrid shape feature.
                | 
                |          Dim PointType As Reference
                |          Set PointType = Intersection.PointType

        :return: int
        """

        return self.com_object.PointType

    @point_type.setter
    def point_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.PointType = value

    @property
    def solid_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SolidMode() As boolean
                |     Returns or sets the SolidMode flag for intersect.
                | 
                |     Example:
                |         This example retrieves in SolidMode the SolidMode to intersect for the
                |         Intersection hybrid shape feature.
                | 
                |          Dim SolidMode As Reference
                |          Set SolidMode = Intersection.SolidMode

        :return: bool
        """

        return self.com_object.SolidMode

    @solid_mode.setter
    def solid_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SolidMode = value

    def __repr__(self):
        return f'HybridShapeIntersection(name="{ self.name }")'
