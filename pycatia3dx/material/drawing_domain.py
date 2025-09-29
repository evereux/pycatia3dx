"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.material.material_domain_content import MaterialDomainContent


class DrawingDomain(MaterialDomainContent):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMaterialIDLItf.MaterialDomainContent
                |                         DrawingDomain
                | 
                | Manages Drafting Material Domain.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_coloring_pattern(self, i_name: str, i_color: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub CreateColoringPattern(CATBSTR iName,long iColor)
                |     Creates a coloring Pattern.
                | 
                |     Parameters:
                | 
                |         iName
                |             Pattern name 
                |         iColor
                |             Color number of the lines of the hatching element.

        :param str i_name:
        :param int i_color:
        :return: None
        """
        return self.com_object.CreateColoringPattern(i_name, i_color)

    def create_dotting_pattern(self, i_name: str, i_pitch: float, i_bright: int, i_color: int, i_zig_zag: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub CreateDottingPattern(CATBSTR iName,double iPitch,long iBright,long
                | iColor,long iZigZag)
                |     Creates a dotting Pattern.
                | 
                |     Parameters:
                | 
                |         iName
                |             Pattern name 
                |         iPitch
                |             Distance between 2 consecutive lines of the Dotting element.
                |             
                |         iBright
                |             Brightness of the dots of the Dotting element 
                |         iColor
                |             Color number of the lines of the hatching element.
                |             
                |         iZigZag
                |             Zigzag of the dots of the Dotting element.

        :param str i_name:
        :param float i_pitch:
        :param int i_bright:
        :param int i_color:
        :param int i_zig_zag:
        :return: None
        """
        return self.com_object.CreateDottingPattern(i_name, i_pitch, i_bright, i_color, i_zig_zag)

    def create_hatching_pattern(self, i_name: str, i_hatching_nb: int, i_offset: float, i_angle: float, i_pitch: tuple,
                                i_texture: tuple, i_thikness: tuple, i_color: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub CreateHatchingPattern(CATBSTR iName,long iHatchingNb,double iOffset,double
                | iAngle,CATSafeArrayVariant iPitch,CATSafeArrayVariant
                | iTexture,CATSafeArrayVariant iThikness,CATSafeArrayVariant
                | iColor)
                |     Creates a hatching Pattern.
                | 
                |     Parameters:
                | 
                |         iName
                |             Pattern name 
                |         iHatchingNb
                |             Number of hatching elements. 
                |         iOffset
                |             Offset between the sheet origin and the first hatching line.
                |             
                |         iAngle
                |             Angle of hatching lines based on axis x (degre). 
                |         iPitch
                |             Distance between 2 consecutive lines of the hatching element.
                |             
                |         iTexture
                |             Texture number of the lines of the hatching element.
                |             
                |         iThikness
                |             Thickness of the lines of the hatching element. 
                |         iColor
                |             Color number of the lines of the hatching element.

        :param str i_name:
        :param int i_hatching_nb:
        :param float i_offset:
        :param float i_angle:
        :param tuple i_pitch:
        :param tuple i_texture:
        :param tuple i_thikness:
        :param tuple i_color:
        :return: None
        """
        return self.com_object.CreateHatchingPattern(i_name, i_hatching_nb, i_offset, i_angle, i_pitch, i_texture,
                                                     i_thikness, i_color)

    def create_none_pattern(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub CreateNonePattern(CATBSTR iName)
                |     Creates an empty Pattern.
                | 
                |     Parameters:
                | 
                |         iName
                |             Pattern name

        :param str i_name:
        :return: None
        """
        return self.com_object.CreateNonePattern(i_name)

    def __repr__(self):
        return f'DrawingDomain(name="{self.name}")'
