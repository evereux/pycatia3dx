"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeNear(HybridShape):

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
                |                         HybridShapeNear
                | 
                | The Near feature : an Near is made up of a face to process and one Near parameter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def multiple_solution(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property MultipleSolution() As Reference
                |     Role: To get_MultipleSolution on the object.
                | 
                |     Parameters:
                | 
                |         oMultipleSolution
                |             multiple element return value for CATScript applications, with
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

        return Reference(self.com_object.MultipleSolution)

    @multiple_solution.setter
    def multiple_solution(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.MultipleSolution = value

    @property
    def reference_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ReferenceElement() As Reference
                |     Role: To get_ReferenceElement on the object.
                | 
                |     Parameters:
                | 
                |         oRefElem
                |             reference element return value for CATScript applications, with
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

        return Reference(self.com_object.ReferenceElement)

    @reference_element.setter
    def reference_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ReferenceElement = value

    def __repr__(self):
        return f'HybridShapeNear(name="{ self.name }")'
