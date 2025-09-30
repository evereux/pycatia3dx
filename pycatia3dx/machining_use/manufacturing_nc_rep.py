"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingNcRep(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingNCRep
                | 
                | This interface is dedicated to NC Doc Reps and it is implemented on PLM NC rep
                | reference.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def export(self, i_directory_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Export(CATBSTR iDirectoryPath)
                |     Export files from NC Rep to directory path
                | 
                |     Parameters:
                | 
                |         iDirectoryPath
                |             [in] directory path

        :param str i_directory_path:
        :return: None
        """
        return self.com_object.Export(i_directory_path)

    def get_files(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFiles() As CATSafeArrayVariant
                |     Returns a list of full path to the files that can be opened and viewed
                |     These files are temporary and will be deleted at the end of V6
                |     session
                | 
                |     Parameters:
                | 
                |         oListOfFiles
                |             [out] list of files

        :return: tuple
        """
        return self.com_object.GetFiles()

    def get_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetType() As long
                |     Returns the type of the rep (1:APT, 2:ISO, 3:CLF)

        :return: int
        """
        return self.com_object.GetType()

    def import_(self, i_list_of_new_files_paths: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Import(CATSafeArrayVariant iListOfNewFilesPaths)
                |     Import Add the new file paths on top of the existing content of the
                |     Rep
                | 
                |     Parameters:
                | 
                |         iListOfNewFilesPaths
                |             List of paths of new files to add in the rep

        :param tuple i_list_of_new_files_paths:
        :return: None
        """
        return self.com_object.Import(i_list_of_new_files_paths)

    def __repr__(self):
        return f'ManufacturingNcRep(name="{ self.name }")'
