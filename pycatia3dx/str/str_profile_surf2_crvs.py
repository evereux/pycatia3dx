"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrProfileSurf2Crvs(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrProfileSurf2Crvs
                | 
                | Object to manage Profile created with one plane and two curves
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstCurve() As Reference
                |     Returns or Sets the Profile's first curve.
                | 
                |     Example:
                | 
                | 
                |              This example gets the first curve of the Profile 
                |              
                | 
                |              Set RefSurface = ObjStrProfileSurf2Crvs.FirstCurve

        :return: Reference
        """

        return Reference(self.com_object.FirstCurve)

    @first_curve.setter
    def first_curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstCurve = value

    @property
    def second_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondCurve() As Reference
                |     Returns or Sets the Profile's second curve.
                | 
                |     Example:
                | 
                | 
                |              This example gets the second curve of the Profile
                |              
                |              
                | 
                |              Set RefSurface = ObjStrProfileSurf2Crvs.SecondCurve

        :return: Reference
        """

        return Reference(self.com_object.SecondCurve)

    @second_curve.setter
    def second_curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondCurve = value

    @property
    def surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Surface() As Reference
                |     Returns or Sets the Profile's surface.
                | 
                |     Example:
                | 
                | 
                |              This example gets the first surface of the Profile 
                |              
                |              
                | 
                |              Dim ObjStrProfileSurf2Crvs As StrProfileSurf2Crvs
                |              Set ObjStrProfileSurf2Crvs = ObjSfdMember.StrProfileSurf2Crvs
                |              Set RefSurface = ObjStrProfileSurf2Crvs.Surface

        :return: Reference
        """

        return Reference(self.com_object.Surface)

    @surface.setter
    def surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Surface = value

    def __repr__(self):
        return f'StrProfileSurf2Crvs(name="{ self.name }")'
