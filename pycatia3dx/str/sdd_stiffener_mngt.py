"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.sdd_product_stiffener import SddProductStiffener
from pycatia3dx.str.sdd_product_stiffener_on_free_edge import SddProductStiffenerOnFreeEdge


class SddStiffenerMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SddStiffenerMngt
                | 
                | Object to manage the SDD Stiffeners.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_stiffener(self) -> SddProductStiffener:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddStiffener() As SddProductStiffener
                |     Returns a Stiffener created with all the data structure. For setting
                |     further attributes please refer to StrCategoryMngt, StrMaterialMngt,
                |     StrSectionMngt, StrOpenings, StrProfileLimitMngt objects. Role: Create a
                |     Stiffener with all the data structure.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example creates a SddProductStiffener
                |              
                | 
                |              Dim ObjSddStiffenerMngt As SddStiffenerMngt
                |              SFDProdSel.Add ObjVPMRootOccurrence
                |              Set ObjSddStiffenerMngt = ObjSelection.FindObject("CATIASddStiffenerMngt")
                |              Dim ObjSddProductStiffener As SddProductStiffener
                |              Set ObjSddProductStiffener = ObjSddStiffenerMngt.AddStiffener

        :return: SddProductStiffener
        """
        return SddProductStiffener(self.com_object.AddStiffener())

    def add_stiffener_on_free_edge(self) -> SddProductStiffenerOnFreeEdge:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddStiffenerOnFreeEdge() As SddProductStiffenerOnFreeEdge
                |     Returns a Stiffener On Free Edge created with all the data structure. For
                |     setting further attributes please refer to StrCategoryMngt, StrMaterialMngt,
                |     StrSectionMngt, StrOpenings, StrProfileLimitMngt objects. Role: Create a
                |     Stiffener with all the data structure.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example creates a
                |              SddProductStiffenerOnFreeEdge
                |              
                | 
                |              Dim ObjSddStiffenerMngt As SddStiffenerMngt
                |              SFDProdSel.Add ObjVPMRootOccurrence
                |              Set ObjSddStiffenerMngt = ObjSelection.FindObject("CATIASddStiffenerMngt")
                |              Dim ObjSddProductStiffenerOnFreeEdge As
                |              SddProductStiffenerOnFreeEdge
                |              Set ObjSddProductStiffenerOnFreeEdge = ObjSddStiffenerMngt.AddStiffenerOnFreeEdge

        :return: SddProductStiffenerOnFreeEdge
        """
        return SddProductStiffenerOnFreeEdge(self.com_object.AddStiffenerOnFreeEdge())

    def __repr__(self):
        return f'SddStiffenerMngt(name="{ self.name }")'
