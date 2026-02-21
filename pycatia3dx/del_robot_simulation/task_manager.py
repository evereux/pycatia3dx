"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.del_robot_simulation.resource_task import ResourceTask
from pycatia3dx.system.any_object import AnyObject


class TaskManager(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TaskManager
                | 
                | Interface representing a Resource Task.
                | 
                | Role: This interface is used to create and manage tasks on a
                | resource
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def task_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TaskList() As CATSafeArrayVariant (Read Only)
                |     Retrieves the list of task on the resource
                | 
                |     Returns:
                |         oTaskList The list of tasks on the resource 
                |     Example:
                | 
                |            
                | 
                |            Dim objTaskManager As TaskManager
                |                   ......
                |         Dim oTasks
                |         oTasks = objTaskManager.TaskList

        :return: tuple
        """

        return self.com_object.TaskList

    def create_task(self) -> ResourceTask:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTask() As ResourceTask
                |     Create a new Robot/Device task If method is called on the resource
                |     reference, task is created under the reference If method is called on resource
                |     occurrence, task is created under its first organizational-physical parent. If
                |     method is called on motion group, task is created for the main
                |     device of the motion based on the above two conditions.
                | 
                |     Returns:
                |         oCreatedTask The created task. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTaskManager As TaskManager
                |                   ......
                |            Dim oRscTask As AnyObject
                |         Call objTaskManager.CreateTask(oRscTask)

        :return: ResourceTask
        """
        return ResourceTask(self.com_object.CreateTask())

    def delete_task(self, i_task: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteTask(AnyObject iTask)
                |     Deletes a task on the resource
                | 
                |     Returns:
                |         iTask The task to delete 
                |     Example:
                | 
                |            
                | 
                |            Dim objTaskManager As TaskManager
                |                   ......
                |         Dim oRscTask As ResourceTask
                |                   ......
                |            Call objTaskManager.DeleteTask(oRscTask)

        :param AnyObject i_task:
        :return: None
        """
        return self.com_object.DeleteTask(i_task.com_object)

    def delete_tasks(self, i_task_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub DeleteTasks(CATSafeArrayVariant iTaskList)
                |     Deletes a list of task on the resource
                |
                |     Returns:
                |         iTaskList The lits of tasks to delete
                |     Example:
                |
                |
                |
                |            Dim objTaskManager As TaskManager
                |                   ......
                |         Dim oTasks
                |                   ......
                |         Call objTaskManager.DeleteTasks(oTasks)

        :param tuple i_task_list:
        :return: None
        """
        return self.com_object.DeleteTasks(i_task_list)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'delete_tasks'
        # vba_code = """
        # Public Function delete_tasks(task_manager)
        #     Dim iTaskList (2)
        #     task_manager.DeleteTasks iTaskList
        #     delete_tasks = iTaskList
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'TaskManager(name="{self.name}")'
