"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.product_structure_client.vpm_publication import VPMPublication
from pycatia3dx.product_structure_client.vpm_reference import VPMReference
from pycatia3dx.system.any_object import AnyObject


class SimPublicationServices(Service):
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
                |                         SimPublicationServices

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_publication(self, i_reference_product: VPMReference, i_link: AnyObject,
                           i_publication_name: str) -> VPMPublication:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreatePublication(VPMReference iReferenceProduct,AnyObject iLink,CATBSTR
                | iPublicationName) As VPMPublication
                |     Creates a publication.
                | 
                |     Parameters:
                | 
                |         iReferenceProduct:
                |             The reference product which will contain the publication.
                |             
                |         iLink:
                |             The link object corresponding to the object to publish.
                |             
                |         iPublicationName:
                |             The name of the publication. 
                | 
                |     Returns:
                |         The created publication.

        :param VPMReference i_reference_product:
        :param AnyObject i_link:
        :param str i_publication_name:
        :return: VPMPublication
        """
        return VPMPublication(
            self.com_object.CreatePublication(i_reference_product.com_object, i_link.com_object, i_publication_name))

    def get_published_element(self, i_publication: VPMPublication, o_link: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPublishedElement(VPMPublication iPublication,AnyObject
                | oLink)
                |     Retrieves the published element
                | 
                |     Parameters:
                | 
                |         iPublication:
                |             The publication on which the published element should be retrieved.
                |             
                |         oLink:
                |             The link object corresponding to the published element.

        :param VPMPublication i_publication:
        :param AnyObject o_link:
        :return: None
        """
        return self.com_object.GetPublishedElement(i_publication.com_object, o_link.com_object)

    def modify_published_element(self, i_publication: VPMPublication, i_link: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ModifyPublishedElement(VPMPublication iPublication,AnyObject
                | iLink)
                |     Modifies the published element
                | 
                |     Parameters:
                | 
                |         iPublication:
                |             The publication on which the published element should be changed.
                |             
                |         iLink:
                |             The link object corresponding to the new object to publish.

        :param VPMPublication i_publication:
        :param AnyObject i_link:
        :return: None
        """
        return self.com_object.ModifyPublishedElement(i_publication.com_object, i_link.com_object)

    def remove_publication(self, i_reference_product: VPMReference, i_publication: VPMPublication) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemovePublication(VPMReference iReferenceProduct,VPMPublication
                | iPublication)
                |     Removes a publication.
                | 
                |     Parameters:
                | 
                |         iReferenceProduct:
                |             The reference product which contains the publication.
                |             
                |         iPublication:
                |             The publication to remove.

        :param VPMReference i_reference_product:
        :param VPMPublication i_publication:
        :return: None
        """
        return self.com_object.RemovePublication(i_reference_product.com_object, i_publication.com_object)

    def remove_publication_by_name(self, i_reference_product: VPMReference, i_publication_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemovePublicationByName(VPMReference iReferenceProduct,CATBSTR
                | iPublicationName)
                |     Removes a publication by its name.
                | 
                |     Parameters:
                | 
                |         iReferenceProduct:
                |             The reference product which contains the publication.
                |             
                |         iPublicationName:
                |             The publication's name to remove.

        :param VPMReference i_reference_product:
        :param str i_publication_name:
        :return: None
        """
        return self.com_object.RemovePublicationByName(i_reference_product.com_object, i_publication_name)

    def replace_and_rename_publication(self, i_publication: VPMPublication, i_new_name: str,
                                       i_reroute: bool) -> VPMPublication:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ReplaceAndRenamePublication(VPMPublication iPublication,CATBSTR
                | iNewName,boolean iReroute) As VPMPublication
                |     Replaces an existing Publication by a new identical Publication with a new
                |     functional name.
                | 
                |     Parameters:
                | 
                |         iPublication
                |             Original Publication to replace and rename. 
                |         iNewName
                |             Functional name of the new Publication.
                |             Has to be unique and different from iOldPub's name
                |             
                |         iReroute
                |             Flag indicating whether loaded links pointing iPublication should
                |             be automatically rerouted. Only links that are loaded in session can be
                |             rerouted, links that are not loaded will be broken.
                |             
                |         oNewPub
                |             The new, renamed Publication.

        :param VPMPublication i_publication:
        :param str i_new_name:
        :param bool i_reroute:
        :return: VPMPublication
        """
        return VPMPublication(
            self.com_object.ReplaceAndRenamePublication(i_publication.com_object, i_new_name, i_reroute))

    def __repr__(self):
        return f'SimPublicationServices(name="{self.name}")'
