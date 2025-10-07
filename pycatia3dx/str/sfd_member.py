"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.str.str_material_mngt import StrMaterialMngt
from pycatia3dx.str.str_user_connections import StrUserConnections
from pycatia3dx.str.structure_member import StructureMember


class SfdMember(StructureMember):

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
                |                             SfdMember
                | 
                | Object to manage Structure Functional Modeler Member.
                | Role: Allows accessing and setting of Sfd Member's data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def str_material_mngt(self) -> StrMaterialMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrMaterialMngt() As StrMaterialMngt (Read Only)
                |     Returns the StrMaterialMngt object.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example retrieves in ObjMaterialMngt the
                |              MaterialMngt
                |              object of the SfdMember
                |              
                | 
                |              'Here RefGeometricalSet is reference to the
                |              GeometricalSet
                |              Set ObjSfdMember = ObjSfdFactory.AddMember(RefGeometricalSet)
                |              Dim ObjMaterialMngt As StrMaterialMngt 
                |              Set ObjMaterialMngt = ObjSfdMember.StrMaterialMngt

        :return: StrMaterialMngt
        """

        return StrMaterialMngt(self.com_object.StrMaterialMngt)

    @property
    def str_user_connections(self) -> StrUserConnections:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrUserConnections() As StrUserConnections (Read
                | Only)
                |     Returns the UserConnections that are inside this object.See
                |     StrUserConnection interface.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the UserConnections inside this
                |              object.
                |              
                | 
                |               Dim ListOfUserConnections As StrUserConnections
                |               Set ListOfUserConnections = ObjSfdMember.StrUserConnections

        :return: StrUserConnections
        """

        return StrUserConnections(self.com_object.StrUserConnections)

    def __repr__(self):
        return f'SfdMember(name="{ self.name }")'
