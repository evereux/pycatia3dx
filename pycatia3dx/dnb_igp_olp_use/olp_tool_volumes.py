"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_tool_volume import OLPToolVolume


class OLPToolVolumes(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpToolVolumes
                | 
                | A list of tool volumes.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved using OlpController.ToolVolumes
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OLPToolVolume)
        self.com_object = com_object

    def create(self) -> OLPToolVolume:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Create() As OlpToolVolume
                |     Create a new tool volume.
                | 
                |     Returns:
                |         The created tool volume.

        :return: OLPToolVolume
        """
        return OLPToolVolume(self.com_object.Create())

    def delete(self, i_tool_volume: OLPToolVolume) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Delete(OlpToolVolume iToolVolume)
                |     Delete a tool volume.
                | 
                |     Parameters:
                | 
                |         iToolVolume
                |             The tool volume to delete.

        :param OLPToolVolume i_tool_volume:
        :return: None
        """
        return self.com_object.Delete(i_tool_volume.com_object)

    def item(self, i_index: int) -> OLPToolVolume:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(long iIndex) As OlpToolVolume
                |     Get a tool volume by index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The tool volume index in collection (not the index property).
                |             
                | 
                |     Returns:
                |         The tool volume. 

        :param int i_index:
        :return: OLPToolVolume
        """
        return OLPToolVolume(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> OLPToolVolume:
        if (n + 1) > self.count:
            raise StopIteration

        return OLPToolVolume(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[OLPToolVolume]:
        for i in range(self.count):
            yield OLPToolVolume(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'OLPToolVolumes(name="{self.name}")'
