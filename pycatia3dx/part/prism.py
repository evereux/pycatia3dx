"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.part.limit import Limit
from pycatia3dx.part.sketch_based_shape import SketchBasedShape


class Prism(SketchBasedShape):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.SketchBasedShape
                |                             Prism
                | 
                | Prism-based features in Part Design : base for pad or pocket.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def direction_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DirectionOrientation() As CatPrismOrientation
                |     Returns the prism direction orientation.
                | 
                |     Returns:
                |         oOrientation The direction orientation (see CatPrismOrientation for
                |         list of possible types)
                | 
                |         Example:
                |             The following example saves in dirOrientation the direction
                |             orientation of prism firstPrism, and then sets it so that the direction will be
                |             now inversed :
                | 
                |              Set dirOrientation = firstPrism.DirectionOrientation
                |              firstPrism.DirectionOrientation = catInverseOrientation

        :return: CatPrismOrientation
        """

        return self.com_object.DirectionOrientation

    @direction_orientation.setter
    def direction_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.DirectionOrientation = value

    @property
    def direction_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DirectionType() As CatPrismExtrusionDirection
                |     Returns the prism direction type.
                | 
                |     Returns:
                |         oDirType The direction type (see CatPrismExtrusionDirection for list of
                |         possible types)
                | 
                |         Example:
                |             The following example saves in dirType the direction type of prism
                |             firstPrism, and then sets it so that the direction will be now normal to the
                |             sketch :
                | 
                |              Set dirType = firstPrism.DirectionType
                |              firstPrism.DirectionType = catNormalToSketchDirection

        :return: CatPrismExtrusionDirection
        """

        return self.com_object.DirectionType

    @direction_type.setter
    def direction_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.DirectionType = value

    @property
    def first_limit(self) -> Limit:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstLimit() As Limit (Read Only)
                |     Returns the first prism limit (one of the two).
                |     This limit manages the way the prism is ended.
                | 
                |     Returns:
                |         oFirstLimit The first limit (see Limit for more
                |         information)
                | 
                |         Example:
                |             The following example returns in firstLimit the first limit of
                |             prism firstPrism:
                | 
                |              Set firstLimit = firstPrism.FirstLimit

        :return: Limit
        """

        return Limit(self.com_object.FirstLimit)

    @property
    def is_symmetric(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsSymmetric() As boolean
                |     Returns the prism symmetry flag.
                |     It returns TRUE if the prism is symmetric (from the base sketch), FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsSymmetric The symmetry flag as a boolean
                | 
                |         Example:
                |             The following example saves in symFlag the symmetry flag of prism
                |             firstPrism, and then sets it so that it will be now symmetric (from the base
                |             sketch) :
                | 
                |              Set symFlag = firstPrism.IsSymmetric
                |              firstPrism.IsSymmetric = TRUE

        :return: bool
        """

        return self.com_object.IsSymmetric

    @is_symmetric.setter
    def is_symmetric(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IsSymmetric = value

    @property
    def is_thin(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsThin() As boolean
                |     Returns the prism thin flag.
                |     It returns TRUE if the prism is a thin prism , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsThin The thin flag as a boolean
                | 
                |         Example:
                |             The following example saves in thinFlag the thin flag of prism
                |             firstPrism, and then sets it so that it will be now thin
                |             :
                | 
                |              Set thinFlag = firstPrism.IsThin
                |              firstPrism.IsThin = TRUE

        :return: bool
        """

        return self.com_object.IsThin

    @is_thin.setter
    def is_thin(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IsThin = value

    @property
    def merge_end(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MergeEnd() As boolean
                |     Returns the prism merge end flag (for thin prism only).
                |     It returns TRUE if merge ends is required , FALSE if not.
                | 
                |     Returns:
                |         oIsMergeEnd The merge end flag as a boolean
                | 
                |         Example:
                |             The following example saves in MergeEndFlag the merge end flag of
                |             prism firstPrism, and then sets it so that merge end will be required
                |             :
                | 
                |              Set MergeEndFlag = firstPrism.IsMergeEnd
                |              firstPrism.IsMergeEnd = TRUE

        :return: bool
        """

        return self.com_object.MergeEnd

    @merge_end.setter
    def merge_end(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MergeEnd = value

    @property
    def neutral_fiber(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NeutralFiber() As boolean
                |     Returns the prism neutral fiber flag (for thin prism
                |     only).
                |     It returns TRUE if the prism is a neutral fiber prism , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsNeutralFiber The neutral fiber flag as a boolean
                | 
                |         Example:
                |             The following example saves in NeutralFiberFlag the neutral fiber
                |             flag of prism firstPrism, and then sets it so that it will be now neutral fiber
                |             :
                | 
                |              Set NeutralFiberFlag = firstPrism.IsNeutralFiber
                |              firstPrism.IsNeutralFiber = TRUE

        :return: bool
        """

        return self.com_object.NeutralFiber

    @neutral_fiber.setter
    def neutral_fiber(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NeutralFiber = value

    @property
    def second_limit(self) -> Limit:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondLimit() As Limit (Read Only)
                |     Returns the second prism limit (one of the two).
                |     This limit manages the way the prism is ended.
                | 
                |     Returns:
                |         oSecondLimit The second limit (see Limit for more
                |         information)
                | 
                |         Example:
                |             The following example returns in secondLimit the second limit of
                |             prism firstPrism:
                | 
                |              Set secondLimit = firstPrism.SecondLimit

        :return: Limit
        """

        return Limit(self.com_object.SecondLimit)

    def get_direction(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDirection(CATSafeArrayVariant ioDirection)
                |     Returns the prism direction with absolute coordinates.
                |     It needs a safe array with 3 elements : X, Y, Z direction coordinates The array must be previously initialized
                | 
                |     Returns:
                |         ioDirection The direction coordinates
                | 
                |         Example:
                |             The following example returns in dirArray the direction coordinates
                |             of prism firstPrism:
                | 
                |              Dim dirArray(2)
                |              Call firstPrism.GetDirection(dirArray)
                |              Set x = dirArray[1]
                |              Set y = dirArray[2]
                |              Set z = dirArray[3]

        :return: tuple
        """
        # todo: check this method, does it require system service?
        return self.com_object.GetDirection()
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise, completely remove all this.
        # # vba_function_name = 'get_direction'
        # # vba_code = """
        # # Public Function get_direction(prism)
        # #     Dim ioDirection (2)
        # #     prism.GetDirection ioDirection
        # #     get_direction = ioDirection
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_profile_element(self, o_profile_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetProfileElement(Reference oProfileElement)

        :param Reference o_profile_element:
        :return: None
        """
        return self.com_object.GetProfileElement(o_profile_element.com_object)

    def reverse_inner_side(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ReverseInnerSide()
                |     Reverses the prism inner side when the profile is open. This is useful for
                |     finding the shape to reach.
                | 
                |     Example:
                |         The following example reverses the current inner side of prism
                |         firstPrism :
                | 
                |          firstPrism.ReverseInnerSide

        :return: None
        """
        return self.com_object.ReverseInnerSide()

    def set_direction(self, i_line: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDirection(Reference iLine)
                |     Sets the prism associative direction.
                | 
                |     Parameters:
                | 
                |         iLine
                |             The support direction reference (see Reference for more
                |             information)
                |             This reference can be valuated with a reference to a line or an
                |             edge.
                |             The following Boundary objects are supported: PlanarFace,
                |             RectilinearTriDimFeatEdge and
                |             RectilinearBiDimFeatEdge.
                | 
                |             Example:
                |                 The following example sets the prism direction reference of
                |                 prism firstPrism with prismDirRef line :
                | 
                |                  firstPrism.SetDirection prismDirRef

        :param Reference i_line:
        :return: None
        """
        return self.com_object.SetDirection(i_line.com_object)

    def __repr__(self):
        return f'Prism(name="{self.name}")'
