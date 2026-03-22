"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_case import OLPCase


class OLPCases(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpCases
                | 
                | A list of case blocks for a test case instruction.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OLPCase)
        self.com_object = com_object

    def add_new_case(self) -> OLPCase:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddNewCase() As OlpCase
                |     Create a new case and add it to the end.

        :return: OLPCase
        """
        return OLPCase(self.com_object.AddNewCase())

    def item(self, i_index: int) -> OLPCase:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(long iIndex) As OlpCase
                |     Retrieve a case by its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the first case in the collection is 1, and the index
                |             of the last parameter is Count. 
                | 
                |     Returns:
                |         The case retrieved. If the index is out of bounds, the function fails.

        :param int i_index:
        :return: OLPCase
        """
        return OLPCase(self.com_object.Item(i_index))

    def __repr__(self):
        return f'OLPCases(name="{self.name}")'
