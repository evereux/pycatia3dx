"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class StrOpeningLimitDimensionsMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrOpeningLimitDimensionsMngt
                | 
                | Object to manage Structure limits of type "Dimensions" for
                | Opening.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_first_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFirstOffset() As Parameter
                |     Returns the first offset defining the length of extrusion following the
                |     direction of the support contour (or the opposite if Invert has been
                |     called)
                | 
                |     Example:
                | 
                | 
                |              This example retrieves FirstOffset of the
                |              StrOpening.
                |              
                | 
                |              Dim ObjStrOpeningLimitDimensionsMngt As
                |              StrOpeningLimitDimensionsMngt
                |              Set ObjStrOpeningLimitDimensionsMngt = oObjStrOpening.StrOpeningLimitDimensionsMngt
                |              Dim FirstOffsetParm As Parameter
                |              Set FirstOffsetParm = ObjStrOpeningLimitDimensionsMngt.GetFirstOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetFirstOffset())

    def get_second_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSecondOffset() As Parameter
                |     Returns the second offset defining the length of extrusion following the
                |     opposite direction of the support contour (or the direction itself if Invert
                |     has been called).
                | 
                |     Example:
                | 
                | 
                |              This example retrieves SecondOffset of the
                |              StrOpening.
                |              
                | 
                |              Dim SecondOffsetParm As Parameter
                |              Set SecondOffsetParm = ObjStrOpeningLimitDimensionsMngt.GetSecondOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetSecondOffset())

    def invert(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Invert()
                |     Inverts first and second offsets. 

        :return: None
        """
        return self.com_object.Invert()

    def __repr__(self):
        return f'StrOpeningLimitDimensionsMngt(name="{ self.name }")'
