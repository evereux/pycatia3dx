"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingResourceFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingResourceFactory
                | 
                | Interface to create manufacturing resources.
                | Role: This interface offers services to create manufacturing
                | resources
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_resource(self, i_type: str, i_add_list: bool) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateResource(CATBSTR iType,boolean iAddList) As
                | AnyObject
                |     This method is used to create a new manufacturing
                |     resource.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the resource to create. 
                |         oResource
                |             Handler on the newly created resource of given type.
                |             
                | 
                |     See also:
                |         ManufacturingResource
                |     Parameters:
                | 
                |         iAddList
                |             Flag to add the resource into the resource List.

        :param str i_type:
        :param bool i_add_list:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateResource(i_type, i_add_list))

    def create_resource2(self, i_type: str, i_catalog_name: str, i_client_id: str, i_add_list: bool) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateResource2(CATBSTR iType,CATBSTR iCatalogName,CATBSTR
                | iClientId,boolean iAddList) As AnyObject
                |     This method is used to create a new user resource.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the resource to create. 
                |         iCatalogName
                |             the catalog base name 
                |         iClientId
                |             the client id related to catalog 
                |         iAddList
                |             Flag to add the resource into the resource List. 
                |         oResource
                |             Handler on the newly created resource of given type.
                |             
                | 
                |     See also:
                |         ManufacturingResource

        :param str i_type:
        :param str i_catalog_name:
        :param str i_client_id:
        :param bool i_add_list:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateResource2(i_type, i_catalog_name, i_client_id, i_add_list))

    def __repr__(self):
        return f'ManufacturingResourceFactory(name="{ self.name }")'
