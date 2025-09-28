"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.os.file import File
from pycatia3dx.os.folder import Folder
from pycatia3dx.system.any_object import AnyObject


class FileSystem(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FileSystem
                | 
                | Represents the file system object.
                | Role: The file system object allows you to access and manipulate folders and
                | files. It can check the existence of, get, create, delete, or copy folders and
                | files.
                | 
                | See also:
                |     Folder, File
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def file_separator(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property FileSeparator() As CATBSTR (Read Only)
                |     Returns the file separator string (usually, \\ on Windows and / on
                |     UNIX)
                | 
                |     Parameters:
                | 
                |         oTmpDirectory
                |             The file separator string.

        :return: str
        """

        return self.com_object.FileSeparator

    @property
    def path_separator(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property PathSeparator() As CATBSTR (Read Only)
                |     Returns the path separator string (usually, ; on Windows and : on UNIX)
                | 
                |     Parameters:
                | 
                |         oTmpDirectory
                |             The path separator string.

        :return: str
        """

        return self.com_object.PathSeparator

    @property
    def temporary_directory(self) -> Folder:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property TemporaryDirectory() As Folder (Read Only)
                |     Returns the temporary system directory (usually, C:\\temp on Windows and
                |     /tmp on UNIX)
                | 
                |     Parameters:
                | 
                |         oTmpDirectory
                |             A folder which corresponds to the temporary system directory.

        :return: Folder
        """

        return Folder(self.com_object.TemporaryDirectory)

    def concatenate_paths(self, i_path_chunk1: str, i_path_chunk2: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func ConcatenatePaths(CATBSTR iPathChunk1,CATBSTR iPathChunk2) As
                | CATBSTR
                |     Concatenates two path chunks to make a new path. Either path chunk can be
                |     empty. The resulting path does not have to exist. The method automatically
                |     corrects improper path separators (/ Unix separators used on a Windows platform
                |     are automatically replaced by \\ and vice versa).
                | 
                |     Parameters:
                | 
                |         iPathChunk1
                |             The first path chunk (for instance "E:\\tmp"). 
                |         iPathChunk2
                |             The second path chunk (for instance "local\myfile.txt").
                |             
                |         oPath
                |             The resulting path (for instance "E:\\tmp\\local\\myfile.txt").

        :param str i_path_chunk1:
        :param str i_path_chunk2:
        :return: str
        """
        return self.com_object.ConcatenatePaths(i_path_chunk1, i_path_chunk2)

    def copy_file(self, i_path_source: str, i_path_destination: str, i_overwrite: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub CopyFile(CATBSTR iPathSource,CATBSTR iPathDestination,boolean
                | iOverwrite)
                |     Copies a file from one location to another.
                | 
                |     Parameters:
                | 
                |         iSourcePath
                |             The full path of the source file. 
                |         iDestinationPath
                |             The full destination path where the source file is to be copied.
                |             
                |         iOverwrite
                |             Boolean value that is True if an existing file with the same name
                |             can be overwritten; False if it is not, and the copy doesn't take
                |             place.
                | 
                |             Example:
                |                 This example copies the file C:\\Tests\\File1 to C:\\Tests\\File2
                |                 from the file system object FileSys, except if a file with the name
                |                 C:\\Tests\\File2 already exists.
                | 
                |                  FileSys.CopyFile("C:\\Tests\\File1", "C:\\Tests\\File2",
                |                  False)

        :param str i_path_source:
        :param str i_path_destination:
        :param bool i_overwrite:
        :return: None
        """
        return self.com_object.CopyFile(i_path_source, i_path_destination, i_overwrite)

    def copy_folder(self, i_source_path: str, i_destination_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub CopyFolder(CATBSTR iSourcePath,CATBSTR iDestinationPath)
                |     Recursively copies a folder from one location to another. Role: The folder
                |     is copied along with its files, and all its subfolders and their own
                |     files.
                | 
                |     Parameters:
                | 
                |         iSourcePath
                |             The full path of the source folder. 
                |         iDestinationPath
                |             The full destination path where the source folder, its files, and
                |             its subfolders are to be copied.
                | 
                |             Example:
                |                 This example copies the folder "C:\\Tests\\Fold1" to
                |                 "C:\\Tests\\Fold2" of the file system object
                |                 FileSys.
                | 
                |                  FileSys.CopyFolder("C:\\Tests\\Fold1",
                |                  "C:\\Tests\\Fold2")

        :param str i_source_path:
        :param str i_destination_path:
        :return: None
        """
        return self.com_object.CopyFolder(i_source_path, i_destination_path)

    def create_file(self, i_path: str, i_overwrite: bool) -> File:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func CreateFile(CATBSTR iPath,boolean iOverwrite) As File
                |     Creates a file and returns the associated file object.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The full path where the file is to be created. 
                |         iOverwrite
                |             Boolean value that is True if an existing file with the same name
                |             can be overwritten; False if it is not, and the creation doesn't take place.
                |             
                | 
                |     Returns:
                |         The created file
                | 
                |         Example:
                |             This example creates the file C:\\Tests\\File1 and retrieves it in
                |             the file object FileObj from the file system object FileSys, except if a file
                |             with the name C:\\Tests\\File1 already exists.
                | 
                |              Dim FileObj As File
                |              Set FileObj = FileSys.CreateFile("C:\\Tests\\File1", False)

        :param str i_path:
        :param bool i_overwrite:
        :return: File
        """
        return File(self.com_object.CreateFile(i_path, i_overwrite))

    def create_folder(self, i_path: str) -> Folder:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func CreateFolder(CATBSTR iPath) As Folder
                |     Creates a folder and returns the associated folder object.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The full path where the folder is to be created. 
                | 
                |     Returns:
                |         The created folder object. If the folder already exists, the method
                |         fails.
                | 
                |         Example:
                |             This example creates the folder "C:\\Tests\\Fold1" and retrieves it
                |             in FoldObj from the FileSystem FileSys.
                | 
                |              Dim FoldObj As Folder
                |              Set FoldObj = FileSys.CreateFolder("C:\\Tests\\Fold1")

        :param str i_path:
        :return: Folder
        """
        return Folder(self.com_object.CreateFolder(i_path))

    def delete_file(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub DeleteFile(CATBSTR iPath)
                |     Deletes a file.
                |     The method fails if the folder doesn't exist.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The full path of the file to delete.
                | 
                |             Example:
                |                 This example deletes the file "C:\\Tests\\File" from the file
                |                 system object FileSys.
                | 
                |                  FileSys.DeleteFile("C:\\Tests\\File1")

        :param str i_path:
        :return: None
        """
        return self.com_object.DeleteFile(i_path)

    def delete_folder(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub DeleteFolder(CATBSTR iPath)
                |     Deletes a folder.
                |     The method fails if the folder doesn't exist.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The full path of the folder to delete.
                | 
                |             Example:
                |                 This example deletes the folder "C:\\Tests\\Fold1" from the
                |                 FileSystem FileSys.
                | 
                |                  FileSys.DeleteFolder("C:\\Tests\\Fold1")

        :param str i_path:
        :return: None
        """
        return self.com_object.DeleteFolder(i_path)

    def file_exists(self, i_path: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func FileExists(CATBSTR iPath) As boolean
                |     Returns whether a given file exists.
                |     True if the file exists.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The full path of the file.
                | 
                |             Example:
                |                 This example retrieves in Exists whether the file
                |                 "C:\\Tests\\File1" exists in the file system object
                |                 FileSys.
                | 
                |                  Dim Exists As Boolean
                |                  Exists = FileSys.FileExists("C:\\Tests\\File1")

        :param str i_path:
        :return: bool
        """
        return self.com_object.FileExists(i_path)

    def folder_exists(self, i_path: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func FolderExists(CATBSTR iPath) As boolean
                |     Returns whether a given folder exists.
                |     True if the folder exists.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The full path of the folder.
                | 
                |             Example:
                |                 This example retrieves in Exists whether the folder
                |                 "C:\\Tests\\Fold1" exists in the file system object
                |                 FileSys.
                | 
                |                  Dim Exists As Boolean
                |                  Exists=FileSys.FolderExists("C:\\Tests\\Fold1")

        :param str i_path:
        :return: bool
        """
        return self.com_object.FolderExists(i_path)

    def get_file(self, i_path: str) -> File:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetFile(CATBSTR iPath) As File
                |     Returns a file using its full path.
                |     The method fails if the folder doesn't exist.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The full path of the file to retrieve.
                | 
                |             Example:
                |                 This example retrieves the file C:\Tests in the FileObj from
                |                 the file system object FileSys.
                | 
                |                  Dim FileObj As File
                |                  Set FileObj = FileSys.GetFile("C:\\Tests")

        :param str i_path:
        :return: File
        """
        return File(self.com_object.GetFile(i_path))

    def get_folder(self, i_path: str) -> Folder:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetFolder(CATBSTR iPath) As Folder
                |     Returns a folder using its full path.
                | 
                |     Parameters:
                | 
                |         iPath
                |             The full path of the folder to retrieve. 
                | 
                |     Returns:
                |         The retrieved folder. If the folder doesn't exist, the method
                |         fails.
                | 
                |         Example:
                |             This example retrieves the C:Tests folder in FoldObj from the file
                |             system object FileSys.
                | 
                |              Dim FoldObj As Folder
                |              Set FoldObj = FileSys.GetFolder("C:\\Tests\\")

        :param str i_path:
        :return: Folder
        """
        return Folder(self.com_object.GetFolder(i_path))

    def __repr__(self):
        return f'FileSystem(name="{self.name}")'
