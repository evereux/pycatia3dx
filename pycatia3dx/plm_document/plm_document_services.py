"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_document.plm_document import PLMDocument


class PLMDocumentServices(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMDocumentServices

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_document(self, i_attr_names: tuple, i_attr_values: tuple, i_file_path_names: tuple, i_file_comment: tuple) -> PLMDocument:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDocument(CATSafeArrayVariant iAttrNames,CATSafeArrayVariant
                | iAttrValues,CATSafeArrayVariant iFilePathNames,CATSafeArrayVariant
                | iFileComment) As PLMDocument
                |     Create Document object with given attributes
                | 
                |     Parameters:
                | 
                |         iAttrNames
                |             Contains list of attributes to be passed while creation
                |             
                |         iAttrValues
                |             Contains list of attribute values corresponding to the attributes
                |             passed. 
                |         iFilePathNames
                |             Contains list of file paths to be connected to the Document.
                |             
                |         iFileComment
                |             Contains list of each file comment 
                |         oDocument

        :param tuple i_attr_names:
        :param tuple i_attr_values:
        :param tuple i_file_path_names:
        :param tuple i_file_comment:
        :return: PLMDocument
        """
        return PLMDocument(self.com_object.CreateDocument(i_attr_names, i_attr_values, i_file_path_names, i_file_comment))

    def __repr__(self):
        return f'PlmDocumentServices(name="{ self.name }")'
