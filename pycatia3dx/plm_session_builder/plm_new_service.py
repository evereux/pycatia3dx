"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.interfaces.service import Service
from pycatia3dx.types.general import CATVariant


class PLMNewService(Service):

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
                |                         PLMNewService
                | 
                | Interface representing the PLMNew service.
                | It can be retreives using the
                | Application.GetSessionService("PLMNewService")
                | Role: provides the services to create and edit in authoring session a new PLM
                | entity. In case this product is not granted the PLMCreate method of the
                | interface fails. The data are created in the default authoring customization
                | domain (environment).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def plm_create(self, i_user_type: str, o_editor: Editor) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PLMCreate(CATBSTR iUserType,Editor oEditor)
                |     Creates a new PLM entity corresponding to a given user
                |     type.
                |     Role:This method creates a PLM entity according to the first
                |     argument.
                | 
                |     The PLM Attributes of the created object are initialized using the
                |     Initialization Business Logic Rule. The creation will fail if all the mandatory
                |     attributes are not filled by the Business Logic Rule.
                | 
                |     The PLM entity is created in the authoring customization defined by the
                |     current PLM Environment.
                | 
                |     Parameters:
                | 
                |         iUserType
                |             The user type to identify the entity to create.
                |             Legal values: 3DShape: to create a 3D Representation, Drawing: to
                |             create a Drawing Representation, 
                |         oEditor
                |             The resulting editor on the newly created data.

        :param str i_user_type:
        :param Editor o_editor:
        :return: None
        """
        return self.com_object.PLMCreate(i_user_type, o_editor.com_object)

    def set_attribute_value(self, i_attribute_id: str, i_attribute_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttributeValue(CATBSTR iAttributeID,CATVariant
                | iAttributeValue)
                |     PreSets the PLM Attribute value for the next entity creation (
                |     PLMCreate).
                |     Role: this method valuates a PLM attribute with the given value int the
                |     next PLM Creation. After next creation, values are flushed. the value will be
                |     set on the created object if the attribute is found in the create mask of the
                |     object and its right access is read/write ( attribute can be modified
                |     interactively) When setting the value on the object, same rules as interactive
                |     modification in terms of Business Logic are applied ( Propagation, check,
                |     Finalization )
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             Attribute name. 
                |         iAttrValue
                |             Attribute value.
                |             example for strings, enumerates : SetAttributeValue "Attribute Name", "Attribute Value"
                |             example for integers : SetAttributeValue "Attribute Name",
                |             8 example for reals, dimensions : SetAttributeValue "Attribute Name",
                |             10.25 If the type of the attribute is a Date, value must be provided as "mm/dd/yyyy" format.
                |             If the type of the attribute is a list, IT IS NOT SUPPORTED
                |             .

        :param str i_attribute_id:
        :param CATVariant i_attribute_value:
        :return: None
        """
        return self.com_object.SetAttributeValue(i_attribute_id, i_attribute_value)

    def __repr__(self):
        return f'PlmNewService(name="{ self.name }")'
