"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_occurrence import PLMOccurrence
from pycatia3dx.product_structure_client.vpm_occurrences import VPMOccurrences
from pycatia3dx.product_structure_client.vpm_reference import VPMReference
from pycatia3dx.product_structure_client.vpm_rep_occurrences import VPMRepOccurrences


class VPMRootOccurrence(PLMOccurrence):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMOccurrence
                |                         VPMRootOccurrence
                | 
                | Represents a PLM Product Root Occurrence.
                | A PLM Product Root Occurrence is edited by a VPM Editor. You retrieve a such
                | object by using PLMProductService.RootOccurrence .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def occurrences(self) -> VPMOccurrences:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Occurrences() As VPMOccurrences (Read Only)
                |     Returns the PLM Product Occurrences collection.
                |     Role: This method retrieves the PLM Product Occurrences collection object
                |     directly aggregated within this object.
                | 
                |     Example:
                | 
                |            This example shows you how retrieve the collection of occurrences
                |            just beneath a given root occurrence.
                |            
                | 
                |            Dim oProdRootOccurrenceToScan As VPMRootOccurrence
                |            ...
                |            Dim  cListOccurrences As VPMOccurrences
                |            Set cListOccurrences = oProdRootOccurrenceToScan.Occurrences

        :return: VPMOccurrences
        """

        return VPMOccurrences(self.com_object.Occurrences)

    @property
    def reference_root_occurrence_of(self) -> VPMReference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceRootOccurrenceOf() As VPMReference (Read
                | Only)
                |     Returns its associated PLM Product Reference.
                | 
                |     Example:
                | 
                |            This example shows you how retrieve the reference associated with a
                |            given occurrence.
                |            
                | 
                |            Dim  oProdRefToRetrieve  As VPMReference
                |            Dim  oProdRootOccurrence  As VPMRootOccurrence
                |            ...
                |            Set oProdRefToRetrieve = oProdRootOccurrence.ReferenceRootOccurrenceOf

        :return: VPMReference
        """

        return VPMReference(self.com_object.ReferenceRootOccurrenceOf)

    @property
    def rep_occurrences(self) -> VPMRepOccurrences:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RepOccurrences() As VPMRepOccurrences (Read Only)
                |     Returns its PLM Product Rep Occurrences Collection.
                |     Role : This method retrieves the PLM Product Rep Occurrences collection object directly aggregated within this object.
                | 
                |     Parameters:
                | 
                |         oRepOccurrences
                |             The collection of PLM Product Rep Occurrences 
                | 
                |     Example:
                | 
                |            This example shows you how to retrieve the collection of rep
                |            occurrences
                |            aggregated under a PLM Product Occurrence
                |            
                | 
                |            Dim oProdRootOccurrenceToScan As VPMRootOccurrence 
                |            ...
                |            Dim cListRepOccurrences As VPMRepOccurrences
                |            Set cListRepOccurrences = oProdRootOccurrenceToScan.RepOccurrences

        :return: VPMRepOccurrences
        """

        return VPMRepOccurrences(self.com_object.RepOccurrences)

    def __repr__(self):
        return f'VpmRootOccurrence(name="{self.name}")'
