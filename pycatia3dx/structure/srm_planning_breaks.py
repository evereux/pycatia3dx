"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.srm_planning_break import SrmPlanningBreak
from pycatia3dx.types.general import CATVariant


class SrmPlanningBreaks(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SrmPlanningBreaks
                | 
                | Object for SrmPlanningBreaks
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SrmPlanningBreak)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SrmPlanningBreak:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SrmPlanningBreak
                |     Retrieves a SrmPlanningBreak
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of SrmPlanningBreak 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first item from the list of
                |              SrmPlanningBreaks.
                |              
                | 
                |               Dim ObjSrmPlanningBreaks As SrmPlanningBreaks
                |               Set ObjSrmPlanningBreaks = ObjSrmProxyPanel.GetPlanningBreaks
                |               Dim ObjSrmPlanningBreak As SrmPlanningBreak
                |               Set ObjSrmPlanningBreak = ObjSrmPlanningBreaks.Item(1)

        :param CATVariant i_index:
        :return: SrmPlanningBreak
        """
        return SrmPlanningBreak(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> SrmPlanningBreak:
        if (n + 1) > self.count:
            raise StopIteration

        return SrmPlanningBreak(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SrmPlanningBreak]:
        for i in range(self.count):
            yield SrmPlanningBreak(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SrmPlanningBreaks(name="{self.name}")'
