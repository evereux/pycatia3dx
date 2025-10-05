"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_spot_welding.spot_dr_manufacturing_pattern import SpotDrManufacturingPattern
from pycatia3dx.del_spot_welding.spot_dr_profile import SpotDrProfile
from pycatia3dx.del_spot_welding.spot_dr_sequence import SpotDrSequence


class SpotDrSequenceFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrSequenceFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_drill_rivet_sequence(self, i_spot_dr_profile: SpotDrProfile, i_spot_dr_pattern: SpotDrManufacturingPattern, i_index: int, i_optimize_cycle_time: bool) -> SpotDrSequence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDrillRivetSequence(SpotDrProfile
                | iSpotDrProfile,SpotDrManufacturingPattern iSpotDrPattern,short iIndex,boolean
                | iOptimizeCycleTime) As SpotDrSequence
                |     This method creates a DrillRivet Sequence
                | 
                |     Parameters:
                | 
                |         iSpotDrProfile,
                |             Drill-Rivet Profile to assign.Targets are created depending on the
                |             DRProfile Type. 
                |         iSpotDrPattern,The
                |             Fasteners in the Pattern will be used to set the target location .
                |             
                |         iIndex,
                |             Index where to create the instruction.If passed as -1 SpotDSequence
                |             is created at the end of the Top sequence. 
                |         iOptimizeCycleTime,Is
                |             Cycle Time Optimization enabled. 
                |         oDrillRivetSequence,
                |             newly created SpotDrSequence. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param SpotDrProfile i_spot_dr_profile:
        :param SpotDrManufacturingPattern i_spot_dr_pattern:
        :param int i_index:
        :param bool i_optimize_cycle_time:
        :return: SpotDrSequence
        """
        return SpotDrSequence(self.com_object.CreateDrillRivetSequence(i_spot_dr_profile.com_object, i_spot_dr_pattern.com_object, i_index, i_optimize_cycle_time))

    def delete_drill_rivet_sequence(self, i_drill_rivet_sequence: SpotDrSequence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteDrillRivetSequence(SpotDrSequence
                | iDrillRivetSequence)
                |     This method deletes the passed DrillRivet Sequence
                | 
                |     Parameters:
                | 
                |         iDrillRivetSequence,
                |             DrillRivet Sequence to be deleted. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param SpotDrSequence i_drill_rivet_sequence:
        :return: None
        """
        return self.com_object.DeleteDrillRivetSequence(i_drill_rivet_sequence.com_object)

    def __repr__(self):
        return f'SpotDrSequenceFactory(name="{ self.name }")'
