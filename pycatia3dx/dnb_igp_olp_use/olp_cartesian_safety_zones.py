"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_cartesian_safety_zone import OLPCartesianSafetyZone


class OLPCartesianSafetyZones(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpCartesianSafetyZones
                | 
                | A list of Cartesian safety zones.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved using
                | OlpController.CartesianSafetyZones
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OLPCartesianSafetyZone)
        self.com_object = com_object

    def create(self) -> OLPCartesianSafetyZone:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Create() As OlpCartesianSafetyZone
                |     Create a new zone.
                | 
                |     Returns:
                |         The created zone.

        :return: OLPCartesianSafetyZone
        """
        return OLPCartesianSafetyZone(self.com_object.Create())

    def delete(self, i_zone: OLPCartesianSafetyZone) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Delete(OlpCartesianSafetyZone iZone)
                |     Delete a zone.
                | 
                |     Parameters:
                | 
                |         iZone
                |             The zone to delete.

        :param OLPCartesianSafetyZone i_zone:
        :return: None
        """
        return self.com_object.Delete(i_zone.com_object)

    def item(self, i_index: int) -> OLPCartesianSafetyZone:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(long iIndex) As OlpCartesianSafetyZone
                |     Get a zone by index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The zone index in collection (not the index property).
                |             
                | 
                |     Returns:
                |         The zone. 

        :param int i_index:
        :return: OLPCartesianSafetyZone
        """
        return OLPCartesianSafetyZone(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> OLPCartesianSafetyZone:
        if (n + 1) > self.count:
            raise StopIteration

        return OLPCartesianSafetyZone(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[OLPCartesianSafetyZone]:
        for i in range(self.count):
            yield OLPCartesianSafetyZone(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'OLPCartesianSafetyZones(name="{self.name}")'
