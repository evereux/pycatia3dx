"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SrsBoundingBox(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SrsBoundingBox
                | 
                | Object for SrsBoundingBox.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_math_box(self, o_math_box: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMathBox(CATSafeArrayVariant oMathBox)
                |     Get MathBox to a bounding box feature.
                | 
                |     Parameters:
                | 
                |         oMathBox
                |             bounding box which limits the space where the refence planes exist.
                |             
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the bounding box feature.
                |              
                | 
                |               Dim oMathBox(5) As Variant
                |               ObjSrsBoundingBox.GetMathBox oMathBox.

        :param tuple o_math_box:
        :return: tuple
        """
        return self.com_object.GetMathBox(o_math_box)

    def is_aft_at_origin(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAftAtOrigin() As boolean
                |     Gets the orientation of a shape representation of a ship.
                | 
                |     Returns:
                |         The orientation of the bounding box (TRUE means that orientation is the
                |         same as direction) 
                |     Example:
                | 
                | 
                |              This example retrieves the shape representation of a
                |              ship.
                |              
                | 
                |               Dim BoolIsAftAtOrigin As Boolean
                |               BoolIsAftAtOrigin = ObjSrsBoundingBox.IsAftAtOrigin

        :return: bool
        """
        return self.com_object.IsAftAtOrigin()

    def __repr__(self):
        return f'SrsBoundingBox(name="{ self.name }")'
