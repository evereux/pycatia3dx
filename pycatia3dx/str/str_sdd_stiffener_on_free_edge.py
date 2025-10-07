"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.str.sdd_support_plate_mngt import SddSupportPlateMngt
from pycatia3dx.str.str_category_mngt import StrCategoryMngt
from pycatia3dx.str.str_profile_crv import StrProfileCrv
from pycatia3dx.str.str_profile_on_limits import StrProfileOnLimits
from pycatia3dx.str.str_profile_on_opening import StrProfileOnOpening
from pycatia3dx.str.structure_profile import StructureProfile


class StrSddStiffenerOnFreeEdge(StructureProfile):

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
                |                         StrSddStiffenerOnFreeEdge
                | 
                | Object to manage SDD Stiffener On Free Edge.
                | Role: Allows accessing and setting of Stiffener On Free Edge
                | data.
                | 
                | See also:
                |     SddStiffenerMngt
                | Example:
                | 
                | 
                |          This example retrieves in SddStiffenerOnFreeEdge.
                |          
                | 
                |          Dim ObjSddStiffenerOnFreeEdge As
                |          StrSddStiffenerOnFreeEdge
                |          Set ObjSddStiffenerOnFreeEdge = ObjSddProductStiffenerOnFreeEdge.StrSddStiffenerOnFreeEdge
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def sdd_support_plate_mngt(self) -> SddSupportPlateMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SddSupportPlateMngt() As SddSupportPlateMngt (Read
                | Only)
                |     Returns the SddSupportPlateMngt object. SddSupportPlateMngt can be used to
                |     manage the Reference Support Plate and other support Plates.
                |     
                |     This example retrieves SddSupportPlateMngt of the
                |     StrSddStiffenerOnFreeEdge.
                | 
                |      Set ObjStrCategoryMngt = ObjStrSddStiffenerOnFreeEdge.SddSupportPlateMngt

        :return: SddSupportPlateMngt
        """

        return SddSupportPlateMngt(self.com_object.SddSupportPlateMngt)

    @property
    def str_category_mngt(self) -> StrCategoryMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrCategoryMngt() As StrCategoryMngt (Read Only)
                |     Returns the StrCategoryMngt object. StrCategoryMngt can be used to set the
                |     category depending on whether to create a Stiffener On Free Edge or a Face
                |     Plate.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrCategoryMngt of the
                |              StrSddStiffenerOnFreeEdge.
                |              
                | 
                |              Set ObjStrCategoryMngt = ObjStrSddStiffenerOnFreeEdge.StrCategoryMngt

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

        :return: StrProfileCrv
        """

        return StrProfileCrv(self.com_object.StrProfileCrv)

    @property
    def str_profile_on_limits(self) -> StrProfileOnLimits:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfileOnLimits() As StrProfileOnLimits (Read
                | Only)
                |     The Stiffener On Free Edge can be of the following three types depending on
                |     the web support: -> Stiffener On Free Edge on a Limit of Plate. -> Stiffener On
                |     Free Edge on the edge of the opening on the Plate. -> Stiffener On Free Edge on
                |     a Limit extracted Curve of the Plate. - This is possible by using GSMExtract in
                |     contextual menu in the UI. - When we use this CATIASddStiffenerOnFreeEdge
                |     interface, the curve has to extracted prior to creation of Stiffener On Free
                |     Edge. The three properties below allow access to the specific type of profile.
                |     Please refer to StrProfileOnLimits, StrProfileOnOpening or StrProfileCrv as the
                |     case may be for further details.

        :return: StrProfileOnLimits
        """

        return StrProfileOnLimits(self.com_object.StrProfileOnLimits)

    @property
    def str_profile_on_opening(self) -> StrProfileOnOpening:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfileOnOpening() As StrProfileOnOpening (Read
                | Only)

        :return: StrProfileOnOpening
        """

        return StrProfileOnOpening(self.com_object.StrProfileOnOpening)

    def __repr__(self):
        return f'StrSddStiffenerOnFreeEdge(name="{ self.name }")'
