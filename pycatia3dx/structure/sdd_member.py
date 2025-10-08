"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.structure.structure_member import StructureMember


class SddMember(StructureMember):
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
                |                         CATStrIDLItf.StructureMember
                |                             SddMember
                | 
                | Object to manage Structure detail Modeler Member.
                | Role: Allows accessing and setting of SDD Member's data.
                | 
                | Example:
                |
                |          This example retrieves in SddMember.
                |          
                | 
                |          Dim ObjSddMember As SddMember 
                |          Set ObjSddMember = ObjSddProductMember.SddMember

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SddMember(name="{self.name}")'
