"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscMotionGroup(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscMotionGroup
                | 
                | Interface to access the motion group data.
                | Role: This interface provides methods to access the motion group data within a
                | given resource motion controller. A motion group is used to indicate the list
                | of controlled resources in terms of motion. It can only have:
                | 
                |     0 to 1 industrial robot
                |     0 to N unique resources controlled specifically
                | 
                | In robotics, motion groups represent all the axes controlled by the motion
                | controller, including the different type of external axes control
                | (DELRscMotionControllerType enumeration). Retrieval of motion group can be
                | performed through selection or through RscMotionController.
                | 
                | See also:
                |     RscMotionController
                | See also:
                |     DELRscMotionControllerType
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def contains_robot(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ContainsRobot() As boolean (Read Only)
                |     Indicates if this motion group contains an industrial robot.

        :return: bool
        """

        return self.com_object.ContainsRobot

    @property
    def motion_group_index(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionGroupIndex() As long

        :return: int
        """

        return self.com_object.MotionGroupIndex

    @motion_group_index.setter
    def motion_group_index(self, value: int):
        """
        :param int value:
        """

        self.com_object.MotionGroupIndex = value

    def retrieve_controlled_resources(self, i_cell_context: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RetrieveControlledResources(AnyObject iCellContext) As
                | CATSafeArrayVariant
                |     Retrieves the list of controlled resources by the current motion group. To
                |     identify how these resources are used by the motion controller, please use
                |     RscMotionController.GetMotionControllerType.
                | 
                |     Parameters:
                | 
                |         iCellContext
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
                |         List of VPMOccurrence for each controlled resources.
                | 
                |         Example:
                | 
                |          Dim MyMotionGroup As RscMotionGroup
                |          ' valuation of MyMotionGroup variable
                |          Dim ListControlledResources
                |          ListControlledResources = MyMotionGroup.RetrieveControlledResources(MainResource)
                |          Dim NbControlled As Integer
                |          NbControlled = UBound(ListControlledResources) + 1
                |          MsgBox ("Number of controlled resource: " &
                |          CStr(NbControlled))
                |          Dim AnyGivenResource As VPMOccurrence
                |          For II = LBound(ListControlledResources) To UBound(ListControlledResources)
                |            Set AnyGivenResource = ListControlledResources(II)
                |            MsgBox ("Controlled resources:" &
                |            AnyGivenResource.Name)
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ListControlledResources() As Variant 'array for
                |          VBA
                |          ListControlledResources = MyMotionGroup.RetrieveControlledResources(MainResource)

        :param AnyObject i_cell_context:
        :return: tuple
        """
        return self.com_object.RetrieveControlledResources(i_cell_context.com_object)

    def retrieve_primary_resource(self, i_cell_context: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RetrievePrimaryResource(AnyObject iCellContext) As
                | AnyObject
                |     Retrieves the primary resource within a group. The primary resource
                |     is:
                | 
                |         the industrial robot if any
                |         the 1st resource if there are no industrial robot in the
                |         group
                | 
                |     Parameters:
                | 
                |         iCellContext
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
                |         A VPMOccurrence for the resource.
                | 
                |         Example:
                | 
                |          Dim MyMotionGroup As RscMotionGroup
                |          ' valuation of MyMotionGroup variable
                |          Dim MyPrimaryResource
                |          Set MyPrimaryResource = objMotionGroup.RetrievePrimaryResource(MyCellResource)

        :param AnyObject i_cell_context:
        :return: AnyObject
        """
        return AnyObject(self.com_object.RetrievePrimaryResource(i_cell_context.com_object))

    def __repr__(self):
        return f'RscMotionGroup(name="{ self.name }")'
