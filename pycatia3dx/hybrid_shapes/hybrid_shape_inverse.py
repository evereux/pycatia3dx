"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeInverse(HybridShape):

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
                |                         HybridShapeInverse
                | 
                | The Inverse feature : an Inverse is made up of a face to process and one Inverse parameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_inverse = com_object

    @property
    def element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Element() As Reference
                |     Role: To get the element inverted.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Element inverted return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.hybrid_shape_inverse.Element)

    @element.setter
    def element(self, value: Reference):
        """
        :param Reference value:
        """

        self.hybrid_shape_inverse.Element = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Gets or sets the element's orientation. Orientation = 1 : the element is not inverted. = -1 : the element is inverted, = 2 : the element can not be inverted. Orientation can not be set to 2.

        :return: int
        """

        return self.hybrid_shape_inverse.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.hybrid_shape_inverse.Orientation = value

    def __repr__(self):
        return f'HybridShapeInverse(name="{ self.name }")'
