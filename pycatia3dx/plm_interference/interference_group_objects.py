"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.plm_modeller_base.plm_occurrence import PLMOccurrence
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class InterferenceGroupObjects(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     InterferenceGroupObjects
                | 
                | A collection of InterferenceGroupObjects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=VPMOccurrence)
        self.com_object = com_object

    def add(self, i_plm_occurence: PLMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(PLMOccurrence iPLMOccurence)
                | 
                |     Deprecated:
                |         R213. use Add2
                |         Adds an occurrence in the InterferenceGroupObjects collection.
                |         
                |     Parameters:
                | 
                |         iPLMOccurence
                |             The occurrence to add. 
                | 
                |     Example:
                | 
                |             The following example adds the oOccurrence1 occurrence to the
                |             cInterferenceGroupObjects collection.
                |             
                | 
                |             cInterferenceGroupObjects.Add(oOccurrence1)

        :param PLMOccurrence i_plm_occurence:
        :return: None
        """
        return self.com_object.Add(i_plm_occurence.com_object)

    def add2(self, i_vpm_occurence: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add2(VPMOccurrence iVPMOccurence)
                |     Adds a VPMOccurrence in the InterferenceGroupObjects
                |     collection.
                | 
                |     Parameters:
                | 
                |         iVPMOccurence
                |             The occurrence to add.

        :param VPMOccurrence i_vpm_occurence:
        :return: None
        """
        return self.com_object.Add2(i_vpm_occurence.com_object)

    def item(self, i_index: CATVariant) -> VPMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns an occurrence using its index from the InterferenceGroupObjects
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the occurrence to retrieve from the collection of
                |             InterferenceGroupObjects. As a numerics, this index is the rank of the
                |             occurrence in the collection. The index of the first occurrence in the
                |             collection is 1, and the index of the last occurrence is Count.
                |             
                | 
                |     Returns:
                |         The retrieved occurrence 
                |     Example:
                | 
                |             This example retrieves in oOccurrence1 the ninth occurrence from
                |             the cInterferenceGroupObjects collection.
                |             
                | 
                |             Dim oOccurrence1 As PLMOccurrence
                |             Set oOccurrence1 = cInterferenceGroupObjects.Item(9)

        :param CATVariant i_index:
        :return: VPMOccurrence
        """
        return VPMOccurrence(self.com_object.Item(i_index))

    def remove(self, i_plm_occurence: PLMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(PLMOccurrence iPLMOccurence)
                | 
                |     Deprecated:
                |         R213. use Remove2
                |         Removes an occurrence from the InterferenceGroupObjects collection.
                |         
                |     Parameters:
                | 
                |         iPLMOccurence
                |             The occurrence to remove. 
                | 
                |     Example:
                | 
                |             The following example removes the oOccurrence1 occurrence from the
                |             cInterferenceGroupObjects collection.
                |             
                | 
                |             cInterferenceGroupObjects.Remove(oOccurrence1)

        :param PLMOccurrence i_plm_occurence:
        :return: None
        """
        return self.com_object.Remove(i_plm_occurence.com_object)

    def remove2(self, i_vpm_occurence: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove2(VPMOccurrence iVPMOccurence)
                |     Removes an occurrence from the InterferenceGroupObjects
                |     collection.
                | 
                |     Parameters:
                | 
                |         iVPMOccurence
                |             The occurrence to remove.

        :param VPMOccurrence i_vpm_occurence:
        :return: None
        """
        return self.com_object.Remove2(i_vpm_occurence.com_object)

    def __getitem__(self, n: int) -> VPMOccurrence:
        if (n + 1) > self.count:
            raise StopIteration

        return VPMOccurrence(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[VPMOccurrence]:
        for i in range(self.count):
            yield VPMOccurrence(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'InterferenceGroupObjects(name="{self.name}")'
