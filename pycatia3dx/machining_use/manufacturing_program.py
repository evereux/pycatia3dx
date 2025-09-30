"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_machining_use.manufacturing_activity import ManufacturingActivity


class ManufacturingProgram(ManufacturingActivity):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MachiningUseItf.ManufacturingActivity
                |                         ManufacturingProgram
                | 
                | Interface dedicated to Program Object.
                | Role: This interface offers services to initialize the current compatible tool
                | in Program for Activity object. It also allows to add and remove Manufacturing
                | Operations.
                | It is implemented on ManufacturingProgram object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def append_operation(self, i_type: str, i_auto_sequence: bool) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AppendOperation(CATBSTR iType,boolean iAutoSequence) As
                | AnyObject
                | 
                |     Deprecated:
                |         R424 Use AppendOperation without iAutoSequence Inserts a new
                |         Manufacturing Operation at the begining of the program.
                |         
                |     Parameters:
                | 
                |         iType
                |             The type of Manufacturing Operation to create
                |             ("Drilling","Pocketing","ToolChange", ...) 
                |         iAutoSequence
                |             To determine if thez created Operation is sequenced in the program
                |             or not. if AutoSequence is TRUE, the new operation will be sequenced in the
                |             Program, otherwise it will not. 
                |         oActivity
                |             The created Manufacturing Operation.

        :param str i_type:
        :param bool i_auto_sequence:
        :return: AnyObject
        """
        return AnyObject(self.com_object.AppendOperation(i_type, i_auto_sequence))

    def append_operation2(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AppendOperation2(CATBSTR iType) As AnyObject
                |     Inserts a new Manufacturing Operation at the begining of the
                |     program.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of Manufacturing Operation to create
                |             ("Drilling","Pocketing","ToolChange", ...) 
                |         oActivity
                |             The created Manufacturing Operation.

        :param str i_type:
        :return: AnyObject
        """
        return AnyObject(self.com_object.AppendOperation2(i_type))

    def get_operations(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOperations() As CATSafeArrayVariant
                |     Retrieves Operations of Program
                | 
                |     Parameters:
                | 
                |         oListOperations
                |             List of Operations

        :return: tuple
        """
        return self.com_object.GetOperations()

    def get_output_nc_rep(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOutputNCRep() As AnyObject
                |     Retrieve NC Representation
                | 
                |     Parameters:
                | 
                |         ospNCRep
                |             [out] NC Representation (@see DELIMfgNCRep)

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetOutputNCRep())

    def move_operation(self, i_reference_operation: AnyObject, i_operation_to_move: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MoveOperation(AnyObject iReferenceOperation,AnyObject
                | iOperationToMove)
                |     Moves an existing Manufacturing Operation before a reference Operation. The
                |     operation to be moved must belong to the program, but not the reference
                |     operation. In this last case, the operation to move also changes its owner
                |     program.
                | 
                |     Parameters:
                | 
                |         iReferenceActivity
                |             The reference Manufacturing Operation before which the operation is
                |             moved. 
                |         iActivityToMove
                |             The Manufacturing Operation to move.

        :param AnyObject i_reference_operation:
        :param AnyObject i_operation_to_move:
        :return: None
        """
        return self.com_object.MoveOperation(i_reference_operation.com_object, i_operation_to_move.com_object)

    def set_current_authorized_tool(self, i_activity: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCurrentAuthorizedTool(AnyObject iActivity)
                |     Writes the current authorized tool.
                | 
                |     Parameters:
                | 
                |         iActivity
                |             The Activity

        :param AnyObject i_activity:
        :return: None
        """
        return self.com_object.SetCurrentAuthorizedTool(i_activity.com_object)

    def __repr__(self):
        return f'ManufacturingProgram(name="{ self.name }")'
