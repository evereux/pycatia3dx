"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.part.surface_based_shape import SurfaceBasedShape


class ThickSurface(SurfaceBasedShape):

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
                |                         CATPartIDLItf.SurfaceBasedShape
                |                             ThickSurface
                | 
                | Represents the ThickSurface feature.
                | It thicks surface using an offset element (such as a surface or a skin) and two
                | offset values TopOffset and Botoffset. TopOffset is the offset between the
                | offset element and the top skin of the feature. BotOffset is the offset between
                | the offset element and the bottom skin of the feature.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def bot_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BotOffset() As Length (Read Only)
                |     Returns the value of the bottom offset.
                | 
                |     Example:
                |         The following example returns in botoffset the bottom offset of the
                |         thicksurface firstThickSurface:
                | 
                |          Set botoffset = firstThickSurface.BotOffset

        :return: Length
        """

        return Length(self.com_object.BotOffset)

    @property
    def offset_side(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OffsetSide() As long (Read Only)
                |     Returns the offset direction (defines in regards of the normal direction)
                |     .
                | 
                |     Example:
                |         The following example returns in offsetside the side of the
                |         ThickSurface firstThickSurface:
                | 
                |          Set offsetside = firstThickSurface.OffsetSide

        :return: int
        """

        return self.com_object.OffsetSide

    @property
    def top_offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TopOffset() As Length (Read Only)
                |     Returns the value of the top offset.
                | 
                |     Example:
                |         The following example returns in topoffset the top offset of the
                |         ThickSurface firstThickSurface:
                | 
                |          Set topoffset = firstThickSurface.TopOffset

        :return: Length
        """

        return Length(self.com_object.TopOffset)

    def swap_offset_side(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub swap_OffsetSide()
                |     Swap the side of the offset. 
                | 
                | Example:
                |     The following example changes the side of the ThickSurface
                |     firstThickSurface:
                | 
                |      call firstThickSurface.swap_OffsetSide()

        :return: None
        """
        return self.com_object.swap_OffsetSide()

    def __repr__(self):
        return f'ThickSurface(name="{ self.name }")'
