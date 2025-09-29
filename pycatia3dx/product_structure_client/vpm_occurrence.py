"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.mode.position import Position
from pycatia3dx.plm_modeller_base.plm_occurrence import PLMOccurrence
from pycatia3dx.product_structure_client.vpm_instance import VPMInstance
from pycatia3dx.product_structure_client.vpm_rep_occurrences import VPMRepOccurrences

if TYPE_CHECKING:
    from pycatia3dx.product_structure_client.vpm_occurrences import VPMOccurrences


class VPMOccurrence(PLMOccurrence):
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
                |                         VPMOccurrence
                | 
                | Represents a PLM Product Occurrence.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def instance_occurrence_of(self) -> VPMInstance:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InstanceOccurrenceOf() As VPMInstance (Read Only)
                |     Returns its associated PLM Product Instance.
                | 
                |     Example:
                | 
                |            This example shows you how retrieve the instance associated with a
                |            given occurrence.
                |            
                | 
                |            Dim  oProdInstToRetrieve  As VPMInstance
                |            Dim  oProdOccurrence  As VPMOccurrence
                |            ...
                |            Set oProdInstToRetrieve = oProdOccurrence.InstanceOccurrenceOf

        :return: VPMInstance
        """

        return VPMInstance(self.com_object.InstanceOccurrenceOf)

    @property
    def occurrences(self) -> 'VPMOccurrences':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Occurrences() As VPMOccurrences (Read Only)
                |     Returns its PLM Product Occurrences collection.
                |     Role: This method retrieves the PLM Product Occurrences collection object
                |     directly aggregated within this object.
                | 
                |     Example:
                | 
                |            This example shows you how retrieve the collection of occurrences
                |            just beneath a given occurrence.
                |            
                | 
                |            Dim oProdOccurrenceToScan As VPMOccurrence
                |            ...
                |            Dim cListOccurrences As VPMOccurrences
                |            Set cListOccurrences = oProdOccurrenceToScan.Occurrences

        :return: VPMOccurrences
        """
        from pycatia3dx.product_structure_client.vpm_occurrences import VPMOccurrences

        return VPMOccurrences(self.com_object.Occurrences)

    @property
    def position(self) -> Position:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Position() As Position (Read Only)
                |     Returns the PLM Product Occurrence position.
                | 
                |     Example:
                | 
                |             This example shows you how to get the PLM Product Occurence
                |             position.
                |            
                | 
                |          
                |            Dim  oProdOccurrence As VPMOccurrence
                |            ...
                |            Dim  oProdOccurrencePosition  As Position
                |            Set oProdOccurrencePosition = oProdOccurrence.Position

        :return: Position
        """

        return Position(self.com_object.Position)

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
                |             The collection of PLM Product Occurrences 
                | 
                |     Example:
                | 
                |            This example shows you how to retrieve the collection of rep
                |            occurrences
                |            aggregated under a PLM Product Occurrence
                |            
                | 
                |            Dim oProdOccurrenceToScan As VPMOccurrence 
                |            ...
                |            Dim cListRepOccurrences As VPMRepOccurrences
                |            Set cListRepOccurrences = oProdOccurrenceToScan.RepOccurrences

        :return: VPMRepOccurrences
        """

        return VPMRepOccurrences(self.com_object.RepOccurrences)

    def __repr__(self):
        return f'VpmOccurrence(name="{self.name}")'
