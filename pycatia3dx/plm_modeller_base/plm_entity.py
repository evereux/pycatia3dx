"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class PLMEntity(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMEntity
                | 
                | Represents a PLM Entity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_attribute_value(self, i_attr_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAttributeValue(CATBSTR iAttrName) As CATVariant
                |     Returns the PLM Attribute value.
                |     Role: this method returns the PLM attribute value from its
                |     name.
                |     From an authoring editor, all public attributes values can be retrieved.
                |     From the Search result window, only attributes available in "Edit Properties"
                |     window can be retrieved.
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             Attribute name. 
                | 
                |     Returns:
                |         Attribute value.

        :param str i_attr_name:
        :return: CATVariant
        """
        return self.com_object.GetAttributeValue(i_attr_name)

    def get_custom_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCustomType() As CATBSTR
                |     Returns the PLM Entity type.
                |     Role: this method returns the internal PLM object type. This type
                |     corresponds to the PLM class that instantiates the PLM entity. Most of the
                |     time, it a modeler customized class. You can use the returned type to query a
                |     PLM Product.
                | 
                |     Returns:
                |         PLM Entity type.

        :return: str
        """
        return self.com_object.GetCustomType()

    def set_attribute_value(self, i_attr_name: str, i_attr_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttributeValue(CATBSTR iAttrName,CATVariant iAttrValue)
                |     Sets the PLM Attribute value.
                |     Role: this method valuates a PLM attribute with the given value. In an
                |     Authoring Editor, all public (R/W) attributes values can be modifed whereas it
                |     is not possible in the Search window.
                | 
                |     Parameters:
                | 
                |         iAttrName
                |             Attribute name. 
                |         iAttrValue
                |             Attribute value.
                |             If the type of the attribute is a Date, value must be provided as
                |             mm/dd/yyyy format.
                |             If the type of the attribute is a list, values must 
                |             be provided as a string with semi colon separators 
                |             (ex : "value1;value2;").

        :param str i_attr_name:
        :param CATVariant i_attr_value:
        :return: None
        """
        return self.com_object.SetAttributeValue(i_attr_name, i_attr_value)

    def __repr__(self):
        return f'PLMEntity(name="{self.name}")'
