"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.sdd_plate import SddPlate
from pycatia3dx.types.general import CATVariant


class SddPlates(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SddPlates
                | 
                | Object to manage list of SddPlate
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_sdd_plate: SddPlate) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(SddPlate iSddPlate)
                |     Adds a already created SddPlate in the collection.
                | 
                |     Parameters:
                | 
                |         iSddPlate
                |             SddPlate. 
                | 
                |     Example:
                | 
                | 
                |              This example Adds SddPlate to the list of
                |              SddPlates.
                |              
                | 
                |               Dim ListOfSddPlates As SddPlates
                |               Set ListOfSddPlates = ObjSddOtherSupportPlates.OtherSupportPlates
                |               'add the SddPlate of the list
                |               ListOfSddPlates.Add ObjSddPlate

        :param SddPlate i_sdd_plate:
        :return: None
        """
        return self.com_object.Add(i_sdd_plate.com_object)

    def item(self, i_index: CATVariant) -> SddPlate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SddPlate
                |     Returns a SddPlate from a list of SddPlates
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of SddPlate 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first plate from the list of
                |              plate.
                |              
                | 
                |               Dim ObjSddPlate As SddPlate
                |               Set ObjSddPlate = ObjSddPlateList.Item(1)

        :param CATVariant i_index:
        :return: SddPlate
        """
        return SddPlate(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SddPlates(name="{self.name}")'
