"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeExtrapol(HybridShape):

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
                |                         HybridShapeExtrapol
                | 
                | Represents the hybrid shape extrapolation feature object.
                | Role: To access the data of the hybrid shape affinity feature object. The
                | hybrid shape extrapolation feature object is created by using an element (a
                | curve or a surface), a boundary of this element (a point in case of curve
                | extrapolation or a curve in case of surface extrapolation), and a limit (which
                | can be specified by a length or a limit element).
                | The continuity between the extrapolated element and the extrapolation can be
                | either tangent continuity or curvature continuity.
                | The extrapolation can be assembled or not with the extrapolated curve or
                | surface. In case of surface extrapolation, extrapolation borders can
                | be:
                | 
                |     Normal to the boundary of the extrapolated surface
                |     Tangent to the edges of the extrapolated surface, that are adjacent to the
                |     boundary
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeExtrapol
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def border_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BorderType() As long
                |     Returns or sets the border type of extrapolation.
                |     This applies for surface extrapolation only.
                |     Legal values: the border type is either normal to the boundary of the
                |     extrapolated surface (CATGSMNormalBorder(=0)), or tangent to the edges of the
                |     extrapolated surface that are adjacent to the boundary
                |     CATGSMTangentBorder(=1)).

        :return: int
        """

        return self.com_object.BorderType

    @border_type.setter
    def border_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.BorderType = value

    @property
    def boundary(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Boundary() As Reference
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetBoundary method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: Reference
        """

        return Reference(self.com_object.Boundary)

    @boundary.setter
    def boundary(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Boundary = value

    @property
    def constant_length_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ConstantLengthMode() As boolean
                |     Returns or sets the constant distance mode in case of Length extrapolation
                |     limit.
                |     This applies in case of Length extrapolation limit.

        :return: bool
        """

        return self.com_object.ConstantLengthMode

    @constant_length_mode.setter
    def constant_length_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ConstantLengthMode = value

    @property
    def continuity_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ContinuityType() As long
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetContinuityType method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: int
        """

        return self.com_object.ContinuityType

    @continuity_type.setter
    def continuity_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ContinuityType = value

    @property
    def elem_to_extrapol(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemToExtrapol() As Reference
                |     Returns or sets the curve or surface to extrapolate.
                |     Sub-element(s) supported (see Boundary object): see Face , TriDimFeatEdge
                |     or BiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.ElemToExtrapol)

    @elem_to_extrapol.setter
    def elem_to_extrapol(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemToExtrapol = value

    @property
    def elem_until(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemUntil() As Reference
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetElemUntil method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: Reference
        """

        return Reference(self.com_object.ElemUntil)

    @elem_until.setter
    def elem_until(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemUntil = value

    @property
    def extend_edges_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtendEdgesMode() As boolean
                |     Returns or sets the extension of extrapolated edges mode.
                |     This applies in case of tangent continuity mode, tangent border mode and
                |     assembled result.

        :return: bool
        """

        return self.com_object.ExtendEdgesMode

    @extend_edges_mode.setter
    def extend_edges_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ExtendEdgesMode = value

    @property
    def extrapol_both_sides_identically(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtrapolBothSidesIdentically() As boolean
                |     Returns or sets the the boolean telling if the second side is extrapolated
                |     according to the first side's settings or to its own ones.
                |     This applies in case the element to extrapol is a wire.

        :return: bool
        """

        return self.com_object.ExtrapolBothSidesIdentically

    @extrapol_both_sides_identically.setter
    def extrapol_both_sides_identically(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ExtrapolBothSidesIdentically = value

    @property
    def length(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Length() As Length (Read Only)
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetLength method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: Length
        """

        return Length(self.com_object.Length)

    @property
    def limit_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property LimitType() As long
                | 
                |     This method is left available for compatibility reasons but it is
                |     preferable to use the GetLimitType method instead.
                | 
                |     Migration instructions: use the signature that uses an integer as the first
                |     argument.

        :return: int
        """

        return self.com_object.LimitType

    @limit_type.setter
    def limit_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.LimitType = value

    @property
    def propagation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PropagationMode() As long
                |     Returns or sets the propagation mode.
                |     This applies in case of curvature extrapolation of a shell.

        :return: int
        """

        return self.com_object.PropagationMode

    @propagation_mode.setter
    def propagation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.PropagationMode = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the support surface.
                |     This applies in case of tangent extrapolation of a wire. If a support
                |     surface is given, the extrapolation will lie on it.
                |     Sub-element(s) supported (see Boundary object): see Face.

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    def get_boundary(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetBoundary(long iPos) As Reference
                |     Returns or sets the iPos-th boundary of an extrapolated curve or surface
                |     from which extrapolation begins. If iPos equals 0 or the number of
                |     extrapolations, SetBoundary appends iBoundary to the list of
                |     boundaries.
                |     The boudary is a point for an extrapolated curve, or a curve for an
                |     extrapolated surface.
                |     Sub-element(s) supported (see Boundary object): see Face , TriDimFeatEdge
                |     or BiDimFeatEdge.

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.GetBoundary(i_pos))

    def get_continuity_type(self, i_pos: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetContinuityType(long iPos) As long
                |     Returns or sets the continuity type between extrapolated element and
                |     extrapolation at the iPos-th boundary. If iPos equals 0 or the number of
                |     extrapolations, SetContinuityType appends iLim to the list of
                |     lengths.
                |     Legal values: the continuity type is either CATGSMTangentContinuity (=0) or
                |     CATGSMCurvatureContinuity (=1).

        :param int i_pos:
        :return: int
        """
        return self.com_object.GetContinuityType(i_pos)

    def get_elem_until(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetElemUntil(long iPos) As Reference
                |     Returns or sets the surface or volume specifying the limit of the
                |     extrapolation that begins from the iPos-th boundary. If iPos equals 0 or the
                |     number of extrapolations, SetElemUntil appends iElemUntil to the list of up-to
                |     elements.
                |     This applies when the limit type is CATGSMUpToElementLimit (=1).

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.GetElemUntil(i_pos))

    def get_internal_edges_element(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetInternalEdgesElement(long iPos) As Reference
                |     Gets an element in the list of internal elements (vertex or
                |     edges).
                | 
                |     Parameters:
                | 
                |         oInternalElement
                |             internal element 
                |         iPos
                |             position of internal element to be retrieved.

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.GetInternalEdgesElement(i_pos))

    def get_length(self, i_pos: int) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetLength(long iPos) As Length
                |     Returns or sets the length specifying the limit of the extrapolation that
                |     begins from the iPos-th boundary. If iPos equals 0 or the number of
                |     extrapolations, SetLength appends iLength to the list of
                |     lengths.
                |     This applies when the limit type is CATGSMLengthLimit (=0).

        :param int i_pos:
        :return: Length
        """
        return Length(self.com_object.GetLength(i_pos))

    def get_limit_type(self, i_pos: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetLimitType(long iPos) As long
                |     Returns or sets the limit type of the extrapolation that begins from the
                |     iPos-th boundary. If iPos equals 0 or the number of extrapolations,
                |     SetLimitType appends iLim to the list of limit types.
                |     The limit can be a length, a surface, or a volume.
                |     Legal values: the limit type is either CATGSMLengthLimit(0) or
                |     CATGSMUpToElementLimit(1).

        :param int i_pos:
        :return: int
        """
        return self.com_object.GetLimitType(i_pos)

    def get_number_of_extrapolations(self, o_number_of_extrapolations: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNumberOfExtrapolations(long oNumberOfExtrapolations)
                |     Returns the number of extrapolations set. An extrapolation is specified by
                |     a boundary of the element to extrapolate, a limit type, a limit and a
                |     continuity type.

        :param int o_number_of_extrapolations:
        :return: None
        """
        return self.com_object.GetNumberOfExtrapolations(o_number_of_extrapolations)

    def is_assemble(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func IsAssemble() As boolean
                |     Retrieves whether extrapolation is assembled with extrapolated curve or
                |     surface.
                | 
                |     Parameters:
                | 
                |         oAssemble
                |             The assemble option
                |             True when the extrapolation is assembled with extrapolated curve or
                |             surface, and False otherwise

        :return: bool
        """
        return self.com_object.IsAssemble()

    def remove_all_extrapolations_except_the_first_one(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllExtrapolationsExceptTheFirstOne()
                |     Removes all extrapolations that may have been set, except the first one.

        :return: None
        """
        return self.com_object.RemoveAllExtrapolationsExceptTheFirstOne()

    def remove_all_internal_edges_element(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllInternalEdgesElement()
                |     Removes all internal elements.

        :return: None
        """
        return self.com_object.RemoveAllInternalEdgesElement()

    def remove_extrapolation(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveExtrapolation(long iPos)
                |     Removes the iPos-th extrapolation that has been set.

        :param int i_pos:
        :return: None
        """
        return self.com_object.RemoveExtrapolation(i_pos)

    def set_assemble(self, i_assemble: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAssemble(boolean iAssemble)
                |     Sets whether extrapolation is to be assembled with extrapolated curve or
                |     surface.
                | 
                |     Parameters:
                | 
                |         iAssemble
                |             The assemble option
                |             True when the extrapolation is to be assembled with extrapolated
                |             curve or surface, and False otherwise.

        :param bool i_assemble:
        :return: None
        """
        return self.com_object.SetAssemble(i_assemble)

    def set_boundary(self, i_pos: int, i_boundary: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetBoundary(long iPos,Reference iBoundary)

        :param int i_pos:
        :param Reference i_boundary:
        :return: None
        """
        return self.com_object.SetBoundary(i_pos, i_boundary.com_object)

    def set_continuity_type(self, i_pos: int, i_lim: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetContinuityType(long iPos,long iLim)

        :param int i_pos:
        :param int i_lim:
        :return: None
        """
        return self.com_object.SetContinuityType(i_pos, i_lim)

    def set_elem_until(self, i_pos: int, i_elem_until: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetElemUntil(long iPos,Reference iElemUntil)

        :param int i_pos:
        :param Reference i_elem_until:
        :return: None
        """
        return self.com_object.SetElemUntil(i_pos, i_elem_until.com_object)

    def set_length(self, i_pos: int, i_length: Length) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLength(long iPos,Length iLength)
                |     Do not use this method.

        :param int i_pos:
        :param Length i_length:
        :return: None
        """
        return self.com_object.SetLength(i_pos, i_length.com_object)

    def set_length_d(self, i_pos: int, i_length: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLengthD(long iPos,double iLength)

        :param int i_pos:
        :param float i_length:
        :return: None
        """
        return self.com_object.SetLengthD(i_pos, i_length)

    def set_limit_type(self, i_pos: int, i_lim: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLimitType(long iPos,long iLim)

        :param int i_pos:
        :param int i_lim:
        :return: None
        """
        return self.com_object.SetLimitType(i_pos, i_lim)

    def __repr__(self):
        return f'HybridShapeExtrapol(name="{ self.name }")'
