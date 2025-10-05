"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_del_robot_simulation.rsc_instruction import RscInstruction


class RscRunInternalTask(RscInstruction):

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
                |                         RscRunInternalTask
                | 
                | Interface representing a Resource RunInternalTask Instruction.
                | 
                | Role: This interface represents a RscRunInternalTask Instruction in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def task(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Task() As AnyObject
                |     Assigns/Retrieves the Internal Task to run
                | 
                |     Parameters:
                | 
                |         iRscRunInternalTask
                |             The Run Task to be assigned 
                | 
                |     Returns:
                |         oRscRunInternalTask The associated Run Task 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iTask
                |            .........
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedRscRunInternalTask
                |            Set oCreatedRscRunInternalTask=ResourceSequence.CreateRscRunInternalTask(iTask,iIndex)
                |
                |            Dim ResourceRunInternalTask As RscRunInternalTask
                |            Set ResourceRunInternalTask = oCreatedRscRunInternalTask
                |            ......
                |            Dim RscInternalTask
                |            RscInternalTask=ResourceRunInternalTask.Task
                |            ......
                |            ResourceRunInternalTask.Task = RscInternalTask

        :return: AnyObject
        """

        return AnyObject(self.com_object.Task)

    @task.setter
    def task(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.Task = value

    def __repr__(self):
        return f'RscRunInternalTask(name="{ self.name }")'
