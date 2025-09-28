"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeUnfold(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeUnfold
                | 
                | Represents the hybrid shape Unfold feature object.
                | Role: To access the data of the hybrid shape Unfold feature object. This data
                | includes:
                | 
                |     The shell to unfold
                |     The edges to tear
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeUnfold
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def direction_to_unfold(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DirectionToUnfold() As Reference
                |     Returns or sets the direction to unfold.

        :return: Reference
        """

        return Reference(self.com_object.DirectionToUnfold)

    @direction_to_unfold.setter
    def direction_to_unfold(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.DirectionToUnfold = value

    @property
    def edge_to_tear_positioning_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EdgeToTearPositioningOrientation() As long
                |     Returns or sets the positioning orientation when the reference origin is
                |     located on an edge to tear.
                | 
                |         0= The orientation is undefined
                |         1= The orientation is the default one
                |         2= The orientation is inversed

        :return: int
        """

        return self.com_object.EdgeToTearPositioningOrientation

    @edge_to_tear_positioning_orientation.setter
    def edge_to_tear_positioning_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.EdgeToTearPositioningOrientation = value

    @property
    def origin_to_unfold(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property OriginToUnfold() As Reference
                |     Returns or sets the origin to unfold.

        :return: Reference
        """

        return Reference(self.com_object.OriginToUnfold)

    @origin_to_unfold.setter
    def origin_to_unfold(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.OriginToUnfold = value

    @property
    def surface_to_unfold(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SurfaceToUnfold() As Reference
                |     Returns or sets the surface to unfold.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge and
                |     BiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.SurfaceToUnfold)

    @surface_to_unfold.setter
    def surface_to_unfold(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SurfaceToUnfold = value

    @property
    def surface_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SurfaceType() As long
                |     Returns or sets the type of surface to unfold.
                | 
                |         0= The type of surface is not defined
                |         1= The type of surface is ruled
                |         2= The type of surface is all

        :return: int
        """

        return self.com_object.SurfaceType

    @surface_type.setter
    def surface_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SurfaceType = value

    @property
    def target_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TargetDirection() As HybridShapeDirection
                |     Role: Retrieves target direction on the object.
                | 
                |     Parameters:
                | 
                |         oDir
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         HybridShapeDirection
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.TargetDirection)

    @target_direction.setter
    def target_direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.TargetDirection = value

    @property
    def target_orientation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TargetOrientationMode() As long
                |     Returns or sets the mode for target surface orientation.
                | 
                |         0= No axis inversion
                |         1= U inversion axis
                |         2= V inversion axis
                |         3= U inversion axis and V inversion axis
                |         4= U inversion axis and swap U and V axis
                |         5= V inversion axis and swap U and V axis
                |         6= U inversion axis, V inversion axis and swap U and V
                |         axis
                |         7= Swap U and V axis

        :return: int
        """

        return self.com_object.TargetOrientationMode

    @target_orientation_mode.setter
    def target_orientation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.TargetOrientationMode = value

    @property
    def target_origin(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TargetOrigin() As Reference
                |     Role: Retrieves target origin on the object.
                | 
                |     Parameters:
                | 
                |         oElem
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.com_object.TargetOrigin)

    @target_origin.setter
    def target_origin(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.TargetOrigin = value

    @property
    def target_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TargetPlane() As Reference
                |     Returns or sets the target plane.
                |     Sub-element(s) supported (see Boundary object):

        :return: Reference
        """

        return Reference(self.com_object.TargetPlane)

    @target_plane.setter
    def target_plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.TargetPlane = value

    def add_edge_to_tear(self, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddEdgeToTear(Reference iElement)
                |     Adds an edge to tear.
                | 
                |     Parameters:
                | 
                |         iEdge
                |             The edge to tear to add to the hybrid shape feature
                |             object.
                |             Sub-element(s) supported (see Boundary object): Edge
                |             
                | 
                |     Examples:
                |         The following example adds the iElement feature object to the
                |         HybridShapeUnfold object.
                | 
                |          HybridShapeUnfold.AddEdgeToTear iElement

        :param Reference i_element:
        :return: None
        """
        return self.com_object.AddEdgeToTear(i_element.com_object)

    def add_element_to_transfer(self, i_element: Reference, i_type_of_transfer: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddElementToTransfer(Reference iElement,long
                | iTypeOfTransfer)
                |     Appends an element to transfer.
                | 
                |     Parameters:
                | 
                |         iElement
                |             Specification to transfer 
                |         iTypeOfTransfer
                |             type of tranfer
                | 
                |                 0= No transfer mode specified
                |                 1= Folded to unfolded
                |                 2= Unfolded to folded

        :param Reference i_element:
        :param int i_type_of_transfer:
        :return: None
        """
        return self.com_object.AddElementToTransfer(i_element.com_object, i_type_of_transfer)

    def get_edge_to_tear(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetEdgeToTear(long iRank) As Reference
                |     Retrieves an element used by the hybrid shape unfold feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to read. 
                | 
                |     Examples:
                |         The following example gets the oElement feature object of the
                |         HybridShapeUnfold object at the position iRank.
                | 
                |          Dim oElement As Reference
                |          Set oElement = HybridShapeUnfold.GetEdgeToTear (iRank).

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetEdgeToTear(i_rank))

    def get_element_to_transfer(self, i_rank: int, op_element: Reference, o_type_of_transfer: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetElementToTransfer(long iRank,Reference opElement,long
                | oTypeOfTransfer)
                |     Gets an element to transfer.
                | 
                |     Parameters:
                | 
                |         iRank
                |             the position of the specification to get 
                |         opElement
                |             Specification to transfer 
                |         oTypeOfTransfer
                |             type of tranfer
                | 
                |                 0= No transfer mode specified
                |                 1= Folded to unfolded
                |                 2= Unfolded to folded

        :param int i_rank:
        :param Reference op_element:
        :param int o_type_of_transfer:
        :return: None
        """
        return self.com_object.GetElementToTransfer(i_rank, op_element.com_object, o_type_of_transfer)

    def remove_edge_to_tear(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveEdgeToTear(long iRank)
                |     Removes an element used by the hybrid shape unfold feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to remove. 
                | 
                |     Examples:
                |         The following example removes the feature object from the
                |         HybridShapeUnfold object at the position iRank.
                | 
                |          HybridShapeUnfold.RemoveEdgeToTear iRank.

        :param int i_rank:
        :return: None
        """
        return self.com_object.RemoveEdgeToTear(i_rank)

    def remove_element_to_transfer(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveElementToTransfer(long iRank)
                |     Remove an elements to transfer.
                | 
                |     Parameters:
                | 
                |         iRank
                |             the position of the specification to remove

        :param int i_rank:
        :return: None
        """
        return self.com_object.RemoveElementToTransfer(i_rank)

    def replace_elements_to_transfer(self, i_rank: int, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ReplaceElementsToTransfer(long iRank,Reference iElement)
                |     Replace an elements to transfer.
                | 
                |     Parameters:
                | 
                |         iRank
                |             the position of the specification to replace 
                |         iElement
                |             the specification to transfer to append.

        :param int i_rank:
        :param Reference i_element:
        :return: None
        """
        return self.com_object.ReplaceElementsToTransfer(i_rank, i_element.com_object)

    def __repr__(self):
        return f'HybridShapeUnfold(name="{ self.name }")'
