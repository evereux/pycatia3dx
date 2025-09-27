"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.os.file_component import FileComponent
from pycatia3dx.os.text_stream import TextStream


class File(FileComponent):
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
                |                         File
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
    def size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Size() As long (Read Only)
                |     Returns the size of the file.
                | 
                |     Example:
                |         This example retrieves in FileSize the size of the File
                |         TestFile.
                | 
                |          Dim FileSize As Long
                |          FileSize = TestFile.Size

        :return: int
        """

        return self.com_object.Size

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Type() As CATBSTR (Read Only)
                |     Returns the type of the file. For instance, if the file has a .txt or .doc
                |     extension, its type will be "Text Document".
                | 
                |     Example:
                |         This example retrieves in FileType the type of the File
                |         TestFile.
                | 
                |          Dim FileType As String
                |          FileSize = TestFile.Size

        :return: str
        """

        return self.com_object.Type

    def open_as_text_stream(self, i_mode: str) -> TextStream:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func OpenAsTextStream(CATBSTR iMode) As TextStream
                |     Opens the file and retrieves it as a TextSteam object. Parameter iMode can
                |     have the value "ForReading", "ForWriting" or
                |     "ForAppending".
                | 
                |     Example:
                |         This example opens the file TestFile for reading and retrieves in the
                |         text stream TextStr.
                | 
                |          Dim TextStr As CATIATextSteam
                |          Set TextStr = TestFile.OpenAsTextStream("ForReading")

        :param str i_mode:
        :return: TextStream
        """
        return TextStream(self.com_object.OpenAsTextStream(i_mode))

    def __repr__(self):
        return f'File(name="{self.name}")'
