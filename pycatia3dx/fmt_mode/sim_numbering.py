"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimNumbering(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimNumbering
                | 
                | Represents a numbering specification.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_attribute_value(self, i_attribute: str, o_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAttributeValue(CATBSTR iAttribute,long oValue)
                |     Retrieves the value corresponding to the given attribute.
                | 
                |     Parameters:
                | 
                |         iAttribute:
                |             The name of attribute. 
                |         oValue:
                |             The value of the attribute.

        :param str i_attribute:
        :param int o_value:
        :return: None
        """
        return self.com_object.GetAttributeValue(i_attribute, o_value)

    def initialize_numbering_values(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InitializeNumberingValues()
                |     Initialize numbering values

        :return: None
        """
        return self.com_object.InitializeNumberingValues()

    def set_attribute_value(self, i_attribute: str, i_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttributeValue(CATBSTR iAttribute,long iValue)
                |     Sets the value corresponding to the given attribute.
                | 
                |     Parameters:
                | 
                |         iAttribute:
                |             The name of attribute. 
                |         iValue:
                |             The value of the attribute. 
                | 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param str i_attribute:
        :param int i_value:
        :return: None
        """
        return self.com_object.SetAttributeValue(i_attribute, i_value)

    def __repr__(self):
        return f'SimNumbering(name="{self.name}")'
