"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mmr_automation_interfaces.shape import Shape
from pycatia3dx.mode.reference import Reference


class Scaling2(Shape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         Scaling2
                | 
                | Represents the Scaling2 feature object.
                | This solid feature is created from an underlying HybridShapeScaling aggregated
                | by the Scaling. Role: To access the data of the feature object. This data
                | includes:
                | 
                |     The element to be transformed using the Scaling2
                |     The reference element for the Scaling2 which is a point or a
                |     plane
                |     The ratio and its value
                | 
                | Use the CATIAShapeFactory to create Part object.
                | 
                | See also:
                |     ShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def center(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Center() As Reference
                |     Returns or sets the reference element.This element can be a point or a
                |     plane.
                |     To set the property, you can use one of the following Boundary objects:
                |     PlanarFace or Vertex.
                | 
                |     Example:
                |         This example retrieves in RefElem the reference element for the
                |         Scaling2 hybrid shape feature.
                | 
                |          Dim RefElem As Reference
                |          Set RefElem = Scaling2.Center

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
    def ratio(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Ratio() As RealParam (Read Only)
                |     Returns the scaling ratio.

        :return: RealParam
        """

        return RealParam(self.com_object.Ratio)

    @property
    def ratio_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RatioValue() As double
                |     Returns or sets the scaling ratio value.
                | 
                |     Example:
                |         This example retrieves in Value the ratio value for the Scaling hybrid
                |         shape feature.
                | 
                |          Dim Value As double
                |          Set Value = Scaling2.RatioValue

        :return: float
        """

        return self.com_object.RatioValue

    @ratio_value.setter
    def ratio_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.RatioValue = value

    def __repr__(self):
        return f'Scaling2(name="{ self.name }")'
