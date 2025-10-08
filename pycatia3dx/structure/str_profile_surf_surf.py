"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrProfileSurfSurf(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrProfileSurfSurf
                | 
                | Object to manage Profile created by the intersection of two
                | surfaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstSurface() As Reference
                |     Returns or Sets the Profile's first surface.
                | 
                |     Example:
                | 
                | 
                |              This example gets the first surface of the Profile
                |              
                |              
                | 
                |              Dim ObjStrProfileSurfSurf As StrProfileSurfSurf
                |              Set ObjStrProfileSurfSurf = ObjSfdStiffener.StrProfileSurfSurf
                |              Set RefSurface = ObjStrProfileSurfSurf.FirstSurface

        :return: Reference
        """

        return Reference(self.com_object.FirstSurface)

    @first_surface.setter
    def first_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstSurface = value

    @property
    def second_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondSurface() As Reference
                |     Returns or Sets the Profile's Second surface.
                | 
                |     Example:
                | 
                | 
                |              This example gets the second surface of the Profile
                |              
                |              
                | 
                |              Set RefSurface = ObjStrProfileSurfSurf.SecondSurface

        :return: Reference
        """

        return Reference(self.com_object.SecondSurface)

    @second_surface.setter
    def second_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondSurface = value

    def get_first_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFirstOffset() As Parameter
                |     Returns the first surface offset.
                | 
                |     Example:
                | 
                | 
                |              This example gets the first surface offset 
                |              
                | 
                |              Set ParmOffset = ObjStrProfileSurfSurf.GetFirstOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetFirstOffset())

    def get_second_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSecondOffset() As Parameter
                |     Returns the second surface offset.
                | 
                |     Example:
                | 
                | 
                |              This example gets the second surface offset 
                |              
                | 
                |              Set ParmOffset = ObjStrProfileSurfSurf.GetSecondOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetSecondOffset())

    def __repr__(self):
        return f'StrProfileSurfSurf(name="{ self.name }")'
