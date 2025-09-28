"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.mode.reference import Reference


class HybridShapePlane3Points(Plane):

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
                |                             HybridShapePlane3Points
                | 
                | Represents the hybrid shape plane through three points feature
                | object.
                | Role: Allows to access data of the plane feature passing though three points.
                | This data includes:
                | 
                |     The first point
                |     The second point
                |     The third point
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
    def first(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property First() As Reference
                |     Returns or sets the first point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example: This example retrieves in FirstPoint the first point for the Plane
                |     passing through three points hybrid shape feature.
                | 
                |      Dim FirstPoint As Reference
                |      Set FirstPoint = Plane3Points.First

        :return: Reference
        """

        return Reference(self.com_object.First)

    @first.setter
    def first(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.First = value

    @property
    def second(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Second() As Reference
                |     Returns or sets the second point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example: This example retrieves in SecondPoint the second point for the
                |     Plane passing through three points hybrid shape feature.
                | 
                |      Dim SecondPoint As Reference
                |      Set SecondPoint = Plane3Points.Second

        :return: Reference
        """

        return Reference(self.com_object.Second)

    @second.setter
    def second(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Second = value

    @property
    def third(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Third() As Reference
                |     Returns or sets the third point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example: This example retrieves in ThirdPoint the third point for the Plane
                |     passing through three points hybrid shape feature.
                | 
                |      Dim ThridPoint As Reference
                |      Set ThirdPoint = Plane3Points.Third

        :return: Reference
        """

        return Reference(self.com_object.Third)

    @third.setter
    def third(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Third = value

    def __repr__(self):
        return f'HybridShapePlane3Points(name="{ self.name }")'
