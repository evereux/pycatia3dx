"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_circle import HybridShapeCircle
from pycatia3dx.mode.reference import Reference


class HybridShapeCircle3Points(HybridShapeCircle):

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
                |                             HybridShapeCircle3Points
                | 
                | Represents the hybrid shape circle object defined using three
                | points.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes the circle three passing points.
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
    def element1(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Element1() As Reference
                |     Returns or sets the circle first passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the first passing point of the HybShpCircle3Pt
                |         hybrid shape circle in HybShpCircle3PtFirstPassingPoint
                |         point.
                | 
                |          Dim HybShpCircle3PtFirstPassingPoint As Reference
                |          Set HybShpCircle3PtFirstPassingPoint=
                |          HybShpCircle3Pt.Element1

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
                |     Returns or sets the circle second passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example sets the second passing point of the HybShpCircle3Pt
                |         hybrid shape circle as the Point2 point.
                | 
                |          HybShpCircle3Pt.Element2 Point2

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
    def element3(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Element3() As Reference
                |     Returns or sets the circle third passing point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves the third passing point of the HybShpCircle3Pt
                |         hybrid shape circle in HybShpCircle3PtThirdPassingPoint
                |         point.
                | 
                |          Dim HybShpCircle3PtThirdPassingPoint As Reference
                |          Set HybShpCircle3PtThirdPassingPoint=
                |          HybShpCircle3Pt.Element3

        :return: Reference
        """

        return Reference(self.com_object.Element3)

    @element3.setter
    def element3(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Element3 = value

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

    def remove_support(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveSupport()
                |     Removes the support surface.

        :return: None
        """
        return self.com_object.RemoveSupport()

    def __repr__(self):
        return f'HybridShapeCircle3Points(name="{ self.name }")'
