"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.os.folder import Folder
from pycatia3dx.system.collection import Collection


class Folders(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Folders
                | 
                | The folders object belongs to a folder.
                | It lists all the folders contained in the folder. It allows to retrieve Folder
                | objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_number: int) -> Folder:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(long iNumber) As Folder
                |     Returns a folder using its index or its name from the folder
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the folder to retrieve from the collection
                |             of folders. As a numerics, this index is the rank of the folder in the
                |             collection. The index of the first folder in the collection is 1, and the index
                |             of the last folder is Count. As a string, it is the name you assigned to the
                |             folder using the AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved folder 
                |     Example:
                |         This example retrieves in ThisFolder the third folder, and it
                |         ThatFolder the folder named MyFolder. in the TestFolders folder
                |         collection.
                | 
                |          Dim ThisFolder As Folder
                |          Set ThisFolder = TestFolders.Item(3)
                |          Dim ThatFolder As Folder
                |          Set ThatFolder = TestFolders.Item("MyFolder")

        :param int i_number:
        :return: Folder
        """
        return Folder(self.com_object.Item(i_number))

    def __repr__(self):
        return f'Folders(name="{self.name}")'
