"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_spot_welding.spot_dr_action import SpotDrAction
from pycatia3dx.del_spot_welding.spot_dr_manufacturing_fastener import SpotDrManufacturingFastener
from pycatia3dx.del_spot_welding.spot_dr_manufacturing_pattern import SpotDrManufacturingPattern
from pycatia3dx.del_spot_welding.spot_dr_profile import SpotDrProfile


class SpotDrActionFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrActionFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_drill_rivet_action(self, i_spot_dr_profile: SpotDrProfile, i_fastener: SpotDrManufacturingFastener, i_index: int) -> SpotDrAction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDrillRivetAction(SpotDrProfile
                | iSpotDrProfile,SpotDrManufacturingFastener iFastener,short iIndex) As
                | SpotDrAction
                |     This method creates a DrillRivet action
                | 
                |     Parameters:
                | 
                |         iSpotDrProfile,
                |             Drill-Rivet Profile to assign.Targets are created depending on the
                |             DRProfile Type. 
                |         iFastener,
                |             The Fastener will be used to set the target location .
                |             
                |         iIndex,
                |             Index where to create the instruction.If passed as -1 SpotDrAction
                |             is created at the end of the Top sequence. 
                |         oDrillRivetAction,
                |             newly created DrillRivet action 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param SpotDrProfile i_spot_dr_profile:
        :param SpotDrManufacturingFastener i_fastener:
        :param int i_index:
        :return: SpotDrAction
        """
        return SpotDrAction(self.com_object.CreateDrillRivetAction(i_spot_dr_profile.com_object, i_fastener.com_object, i_index))

    def create_drill_rivet_actions(self, i_spot_dr_profile: SpotDrProfile, i_pattern: SpotDrManufacturingPattern, i_index: int, i_optimize_cycle_time: bool) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDrillRivetActions(SpotDrProfile
                | iSpotDrProfile,SpotDrManufacturingPattern iPattern,short iIndex,boolean
                | iOptimizeCycleTime) As CATSafeArrayVariant
                |     This method creates a DrillRivet action
                | 
                |     Parameters:
                | 
                |         iSpotDrProfile,
                |             Drill-Rivet Profile to assign.Targets are created depending on the
                |             DRProfile Type. 
                |         iPattern,The
                |             Fasteners in the Pattern will be used to set the target location .
                |             
                |         iIndex,
                |             Index where to create the instruction.If passed as -1 SpotDrAction
                |             is created at the end of the Top sequence. 
                |         iOptimizeCycleTime,Is
                |             Cycle Time Optimization enabled. 
                |         oDrillRivetActions,
                |             Newly created DrillRivet actions 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param SpotDrProfile i_spot_dr_profile:
        :param SpotDrManufacturingPattern i_pattern:
        :param int i_index:
        :param bool i_optimize_cycle_time:
        :return: tuple
        """
        return self.com_object.CreateDrillRivetActions(i_spot_dr_profile.com_object, i_pattern.com_object, i_index, i_optimize_cycle_time)

    def delete_drill_rivet_action(self, i_drill_rivet_action: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteDrillRivetAction(AnyObject iDrillRivetAction)
                |     This method deletes the DrillRivet action
                | 
                |     Parameters:
                | 
                |         iDrillRivetAction,
                |             DrillRivet action to be deleted. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param AnyObject i_drill_rivet_action:
        :return: None
        """
        return self.com_object.DeleteDrillRivetAction(i_drill_rivet_action.com_object)

    def __repr__(self):
        return f'SpotDrActionFactory(name="{ self.name }")'
