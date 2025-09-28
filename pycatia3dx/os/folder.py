"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.os.file_component import FileComponent
from pycatia3dx.os.files import Files
from pycatia3dx.os.folders import Folders


class Folder(FileComponent):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfOSIDLItf.FileComponent
                |                         Folder
                | 
                | Represents the folder object.
                | It allows you to manipulate folders and gives access to information about
                | them.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def files(self) -> Files:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Files() As Files (Read Only)
                |     Returns the file collection of the folder.
                | 
                |     Example:
                |         This example retrieves in TestFiles the file collection of the folder
                |         TestFolder.
                | 
                |          Dim TestFiles As Files
                |          Set TestFiles = TestFolder.Files

        :return: Files
        """

        return Files(self.com_object.Files)

    @property
    def sub_folders(self) -> Folders:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property SubFolders() As Folders (Read Only)
                |     Returns the folder collection of the folder.
                | 
                |     Example:
                |         This example retrieves in TestSubFolders the folder colection of the
                |         folder TestFolder.
                | 
                |          Dim TestSubFolders As CATIAFolders
                |          Set TestSubFolders = TestFolder.SubFolders

        :return: Folders
        """

        return Folders(self.com_object.SubFolders)

    def __repr__(self):
        return f'Folder(name="{self.name}")'
