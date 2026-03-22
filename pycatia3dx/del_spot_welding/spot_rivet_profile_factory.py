"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.del_spot_welding.spot_rivet_profile import SpotRivetProfile


class SpotRivetProfileFactory(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SpotRivetProfileFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SpotRivetProfile)
        self.com_object = com_object

    def create_rivet_profile(self, o_spot_rivet_profile: SpotRivetProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateRivetProfile(SpotRivetProfile oSpotRivetProfile)
                |     This method creates a Spot-Rivet profile
                | 
                |     Parameters:
                | 
                |         oSpotRivetProfile,
                |             newly created DrillRivet profile 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param SpotRivetProfile o_spot_rivet_profile:
        :return: None
        """
        return self.com_object.CreateRivetProfile(o_spot_rivet_profile.com_object)

    def destroy_rivet_profile(self, i_spot_rivet_profile: SpotRivetProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DestroyRivetProfile(SpotRivetProfile iSpotRivetProfile)
                |     This method destroys the Spot-Rivet profile
                | 
                |     Parameters:
                | 
                |         iSpotRivetProfile,
                |             Spot-Rivet profile to be destroyed. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param SpotRivetProfile i_spot_rivet_profile:
        :return: None
        """
        return self.com_object.DestroyRivetProfile(i_spot_rivet_profile.com_object)

    def __repr__(self):
        return f'SpotRivetProfileFactory(name="{self.name}")'
