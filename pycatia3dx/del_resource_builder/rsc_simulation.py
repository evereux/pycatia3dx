"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx import DELRscSimulationStatus
from pycatia3dx.del_resource_builder.rsc_transform import RscTransform
from pycatia3dx.system.any_object import AnyObject


class RscSimulation(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscSimulation
                | 
                | Interface to manipulate the kinematics of the a programmable
                | resource.
                | Role: This interface provides methods to manipulate the different degrees of
                | freedom of a programmable resource (as well as its inverse kinematics if
                | available).
                | To simulate an assembly containing kinematics, users must specify for which
                | motion group the simulation is required. Motion groups can be retrieved from
                | RscMotionController.ListControlledResources.
                | To use this API, users must always do the following:
                | 
                |     call Initialize before any other calls.
                |     call Finalize after usage.
                | 
                | Example:
                |     Let assume there is a robot opened as a root entity in a given
                |     editor.
                | 
                |      Dim MainResource As Variant
                |      Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |      Dim MySimulatedResource As RscSimulation
                |      Set MySimulatedResource = MainResource.GetItem("CAARscSimulation")
                |      
                |      If Not MySimulatedResource Is Nothing Then
                | 
                |      End If
                | 
                | Note:API documentation will include sample code referring to:
                | 
                |     MySimulatedResource as a variable of type RscSimulation.
                |     MainResource as the resource to be simulated (can be obtained through
                |     selection or model scanning.
                | 
                | Remark:All API will not work if the Initialize has not been
                | performed.
                | 
                | See also:
                |     RscMotionController
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def all_posture_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllPostureNames() As CATSafeArrayVariant (Read Only)
                |     Retrieves the list of all configuration names on the given robot. Only
                |     applicable when the resource has inverse kinematics. Be aware, a resource may
                |     not be able to reach properly a given target location for a specific config,
                |     although other configurations are feasible.
                | 
                |     Example:
                | 
                |      Dim MyPostureID As String
                |      Dim MyListPostureID
                |      MyListPostureID = MySimulatedResource.AllPostureNames
                |      For II = LBound(MyListPostureID) To UBound(MyListPostureID)
                |        Set MyPostureID = MyListPostureID(II)
                |        'uncomment next line to display value
                |        'MsgBox ("Posture name:" & MyPostureID)
                |      Next

        :return: tuple
        """

        return self.com_object.AllPostureNames

    @property
    def all_tool_profile_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllToolProfileNames() As CATSafeArrayVariant (Read
                | Only)
                |     Retrieves the list of all configuration names on the given robot. Only
                |     applicable when the resource has inverse kinematics. Be aware, a resource may
                |     not be able to reach properly a given target location for a specific config,
                |     although other configurations are feasible.
                | 
                |     Example:
                | 
                |      Dim MyToolProfileID As String
                |      Dim MyListToolProfileID
                |      MyListToolProfileID = MySimulatedResource.AllToolProfileNames
                |      For II = LBound(MyListToolProfileID) To UBound(MyListToolProfileID)
                |        Set MyToolProfileID = MyListToolProfileID(II)
                |        'uncomment next line to display value
                |        'MsgBox ("ToolProfile name:" & MyToolProfileID)
                |      Next

        :return: tuple
        """

        return self.com_object.AllToolProfileNames

    @property
    def can_be_simulated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CanBeSimulated() As boolean (Read Only)
                |     Indicates if the current resource can be simulated. A given resource may
                |     not be simulated if:
                | 
                |         There is no proper control object
                |         initialization has failed (or missing) due to wrong kinematics
                |         definition
                |         There is no proper license
                | 
                |     Example:
                | 
                |      Dim bCanBeSimulated As Boolean
                |      bCanBeSimulated = MySimulatedResource.CanBeSimulated

        :return: bool
        """

        return self.com_object.CanBeSimulated

    @property
    def current_posture(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentPosture() As CATBSTR
                |     Indicates if which robot configuration is currently set. Only applicable
                |     when the resource has inverse kinematics. Be aware, a resource may not be able
                |     to reach properly a given target location for a specific config, although other
                |     configurations are feasible.
                | 
                |     Example:
                | 
                |      Dim MyPostureID As String
                |      MyPostureID = MySimulatedResource.CurrentPosture

        :return: str
        """

        return self.com_object.CurrentPosture

    @current_posture.setter
    def current_posture(self, value: str):
        """
        :param str value:
        """

        self.com_object.CurrentPosture = value

    @property
    def current_tool_profile(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentToolProfile() As CATBSTR
                |     Indicates which tool profile is currently in use. The tool profile is used
                |     to manage the tool offset. Only applicable when the resource has inverse
                |     kinematics.Each tool profile defines both:
                | 
                |         the type of tool (mobile or fixed)
                |         the offset
                | 
                |     Example:
                | 
                |      Dim MyToolProfileName As String
                |      MyToolProfileName = MySimulatedResource.CurrentToolProfile

        :return: str
        """

        return self.com_object.CurrentToolProfile

    @current_tool_profile.setter
    def current_tool_profile(self, value: str):
        """
        :param str value:
        """

        self.com_object.CurrentToolProfile = value

    @property
    def simulated_dof_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SimulatedDOFCount() As long (Read Only)
                |     Returns the DOF count of the current simulated resource.
                | 
                |     Example:
                | 
                |      Dim iRscDOFCount As Integer
                |      iRscDOFCount = MySimulatedResource.SimulatedDOFCount
                |      'uncomment next line to display value
                |      'MsgBox ("Number of motion group:" & CStr(iRscDOFCount))

        :return: int
        """

        return self.com_object.SimulatedDOFCount

    @property
    def simulation_state(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SimulationState() As DELRscSimulationStatus (Read
                | Only)
                |     Returns the simulation state of the resource. The simulated resource is
                |     always into a certain simulation state. Users may check the simulation state of
                |     the resource after performing some changes (DOF values or inverse
                |     kinematics).
                | 
                |     Example:
                | 
                |      Dim MySimStatus As DELRscSimulationStatus
                |      MySimStatus = MySimulatedResource.SimulationState
                | 
                |     See also:
                |         DELRscSimulationStatus

        :return: DELRscSimulationStatus
        """

        return self.com_object.SimulationState

    @property
    def simulation_visualization_update(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SimulationVisualizationUpdate() As
                | DELRscSimulationVisualizationUpdate
                |     Indicates the simulation visualization update currently in used. Simulation
                |     visualization update mode is used to control the display upon changes (DOF
                |     values, configuration, TCP). By default it is activated
                |     (DELRscSimulationVisualizationUpdate_ON).
                | 
                |     Example:
                | 
                |      MySimulatedResource.SimulationVisualizationUpdate
                | 
                |     See also:
                |         DELRscSimulationVisualizationUpdate

        :return: DELRscSimulationVisualizationUpdate
        """

        return self.com_object.SimulationVisualizationUpdate

    @simulation_visualization_update.setter
    def simulation_visualization_update(self, value: int):
        """
        :param int value:
        """

        self.com_object.SimulationVisualizationUpdate = value

    @property
    def specific_dof_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecificDOFCount() As long (Read Only)
                |     Retrieves the number of specific DOF. Specific DOF are specific degrees of
                |     freedom the current resource has. Typically, the elbow angle on special 7 axis
                |     robot is one of them.
                | 
                |     Example:
                | 
                |      Dim iSpecificDOFCount As Integer
                |      iSpecificDOFCount = MySimulatedResource.SpecificDOFCount
                |      'uncomment next line to display value
                |      'MsgBox ("Number of specific DOF count:" &
                |      CStr(iSpecificDOFCount))

        :return: int
        """

        return self.com_object.SpecificDOFCount

    @property
    def support_ik(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportIK() As boolean (Read Only)
                |     Indicates if the current resource has any inverse kinematics capabilities.
                |     This API can be used to check if existing API related to inverse kinematics
                |     capabilities are supported (like SetTCPValues.)
                | 
                |     Example:
                | 
                |      Dim MyIKStatus As Boolean
                |      MyIKStatus = MySimulatedResource.SupportIK

        :return: bool
        """

        return self.com_object.SupportIK

    def finalize(self, i_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Finalize(long iMode)
                |     Clean the simulation entity. Call this API after there is no more usage of
                |     the simulation for this resource.
                | 
                |     Parameters:
                | 
                |         iMode
                |             Internal usage. Set the value to 0.
                | 
                |             Example:
                | 
                |              MySimulatedResource.Finalize(0)

        :param int i_mode:
        :return: None
        """
        return self.com_object.Finalize(i_mode)

    def get_base_part(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBasePart() As AnyObject
                |     Retrieve the base part. Only applicable when the resource has inverse
                |     kinematics.
                | 
                |     Example:
                | 
                |      Dim MyBasePart As VPMOccurrence
                |      Set MyBasePart = MySimulatedResource.GetBasePart()
                |      'uncomment next line to display value
                |      'MsgBox ("Base part name:" & MyBasePart.Name)
                | 
                |     See also:
                |         VPMOccurrence

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetBasePart())

    def get_dof_limits(self, i_dof_index: int, o_lower: float, o_upper: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDOFLimits(long iDOFIndex,double oLower,double oUpper)
                |     Retrieve the current limits for a given DOF index. The index must be within
                |     1 and SimulatedDOFCount included.
                | 
                |     Example:
                | 
                |      Dim iDOFIndex As Integer
                |      Dim LowerLimit As Double
                |      Dim UpperLimit As Double
                |      'valuation of iDOFIndex
                |      MySimulatedResource.GetDOFLimits iDOFIndex, LowerLimit,
                |      UpperLimit.
                | 
                |     See also:
                |         DELRscJointType

        :param int i_dof_index:
        :param float o_lower:
        :param float o_upper:
        :return: None
        """
        return self.com_object.GetDOFLimits(i_dof_index, o_lower, o_upper)

    def get_dof_type(self, i_dof_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDOFType(long iDOFIndex) As DELRscJointType
                |     Retrieve the type of joint for a given DOF index. The index must be within
                |     1 and SimulatedDOFCount included.
                | 
                |     Example:
                | 
                |      Dim iDOFIndex As Integer
                |      Dim MyJointType As DELRscJointType
                |      'valuation of iDOFIndex
                |      MyJointType = MySimulatedResource.GetDOFType iDOFIndex, LowerLimit, UpperLimit.
                | 
                |     See also:
                |         DELRscJointType

        :param int i_dof_index:
        :return: DELRscJointType
        """
        return self.com_object.GetDOFType(i_dof_index)

    def get_dof_values(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDOFValues() As CATSafeArrayVariant
                |     Get the DOF values for a resource kinematics. The array must have the same
                |     size as the simulated DOF count provided by
                |     SimulatedDOFCount.
                | 
                |     Example:
                | 
                |      Dim MyDOFValuesList
                |      MyDOFValuesList = MySimulatedResource.GetDOFValues()
                | 
                |     Important remark: the list of values also contain external axes values. In
                |     case of external axes, the list of values is structured as
                |     follows:
                | 
                |         first comes the DOF values for the main resource
                |         (robot)
                |         then comes the DOF values for the other mechanism
                | 
                |     To identify which DOF values are matching which resource, similar order is
                |     keep with GetRelatedSimulatedResourcesObjects. From there, it is possible to
                |     identify each individual resource DOF count using
                |     GetRelatedSimulatedResourceDOFCount.

        :return: tuple
        """
        return self.com_object.GetDOFValues()

    def get_fixed_part(self, i_local: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFixedPart(long iLocal) As AnyObject
                |     Retrieve the fixed part. It can be either:
                | 
                |         0: the fixed part of the robot
                |         1: the fixed part of the rail if there is a rail as external
                |         axes
                | 
                |     Example:
                | 
                |      Dim MyFixPart As VPMOccurrence
                |      Set MyFixPart = MySimulatedResource.GetFixedPart(0)
                |      'uncomment next line to display value
                |      'MsgBox ("Fix part name:" & MyFixPart.Name)
                | 
                |     See also:
                |         VPMOccurrence

        :param int i_local:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetFixedPart(i_local))

    def get_mount_location(self) -> RscTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMountLocation() As RscTransform
                |     Retrieve the current mount location. The mount location is the coordinate
                |     where the tool can be mounted.
                | 
                |     Example:
                | 
                |      Dim MyMountOffset As RscTransform
                |      Set MyMountOffset = MySimulatedResource.GetMountLocation()
                | 
                |     See also:
                |         RscTransform

        :return: RscTransform
        """
        return RscTransform(self.com_object.GetMountLocation())

    def get_mount_offset(self) -> RscTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMountOffset() As RscTransform
                |     Retrieve the current mount offset. The mount offset is the transformation
                |     containing the difference between the mount part location and the mounting
                |     point on the mount part.
                | 
                |     Example:
                | 
                |      Dim MyMountOffset As RscTransform
                |      Set MyMountOffset = MySimulatedResource.GetMountOffset()
                | 
                |     See also:
                |         RscTransform

        :return: RscTransform
        """
        return RscTransform(self.com_object.GetMountOffset())

    def get_mount_part(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMountPart() As AnyObject
                |     Retrieve the current mount part. The mount part is the product where
                |     tooling can be mounted.
                | 
                |     Example:
                | 
                |      Dim MyBasePart As VPMOccurrence
                |      Set MyBasePart = MySimulatedResource.GetBasePart()
                |      'uncomment next line to display value
                |      'MsgBox ("Base part name:" & MyBasePart.Name)
                | 
                |     See also:
                |         VPMOccurrence

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetMountPart())

    def get_related_simulated_resource_dof_count(self, i_related_resource: AnyObject) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRelatedSimulatedResourceDOFCount(AnyObject iRelatedResource) As
                | long
                |     Retrieve the simulated resource DOF count. This is applicable for resources
                |     driving others (like a robot and its external axes). This method can be used to
                |     identify the order of the simulated resources in terms of DOF values thanks to
                |     DELRscMotionControllerType_Default. It is used in conjunction with
                |     GetRelatedSimulatedResourcesObjects.
                | 
                |     Parameters:
                | 
                |         iRelatedResource
                |             A given resource retrieved with
                |             GetRelatedSimulatedResourcesObjects. 
                | 
                |     Returns:
                |         Simulation DOF count for the associated resource.
                | 
                |         Example:
                | 
                |          Dim AnyOccurrence As VPMOccurrence
                |          Dim ListRelated
                |          ListRelated = MySimulatedResource.GetRelatedSimulatedResourcesObjects(DELRscMotionControllerType_EndOfArm)
                |          
                |          For ee = LBound(ListRelated) To UBound(ListRelated)
                |              MsgBox ("Index:" & CStr(ee))
                |              Set AnyOccurrence = ListRelated(ee)
                |              Dim iRscDOFCount As Integer
                |              iRscDOFCount = MySimulatedResource.GetRelatedSimulatedResourceDOFCount(AnyOccurrence)
                |          Next

        :param AnyObject i_related_resource:
        :return: int
        """
        return self.com_object.GetRelatedSimulatedResourceDOFCount(i_related_resource.com_object)

    def get_related_simulated_resources_count(self, i_type: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRelatedSimulatedResourcesCount(DELRscMotionControllerType iType) As
                | long
                |     Retrieves the number of related simulated resources. This is applicable for
                |     resources driving others (like a robot and its external axes). If the input
                |     argument is set to DELRscMotionControllerType_Default, all resources including
                |     the current one will be included.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of control used to simulate the resource. 
                | 
                |     Returns:
                |         Return the number of resources of a given control
                |         type.
                | 
                |         Example:
                | 
                |          Dim iRelatedResourceCount As Integer
                |          iRelatedResourceCount = MySimulatedResource.GetRelatedSimulatedResourcesCount(DELRscMotionControllerType_EndOfArm)
                |          'uncomment next line to display value
                |          'MsgBox ("End of arm count:" &
                |          CStr(iRelatedResourceCount))

        :param int i_type:
        :return: int
        """
        return self.com_object.GetRelatedSimulatedResourcesCount(i_type)

    def get_related_simulated_resources_objects(self, i_type: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRelatedSimulatedResourcesObjects(DELRscMotionControllerType iType) As
                | CATSafeArrayVariant
                |     Retrieve the simulated resource related to this one. This is applicable for
                |     resources driving others (like a robot and its external axes). This method can
                |     be used to identify the order of the simulated resources in terms of DOF values
                |     thanks to DELRscMotionControllerType_Default. It will return all simulated
                |     resources in a order similar to GetDOFValues. In that case, use it in
                |     conjunction with GetRelatedSimulatedResourceDOFCount.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of control used to simulate the resource. 
                | 
                |     Returns:
                |         List of resources for a given control type.
                | 
                |         Example:
                | 
                |          Dim AnyOccurrence As VPMOccurrence
                |          Dim ListRelated
                |          ListRelated = MySimulatedResource.GetRelatedSimulatedResourcesObjects(DELRscMotionControllerType_EndOfArm)
                |          
                |          For ee = LBound(ListRelated) To UBound(ListRelated)
                |              Set AnyOccurrence = ListRelated(ee)
                |              MsgBox ("Related Resource[" & CStr(ee + 1) & "]=" &
                |              CStr(AnyOccurrence.Name))
                |          Next

        :param int i_type:
        :return: tuple
        """
        return self.com_object.GetRelatedSimulatedResourcesObjects(i_type)

    def get_specific_dof_limits(self, i_dof_index: int, o_lower: float, o_upper: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSpecificDOFLimits(long iDOFIndex,double oLower,double
                | oUpper)
                |     Retrieve the current limits for a given DOF index. The index must be within
                |     1 and SimulatedDOFCount included.
                | 
                |     Example:
                | 
                |      Dim iDOFIndex As Integer
                |      Dim LowerLimit As Double
                |      Dim UpperLimit As Double
                |      'valuation of iDOFIndex
                |      MySimulatedResource.GetSpecificDOFLimits iDOFIndex, LowerLimit,
                |      UpperLimit.
                | 
                |     See also:
                |         DELRscJointType

        :param int i_dof_index:
        :param float o_lower:
        :param float o_upper:
        :return: None
        """
        return self.com_object.GetSpecificDOFLimits(i_dof_index, o_lower, o_upper)

    def get_specific_dof_type(self, i_dof_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSpecificDOFType(long iDOFIndex) As DELRscJointType
                |     Retrieve the type of joint for a given DOF index. The index must be within
                |     1 and SimulatedDOFCount included.
                | 
                |     Example:
                | 
                |      Dim iDOFIndex As Integer
                |      Dim MyJointType As DELRscJointType
                |      'valuation of iDOFIndex
                |      MyJointType = MySimulatedResource.GetSpecificDOFType iDOFIndex, LowerLimit, UpperLimit.
                | 
                |     See also:
                |         DELRscJointType

        :param int i_dof_index:
        :return: DELRscJointType
        """
        return self.com_object.GetSpecificDOFType(i_dof_index)

    def get_specific_dof_values(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSpecificDOFValues() As CATSafeArrayVariant
                |     Get the specific DOF values for a resource kinematics. The array has the
                |     same size as the specific DOF count provided by SpecificDOFCount. Only
                |     applicable during simulation.
                | 
                |     Example:
                | 
                |      Dim MySpecificDOFValuesList
                |      MySpecificDOFValuesList = MySimulatedResource.GetSpecificDOFValues()

        :return: tuple
        """
        return self.com_object.GetSpecificDOFValues()

    def get_tcp_values(self) -> RscTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTCPValues() As RscTransform
                |     Get the cartesian value of the current resource target location. Only
                |     applicable when the resource has inverse kinematics.
                | 
                |     Example:
                | 
                |      Dim MyTransform As RscTransform
                |      Set MyTransform = MySimulatedResource.GetTCPValues

        :return: RscTransform
        """
        return RscTransform(self.com_object.GetTCPValues())

    def initialize(self, i_rsc_control_entity: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Initialize(AnyObject iRscControlEntity)
                |     Initializes the simulation for a given control entity. The motion group is
                |     a control entity to drive properly the kinematics assembly. This API must be
                |     called before any usage of this object API. To retrieve existing motion group,
                |     please use RscMotionController.ListMotionGroups.
                | 
                |     Parameters:
                | 
                |         iRscControlEntity
                |             Motion group object. When simulating the current resource, the
                |             motion group object must be passed as an input
                |             parameter.
                | 
                |             Example:
                | 
                |              'retrieval of the motion group
                |              Dim MyMotionResource As RscMotionController
                |              Set MyMotionResource = MainResource.GetItem("CAARscMotionController")
                |              If Not MyMotionResource Is Nothing Then
                |                Dim NbMotionGroup As Integer
                |                NbMotionGroup = UBound(ListMG) + 1
                | 
                |                Dim MyMG As RscMotionGroup
                |                If NbMotionGroup <> 0 Then
                |                    Set MyMG = ListMG(0)
                |                End If
                | 
                |                If Not MyMG Is Nothing Then
                |                  Dim MySimulatedResource As RscSimulation
                |                  Set SimObject = MainResource.GetItem("CAARscSimulation")
                |                  If Not SimObject Is Nothing Then
                |                    'simulation preparation
                |                    SimObject.Initialize MyMG
                |                  End If
                |                  
                |              End If

        :param AnyObject i_rsc_control_entity:
        :return: None
        """
        return self.com_object.Initialize(i_rsc_control_entity.com_object)

    def set_dof_values(self, i_values: tuple) -> DELRscSimulationStatus:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func SetDOFValues(CATSafeArrayVariant iValues) As
                | DELRscSimulationStatus
                |     Set the DOF values for a resource kinematics. The array must have the same
                |     size as the simulated DOF count provided by
                |     SimulatedDOFCount.
                |
                |     Example:
                |
                |
                |      Dim iRscDOFCount As Integer
                |      iRscDOFCount = MySimulatedResource.SimulatedDOFCount
                |      Dim NewDOFValues 'array for VBScript
                |      ReDim NewDOFValues(iRscDOFCount-1)
                |      For KK = 0 To UBound(NewDOFValues)
                |        NewDOFValues(KK) = 0.5
                |      Next
                |
                |      Dim MySimStatus As DELRscSimulationStatus
                |      MySimStatus = MySimulatedResource.SetDOFValues(NewDOFValues)
                |
                |     Important remark: the list of values also contain external axes values. In
                |     case of external axes, the list of values is structured as
                |     follows:
                |
                |         first comes the DOF values for the main resource
                |         (robot)
                |         then comes the DOF values for the other mechanism
                |
                |     To identify which DOF values are matching which resource, similar order is
                |     keep with GetRelatedSimulatedResourcesObjects. From there, it is possible to
                |     identify each individual resource DOF count using
                |     GetRelatedSimulatedResourceDOFCount.
                |     Note: previous example is for CATScript. In case of VBA, the syntax is
                |     significantly different:
                |
                |      Dim iRscDOFCount As Integer
                |      iRscDOFCount = MySimulatedResource.HomePositionDOFCount
                |      Dim NewDOFValues() As Variant 'array for VBA
                |      ReDim NewDOFValues(iRscDOFCount-1)
                |      For KK = 0 To UBound(NewDOFValues)
                |        NewDOFValues(KK) = 0.5
                |      Next
                |      Dim MyObj 'need to change typing due to early typing for
                |      VBA
                |      Set MyObj = MySimulatedResource
                |      Dim MySimStatus As DELRscSimulationStatus
                |      MySimStatus = MyObj.SetDOFValues(NewDOFValues)
                |
                |     See also:
                |         DELRscSimulationStatus

        :param tuple i_values:
        :return: DELRscSimulationStatus
        """
        return DELRscSimulationStatus(self.com_object.SetDOFValues(i_values))
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_dof_values'
        # vba_code = """
        # Public Function set_dof_values(rsc_simulation)
        #     Dim iValues (2)
        #     rsc_simulation.SetDOFValues iValues
        #     set_dof_values = iValues
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_specific_dof_values(self, i_values: tuple) -> DELRscSimulationStatus:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func SetSpecificDOFValues(CATSafeArrayVariant iValues) As
                | DELRscSimulationStatus
                |     Set the specific DOF values for a resource kinematics. The array has the
                |     same size as the specific DOF count provided by
                |     SpecificDOFCount.
                |
                |     Example:
                |
                |
                |      Dim iRscSpecificDOFCount As Integer
                |      iRscSpecificDOFCount = MySimulatedResource.SpecificDOFCount
                |      Dim NewDOFValues 'array for VBScript
                |      ReDim NewDOFValues(iRscSpecificDOFCount-1)
                |      For KK = 0 To UBound(NewDOFValues)
                |        NewDOFValues(KK) = 0.5
                |      Next
                |
                |      Dim MySimStatus As DELRscSimulationStatus
                |      MySimStatus = MySimulatedResource.SetSpecificDOFValues(NewDOFValues)
                |
                |     Note: previous example is for CATScript. In case of VBA, the syntax is
                |     significantly different:
                |
                |      Dim iRscSpecificDOFCount As Integer
                |      iRscSpecificDOFCount = MySimulatedResource.SpecificDOFCount
                |      Dim NewDOFValues() As Variant 'array for VBA
                |      ReDim NewDOFValues(iRscSpecificDOFCount-1)
                |      For KK = 0 To UBound(NewDOFValues)
                |        NewDOFValues(KK) = 0.5
                |      Next
                |      Dim MyObj 'need to change typing due to early typing for
                |      VBA
                |      Set MyObj = MySimulatedResource
                |      Dim MySimStatus As DELRscSimulationStatus
                |      MySimStatus = MyObj.SetSpecificDOFValues(NewDOFValues)
                |
                |     See also:
                |         DELRscSimulationStatus

        :param tuple i_values:
        :return: DELRscSimulationStatus
        """
        return DELRscSimulationStatus(self.com_object.SetSpecificDOFValues(i_values))
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_specific_dof_values'
        # vba_code = """
        # Public Function set_specific_dof_values(rsc_simulation)
        #     Dim iValues (2)
        #     rsc_simulation.SetSpecificDOFValues iValues
        #     set_specific_dof_values = iValues
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tcp_values(self, i_values: RscTransform) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SetTCPValues(RscTransform iValues) As
                | DELRscSimulationStatus
                |     Set the cartesian value of the current resource target location to reach.
                |     Only applicable when the resource has inverse kinematics. Transformation can be
                |     retrieved from GetTCPValues and duplicated through
                |     RscTransform.Duplicate.
                | 
                |     Example:
                | 
                |      Dim MySimStatus As DELRscSimulationStatus
                |      MySimStatus = MySimulatedResource.SetTCPValues(MyTransform)
                | 
                |     See also:
                |         DELRscSimulationStatus
                |     See also:
                |         RscTransform

        :param RscTransform i_values:
        :return: DELRscSimulationStatus
        """
        return self.com_object.SetTCPValues(i_values.com_object)

    def update_visualization(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UpdateVisualization()
                |     Update the visualization upon changes of position. This API can be used as
                |     a manual visualization update, especially when SimulationVisualizationUpdate is
                |     deactivated (DELRscSimulationVisualizationUpdate_OFF)
                | 
                |     Example:
                | 
                |      MySimulatedResource.UpdateVisualization
                | 
                |     See also:
                |         DELRscSimulationVisualizationUpdate

        :return: None
        """
        return self.com_object.UpdateVisualization()

    def __repr__(self):
        return f'RscSimulation(name="{self.name}")'
