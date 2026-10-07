"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.agt.agt_draught_stop import AGTDraughtStop
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class AGTDraughtStops(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AGTDraughtStops
                | 
                | Object for AGTDraughtStops.
                | To retrieve DraughtStop from collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AGTDraughtStop)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> AGTDraughtStop:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As AGTDraughtStop
                |     Retrieves a DraughtStop from the collection of
                |     DraughtStop.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of DraughtStop. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ThisDraughtStop the second DraughtStop,
                |              
                |              and in ThisDraughtStop the DraughtStop named MyDraughtStop.2 in
                |              the DraughtStop collection. 
                |              
                | 
                |              Dim myPart as CATIAPart
                |              Set myPart = CATIA.ActiveEditor.ActievObject
                |              Dim ThisAGTRoot As AGTRoot
                |              Set ThisAGTRoot = myPart.GetItem("CATAGTRoot")
                |              Dim ThisDraughtStop As AGTDraughtStop
                |              Set ThisDraughtStop = ThisAGTRoot.DraughtStops.Item(2)
                |              Dim ThisDraughtStop As AGTDraughtStop
                |              Set ThisDraughtStop = ThisAGTRoot.DraughtStops.Item("MyDraughtStop.2")

        :param CATVariant i_index:
        :return: AGTDraughtStop
        """
        return AGTDraughtStop(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> AGTDraughtStop:
        if (n + 1) > self.count:
            raise StopIteration

        return AGTDraughtStop(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[AGTDraughtStop]:
        for i in range(self.count):
            yield AGTDraughtStop(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'AGTDraughtStops(name="{self.name}")'
