"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.tps.tps_view import TPSView
from pycatia3dx.types.general import CATVariant


class TPSViews(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     TPSViews
                | 
                | Interface for collection of TPS Views CATIATPSView.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=TPSView)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> TPSView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As AnyObject
                |     Retrieve a TPS View. 

        :param CATVariant i_index:
        :return: TPSView
        """
        return TPSView(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> TPSView:
        if (n + 1) > self.count:
            raise StopIteration

        return TPSView(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[TPSView]:
        for i in range(self.count):
            yield TPSView(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'TpsViews(name="{self.name}")'
