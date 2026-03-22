"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class VPMOccurrences(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VPMOccurrences
                | 
                | A collection of PLM Product Occurrences.
                | This collection contains the children of a PLM Product
                | Occurrence.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=VPMOccurrence)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> VPMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As VPMOccurrence
                |     Returns a PLM Product Occurrence from its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the PLM Product Occurrence (occurrence) to retrieve
                |             from the collection. As a numerics, this index is the rank of the occurrence in
                |             the collection. The index of the first occurrence in the collection is 1, and
                |             the index of the last Occurrence is returned by Collection.get_Count method.
                |             
                | 
                |     Returns:
                |         The retrieved PLM Product Occurrence. 
                |     Example:
                | 
                |             This example shows you how to retrieve the third occurrence beneath
                |             another occurence (oOccurrenceToScan)
                |            
                | 
                |            Dim  oOccurrenceToRetrieve  As VPMOccurrence
                |            Dim oOccurrenceToScan As VPMOccurrence
                |            ...
                |            Dim  cListOccurrences As VPMOccurrences
                |            Set cListOccurrences = oOccurrenceToScan.Occurrences
                |            ...
                |            Set  oOccurrenceToRetrieve = cListOccurrences.Item(3)
                |           
                | 
                | 
                |            This second example shows you how to retrieve an occurrence by its
                |            name.
                |            
                | 
                |            Dim  oOccurrenceToRetrieve  As VPMOccurrence
                |            Dim oOccurrenceToScan As VPMOccurrence
                |            ...
                |            Dim  cCollecOccurrences As Collection
                |            Set cCollecOccurrences = oOccurrenceToScan.Occurrences
                |            ...
                |            Set  oOccurrenceToRetrieve = cCollecOccurrences.GetItem("MyName")
                |           
                | 
                | 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param CATVariant i_index:
        :return: VPMOccurrence
        """
        return VPMOccurrence(self.com_object.Item(i_index))

    def __repr__(self):
        return f'VpmOccurrences(name="{self.name}")'
