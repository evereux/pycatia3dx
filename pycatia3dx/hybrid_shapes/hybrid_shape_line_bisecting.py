"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.line import Line
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapeLineBisecting(Line):

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
                |                         CATGSMIDLItf.Line
                |                             HybridShapeLineBisecting
                | 
                | Represents the hybrid shape bisecting line feature object.
                | Role: To access the data of the hybrid shape bisecting line feature object.
                | This data includes:
                | 
                |     The two lines used to create the bisecting line
                |     The reference point
                |     The support
                |     The start and end offsets
                |     The orientation
                |     The solution type
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeAffinity
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def begin_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BeginOffset() As Length (Read Only)
                |     Returns the start offset of the line.

        :return: Length
        """

        return Length(self.com_object.BeginOffset)

    @property
    def elem1(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Elem1() As Reference
                |     Returns or sets the first line used to create the bisecting
                |     line.
                | 
                |     Sub-element(s) supported (see Boundary object): see
                |     RectilinearTriDimFeatEdge or RectilinearBiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.Elem1)

    @elem1.setter
    def elem1(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Elem1 = value

    @property
    def elem2(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Elem2() As Reference
                |     Returns or sets the second line used to create the bisecting
                |     line.
                |     Sub-element(s) supported (see Boundary object): see
                |     RectilinearTriDimFeatEdge or RectilinearBiDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.Elem2)

    @elem2.setter
    def elem2(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Elem2 = value

    @property
    def end_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndOffset() As Length (Read Only)
                |     Returns the end offset of the line.

        :return: Length
        """

        return Length(self.com_object.EndOffset)

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Returns or sets the orientation used to compute the bisecting
                |     line.
                |     Role: the orientation specifies bisecting line position
                |     Legal values: The orientation can be the same(1) or the inverse(-1)

        :return: int
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation = value

    @property
    def ref_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RefPoint() As Reference
                |     Returns or sets the reference point used to create the bisecting
                |     line.
                |     Sub-element(s) supported (see Boundary object): see Vertex.

        :return: Reference
        """

        return Reference(self.com_object.RefPoint)

    @ref_point.setter
    def ref_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RefPoint = value

    @property
    def solution_type(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SolutionType() As boolean
                |     Returns or sets the solution type.
                |     Role: The solution type allows you to know where is the bisecting line.

        :return: bool
        """

        return self.com_object.SolutionType

    @solution_type.setter
    def solution_type(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SolutionType = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the support used to create the bisecting
                |     line.
                | 
                |     Parameters:
                | 
                |         oElem
                |             retrieve the support of the bisecting line.
                |             Sub-element(s) supported (see Boundary object): see Face.

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    def get_length_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetLengthType() As long
                |     Gets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         oType
                |             The length type = 0 : length - the line is limited by its extremities = 1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite on the side of the start point = 3 : infinite end point - the line is infinite on the side of the end point

        :return: int
        """
        return self.com_object.GetLengthType()

    def get_symmetrical_extension(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSymmetricalExtension() As boolean
                |     Gets whether the symmetrical extension of the line is
                |     active.
                | 
                |     Parameters:
                | 
                |         oSym
                |             Symetry flag

        :return: bool
        """
        return self.com_object.GetSymmetricalExtension()

    def set_length_type(self, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLengthType(long iType)
                |     Sets the length type Default is 0.
                | 
                |     Parameters:
                | 
                |         iType
                |             The length type = 0 : length - the line is limited by its extremities = 1 : infinite - the line is infinite = 2 : infinite start point - the line is infinite on the side of the start point = 3 : infinite end point - the line is infinite on the side of the end point

        :param int i_type:
        :return: None
        """
        return self.com_object.SetLengthType(i_type)

    def set_symmetrical_extension(self, i_sym: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSymmetricalExtension(boolean iSym)
                |     Sets the symmetrical extension of the line (start = -end).
                | 
                |     Parameters:
                | 
                |         iSym
                |             Symetry flag

        :param bool i_sym:
        :return: None
        """
        return self.com_object.SetSymmetricalExtension(i_sym)

    def __repr__(self):
        return f'HybridShapeLineBisecting(name="{ self.name }")'
