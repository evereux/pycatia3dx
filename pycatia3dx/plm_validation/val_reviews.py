"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.plm_validation.val_review import VALReview
from pycatia3dx.types.general import CATVariant


class VALReviews(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VALReviews
                | 
                | A collection of Reviews.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=VALReview)
        self.com_object = com_object

    def add(self) -> VALReview:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As VALReview
                |     Creates a Review and adds it to the Review collection.
                | 
                |     Returns:
                |         The created Review 
                |     Example:
                | 
                |             This example creates a new Review in the cReviews
                |             collection.
                |
                |             Dim oNewReviewText As Review
                |             Set oNewReviewText = cReviews.Add

        :return: VALReview
        """
        return VALReview(self.com_object.Add())

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Review using its index from the Reviews
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Review to retrieve from the collection
                |             of Reviews. As a numerics, this index is the rank of the Review in the
                |             collection. The index of the first Review in the collection is 1, and the index
                |             of the last Review is Count. As a string, it is the name you assigned to the
                |             Review. 
                | 
                |     Returns:
                |         The retrieved Review 
                |     Example:
                | 
                |             This example retrieves in oReview1 the ninth
                |             Review,
                |             and in oReview2 the Review named
                |             Review3 from the cReviews collection. 
                |
                |             Dim oReview1 As Review
                |             Set oReview1 = cReviews.Item(9)
                |             Dim oReview2 As Review
                |             Set oReview2 = cReviews.Item("Review3")

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Review from the Reviews collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Review to retrieve from the collection
                |             of Reviews. As a numerics, this index is the rank of the Review in the
                |             collection. The index of the first Review in the collection is 1, and the index
                |             of the last Review is Count. As a string, it is the name you assigned to the
                |             Review. 
                | 
                |     Example:
                | 
                |             The following example removes the tenth Review and the Review
                |             named
                |             Review2 from the cReviews collection.
                |
                |             cReviews.Remove(10)
                |             cReviews.Remove("Review2")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __getitem__(self, n: int) -> VALReview:
        if (n + 1) > self.count:
            raise StopIteration

        return VALReview(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[VALReview]:
        for i in range(self.count):
            yield VALReview(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'ValReviews(name="{self.name}")'
