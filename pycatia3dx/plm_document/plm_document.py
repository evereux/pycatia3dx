"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class PLMDocument(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMDocument
                | 
                | Represents the PLM Document object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def file_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FileNames() As CATSafeArrayVariant (Read Only)
                |     To Get the List of Files attached to the Document object
                | 
                |     Parameters:
                | 
                |         oFileNames
                |             list of file names attached to the Document.

        :return: tuple
        """

        return self.com_object.FileNames

    @property
    def parents(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parents() As CATSafeArrayVariant (Read Only)
                |     To retrive parents where Document object is attached.
                | 
                |     Parameters:
                | 
                |         oParents
                |             Parent IDs where Document Object is attached.

        :return: tuple
        """

        return self.com_object.Parents

    def check_in_file(self, i_old_file_name: str, i_new_file_path: str, i_file_comment: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CheckInFile(CATBSTR iOldFileName,CATBSTR iNewFilePath,CATBSTR
                | iFileComment)
                |     To Checkin file to the Document object to the specified new file
                |     path.
                | 
                |     Parameters:
                | 
                |         iFileName
                |             File name to download. 
                |         iNewFilePath
                |             File path to download the specified file. 
                |         iFileComment
                |             File Comment while adding the specified file.

        :param str i_old_file_name:
        :param str i_new_file_path:
        :param str i_file_comment:
        :return: None
        """
        return self.com_object.CheckInFile(i_old_file_name, i_new_file_path, i_file_comment)

    def check_out_file(self, i_file_name: str, i_check_out_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CheckOutFile(CATBSTR iFileName,CATBSTR iCheckOutPath)
                |     To Checkout the file attached to the Document object to the specified file
                |     path.
                | 
                |     Parameters:
                | 
                |         iFileName
                |             File name to checkout. 
                |         iCheckOutPath
                |             File path to checkout the specified file.

        :param str i_file_name:
        :param str i_check_out_path:
        :return: None
        """
        return self.com_object.CheckOutFile(i_file_name, i_check_out_path)

    def create_file(self, i_file_path: str, i_file_comment: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateFile(CATBSTR iFilePath,CATBSTR iFileComment)
                |     Attach new file to the Document object.
                | 
                |     Parameters:
                | 
                |         iFilePath
                |             File name along with file path. 
                |         iFileComment
                |             File Comment while adding the specified file.

        :param str i_file_path:
        :param str i_file_comment:
        :return: None
        """
        return self.com_object.CreateFile(i_file_path, i_file_comment)

    def delete_file(self, i_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteFile(CATBSTR iFileName)
                |     To Delete specified file attached to the Document object.
                | 
                |     Parameters:
                | 
                |         iFileName
                |             Delete the specified file.

        :param str i_file_name:
        :return: None
        """
        return self.com_object.DeleteFile(i_file_name)

    def download_file(self, i_file_name: str, i_download_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DownloadFile(CATBSTR iFileName,CATBSTR iDownloadPath)
                |     To Download file attached to the Document object to the specified file
                |     path.
                | 
                |     Parameters:
                | 
                |         iFileName
                |             File name to download. 
                |         iDownloadPath
                |             File path to download the specified file.

        :param str i_file_name:
        :param str i_download_path:
        :return: None
        """
        return self.com_object.DownloadFile(i_file_name, i_download_path)

    def __repr__(self):
        return f'PLMDocument(name="{self.name}")'
