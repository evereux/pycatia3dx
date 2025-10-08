"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.structure.str_reference import StrReference


class StrRefOffset(StrReference):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATStrIDLItf.StrReference
                |                         StrRefOffset
                | 
                | Object to access a volatile parameter group for the positioning
                | strategy
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_offset_parm(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOffsetParm() As Parameter
                |     Returns the Offset parameter.
                |     Role:The Offset parameter defines the offset distance, in the direction of
                |     the Relevant Side orientation, for the reference surface (from the surface
                |     selected from the specification object - see SetRelevantSide ). Use this
                |     function to get the parameter so you can get or set the
                |     value.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the offset parameter.
                |              
                | 
                |               Dim OffsetParm As Parameter
                |               Set OffsetParm = ObjStrRefOffset.GetOffsetParm

        :return: Parameter
        """
        return Parameter(self.com_object.GetOffsetParm())

    def get_relevant_side(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRelevantSide() As long
                |     Returns the Relevant Side Orientation.
                |     Role:The Relevant Side Orientation is the nominal orientation (outward)
                |     used to define the positive direction for offsetting the reference surface by
                |     the distance specified in the Offset parameter. If the reference element is a
                |     solid (e.g. plate or thick surface), the Relevant Side Orientation is also used
                |     to select which face of the solid is used as the reference
                |     surface.
                |     Legal values :
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
                |              This example retrieves  the relevant side
                |              orientation.
                |              
                | 
                |               StrOrientation = ObjStrRefOffset.GetRelevantSide

        :return: int
        """
        return self.com_object.GetRelevantSide()

    def set_relevant_side(self, i_str_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRelevantSide(long iStrOrientation)
                |     Sets the Relevant Side Orientation.
                |     Role:The Relevant Side Orientation is the nominal orientation (outward)
                |     used to define the positive direction for offsetting the reference surface by
                |     the distance specified in the Offset parameter. If the reference element is a
                |     solid (e.g. plate or thick surface), the Relevant Side Orientation is also used
                |     to select which face of the solid is used as the reference
                |     surface.
                | 
                |     Parameters:
                | 
                |         iStrOrientation
                |             The nominal Relevant Side Orientation.
                |             Legal values :
                |             -1 = InvertOrientation
                |             0 = UnknownOrientation
                |             1 = SameOrientation
                |             2 = X+ ( X+ vector = ( 1, 0, 0) )
                |             3 = X- ( X- vector = (-1, 0, 0) )
                |             4 = Y+ ( Y+ vector = ( 0, 1, 0) )
                |             5 = Y- ( Y- vector = ( 0,-1, 0) )
                |             6 = Z+ ( Z+ vector = ( 0, 0, 1) )
                |             7 = Z- ( Z- vector = ( 0, 0,-1) )
                |             8 = Inside
                |             9 = Outside
                |             10 = Inboard ( Toward center line )
                |             11 = Outboard ( Opposite of previous one )
                |             12 = Inboard ( Toward midship )
                |             13 = Outboard ( Opposite of previous one ) 
                | 
                |     Example:
                | 
                | 
                |              This example sets the relevant side orientation.
                |              
                | 
                |               ObjStrRefOffset.SetRelevantSide 4

        :param int i_str_orientation:
        :return: None
        """
        return self.com_object.SetRelevantSide(i_str_orientation)

    def __repr__(self):
        return f'StrRefOffset(name="{self.name}")'
