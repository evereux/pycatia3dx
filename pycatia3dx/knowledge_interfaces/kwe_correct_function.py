"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class KweCorrectFunction(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KWECorrectFunction
                | 
                | Represents the Knowledge correct function.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def check(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Check() As CATBaseDispatch
                |     Retrieves the check associated to this correct function.
                | 
                |     Returns:
                |         oAssociatedCheck ExpertCheck associated to this correct function.

        :return: AnyObject
        """
        return self.com_object.Check()

    def get_number_of_list_failed_elements(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetNumberOfListFailedElements() As long
                |     Retrieves the number of roots of facts of the rule base.
                | 
                |     Returns:
                |         oArraySize Number of roots of facts.

        :return: int
        """
        return self.com_object.GetNumberOfListFailedElements()

    def list_failed_elements(self, o_list_elements_of_tuple_failed: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub ListFailedElements(CATSafeArrayVariant
                | oListElementsOfTupleFailed)
                |     Returns the list of elements of current tuple failed.
                | 
                |     Parameters:
                | 
                |         oListElementsOfTupleFailed
                |             array of tuple elements.

        :param tuple o_list_elements_of_tuple_failed:
        :return: None
        """
        return self.com_object.ListFailedElements(o_list_elements_of_tuple_failed)

    def __repr__(self):
        return f'KweCorrectFunction(name="{ self.name }")'
