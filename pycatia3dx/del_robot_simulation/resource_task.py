"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ResourceTask(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ResourceTask
                | 
                | Interface representing a Resource Task.
                | 
                | Role: This interface is used to create and get motion activities from task and
                | retieve/assign the attributes of task.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def context(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Context() As AnyObject (Read Only)
                |     This property returns the context where the task is
                |     created.
                | 
                |     Returns:
                |         oContext The Context 
                |     Example:
                |
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  objContext
                |            set objContext=objResTask.Context

        :return: AnyObject
        """

        return AnyObject(self.com_object.Context)

    @property
    def motion_activities(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionActivities() As CATSafeArrayVariant (Read Only)
                |     Retreives the list of motion activities from the task.
                | 
                |     Returns:
                |         oMotionActivities The list of motion activities. 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim MotionActivities
                |            MotionActivities=objResTask.MotionActivities

        :return: tuple
        """

        return self.com_object.MotionActivities

    @property
    def motion_groups(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionGroups() As CATSafeArrayVariant (Read Only)
                |     Retreives the list of motion groups from the task.
                | 
                |     Returns:
                |         oMotionGroups The list of motion groups. 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim MotionGroups
                |            MotionGroups=objResTask.MotionGroups

        :return: tuple
        """

        return self.com_object.MotionGroups

    @property
    def primary_mca(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PrimaryMCA() As AnyObject (Read Only)
                |     Retreives primary MCA which is the MCA for the owning
                |     resource
                | 
                |     Returns:
                |         oMCA The MCA of the owning resource in the task context.
                |         
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  objMCA
                |            set objMCA=objResTask.PrimaryMCA

        :return: AnyObject
        """

        return AnyObject(self.com_object.PrimaryMCA)

    @property
    def resource(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Resource() As AnyObject (Read Only)
                |     This property returns the resource for which the task is
                |     created.
                | 
                |     Returns:
                |         oResource The resource 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  objResource
                |            set objResource=objResTask.Resource

        :return: AnyObject
        """

        return AnyObject(self.com_object.Resource)

    @property
    def task_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TaskType() As CATBSTR (Read Only)
                |     This property returns the type of the task.
                | 
                |     Returns:
                |         oType The Type of the task which can either RobotTask or DeviceTask.
                |         
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  Type as string
                |            Type=objResTask.TaskType

        :return: str
        """

        return self.com_object.TaskType

    @property
    def trajectory_reference(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TrajectoryReference() As AnyObject (Read Only)
                |     Retreives Trajectory reference of the task.
                | 
                |     Returns:
                |         oTrajectory The trajectory set as reference. 
                |     Returns:
                |         oTrajectory The product occurrence which aggregates the trajectory (in
                |         case the trajectory is in PRODUCT DAG). In case the trajectory is not in
                |         PRODUCT DAG then Root Product is returned. 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  objTrajectory
                |            set objTrajectory=objResTask.TrajectoryReference

        :return: AnyObject
        """

        return AnyObject(self.com_object.TrajectoryReference)

    def create_motion_activity(self, i_before: bool, i_reference_instruction: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateMotionActivity(boolean iBefore,AnyObject iReferenceInstruction) As
                | AnyObject
                |     Creates a motion activity.
                | 
                |     Returns:
                |         oCreatedMotionAct The created motion activity. 
                |     Parameters:
                | 
                |         iBefore
                |             Create before the reference instruction or not. 
                |         iReferenceInstruction
                |             The reference instruction after which the motion activity and its
                |             instrution has to be created. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  objNewMotionAct As RobotMotion
                |            Dim  objRefMotionAct As RobotMotion
                |            Dim  CreateBefore As Boolean
                |            CreateBefore = FALSE
                |                   ......
                |            Call objResTask.CreateMotionActivity(CreateBefore, objRefMotionAct,
                |            objNewMotionAct)

        :param bool i_before:
        :param AnyObject i_reference_instruction:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateMotionActivity(i_before, i_reference_instruction.com_object))

    def create_spm_operation(self, i_before: bool, i_reference_instruction: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSPMOperation(boolean iBefore,AnyObject iReferenceInstruction) As
                | AnyObject
                |     Creates an SPMOperation under a DeviceTask (not supported for
                |     RobotTask)
                | 
                |     Returns:
                |         oCreatedSPMOp The created SPMOperation. 
                |     Parameters:
                | 
                |         iBefore
                |             Create before the reference instruction or not. 
                |         iReferenceInstruction
                |             The reference instruction before/after which the SPMOperation has
                |             to be created. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  objNewSPMOp As SPMOperation
                |            Dim  objRefAct As DeviceMotion
                |            Dim  CreateBefore As Boolean
                |            CreateBefore = FALSE
                |                   ......
                |            Call objResTask.CreateSPMOperation(CreateBefore, objRefAct,
                |            objNewSPMOp)

        :param bool i_before:
        :param AnyObject i_reference_instruction:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateSPMOperation(i_before, i_reference_instruction.com_object))

        def delete_motion_activities(self, i_motion_activities: tuple) -> None:
            """
            .. note::
                :class: toggle

                3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                    | Sub DeleteMotionActivities(CATSafeArrayVariant
                    | iMotionActivities)
                    |     Deletes a list of motion activities.
                    |
                    |     Parameters:
                    |
                    |         iMotionActivities
                    |             The list if motion activities to delete
                    |
                    |     Example:
                    |
                    |
                    |
                    |            Dim objResTask As ResourceTask
                    |                   ......
                    |            Dim  objMotionActivities
                    |                   ......
                    |            Call objResTask.DeleteMotionActivities(oMotionActivities)

            :param tuple i_motion_activities:
            :return: None
            """
            return self.com_object.DeleteMotionActivities(i_motion_activities)
            # todo: check this method, does it require system service?
            # Autogenerated comment:
            # some methods require a system service call as the methods expects a vb array object
            # passed to it and there is no way to do this directly with python. In those cases the following code
            # should be uncommented and edited accordingly. Otherwise completely remove all this.
            # vba_function_name = 'delete_motion_activities'
            # vba_code = """
            # Public Function delete_motion_activities(resource_task)
            #     Dim iMotionActivities (2)
            #     resource_task.DeleteMotionActivities iMotionActivities
            #     delete_motion_activities = iMotionActivities
            # End Function
            # """

            # system_service = SystemService(self.application.SystemService)
            # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def delete_motion_activity(self, i_motion_activity: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteMotionActivity(AnyObject iMotionActivity)
                |     Deletes a motion activity.
                | 
                |     Parameters:
                | 
                |         iMotionActivity
                |             The motion activity to delete 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  objMotionAct As RobotMotion
                |                   ......
                |            Call objResTask.DeleteMotionActivity(objMotionAct)

        :param AnyObject i_motion_activity:
        :return: None
        """
        return self.com_object.DeleteMotionActivity(i_motion_activity.com_object)

    def get_trajectory_reference(self, o_trajectory: AnyObject, o_trajectory_owner: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTrajectoryReference(AnyObject oTrajectory,AnyObject
                | oTrajectoryOwner)
                |     Retreives Trajectory reference of the task.
                | 
                |     Returns:
                |         oTrajectory The trajectory set as reference. 
                |     Returns:
                |         oTrajectoryOwner The product occurrence which aggregates the trajectory
                |         (in case the trajectory is in PRODUCT DAG). In case the trajectory is not in
                |         PRODUCT DAG then Root Product is returned. 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  objTrajectory As AnyObject
                |            Dim  objTrajectoryOwner As TrajectoryOwner
                |            Call objResTask.GetTrajectoryReference objTrajectory
                |            objTrajectoryOwner

        :param AnyObject o_trajectory:
        :param AnyObject o_trajectory_owner:
        :return: None
        """
        return self.com_object.GetTrajectoryReference(o_trajectory.com_object, o_trajectory_owner.com_object)

    def set_trajectory_reference(self, i_trajectory: AnyObject, i_trajectory_owner: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTrajectoryReference(AnyObject iTrajectory,AnyObject
                | iTrajectoryOwner)
                |     Sets the Trajectory reference of the task.
                | 
                |     Parameters:
                | 
                |         iTrajectory
                |             The Trajectory to be set for reference. 
                |         iTrajectoryOwner
                |             The product occurrence which aggregates the Trajectory (in case the
                |             Trajectory is in PRODUCT DAG). 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask
                |                   ......
                |            Dim  objTrajectory As AnyObject
                |            Dim  objTrajectoryOwner As TrajectoryOwner
                |                   ......
                |            Call objResTask.SetTrajectoryReference(objTrajectory,objTrajectoryOwner)

        :param AnyObject i_trajectory:
        :param AnyObject i_trajectory_owner:
        :return: None
        """
        return self.com_object.SetTrajectoryReference(i_trajectory.com_object, i_trajectory_owner.com_object)

    def __repr__(self):
        return f'ResourceTask(name="{self.name}")'
