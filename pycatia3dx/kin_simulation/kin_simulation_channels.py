"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.kin_simulation.kin_simulation_channel import KinSimulationChannel
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class KinSimulationChannels(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     KinSimulationChannels
                | 
                | The collection of KinSimulationChannel.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=KinSimulationChannel)
        self.com_object = com_object

    def item(self, i_channel_rank: CATVariant) -> KinSimulationChannel:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iChannelRank) As KinSimulationChannel
                |     Returns a KinSimulationChannel using its rank inside the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iChannelRank
                |             Rank of the KinSimulationChannel inside the collection. It starts
                |             at 1. iChannelRank is a number. 
                | 
                |     Returns:
                |         A KinSimulationChannel.

        :param CATVariant i_channel_rank:
        :return: KinSimulationChannel
        """
        return KinSimulationChannel(self.com_object.Item(i_channel_rank))

    def __getitem__(self, n: int) -> KinSimulationChannel:
        if (n + 1) > self.count:
            raise StopIteration

        return KinSimulationChannel(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[KinSimulationChannel]:
        for i in range(self.count):
            yield KinSimulationChannel(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'KinSimulationChannels(name="{self.name}")'
