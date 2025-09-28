"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mode.reference import Reference


class HybridShapePlaneBetween(Plane):

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
                |                             HybridShapePlaneBetween

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstElement() As Reference
                |     Returns or sets the first reference Plane.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in RefPlane1 the first reference Plane for the
                |         PlaneBetween hybrid shape feature.
                | 
                |          Dim RefPlane1 As Reference
                |          Set RefPlane1 = PlaneBetween.FirstPlane

        :return: Reference
        """

        return Reference(self.com_object.FirstElement)

    @first_element.setter
    def first_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstElement = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Returns or sets the orientation. Role:
                |     Orientation = 1 means that distance is measured from the second Plane
                | 
                |     Example:
                |         This example retrieves in Orient the orientation for the PlaneBetween
                |         hybrid shape feature.
                | 
                |          Dim Orient As long
                |          Set Orient = PlaneBetween.Orientation

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
                |     if d1 is the distance between the first Plane and the created Plane, and d2 is the distance between the first Plane and the second Plane, then ratio = d1/d2.
                | 
                |     Example:
                |         This example retrieves in ratio the orientation for the PlaneBetween
                |         hybrid shape feature.
                | 
                |          Dim ratio  As CATIARealParam
                |          Get ratio = PlaneBetween.Ratio

        :return: RealParam
        """

        return RealParam(self.com_object.Ratio)

    @property
    def second_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondElement() As Reference
                |     Returns or sets the second reference Plane.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in RefPlane2 the second reference Plane for the
                |         PlaneBetween hybrid shape feature.
                | 
                |          Dim RefPlane2 As Reference
                |          Set RefPlane2 = PlaneBetween.SecondPlane

        :return: Reference
        """

        return Reference(self.com_object.SecondElement)

    @second_element.setter
    def second_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondElement = value

    def __repr__(self):
        return f'HybridShapePlaneBetween(name="{ self.name }")'
