"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscMotionController(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscMotionController
                | 
                | Interface to access the resource motion controller data.
                | Role: This interface provides methods to access the resource motion controller
                | data from a given resource. A resource is a product which is used in DELMIA
                | applications for planning and/or programming. There are many resource types and
                | not all of them supports a motion controller.
                | A resource motion controller is used to program a given resource. It relies
                | upon:
                | 
                |     a default product assembly
                |     a kinematic mechanism driving the parts under the assembly
                | 
                | The resource motion controller provides programming capabilities to such
                | assembly. Dedicated resource type(s) also allows the control of multiple
                | resources through many motion groups (example: Control Equipment). Current API
                | are providing navigation capabilities.
                | 
                | Example:
                |     Let assume there is a robot opened as a root entity in a given
                |     editor.
                | 
                |     Dim MainResource As Variant
                |     Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |     Dim MyMotionResource As RscMotionController
                |     Set MyMotionResource = MainResource.GetItem("CAARscMotionController")
                |     If Not MyMotionResource Is Nothing Then
                | 
                |     End If
                | 
                | Note:API documentation will include sample code referring to MyMotionResource
                | as a variable of type RscMotionController.
                | 
                | See also:
                |     RscMotionGroup
                | See also:
                |     DELRscMotionControllerType
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def list_motion_groups(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ListMotionGroups() As CATSafeArrayVariant (Read Only)
                |     Returns the list of motion groups associated to the current resource
                |     depending on its type.
                | 
                |         on a Control Equipment, there may be multiple groups
                |         on other supported equipment (like Industrial robot), there is only
                |         one.
                | 
                |     Returns:
                |         List of motion groups managed by the current resource.
                | 
                |         Example:
                | 
                |          Dim ListMG 'array for VBScript
                |          ListMG = MyMotionResource.ListMotionGroups
                |          Dim NbMG As Integer
                |          NbMG = UBound(ListMG) + 1
                |          'uncomment next line to display value
                |          'MsgBox ("Number of motion group: " & CStr(NbMG))
                |          Dim MyMG As RscMotionGroup
                |          For II = LBound(ListMG) To UBound(ListMG)
                |            MyMG = ListMG(II)
                |            'uncomment next line to display value
                |            'MsgBox ("My motion group name is:" & MyMG.Name)
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ListMG() As Variant 'array for VBA
                |          ListMG = MyMotionResource.ListMotionGroups

        :return: tuple
        """

        return self.com_object.ListMotionGroups

    @property
    def motion_controller_context(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionControllerContext() As DELRscControllerDataContext (Read
                | Only)
                |     Indicates if there is motion controller defined on the reference resource
                |     or on its instance.
                | 
                |     Returns:
                |         Indicates if there is already a motion controller and, given the
                |         selected resource it is an instance or reference.
                | 
                |         Example:
                | 
                |          Dim MyControllerContext As
                |          DELRscControllerDataContext
                |          MyControllerContext = MyMotionResource.MotionControllerContext
                |          'uncomment next line to display value
                |          'MsgBox ("Motion controller context: " &
                |          CStr(MyControllerContext))
                | 
                |     See also:
                |         DELRscControllerDataContext

        :return: DELRscControllerDataContext
        """

        return self.com_object.MotionControllerContext

    @property
    def support_motion_controller(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportMotionController() As boolean (Read Only)
                |     Indicates if the current resource supports a motion controller. Not all
                |     resource type supports a motion controller.
                | 
                |     Returns:
                |         Indicates if the current resource supports a motion controller.

        :return: bool
        """

        return self.com_object.SupportMotionController

    def get_list_controlled_resources(self, i_context: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetListControlledResources(AnyObject iContext) As
                | CATSafeArrayVariant
                |     Returns the list of controlled resources. A resource motion controller may
                |     control several resources if the context allows it (at the instance level
                |     only). Otherwise, it will return itself. These resources may be grouped in
                |     different motion groups.
                | 
                |     Parameters:
                | 
                |         iContext
                |             Specific occurrence indicating the context. It can either
                |             be:
                | 
                |                 the resource itself it is opened in its own
                |                 editor.
                |                 the parent product of the current resource if the current
                |                 resource has been inserted inside a manufacturing
                |                 cell.
                | 
                |     Returns:
                |         List of resource occurrence (same as product
                |         occurrence).
                | 
                |         Example:
                | 
                |          Dim ListControlledResources
                |          ListControlledResources = MyMotionResource.GetListControlledResources(MainResource)
                |          Dim NbControlled As Integer
                |          NbControlled = UBound(ListControlledResources) + 1
                |          'uncomment next line to display value
                |          'MsgBox ("Number of controlled resource: " &
                |          CStr(NbControlled))
                |          Dim AnyGivenResource As VPMOccurrence
                |          For II = LBound(ListControlledResources) To UBound(ListControlledResources)
                |            Set AnyGivenResource = ListControlledResources(II)
                |            'uncomment next line to display value
                |            'MsgBox ("Controlled resources:" &
                |            AnyGivenResource.Name)
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ListControlledResources() As Variant 'array for
                |          VBA
                |          ListControlledResources = MyMotionResource.GetListControlledResources(MainResource)

        :param AnyObject i_context:
        :return: tuple
        """
        return self.com_object.GetListControlledResources(i_context.com_object)

    def get_motion_controller_type(self, i_controlled_resource: AnyObject) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMotionControllerType(AnyObject iControlledResource) As
                | DELRscMotionControllerType
                |     Retrieve the type of control for a given resource controlled by the current
                |     motion controller. This API allows to identify if a resource is used rail or
                |     end-effector thanks to DELRscMotionControllerType enumeration. Input argument
                |     iControlledResource is valuated from
                |     GetListControlledResources.
                | 
                |     Parameters:
                | 
                |         iControlledResource
                |             Specific controlled occurrence. 
                | 
                |     Returns:
                |         Enumeration type indicating the type of control.
                | 
                |         Example:
                | 
                |          Dim AnyGivenResource As VPMOccurrence
                |          'valuation of AnyGivenResource 
                |          Dim RscControlType As DELRscMotionControllerType
                |          RscControlType = MyMotionResource.GetMotionControllerType(AnyGivenResource)

        :param AnyObject i_controlled_resource:
        :return: DELRscMotionControllerType
        """
        return self.com_object.GetMotionControllerType(i_controlled_resource.com_object)

    def modify_control_display_name(self, i_controlled_resource: AnyObject, i_control_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ModifyControlDisplayName(AnyObject iControlledResource,CATBSTR
                | iControlName)
                |     Modify the name of the control object related to a resource. Input argument
                |     iControlledResource is valuated from
                |     GetListControlledResources.
                | 
                |     Parameters:
                | 
                |         iControlledResource
                |             Specific controlled occurrence. 
                |         iControlName
                |             New name to apply on the control entity driving the controlled
                |             occurrence.
                | 
                |             Example:
                | 
                |              Dim AnyGivenResource As VPMOccurrence
                |              'valuation of AnyGivenResource 
                |              Dim iNewName As String
                |              iNewName = "NewTestName"
                |              MyMotionResource.ModifyControlDisplayName AnyGivenResource,
                |              iNewName

        :param AnyObject i_controlled_resource:
        :param str i_control_name:
        :return: None
        """
        return self.com_object.ModifyControlDisplayName(i_controlled_resource.com_object, i_control_name)

    def retrieve_control_display_name(self, i_controlled_resource: AnyObject) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RetrieveControlDisplayName(AnyObject iControlledResource) As
                | CATBSTR
                |     Retrieve the name of the control object related to a resource. Input
                |     argument iControlledResource is valuated from
                |     GetListControlledResources.
                | 
                |     Parameters:
                | 
                |         iControlledResource
                |             Specific controlled occurrence. 
                | 
                |     Returns:
                |         Name of the control entity driving the controlled
                |         occurrence.
                | 
                |         Example:
                | 
                |          Dim AnyGivenResource As VPMOccurrence
                |          'valuation of AnyGivenResource 
                |          Dim MyControlledDisplayName As String
                |          MyControlledDisplayName = MyMotionResource.RetrieveControlDisplayName(AnyGivenResource)

        :param AnyObject i_controlled_resource:
        :return: str
        """
        return self.com_object.RetrieveControlDisplayName(i_controlled_resource.com_object)

    def retrieve_controlled_mechanism(self, i_controlled_resource: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RetrieveControlledMechanism(AnyObject iControlledResource) As
                | AnyObject
                |     Retrieve the mechanism associated with controlled resource. Input argument
                |     iControlledResource is valuated from
                |     GetListControlledResources.
                | 
                |     Parameters:
                | 
                |         iControlledResource
                |             Specific controlled occurrence. 
                | 
                |     Returns:
                |         Mechanism object.
                | 
                |         Example:
                | 
                |          Dim AnyGivenResource As VPMOccurrence
                |          'valuation of AnyGivenResource 
                |          Dim MyControlledMechanism As KinMechanism
                |          Set MyControlledMechanism = MyMotionResource.RetrieveControlledMechanism(AnyGivenResource)

        :param AnyObject i_controlled_resource:
        :return: AnyObject
        """
        return AnyObject(self.com_object.RetrieveControlledMechanism(i_controlled_resource.com_object))

    def retrieve_dof_count(self, i_controlled_resource: AnyObject) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RetrieveDOFCount(AnyObject iControlledResource) As long
                |     Retrieve the DOF count associated with the controlled resource. Input
                |     argument iControlledResource is valuated from
                |     GetListControlledResources.
                | 
                |     Parameters:
                | 
                |         iControlledResource
                |             Specific controlled occurrence. 
                | 
                |     Returns:
                |         DOF count associated to the controlled resource.
                | 
                |         Example:
                | 
                |          Dim AnyGivenResource As VPMOccurrence
                |          'valuation of AnyGivenResource 
                |          Dim MyControlledDOFCount As Integer
                |          MyControlledDOFCount = MyMotionResource.RetrieveDOFCount(AnyGivenResource)

        :param AnyObject i_controlled_resource:
        :return: int
        """
        return self.com_object.RetrieveDOFCount(i_controlled_resource.com_object)

    def __repr__(self):
        return f'RscMotionController(name="{ self.name }")'
