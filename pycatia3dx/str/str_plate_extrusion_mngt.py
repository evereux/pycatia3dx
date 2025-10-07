"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class StrPlateExtrusionMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrPlateExtrusionMngt
                | 
                | Object to manage Structure Functional Modeler Plate/Panel
                | Geometry.
                | Role: To access geometrical parameters of plate.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def offset_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OffsetMode() As long
                |     Returns or Sets the OffsetMode used to create this
                |     Plate/Panel.
                |     Legal values:
                |     -1 : undefined mode
                |     0 : Offset
                |     1 : Center
                |     2 : Flush
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in OffsetMode of the
                |              plate.
                |              
                | 
                |              lOffsetMode = ObjStrPlateExtrusionMngt.OffsetMode

        :return: int
        """

        return self.com_object.OffsetMode

    @offset_mode.setter
    def offset_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.OffsetMode = value

    @property
    def throw_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThrowOrientation() As long
                |     Returns or Sets the ThrowOrientation of this object. Legal values for
                |     ThrowOrientation:
                |     -1 = InvertOrientation
                |     0 = UnknownOrientation
                |     1 = SameOrientation
                |     2 = X+ ( X+ vector = ( 1, 0, 0) )
                |     3 = X- ( X- vector = (-1, 0, 0) )
                |     4 = Y+ ( Y+ vector = ( 0, 1, 0) )
                |     5 = Y- ( Y- vector = ( 0,-1, 0) )
                |     6 = Z+ ( Z+ vector = ( 0, 0, 1) )
                |     7 = Z- ( Z- vector = ( 0, 0,-1) )
                |     8 = Inside
                |     9 = Outside
                |     10 = Inboard ( Toward center line )
                |     11 = Outboard ( Opposite of previous one )
                |     12 = Inboard ( Toward midship )
                |     13 = Outboard ( Opposite of previous one )
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ThrowOrientation of the
                |              plate.
                |              
                | 
                |              Dim ObjStrPlateExtrusionMngt As
                |              StrPlateExtrusionMngt
                |              Set ObjStrPlateExtrusionMngt = ObjSfdPanel.StrPlateExtrusionMngt
                |              lThrowOrientation = ObjStrPlateExtrusionMngt.ThrowOrientation

        :return: int
        """

        return self.com_object.ThrowOrientation

    @throw_orientation.setter
    def throw_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.ThrowOrientation = value

    def get_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOffset() As Parameter
                |     Returns Offset of this Plate / Panel. The offset cannot be greater than
                |     Thickness / 2. 
                | Example
                | :
                |     This example retrieves in offset of the plate.
                | 
                |       Dim ParmOffset As Parameter
                |       Set ParmOffset = ObjStrPlateExtrusionMngt.GetOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetOffset())

    def get_thickness(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetThickness() As Parameter
                |     Returns Thickness parameter of this Plate / Panel.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in thickness of the plate.
                |              
                | 
                |               Dim ParmThickness As Parameter
                |               Set ParmThickness = ObjStrPlateExtrusionMngt.GetThickness

        :return: Parameter
        """
        return Parameter(self.com_object.GetThickness())

    def reverse_throw_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ReverseThrowOrientation()
                |     Reverses Throw Orientation of this Plate / Panel. 

        :return: None
        """
        return self.com_object.ReverseThrowOrientation()

    def __repr__(self):
        return f'StrPlateExtrusionMngt(name="{ self.name }")'
