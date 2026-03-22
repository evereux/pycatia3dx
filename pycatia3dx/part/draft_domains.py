"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.part.draft_domain import DraftDomain
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DraftDomains(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DraftDomains
                | 
                | The collection of draft domains used by the draft shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DraftDomain)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> DraftDomain:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As DraftDomain
                |     Returns a draft domain using its index or its name from the DraftDomains
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the draft domain to retrieve from the
                |             collection of draft domains. As a numerics, this index is the rank of the draft
                |             domain in the collection. The index of the first draft domain in the collection
                |             is 1, and the index of the last draft domain is Count. As a string, it is the
                |             name you assigned to the draft domain using the AnyObject.Name property.
                |             
                | 
                |     Returns:
                |         The retrieved draft domain
                | 
                |         Example:
                |             The following example returns in domain the third draft domain of
                |             the firstDraftDomains collection:
                | 
                |              Set domain = firstDraftDomains.Item(3)

        :param CATVariant i_index:
        :return: DraftDomain
        """
        return DraftDomain(self.com_object.Item(i_index))

    def __repr__(self):
        return f'DraftDomains(name="{self.name}")'
