"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class TPSHyperLinksManager(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TPSHyperLinksManager
                | 
                | Interface for the Technological Product Specification (TPS)
                | objects.
                | Leaf entity in the Design Pattern Composite. TPS modeler enables definition of
                | specification related to surfaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_nbr_url2(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbrURL2() As long
                |     Gets the number of URL.
                | 
                |     Parameters:
                | 
                |         oNumberOfURL
                |             returns param oNumberOfURL.

        :return: int
        """
        return self.com_object.GetNbrURL2()

    def url(self, i_index: CATVariant) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func URL(CATVariant iIndex) As CATBSTR
                |     Retrieves URL.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of URL. 
                |         oUrl
                |             URL 

        :param CATVariant i_index:
        :return: str
        """
        return self.com_object.URL(i_index)

    def __repr__(self):
        return f'TpsHyperLinksManager(name="{ self.name }")'
