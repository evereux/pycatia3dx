"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.str.str_category_mngt import StrCategoryMngt
from pycatia3dx.str.str_profile_crv import StrProfileCrv
from pycatia3dx.str.str_profile_pt_length import StrProfilePtLength
from pycatia3dx.str.str_profile_pt_limit import StrProfilePtLimit
from pycatia3dx.str.str_profile_pt_pt import StrProfilePtPt
from pycatia3dx.str.str_profile_surf2_crvs import StrProfileSurf2Crvs
from pycatia3dx.str.str_profile_surf_surf import StrProfileSurfSurf
from pycatia3dx.str.structure_profile import StructureProfile


class StructureMember(StructureProfile):

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
                |                         StructureMember
                | 
                | Object to manage Structure Member.
                | Role: Allows accessing and setting of structure Member's data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def str_category_mngt(self) -> StrCategoryMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrCategoryMngt() As StrCategoryMngt (Read Only)
                |     Returns the StrCategoryMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrCategoryMngt of the
                |              SddMember.
                |              
                | 
                |              Set ObjStrProfilePtPt = ObjSddMember.StrCategoryMngt

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
                |     Returns the StrProfileCrv object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfileCrv of the
                |              SddMember.
                |              
                | 
                |              Set ObjStrProfilePtPt = ObjSddMember.StrProfileCrv

        :return: StrProfileCrv
        """

        return StrProfileCrv(self.com_object.StrProfileCrv)

    @property
    def str_profile_pt_length(self) -> StrProfilePtLength:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfilePtLength() As StrProfilePtLength (Read
                | Only)
                |     Returns the StrProfilePtLength object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfilePtLength of the
                |              SddMember.
                |              
                | 
                |              Set ObjStrProfilePtPt = ObjSddMember.StrProfilePtLength

        :return: StrProfilePtLength
        """

        return StrProfilePtLength(self.com_object.StrProfilePtLength)

    @property
    def str_profile_pt_limit(self) -> StrProfilePtLimit:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfilePtLimit() As StrProfilePtLimit (Read Only)
                |     Returns the StrProfilePtLimit object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfilePtLimit of the
                |              SddMember.
                |              
                | 
                |              Set ObjStrProfilePtPt = ObjSddMember.StrProfilePtLimit

        :return: StrProfilePtLimit
        """

        return StrProfilePtLimit(self.com_object.StrProfilePtLimit)

    @property
    def str_profile_pt_pt(self) -> StrProfilePtPt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfilePtPt() As StrProfilePtPt (Read Only)
                |     Returns the StrProfilePtPt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfilePtPt of the
                |              SddMember.
                |              
                | 
                |              Set ObjStrProfilePtPt = ObjSddMember.StrProfilePtPt

        :return: StrProfilePtPt
        """

        return StrProfilePtPt(self.com_object.StrProfilePtPt)

    @property
    def str_profile_surf2_crvs(self) -> StrProfileSurf2Crvs:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfileSurf2Crvs() As StrProfileSurf2Crvs (Read
                | Only)
                |     Returns the StrProfileSurf2Crvs object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfileSurf2Crvs of the
                |              SddMember.
                |              
                | 
                |              Set ObjStrProfilePtPt = ObjSddMember.StrProfileSurf2Crvs

        :return: StrProfileSurf2Crvs
        """

        return StrProfileSurf2Crvs(self.com_object.StrProfileSurf2Crvs)

    @property
    def str_profile_surf_surf(self) -> StrProfileSurfSurf:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfileSurfSurf() As StrProfileSurfSurf (Read
                | Only)
                |     Returns the StrProfileSurfSurf object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfileSurfSurf of the
                |              SddMember.
                |              
                | 
                |              Set ObjStrProfilePtPt = ObjSddMember.StrProfileSurfSurf

        :return: StrProfileSurfSurf
        """

        return StrProfileSurfSurf(self.com_object.StrProfileSurfSurf)

    def __repr__(self):
        return f'StructureMember(name="{ self.name }")'
