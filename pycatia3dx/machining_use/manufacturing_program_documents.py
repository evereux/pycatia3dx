"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingProgramDocuments(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingProgramDocuments
                | 
                | Interface dedicated to published documents of a manufacturing
                | program.
                | It is implemented on ManufacturingProgram object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_published_documents(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPublishedDocuments() As CATSafeArrayVariant
                |     Retrieve PLM documents attached to the manufacturing program.

        :return: tuple
        """
        return self.com_object.GetPublishedDocuments()

    def publish(self, i_file_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Publish(CATBSTR iFilePath)
                |     Create a PLM document and attach it to the manufacturing program. When a
                |     document with same file name already exists, it updates its
                |     content.
                | 
                |     Parameters:
                | 
                |         iFilePath
                |             The full path of file to add to the document.

        :param str i_file_path:
        :return: None
        """
        return self.com_object.Publish(i_file_path)

    def __repr__(self):
        return f'ManufacturingProgramDocuments(name="{ self.name }")'
