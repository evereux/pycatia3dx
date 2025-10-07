"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.str.str_sfd_stiffener import StrSfdStiffener
from pycatia3dx.str.str_sfd_stiffener_on_free_edge import StrSfdStiffenerOnFreeEdge
from pycatia3dx.str.structure_profile import StructureProfile
from pycatia3dx.types.general import CATVariant


class StrSfdStiffeners(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrSfdStiffeners
                | 
                | Object for SfdStiffeners
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_stiffener(self) -> StrSfdStiffener:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddStiffener() As StrSfdStiffener
                |     Returns the stiffener created For setting further attributes please refer
                |     to StrCategoryMngt, StrMaterialMngt, StrSectionMngt, StrProfileLimitMngt
                |     interfaces.
                |     Role: Creates a Stiffener with all the data structure.
                | 
                |     Example:
                | 
                | 
                |              This example creates a Stiffener on a SfdPanel.
                |              
                | 
                |               'Get SfdStiffeners object
                |               Dim ObjSfdStiffeners As SfdStiffeners
                |               Set ObjSfdStiffeners = ObjSfdPanel.SfdStiffeners
                |               'Create a stiffener
                |               Set ObjSfdStiffener = ObjSfdStiffeners.AddStiffener

        :return: StrSfdStiffener
        """
        return StrSfdStiffener(self.com_object.AddStiffener())

    def add_stiffener_on_free_edge(self) -> StrSfdStiffenerOnFreeEdge:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddStiffenerOnFreeEdge() As StrSfdStiffenerOnFreeEdge
                |     Returns the created StiffenerOnFreeEdge For setting further attributes
                |     please refer to StrCategoryMngt, StrMaterialMngt, StrSectionMngt,
                |     StrProfileLimitMngt interfaces.
                |     Role: Create a StiffenerOnFreeEdge.
                | 
                |     Example:
                | 
                | 
                |              This example creates a StiffenerOnFreeEdge on a
                |              SfdPanel.
                |              
                | 
                |               'Get SfdStiffeners object
                |               Dim ObjSfdStiffeners As SfdStiffeners
                |               Set ObjSfdStiffeners = ObjSfdPanel.SfdStiffeners
                |               'Create a stiffener on free edge
                |               Set ObjSfdStiffenerOnFreeEdge = ObjSfdStiffeners.AddStiffenerOnFreeEdge

        :return: StrSfdStiffenerOnFreeEdge
        """
        return StrSfdStiffenerOnFreeEdge(self.com_object.AddStiffenerOnFreeEdge())

    def item(self, i_index: CATVariant) -> StructureProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As StructureProfile
                |     Returns a SfdStiffener or SfdStiffenerOnFreeEdge
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of SfdStiffener or SfdStiffenerOnFreeEdge
                |             
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first item from the list of
                |              stiffeners/SFEs.
                |              
                | 
                |               Dim ObjSfdStiffener As SfdProfile
                |               Set ObjSfdStiffener = ObjSfdStiffenerList.Item(1)

        :param CATVariant i_index:
        :return: StructureProfile
        """
        return StructureProfile(self.com_object.Item(i_index))

    def remove(self, i_stiffener: StructureProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(StructureProfile iStiffener)
                |     Removes a Stiffener of this Panel.
                | 
                |     Parameters:
                | 
                |         iStiffener
                |             Stiffener. 

        :param StructureProfile i_stiffener:
        :return: None
        """
        return self.com_object.Remove(i_stiffener.com_object)

    def __repr__(self):
        return f'StrSfdStiffeners(name="{ self.name }")'
