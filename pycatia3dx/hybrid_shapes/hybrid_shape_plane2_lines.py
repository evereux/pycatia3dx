"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.mode.reference import Reference


class HybridShapePlane2Lines(Plane):

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
                |                             HybridShapePlane2Lines
                | 
                | plane defined by two lines.
                | Role: Allows to access data of the plane feature passing though two
                | lines.
    
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
                |     Role: Get the first line.
                | 
                |     Parameters:
                | 
                |         oLine1
                |             first line. 
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

        return Reference(self.com_object.First)

    @first.setter
    def first(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.First = value

    @property
    def forbid_non_coplanar_lines(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ForbidNonCoplanarLines(boolean iCoplanarLines)
                |     if ForbidNonCoplanarLines = TRUE, both lines have to be on the same plane. if ForbidNonCoplanarLines = FALSE, both lines can be non coplanar.

        :return: bool
        """

        return self.com_object.ForbidNonCoplanarLines

    @forbid_non_coplanar_lines.setter
    def forbid_non_coplanar_lines(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ForbidNonCoplanarLines = value

    @property
    def second(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Second() As Reference
                |     Role: Get the second line.
                | 
                |     Parameters:
                | 
                |         oLine2
                |             second line. 
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

        return Reference(self.com_object.Second)

    @second.setter
    def second(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Second = value

    def __repr__(self):
        return f'HybridShapePlane2Lines(name="{ self.name }")'
