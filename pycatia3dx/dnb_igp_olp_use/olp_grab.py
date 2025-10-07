"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction


class OLPGrab(OLPInstruction):

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
                |                         OlpGrab
                | 
                | An instruction for grabbing a part.
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
                |     Retrieves the list of products to be grabbed.

        :return: tuple
        """

        return self.com_object.Products

    def add_product(self, i_product_to_add: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddProduct(VPMOccurrence iProductToAdd)
                |     Adds a product to the Grab activity.
                | 
                |     Parameters:
                | 
                |         iVPMOccurrence
                |             The product to grab.

        :param VPMOccurrence i_product_to_add:
        :return: None
        """
        return self.com_object.AddProduct(i_product_to_add.com_object)

    def add_product_by_name(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddProductByName(CATBSTR iName)
                |     Adds a product to the Grab activity by name.
                |     The current editor is searched for products that contain this name. If the
                |     name is not found a warning is posted, but the function succeeds. If multiple
                |     matches are found, they are all added, but a warning is
                |     issued.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The name of the product to grab. 

        :param str i_name:
        :return: None
        """
        return self.com_object.AddProductByName(i_name)

    def __repr__(self):
        return f'OLPGrab(name="{ self.name }")'
