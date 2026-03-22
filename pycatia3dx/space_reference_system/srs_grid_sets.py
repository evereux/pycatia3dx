"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.space_reference_system.srs_grid_set import SrsGridSet
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SrsGridSets(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SrsGridSets
                | 
                | Object for RfgPlaneSystems
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SrsGridSet)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SrsGridSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SrsGridSet
                |     Returns a SrsGridSet from a list of PlaneSystems
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of SrsGridSet 
                | 
                |     Returns:
                |         The retrieved grid face based on the index. 
                |     Example:
                | 
                |              This example retrieves  the first PlaneSet from the list of
                |              GridSets.
                |
                |               Set GridSetReference = ListOfPlaneSystems.Item(1)

        :param CATVariant i_index:
        :return: SrsGridSet
        """
        return SrsGridSet(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SrsGridSets(name="{self.name}")'
