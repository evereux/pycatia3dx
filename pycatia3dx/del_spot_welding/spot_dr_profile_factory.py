"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.del_spot_welding.spot_dr_profile import SpotDrProfile


class SpotDrProfileFactory(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SpotDrProfileFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SpotDrProfile)
        self.com_object = com_object

    def create_drill_rivet_profile(self, i_type: int, o_drill_rivet_profile: SpotDrProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateDrillRivetProfile(DELDRProfileType iType,SpotDrProfile
                | oDrillRivetProfile)
                |     This method creates a DrillRivet profile
                | 
                |     Parameters:
                | 
                |         iType,
                |             Valid Values : DrillOnly, RivetOnly, DrillRivet 
                |         oDrillRivetProfile,
                |             newly created DrillRivet profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_type:
        :param SpotDrProfile o_drill_rivet_profile:
        :return: None
        """
        return self.com_object.CreateDrillRivetProfile(i_type, o_drill_rivet_profile.com_object)

    def destroy_drill_rivet_profile(self, i_drill_rivet_profile: SpotDrProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DestroyDrillRivetProfile(SpotDrProfile iDrillRivetProfile)
                |     This method destroys the DrillRivet profile
                | 
                |     Parameters:
                | 
                |         iDrillRivetProfile,
                |             DrillRivet profile to be destroyed. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param SpotDrProfile i_drill_rivet_profile:
        :return: None
        """
        return self.com_object.DestroyDrillRivetProfile(i_drill_rivet_profile.com_object)

    def __getitem__(self, n: int) -> SpotDrProfile:
        if (n + 1) > self.count:
            raise StopIteration

        return SpotDrProfile(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SpotDrProfile]:
        for i in range(self.count):
            yield SpotDrProfile(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SpotDrProfileFactory(name="{self.name}")'
