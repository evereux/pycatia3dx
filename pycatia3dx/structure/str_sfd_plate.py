"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_flanges import StrFlanges
from pycatia3dx.structure.str_material_mngt import StrMaterialMngt
from pycatia3dx.structure.str_plate_extrusion_mngt import StrPlateExtrusionMngt


class StrSfdPlate(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrSfdPlate
                | 
                | Object to filter Structure Functional Modeler functions Plate.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def flanges(self) -> StrFlanges:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Flanges() As StrFlanges (Read Only)
                |     Returns the StrFlanges object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrFlanges the StrFlanges
                |              object
                |              of the SfdPlate.
                |              
                | 
                |              Dim ObjStrFlanges As StrFlanges
                |              Set ObjStrFlanges = iObjSfdPlate.Flanges

        :return: StrFlanges
        """

        return StrFlanges(self.com_object.Flanges)

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
                |              This example retrieves in ObjStrMaterialMngt the StrMaterialMngt
                |              object
                |              of the SfdPlate.
                |              
                | 
                |              Dim ObjSfdPlate As SfdPlate
                |              Set ObjSfdPlate = ObjSfdPlates.Item(1)
                |              Dim ObjStrMaterialMngt As StrMaterialMngt
                |              Set ObjStrMaterialMngt = ObjSfdPlate.StrMaterialMngt

        :return: StrMaterialMngt
        """

        return StrMaterialMngt(self.com_object.StrMaterialMngt)

    @property
    def str_plate_extrusion_mngt(self) -> StrPlateExtrusionMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrPlateExtrusionMngt() As StrPlateExtrusionMngt (Read
                | Only)
                |     Returns the StrPlateExtrusionMngt object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrPlateExtrusionMngt the
                |              StrPlateExtrusionMngt object
                |              of the SfdPlate.
                |              
                | 
                |              Dim ObjStrPlateExtrusionMngt As
                |              StrPlateExtrusionMngt
                |              Set ObjStrPlateExtrusionMngt = ObjSfdPlate.StrPlateExtrusionMngt

        :return: StrPlateExtrusionMngt
        """

        return StrPlateExtrusionMngt(self.com_object.StrPlateExtrusionMngt)

    def __repr__(self):
        return f'StrSfdPlate(name="{self.name}")'
