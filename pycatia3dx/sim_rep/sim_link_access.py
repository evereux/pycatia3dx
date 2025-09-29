"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimLinkAccess(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimLinkAccess
                | 
                | Represents the service to manage the feature links.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_link(self, i_name: str, i_link: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddLink(CATBSTR iName,AnyObject iLink)
                |     Adds a link.
                | 
                |     Parameters:
                | 
                |         iName:
                |             Name of the attribute will receive the built connector.
                |             
                |         iLink:
                |             The link object that represent the link to store.
                |             PLMProductService.ComposeLink

        :param str i_name:
        :param AnyObject i_link:
        :return: None
        """
        return self.com_object.AddLink(i_name, i_link.com_object)

    def add_link_with_context(self, i_attr_name: str, i_link: AnyObject, i_context: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddLinkWithContext(CATBSTR iAttrName,AnyObject iLink,VPMOccurrence
                | iContext)
                |     Adds a link.
                | 
                |     Parameters:
                | 
                |         iName:
                |             Name of the attribute will receive the built connector.
                |             
                |         iLink:
                |             The link object that represent the link to store. 
                |         iContext:
                |             The context that will be concatenated with the support when the
                |             created mesh part and the support are not in the same product
                |             .
                |             PLMProductService.ComposeLink

        :param str i_attr_name:
        :param AnyObject i_link:
        :param VPMOccurrence i_context:
        :return: None
        """
        return self.com_object.AddLinkWithContext(i_attr_name, i_link.com_object, i_context.com_object)

    def get_all_links(self, i_name: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAllLinks(CATBSTR iName) As CATSafeArrayVariant
                |     Gets all links.
                | 
                |     Parameters:
                | 
                |         iName:
                |             Name of the attribute containing the links. 
                | 
                |     Returns:
                |         The links

        :param str i_name:
        :return: tuple
        """
        return self.com_object.GetAllLinks(i_name)

    def get_nb_links(self, i_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbLinks(CATBSTR iName) As long
                |     Gets the number of links.
                | 
                |     Parameters:
                | 
                |         iName:
                |             Name of the attribute containing the links. 
                | 
                |     Returns:
                |         The number of links.

        :param str i_name:
        :return: int
        """
        return self.com_object.GetNbLinks(i_name)

    def remove_all_links(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAllLinks(CATBSTR iName)
                |     Removes all links.
                | 
                |     Parameters:
                | 
                |         iName:
                |             Name of the attribute containing the links.

        :param str i_name:
        :return: None
        """
        return self.com_object.RemoveAllLinks(i_name)

    def remove_link(self, i_name: str, i_link: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveLink(CATBSTR iName,AnyObject iLink)
                |     Removes a link.
                | 
                |     Parameters:
                | 
                |         iName:
                |             Name of the attribute containing the links. 
                |         iLink:
                |             The link object that represent the link to remove.
                |             PLMProductService.ComposeLink

        :param str i_name:
        :param AnyObject i_link:
        :return: None
        """
        return self.com_object.RemoveLink(i_name, i_link.com_object)

    def __repr__(self):
        return f'SimLinkAccess(name="{self.name}")'
