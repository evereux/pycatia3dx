"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_unknown import CATBaseUnknown


class SurfaceOperationFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SurfaceOperationFactory
                | 
                | Interface to create and destroy a Surface Operation.
                | Role: This interface provides methods to create and destroy Surface
                | Operations.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_surface_operation(self, i_operation_type: str, iref_instr: CATBaseUnknown, i_position: int, ip_tag: CATBaseUnknown, ip_tag_owner_occ: CATBaseUnknown, i_parent_seq: CATBaseUnknown) -> CATBaseUnknown:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSurfaceOperation(CATBSTR iOperationType,CATBaseUnknown
                | irefInstr,SurfaceOperationPosition iPosition,CATBaseUnknown
                | ipTag,CATBaseUnknown ipTagOwnerOcc,CATBaseUnknown iParentSeq) As
                | CATBaseUnknown
                |     This method creates a SurfaceOperation
                | 
                |     Parameters:
                | 
                |         iOperationType,
                |             input the Operation type. The approved list of Operation type is
                |             listed in \\win_b64\\resources\\msgcatalog\\DELApprovedOperationTypes.txt
                |             
                |         oSurfaceOperation,
                |             newly created SurfaceOperation. 
                |         irefInstr,
                |             reference activity relative to which the new Surface operation is to be created. If irefInstr = NULL, create the Surface operation at the end of the Surface task valid irefInstr should be set to create Surface operation as a child 
                |         iPosition,
                |             position of the Surface Operation to be created. 
                |         ipTag,
                |             the Target Tag for the Surface Operation 
                |         ipTagOwnerOcc,
                |             the Target Tag's Owner Occurrence 
                |         iParentSeq,
                |             Parent sequence in which the MotionActivity will be created. This
                |             argument is manadatory if iPosition is 'Begin' or 'End'. If iPosition is
                |             'Before' or 'After' and if this argument is NULL, MotionActivity is created in
                |             the MainSequence of the Task. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param str i_operation_type:
        :param CATBaseUnknown iref_instr:
        :param int i_position:
        :param CATBaseUnknown ip_tag:
        :param CATBaseUnknown ip_tag_owner_occ:
        :param CATBaseUnknown i_parent_seq:
        :return: CATBaseUnknown
        """
        return CATBaseUnknown(self.com_object.CreateSurfaceOperation(i_operation_type, iref_instr.com_object, i_position, ip_tag.com_object, ip_tag_owner_occ.com_object, i_parent_seq.com_object))

    def delete_surface_operation(self, i_surface_operation: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteSurfaceOperation(CATBaseUnknown iSurfaceOperation)
                |     This method destroys a SurfaceOperation
                | 
                |     Parameters:
                | 
                |         ispSurfaceOperation,
                |             SurfaceOperation to be destroyed. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param CATBaseUnknown i_surface_operation:
        :return: None
        """
        return self.com_object.DeleteSurfaceOperation(i_surface_operation.com_object)

    def __repr__(self):
        return f'SurfaceOperationFactory(name="{ self.name }")'
