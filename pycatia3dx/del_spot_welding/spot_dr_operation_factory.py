"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_spot_welding.spot_dr_operation import SpotDrOperation


class SpotDrOperationFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrOperationFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_operation(self, i_type: str, i_ref_act: AnyObject) -> SpotDrOperation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateOperation(CATBSTR iType,AnyObject iRefAct) As
                | SpotDrOperation
                |     This method creates a DrillRivet operation
                | 
                |     Parameters:
                | 
                |         oDrillRivetOperation,
                |             newly created DrillRivet operation 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param str i_type:
        :param AnyObject i_ref_act:
        :return: SpotDrOperation
        """
        return SpotDrOperation(self.com_object.CreateOperation(i_type, i_ref_act.com_object))

    def delete_operation(self, i_drill_rivet_operation: SpotDrOperation) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteOperation(SpotDrOperation iDrillRivetOperation)
                |     This method deletes the passed DrillRivet operation
                | 
                |     Parameters:
                | 
                |         iDrillRivetOperation,
                |             DrillRivet operation to be deleted. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param SpotDrOperation i_drill_rivet_operation:
        :return: None
        """
        return self.com_object.DeleteOperation(i_drill_rivet_operation.com_object)

    def __repr__(self):
        return f'SpotDrOperationFactory(name="{ self.name }")'
