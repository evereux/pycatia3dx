"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_rep_occurrence import VPMRepOccurrence
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class VPMRepOccurrences(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VPMRepOccurrences
                | 
                | Interface representing a list of PLM Rep Occurrences.
                | 
                | Role : This collections contains the list of PLM Rep Occurrences
                | under a PLM Occurrence Use : In order to retrieve this collection,
                | please refer to the service :
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=VPMRepOccurrence)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> VPMRepOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As VPMRepOccurrence
                |     Returns a PLM Rep Occurrence from its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the PLM Rep Occurrence to retrieve from the
                |             collection. As a numerics, this index is the rank of the rep occurrence in the
                |             collection. The index of the first rep occurrence in the collection is 1, and
                |             the index of the last rep occurrence is returned by Collection.get_Count
                |             method. 
                | 
                |     Returns:
                |         The retrieved PLM Rep Occurrence. 
                |     Example:
                | 
                |             This example shows you how to retrieve the third rep occurrence
                |             beneath an occurrence (oOccurrenceToScan)
                |            
                | 
                |            Dim  oRepOccurrenceToRetrieve  As VPMRepOccurrence
                |            Dim oOccurrenceToScan As VPMOccurrence
                |            ...
                |            Dim  cListRepOccurrences As VPMRepOccurrences
                |            Set cListOccurrences = oOccurrenceToScan.RepOccurrences
                |            ...
                |            Set  oRepOccurrenceToRetrieve = cListOccurrences.Item( 3 )

        :param CATVariant i_index:
        :return: VPMRepOccurrence
        """
        return VPMRepOccurrence(self.com_object.Item(i_index))

    def __repr__(self):
        return f'VpmRepOccurrences(name="{self.name}")'
