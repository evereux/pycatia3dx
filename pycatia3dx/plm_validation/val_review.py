"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.system.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia3dx.plm_validation.val_reviews import VALReviews


class VALReview(PLMEntity):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         VALReview
                | 
                | Allows management of Review entity
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def reviews(self) -> 'VALReviews':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Reviews() As VALReviews (Read Only)
                |     Returns the Reviews collection.

        :return: VALReviews
        """
        from pycatia3dx.plm_validation.val_reviews import VALReviews
        return VALReviews(self.com_object.Reviews)

    def get_factory(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFactory(CATBSTR iType) As CATBaseDispatch
                |     Returns the Factory for a given type.
                | 
                |     Example:
                | 
                |           Example to get the cMarkers collection.
                |             
                | 
                |              Dim cMarkers As Markers 
                |              Set cMarkers = TheVALReview.GetFactory("Markers")
                |             
                | 
                | 
                |           Example to get the cSlides collection.
                |             
                | 
                |              Dim cSlides As Slides 
                |              Set cSlides = TheVALReview.GetFactory("Slides")

        :param str i_type:
        :return: AnyObject
        """
        return self.com_object.GetFactory(i_type)

    def __repr__(self):
        return f'ValReview(name="{self.name}")'
