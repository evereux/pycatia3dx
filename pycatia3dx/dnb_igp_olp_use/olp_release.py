"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction


class OLPRelease(OLPInstruction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpInstruction
                |                         OlpRelease
                | 
                | An instruction that releases a grabbed part.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def products(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Products() As CATSafeArrayVariant (Read Only)
                |     Retrieves the list of products to be released.

        :return: tuple
        """

        return self.com_object.Products

    def add_product(self, i_vpm_occurrence: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddProduct(VPMOccurrence iVPMOccurrence)
                |     Adds a product to the Release activity.
                | 
                |     Parameters:
                | 
                |         iVPMOccurrence
                |             The product to release.

        :param VPMOccurrence i_vpm_occurrence:
        :return: None
        """
        return self.com_object.AddProduct(i_vpm_occurrence.com_object)

    def add_product_by_name(self, i_product: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddProductByName(CATBSTR iProduct)
                |     Adds a product to the Release activity by name.
                |     The current editor is searched for products that contain this name. If the
                |     name is not found a warning is posted, but the function succeeds. If multiple
                |     matches are found, they are all added, but a warning is
                |     issued.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The name of the product to release. 

        :param str i_product:
        :return: None
        """
        return self.com_object.AddProductByName(i_product)

    def __repr__(self):
        return f'OLPRelease(name="{ self.name }")'
