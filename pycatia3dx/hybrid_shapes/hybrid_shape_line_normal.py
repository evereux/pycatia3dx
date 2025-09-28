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


class HybridShapeLineNormal(Line):

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
                |                             HybridShapeLineNormal
                | 
                | Line defined by a point and a direction normal to a surface.
                | Role: To access data of the line feature created by using the normal direction
                | of a surface
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLineNormal
                | object.
                | 
                | See also:
                |     Reference
                | See also:
                |     Length
                | See also:
                |     HybridShapeDirection
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
                |     Returns the start length of the line.
                |     Start length : extension of the line, beginning at the starting point
                | 
                |     Example:
                |         This example retrieves in oStart the beginning offset length for the
                |         LineNormal hybrid shape feature.
                | 
                |          Dim oStart As  CATIALength 
                |          Set oStart = LineNormal.BeginOffset

        :return: Length
        """

        return Length(self.com_object.BeginOffset)

    @property
    def end_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndOffset() As Length (Read Only)
                |     Returns the end length of the line.
                |     End length : extension of the line, beginning at the ending point
                | 
                |     Example:
                |         This example retrieves in oEnd the starting length for the LineNormal
                |         hybrid shape feature.
                | 
                |          Dim oEnd As  CATIALength 
                |          Set oEnd = LineNormal.EndOffset

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
                |     Returns or Sets the line orientation.
                |     Orientation allows to reverse the line direction from the reference
                |     point.
                |     For a line of L length, it is the same as creating this line with -L length : Orientation : can be 1 or -1
                | 
                |     Example:
                |         This example retrieves in oOrientation the starting length for the
                |         LineNormal hybrid shape feature.
                | 
                |          Dim oOrientation As long
                |          Set oOrientation = LineNormal.Orientation

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
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Point() As Reference
                |     Returns or Sets the starting point of the line.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in oPoint the starting point for the LineNormal
                |         hybrid shape feature.
                | 
                |          Dim oPoint As Reference
                |          Set oPoint = LineNormal.Point

        :return: Reference
        """

        return Reference(self.com_object.Point)

    @point.setter
    def point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Point = value

    @property
    def surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Surface() As Reference
                |     Returns or Sets the surface to which the line will be
                |     normal.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in oSurface the surface for the LineNormal
                |         hybrid shape feature.
                | 
                |          Dim oSurface As Reference 
                |          Set oSurface = LineNormal.Surface

        :return: Reference
        """

        return Reference(self.com_object.Surface)

    @surface.setter
    def surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Surface = value

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
        return f'HybridShapeLineNormal(name="{ self.name }")'
