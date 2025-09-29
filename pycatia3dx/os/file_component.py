"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.system.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia3dx.os.folder import Folder


class FileComponent(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FileComponent
                | 
                | Represents the file object.
                | Role: The file object allows to manipulate files with UNIX and Windows. Use it
                | instead of the one of Visual Basic to make portable macros. Its gives access to
                | information about the file and can open a file as a TextStream
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def parent_folder(self) -> 'Folder':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ParentFolder() As Folder
                |     Returns or sets the parent folder of the file.
                | 
                |     Example:
                |         This example sets the folder ParentFold as parent of the file TestFile.
                |         This moves the file into ParentFold.
                | 
                |          TestFile.ParentFolder

        :return: Folder
        """
        from pycatia3dx.os.folder import Folder

        return Folder(self.com_object.ParentFolder)

    @parent_folder.setter
    def parent_folder(self, value: 'Folder'):
        """
        :param Folder value:
        """

        self.com_object.ParentFolder = value

    @property
    def path(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Path() As CATBSTR (Read Only)
                |     Returns the full path of the file.
                | 
                |     Example:
                |         This example retrieves in FilePath the path of the File
                |         TestFile.
                | 
                |          Dim FilePath As String
                |          FilePath = TestFile.Path

        :return: str
        """

        return self.com_object.Path

    def __repr__(self):
        return f'FileComponent(name="{self.name}")'
