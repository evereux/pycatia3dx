"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.str.str_break import StrBreak
from pycatia3dx.str.str_category_mngt import StrCategoryMngt
from pycatia3dx.str.str_profile_crv import StrProfileCrv
from pycatia3dx.str.str_profile_surf_surf import StrProfileSurfSurf
from pycatia3dx.str.structure_profile import StructureProfile


class StrStiffener(StructureProfile):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATStrIDLItf.StructureProfile
                |                         StrStiffener
                | 
                | Object to manage Structure Functional Modeler Stiffener.
                | Role: Allows accessing and setting of Stiffener's data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def str_break(self) -> StrBreak:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrBreak() As StrBreak (Read Only)
                |     Returns StrBreak object
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrBreak object of the
                |              Stiffener.
                |              
                | 
                |              Set ObjStrBreak = ObjStrStiffener.StrBreak

        :return: StrBreak
        """

        return StrBreak(self.com_object.StrBreak)

    @property
    def str_category_mngt(self) -> StrCategoryMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrCategoryMngt() As StrCategoryMngt (Read Only)
                |     Returns StrCategoryMngt object
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrCategoryMngt object of the
                |              Stiffener.
                |              
                | 
                |              Set ObjStrCategoryMngt = ObjStrStiffener.StrCategoryMngt

        :return: StrCategoryMngt
        """

        return StrCategoryMngt(self.com_object.StrCategoryMngt)

    @property
    def str_profile_crv(self) -> StrProfileCrv:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfileCrv() As StrProfileCrv (Read Only)
                |     Returns StrProfileCrv object
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfileCrv object of the
                |              Stiffener.
                |              
                | 
                |              Set ObjStrProfileCrv = ObjStrStiffener.StrProfileCrv

        :return: StrProfileCrv
        """

        return StrProfileCrv(self.com_object.StrProfileCrv)

    @property
    def str_profile_surf_surf(self) -> StrProfileSurfSurf:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfileSurfSurf() As StrProfileSurfSurf (Read
                | Only)
                |     Returns StrProfileSurfSurf object
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfileSurfSurf object of the
                |              Stiffener.
                |              
                | 
                |              Set ObjProfileSurfSurf = ObjStrStiffener.StrProfileSurfSurf

        :return: StrProfileSurfSurf
        """

        return StrProfileSurfSurf(self.com_object.StrProfileSurfSurf)

    def __repr__(self):
        return f'StrStiffener(name="{ self.name }")'
