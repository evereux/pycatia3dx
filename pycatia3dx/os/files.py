"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.os.file import File
from pycatia3dx.system.collection import Collection


class Files(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Files
                | 
                | A collection of all the file objects in a folder.
                | It lists all the files contained in the folder. It allows to retrieve File
                | objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=File)
        self.com_object = com_object

    def item(self, i_number: int) -> File:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(long iNumber) As File
                |     Returns a file using its index or its name from the file
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the file to retrieve from the collection
                |             of files. As a numerics, this index is the rank of the file in the collection.
                |             The index of the first file in the collection is 1, and the index of the last
                |             file is Count. As a string, it is the name you assigned to the file using the
                |             AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved file 
                |     Example:
                |         This example retrieves in ThisFile the third file, and it ThatFile the
                |         file named MyFile. in the TestFiles file collection.
                | 
                |          Dim ThisFile As File
                |          Set ThisFile = TestFiles.Item(3)
                |          Dim ThatFile As File
                |          Set ThatFile = TestFiles.Item("MyFile")

        :param int i_number:
        :return: File
        """
        return File(self.com_object.Item(i_number))

    def __repr__(self):
        return f'Files(name="{self.name}")'
