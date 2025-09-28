#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class HybridShape(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     HybridShape
                | 
                | Represents the hybrid shape object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def thickness(self) -> 'HybridShape':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Thickness() As HybridShape (Read Only)
                |     Returns the thickness of the hybrid shape.
                |     The thickness is a CATIAHybridShapeThickness.
                | 
                |     Example:
                |         The following example returns the thickness ExtrudeThickness of the
                |         extrude Extrude.1 as the origin point of the axis system
                |         AxisSystem0:
                | 
                |          Dim Extrude1 As AnyObject
                |          Set Extrude1 = HybridBody1.HybridShapes.Item  ( "Extrude.1" ) 
                |          Dim Thickness1 As HybridShapeThickness
                |          Set Thickness1 = Extrude1.Thickness

        :return: HybridShape
        """

        return HybridShape(self.com_object.Thickness)

    def append_hybrid_shape(self, i_hybrid_shape: 'HybridShape') -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub AppendHybridShape(HybridShape iHybridShape)
                |     Appends a hybrid shape to another hybrid shape.
                | 
                |     Parameters:
                | 
                |         iHybridShape
                |             The hybrid shape to append. 
                | 
                |     Example:
                |         This example appends the hybrid shape newHybridShape to the hybrid
                |         shape oldHybridShape:
                | 
                |          oldHybridShape.AppendHybridShape (newHybridShape)

        :param HybridShape i_hybrid_shape:
        :return: None
        """
        return self.com_object.AppendHybridShape(i_hybrid_shape.com_object)

    def compute(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Compute()
                |     Computes the result of the hybrid shape.

        :return: None
        """
        return self.com_object.Compute()

    def __repr__(self):
        return f'HybridShape(name="{ self.name }")'
