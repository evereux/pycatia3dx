"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_point_operation.point_operation import PointOperation


class PointOperationFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PointOperationFactory
                | 
                | Interface representing the Point Operation Factory to create and delete Point
                | Operations.
                | 
                | Role: This interface is used to create and delete Point
                | Operations
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_point_operation(self, i_type: str, iref_inst: AnyObject, i_before: bool, i_tag: AnyObject, i_tag_owner_occ: AnyObject) -> PointOperation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func CreatePointOperation(CATBSTR iType,AnyObject irefInst,boolean
                | iBefore,AnyObject iTag,AnyObject iTagOwnerOcc) As
                | PointOperation
                |     Creates a Point Operation.
                | 
                |     Returns:
                |         oPointOperation The created Point Operation. 
                |     Parameters:
                | 
                |         iType
                |             Type of Point Operation to create (could be "Weld", "Rivet").
                |             
                |         irefInst
                |             The reference instruction before/after which the Point Operation
                |             has to be created. If Reference Instruction is NULL, the instruction will be
                |             created at the end 
                |         iBefore
                |             Create before the reference instruction or not. 
                |         iTag
                |             The Tag target for the Point Operation. This parameter cannot be
                |             NULL 
                |         iTagOwnerOcc
                |             Tag target's Owner Occurrence. If this parameter is NULL, first
                |             occurrence of the Owner is used. 
                | 
                |     Example:
                | 
                |            
                | 
                |             Dim objPointOperationFactory As
                |             PointOperationFactory
                |             Dim ATag As Tag
                |                   ......
                |             Dim objTagOwnerOcc As AnyObject
                |             Dim objRefAct As AnyObject
                |             Dim CreateBefore As Boolean
                |             CreateBefore = FALSE
                |                   ......
                |                   ......
                |             Dim oPointOperation As PointOperation
                |             Set oPointOperation = objPointOperationFactory.CreatePointOperation("Weld", objRefAct, CreateBefore, ATag, objTagOwnerOcc)

        :param str i_type:
        :param AnyObject iref_inst:
        :param bool i_before:
        :param AnyObject i_tag:
        :param AnyObject i_tag_owner_occ:
        :return: PointOperation
        """
        return PointOperation(self.com_object.CreatePointOperation(i_type, iref_inst.com_object, i_before, i_tag.com_object, i_tag_owner_occ.com_object))

    def delete_point_operation(self, i_point_operation: PointOperation) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub DeletePointOperation(PointOperation iPointOperation)
                |     Deletes Point Operation.
                | 
                |     Parameters:
                | 
                |         iPointOperation
                |             The Point Operation to delete 
                | 
                |     Example:
                | 
                |            
                | 
                |             Dim objResTask As ResourceTask
                |                   ......
                |             Dim objPointOperation As PointOperation
                |                   ......
                |             Call
                |             objResTask.DeletePointOperation(objPointOperation)

        :param PointOperation i_point_operation:
        :return: None
        """
        return self.com_object.DeletePointOperation(i_point_operation.com_object)

    def __repr__(self):
        return f'PointOperationFactory(name="{ self.name }")'
