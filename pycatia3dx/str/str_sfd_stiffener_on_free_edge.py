"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.str.str_break import StrBreak
from pycatia3dx.str.str_category_mngt import StrCategoryMngt
from pycatia3dx.str.str_material_mngt import StrMaterialMngt
from pycatia3dx.str.str_profile_on_limits import StrProfileOnLimits
from pycatia3dx.str.str_profile_on_opening import StrProfileOnOpening
from pycatia3dx.str.structure_profile import StructureProfile


class StrSfdStiffenerOnFreeEdge(StructureProfile):

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
                |                         StrSfdStiffenerOnFreeEdge
                | 
                | Object to manage Structure Functional Modeler
                | StiffenerOnFreeEdge.
                | Role: Allows accessing and setting of SFE(StiffenerOnFreeEdge)'s
                | data.
    
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
                |     Returns the StrBreak object.

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
                |     Returns the StrCategoryMngt object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrCategoryMngt the StrCategoryMngt
                |              object
                |              of the SfdStiffenerOnFreeEdge
                |              
                | 
                |              Dim ObjStrCategoryMngt As StrCategoryMngt
                |              Set ObjStrCategoryMngt = SfdStiffenerOnFreeEdge.StrCategoryMngt

        :return: StrCategoryMngt
        """

        return StrCategoryMngt(self.com_object.StrCategoryMngt)

    @property
    def str_material_mngt(self) -> StrMaterialMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrMaterialMngt() As StrMaterialMngt (Read Only)
                |     Returns the StrMaterialMngt object.

        :return: StrMaterialMngt
        """

        return StrMaterialMngt(self.com_object.StrMaterialMngt)

    @property
    def str_profile_on_limits(self) -> StrProfileOnLimits:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfileOnLimits() As StrProfileOnLimits (Read
                | Only)
                |     Returns StrProfileOnLimits object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrProfileOnLimits the
                |              StrProfileOnLimits object
                |              of the SfdStiffenerOnFreeEdge
                |              
                | 
                |              Dim ObjSfdStiffenerOnFreeEdge As
                |              SfdStiffenerOnFreeEdge
                |              Set ObjSfdStiffenerOnFreeEdge = ObjSfdStiffeners.AddStiffenerOnFreeEdge
                |              Dim ObjStrProfileOnLimits As StrProfileOnLimits
                |              Set ObjStrProfileOnLimits = ObjSfdStiffenerOnFreeEdge.StrProfileOnLimits

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
                |     Returns StrProfileOnOpening object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrProfileOnOpening the
                |              StrProfileOnOpening object
                |              of the SfdStiffenerOnFreeEdge
                |              
                | 
                |              Dim ObjStrProfileOnOpening As StrProfileOnOpening
                |              Set ObjStrProfileOnOpening = SfdStiffenerOnFreeEdge.StrProfileOnOpening

        :return: StrProfileOnOpening
        """

        return StrProfileOnOpening(self.com_object.StrProfileOnOpening)

    def __repr__(self):
        return f'StrSfdStiffenerOnFreeEdge(name="{ self.name }")'
