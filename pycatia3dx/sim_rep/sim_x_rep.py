"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimXRep(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimXRep
                | 
                | Represents a XRep.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def file_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FileName() As CATBSTR
                |     Sets or retrieves the data file name associated to the XRep.

        :return: str
        """

        return self.com_object.FileName

    @file_name.setter
    def file_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.FileName = value

    @property
    def nav_rep_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NavRepName() As CATBSTR
                |     Sets or retrieves the nav rep file name associated to the XRep.

        :return: str
        """

        return self.com_object.NavRepName

    @nav_rep_name.setter
    def nav_rep_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.NavRepName = value

    def add_relation(self, i_pointed_object: AnyObject, i_relation_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddRelation(AnyObject iPointedObject,SimXRepRelationType
                | iRelationType)
                |     Adds a relation to the XRep.
                | 
                |     Parameters:
                | 
                |         iPointedObject:
                |             The link object that represent the pointed object.
                |             
                |         iRelationType:
                |             The kind of relation, depending on the linked objects.
                |             PLMProductService.ComposeLink

        :param AnyObject i_pointed_object:
        :param int i_relation_type:
        :return: None
        """
        return self.com_object.AddRelation(i_pointed_object.com_object, i_relation_type)

    def export_file(self, i_folder_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportFile(CATBSTR iFolderPath)
                |     Exports the data of the XRep to a data file.
                | 
                |     Parameters:
                | 
                |         iFolderPath:
                |             The path of the folder in which the data file will be exported.

        :param str i_folder_path:
        :return: None
        """
        return self.com_object.ExportFile(i_folder_path)

    def export_nav_rep(self, i_folder_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportNavRep(CATBSTR iFolderPath)
                |     Exports the data of the XRep to a data file.
                | 
                |     Parameters:
                | 
                |         iFolderPath:
                |             The path of the folder in which the navrep file will be exported.

        :param str i_folder_path:
        :return: None
        """
        return self.com_object.ExportNavRep(i_folder_path)

    def generate_nav_rep(self, i_file_path: str, i_length_unit: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GenerateNavRep(CATBSTR iFilePath,CATBSTR iLengthUnit)
                |     Generates a navrep file from a data file and imports it into the X
                |     representation.
                | 
                |     Parameters:
                | 
                |         iFilePath
                |             The path of the data file from which the navrep file will be
                |             generated. 
                |         iLengthUnit
                |             The length unit of the data file.
                |             Legal values:
                | 
                |             METER
                |             INCH
                |             FOOT
                |             YARD
                |             ...

        :param str i_file_path:
        :param str i_length_unit:
        :return: None
        """
        return self.com_object.GenerateNavRep(i_file_path, i_length_unit)

    def import_file(self, i_folder_path: str, i_keep_nav_rep: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ImportFile(CATBSTR iFolderPath,boolean iKeepNavRep)
                |     Imports a data file in the XRep.
                | 
                |     Parameters:
                | 
                |         iFolderPath:
                |             The path of the folder from which the data file will be imported.
                |             
                |         iKeepNavRep:
                |             Tells whether the existing navrep (if any) will be kept or replaced
                |             by the default one.

        :param str i_folder_path:
        :param bool i_keep_nav_rep:
        :return: None
        """
        return self.com_object.ImportFile(i_folder_path, i_keep_nav_rep)

    def import_nav_rep(self, i_folder_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ImportNavRep(CATBSTR iFolderPath)
                |     Imports a navrep file in the XRep.
                | 
                |     Parameters:
                | 
                |         iFolderPath:
                |             The path of the folder from which the navrep file will be imported.

        :param str i_folder_path:
        :return: None
        """
        return self.com_object.ImportNavRep(i_folder_path)

    def remove_relation(self, i_relation_pointed_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveRelation(AnyObject iRelationPointedObject)
                |     Removes a relation from the XRep.
                | 
                |     Parameters:
                | 
                |         iRelationPointedObject:
                |             The link object that represent the pointed object, stored into the
                |             relation. PLMProductService.ComposeLink

        :param AnyObject i_relation_pointed_object:
        :return: None
        """
        return self.com_object.RemoveRelation(i_relation_pointed_object.com_object)

    def __repr__(self):
        return f'SimXRep(name="{self.name}")'
