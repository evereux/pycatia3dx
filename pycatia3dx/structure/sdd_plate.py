"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.structure.sdd_plate_sub_element_mngt import SddPlateSubElementMngt
from pycatia3dx.structure.str_flanges import StrFlanges
from pycatia3dx.structure.structure_plate import StructurePlate


class SddPlate(StructurePlate):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATStrIDLItf.StructurePlate
                |                         SddPlate
                | 
                | Object for representing Structure Detail Design Plate.
                | Role: To manage the Plate structure object.
                | 
                | Example:
                | 
                | 
                |          This example retrieves in SddPlate.
                |          
                | 
                |          Dim ObjSddPlate As SddPlate
                |          Set ObjSddPlate = ObjSddProductPlate.SddPlate
    
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
                |              of the SddPlate
                |              
                | 
                |              Dim ObjStrFlanges As StrFlanges
                |              Set ObjStrFlanges = iObjSddPlate.Flanges

        :return: StrFlanges
        """

        return StrFlanges(self.com_object.Flanges)

    @property
    def plate_sub_elements(self) -> SddPlateSubElementMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlateSubElements() As SddPlateSubElementMngt (Read
                | Only)
                |     Returns the SddPlateSubElementMngt object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in oObjSddPlateSubElementMngt the
                |              SddPlateSubElementMngt object
                |              of the SddPlate
                |              
                | 
                |              Set oObjSddPlateSubElementMngt = iObjSddPlate.PlateSubElements

        :return: SddPlateSubElementMngt
        """

        return SddPlateSubElementMngt(self.com_object.PlateSubElements)

    def __repr__(self):
        return f'SddPlate(name="{self.name}")'
