"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingNcRepManagement(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingNCRepManagement
                | 
                | Interface dedicated to NC Rep management.
                | Role: This interface offers services to manage NC Rer.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_nc_rep(self, i_name: str, i_type: int, i_list_of_files_paths: tuple) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateNCRep(CATBSTR iName,long iType,CATSafeArrayVariant
                | iListOfFilesPaths) As AnyObject
                |     CreateNCRep
                |     Create a new NC Rep and aggregate it under the machining
                |     cell:
                | 
                |     Parameters:
                | 
                |         iName
                |             PLM external id of the rep 
                |         iType
                |             iType: Type of the rep (1:APT, 2:ISO, 3:CLF) 
                |         iListOfFilesPaths
                |             iListOfFilePaths: List of paths of files to add in the rep
                |             (optional argument) 
                | 
                |     Returns:
                |         The PLM rep reference of the rep. NULL_var when an error occurs

        :param str i_name:
        :param int i_type:
        :param tuple i_list_of_files_paths:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateNCRep(i_name, i_type, i_list_of_files_paths))

    def __repr__(self):
        return f'ManufacturingNcRepManagement(name="{ self.name }")'
