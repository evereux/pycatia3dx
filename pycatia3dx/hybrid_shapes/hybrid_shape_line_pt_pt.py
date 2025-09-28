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


class HybridShapeLinePtPt(Line):

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
                |                             HybridShapeLinePtPt
                | 
                | Represents the hybrid shape line between two points feature
                | object.
                | Role: To access the data of the line feature created between two
                | points.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLinePtPt
                | object.
                | 
                | See also:
                |     Reference
                | See also:
                |     Length
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
                |         LinePtPt hybrid shape feature.
                | 
                |          Dim oStart As  CATIALength 
                |          Set oStart = LinePtPt.BeginOffset

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
                |         This example retrieves in oEnd the starting length for the LinePtPt
                |         hybrid shape feature.
                | 
                |          Dim oEnd As  CATIALength 
                |          Set oEnd = LinePtPt.EndOffset

        :return: Length
        """

        return Length(self.com_object.EndOffset)

    @property
    def pt_extremity(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PtExtremity() As Reference
                |     Returns or Sets the extremity point of the LinePtPt(Second
                |     Point).
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in oPtExtremity the ending point for the
                |         LinePtPt hybrid shape feature.
                | 
                |          Dim oPtExtremity As Reference 
                |          Set oPtExtremity = LinePtPt.PtExtremity

        :return: Reference
        """

        return Reference(self.com_object.PtExtremity)

    @pt_extremity.setter
    def pt_extremity(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PtExtremity = value

    @property
    def pt_origine(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PtOrigine() As Reference
                |     Returns or Sets the origin point of the LinePtPt(First
                |     point).
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in oPtOrigine the initial point for the LinePtPt
                |         hybrid shape feature.
                | 
                |          Dim oPtOrigine As Reference 
                |          Set oPtOrigine = LinePtPt.PtOrigine

        :return: Reference
        """

        return Reference(self.com_object.PtOrigine)

    @pt_origine.setter
    def pt_origine(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PtOrigine = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or Sets the supporting surface.
                |     Note: the support surface is not mandatory for LinePtPt
                | 
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in oSurface the supporting surface (if it exist)
                |         for the LinePtPt hybrid shape feature.
                | 
                |          Dim oSurface As Reference 
                |          Set oSurface = LinePtPt.Surface

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

    def remove_support(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveSupport()
                |     Removes the support surface.

        :return: None
        """
        return self.com_object.RemoveSupport()

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
        return f'HybridShapeLinePtPt(name="{ self.name }")'
