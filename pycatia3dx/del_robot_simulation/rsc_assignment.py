"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_del_robot_simulation.rsc_data_entity import RscDataEntity
from pycatia3dx.todo_del_robot_simulation.rsc_instruction import RscInstruction


class RscAssignment(RscInstruction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DELRobotSimulationIDLItf.RscInstruction
                |                         RscAssignment
                | 
                | Interface representing a Resource Assignment Instruction.
                | 
                | Role: This interface represents a RscAssignment Instruction in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def assigned_data_entity(self) -> RscDataEntity:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AssignedDataEntity() As RscDataEntity
                |     Set/Get the assigned Data Entity.
                | 
                |     Returns:
                |         oAssignedEntity The returned assigned entity. 
                |     Parameters:
                | 
                |         iAssignedEntity
                |             The new assigned entity. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iAssignedEntity As RscDataEntity
                |            Dim iAssignedValue As String
                |            ......
                |            Dim oCreatedAssignment As RscAssignment
                |            Set oCreatedAssignment = ResourceSequence.CreateRscAssignment(iIndex, iAssignedEntity, iAssignedValue)
                |            Dim AssignedDataEntity
                |            AssignedDataEntity = oCreatedAssignment.AssignedDataEntity
                |            ......
                |            oCreatedAssignment.AssignedDataEntity = AssignedDataEntity

        :return: RscDataEntity
        """

        return RscDataEntity(self.com_object.AssignedDataEntity)

    @assigned_data_entity.setter
    def assigned_data_entity(self, value: RscDataEntity):
        """
        :param RscDataEntity value:
        """

        self.com_object.AssignedDataEntity = value

    @property
    def value(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Value(CATBSTR iValue)
                |     Set/Get the Value assigned to this Data Entity.
                | 
                |     Parameters:
                | 
                |         iValue
                |             The new assigned value. 
                | 
                |     Returns:
                |         oValue The returned assigned value. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iAssignedEntity As RscDataEntity
                |            Dim iAssignedValue As String
                |            ......
                |            Dim oCreatedAssignment As RscAssignment
                |            Set oCreatedAssignment = ResourceSequence.CreateRscAssignment(iIndex, iAssignedEntity, iAssignedValue)
                |            Dim oValue As String
                |            oValue = oCreatedAssignment.Value
                |            ......
                |            oCreatedAssignment.Value = oValue

        :return: str
        """

        return str

    @value.setter
    def value(self, value: str):
        """
        :param str value:
        """

        self.com_object.Value = value

    def __repr__(self):
        return f'RscAssignment(name="{ self.name }")'
