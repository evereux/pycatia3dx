"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.agt.agt_insulation import AGTInsulation
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class AGTInsulations(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AGTInsulations
                | 
                | Object for AGTInsulations.
                | To retrieve Insulation from collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AGTInsulation)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> AGTInsulation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As AGTInsulation
                |     Retrieves a Insulation from the collection of Insulation.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of AGTInsulation 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ThisInsulation the second Insulation,
                |              
                |              and in ThisInsulation the Insulation named MyInsulation.2 in the
                |              Insulation collection. 
                |              
                | 
                |              Dim myPart as CATIAPart
                |              Set myPart = CATIA.ActiveEditor.ActievObject
                |              Dim ThisAGTRoot As AGTRoot
                |              Set ThisAGTRoot = myPart.GetItem("CATAGTRoot")
                |              Dim ThisInsulation As AGTInsulation
                |              Set ThisInsulation = ThisAGTRoot.Insulations.Item(2)
                |              Dim ThisInsulation As AGTInsulation
                |              Set ThisInsulation = ThisAGTRoot.Insulations.Item("MyInsulation.2")

        :param CATVariant i_index:
        :return: AGTInsulation
        """
        return AGTInsulation(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> AGTInsulation:
        if (n + 1) > self.count:
            raise StopIteration

        return AGTInsulation(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[AGTInsulation]:
        for i in range(self.count):
            yield AGTInsulation(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'AGTInsulations(name="{self.name}")'
