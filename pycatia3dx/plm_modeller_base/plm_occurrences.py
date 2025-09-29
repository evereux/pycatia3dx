"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_occurrence import PLMOccurrence
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class PLMOccurrences(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMOccurrences
                | 
                | Collection of PLM Product Occurrences.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> PLMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As PLMOccurrence
                |     Returns a PLM Product Occurrence from its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the PLMOccurrence to retrieve from the collection of
                |             PLMOccurrences. As a numerics, this index is the rank of the PLMOccurrence in
                |             the collection. The index of the first PLMOccurrence in the collection is 1,
                |             and the index of the last PLMOccurrence is returned by Collection.get_Count
                |             method. 
                | 
                |     Returns:
                |         A PLM Product Occurrence.

        :param CATVariant i_index:
        :return: PLMOccurrence
        """
        return PLMOccurrence(self.com_object.Item(i_index))

    def __repr__(self):
        return f'PlmOccurrences(name="{self.name}")'
