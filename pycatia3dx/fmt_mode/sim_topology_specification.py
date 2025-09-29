"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class SimTopologySpecification(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimTopologySpecification
                | 
                | Represents a Local Topology Specification.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     Returns the type of the Local Topology Specification.

        :return: str
        """

        return self.com_object.Type

    def get_attribute_value(self, i_attribute: str, o_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAttributeValue(CATBSTR iAttribute,CATVariant oValue)
                |     Retrieves the value corresponding to the given attribute.
                | 
                |     Parameters:
                | 
                |         iAttribute:
                |             The identifier of the attribute. 
                | 
                |     Returns:
                |         The value of the Local Topology Specification attribute.

        :param str i_attribute:
        :param CATVariant o_value:
        :return: None
        """
        return self.com_object.GetAttributeValue(i_attribute, o_value)

    def set_attribute_value(self, i_attribute: str, i_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttributeValue(CATBSTR iAttribute,CATVariant iValue)
                |     Sets the value corresponding to the given attribute.
                | 
                |     Parameters:
                | 
                |         iAttribute:
                |             The identifier of the attribute. 
                |         iValue:
                |             The value of the Local Topology Specification attribute.

        :param str i_attribute:
        :param CATVariant i_value:
        :return: None
        """
        return self.com_object.SetAttributeValue(i_attribute, i_value)

    def __repr__(self):
        return f'SimTopologySpecification(name="{self.name}")'
