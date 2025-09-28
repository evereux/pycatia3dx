"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.point import Point
from pycatia3dx.mode.reference import Reference


class HybridShapePointCenter(Point):

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
                |                             HybridShapePointCenter
                | 
                | Represents the hybrid shape PointCenter feature object.
                | Role: To access the data of the hybrid shape PointCenter feature object. It has
                | been created by the CATIAHybridShapeFactory. This data
                | includes:
                | 
                |     The circle, ellipsa element 
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Element() As Reference
                |     Returns or sets the circle, ellipse or sphere.
                |     Sub-element(s) supported (see Boundary object): Edge.
                | 
                |     Example
                |     :
                |         This example retrieves in Ref_Circle the center point for the
                |         PointCenter hybrid shape feature.
                | 
                |          Dim Ref_Circle As Reference
                |          Set Ref_Circle = PointCenter.Element

        :return: Reference
        """

        return Reference(self.com_object.Element)

    @element.setter
    def element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Element = value

    def __repr__(self):
        return f'HybridShapePointCenter(name="{ self.name }")'
