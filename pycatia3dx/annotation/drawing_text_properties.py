"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class DrawingTextProperties(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingTextProperties
                | 
                | Represents the properties of a drawing text in a drawing view.
                | 
                | This interface is obtained from CATIADrawingText or CATIADrawingWelding
                | interface. Update method must be called after text properties modification to
                | refresh the visualization.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def anchor_point(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnchorPoint() As CatTextAnchorPosition
                |     Returns or sets the anchor point of the drawing text.
                | 
                |     Example:
                |         This example sets the AnchorPoint of the MyText drawing text to the
                |         right
                | 
                |          MyText.AnchorPoint = catRight

        :return: int
        """

        return self.com_object.AnchorPoint

    @anchor_point.setter
    def anchor_point(self, value: int):
        """
        :param int value:
        """

        self.com_object.AnchorPoint = value

    @property
    def blanking(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Blanking() As CatBlankingMode
                |     Returns or sets the blanking mode of the drawing text.
                | 
                |     Example:
                |         This example sets the blanking mode type of MyText drawing text to
                |         active on geom
                | 
                |          MyText.Blanking = catBlankingOnGeom

        :return: int
        """

        return self.com_object.Blanking

    @blanking.setter
    def blanking(self, value: int):
        """
        :param int value:
        """

        self.com_object.Blanking = value

    @property
    def bold(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Bold() As long
                |     Returns or sets the drawing text font bold property.
                |     True if the drawing text is bold formatted.
                | 
                |     Example:
                |         This example get the parameter bold on MyText drawing
                |         text.
                | 
                |          oVal = MyText.Bold

        :return: int
        """

        return self.com_object.Bold

    @bold.setter
    def bold(self, value: int):
        """
        :param int value:
        """

        self.com_object.Bold = value

    @property
    def color(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Color() As long
                |     Returns or sets the color of the drawing text.
                | 
                |     Example:
                |         This example sets the Color type of the MyText drawing text to
                |         red
                | 
                |          redCol  =-16776961 'Encoded RGBA color within long integer (R=255 G=0 
                |          B=0   A=255)
                |          MyText.Color = redCol

        :return: int
        """

        return self.com_object.Color

    @color.setter
    def color(self, value: int):
        """
        :param int value:
        """

        self.com_object.Color = value

    @property
    def font_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FontName() As CATBSTR
                |     Returns or sets the font name of the drawing text.
                | 
                |     Example:
                |         This example sets the MyText drawing text font as Courrier 10
                |         BT.
                | 
                |          MyText.SetFontName("Courrier 10 BT")

        :return: str
        """

        return self.com_object.FontName

    @font_name.setter
    def font_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.FontName = value

    @property
    def font_size(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FontSize() As double
                |     Returns or sets the font size of the drawing text.
                | 
                |     Example:
                |         This example sets the MyText drawing text font size to
                |         3.5.
                | 
                |          iFontSize = 3.5
                |          MyText.SetFontSize 0, 0, iFontSize

        :return: float
        """

        return self.com_object.FontSize

    @font_size.setter
    def font_size(self, value: float):
        """
        :param float value:
        """

        self.com_object.FontSize = value

    @property
    def frame_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrameType() As CatTextFrameType
                |     Returns or sets the frame type of the drawing text.
                | 
                |     Example:
                |         This example sets the frame type of the MyText drawing text to an
                |         ellipse
                | 
                |          MyText.FrameType = catEllipse

        :return: int
        """

        return self.com_object.FrameType

    @frame_type.setter
    def frame_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.FrameType = value

    @property
    def italic(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Italic() As long
                |     Returns or sets the drawing text font italic property.
                |     True if the drawing text is formatted as italic.
                | 
                |     Example:
                |         This example set the parameter Italic on MyText drawing
                |         text.
                | 
                |          MyText.Italic = 1

        :return: int
        """

        return self.com_object.Italic

    @italic.setter
    def italic(self, value: int):
        """
        :param int value:
        """

        self.com_object.Italic = value

    @property
    def justification(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Justification() As CatJustification
                |     Returns or sets the drawing text font justification
                |     property.
                |     True if the drawing text font is justified.
                | 
                |     Example:
                |         This example sets the Justification type of the MyText drawing text to
                |         the right
                | 
                |          MyText.Justification = catRight

        :return: int
        """

        return self.com_object.Justification

    @justification.setter
    def justification(self, value: int):
        """
        :param int value:
        """

        self.com_object.Justification = value

    @property
    def kerning(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Kerning() As long
                |     Font kerning property.
                |     True if the drawing text font is formatted as kerning
                | 
                |     Example:
                |         This example set the parameter kerning on MyText drawing
                |         text.
                | 
                |          MyText.Kerning = 1

        :return: int
        """

        return self.com_object.Kerning

    @kerning.setter
    def kerning(self, value: int):
        """
        :param int value:
        """

        self.com_object.Kerning = value

    @property
    def mirror(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mirror() As CatTextFlipMode
                |     Returns or sets the mirroring of the drawing text.
                | 
                |     Example:
                |         This example sets the Mirror type of the MyText drawing text to no
                |         flip
                | 
                |          MyText.Mirror = catTextNoFlip

        :return: int
        """

        return self.com_object.Mirror

    @mirror.setter
    def mirror(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mirror = value

    @property
    def overline(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Overline() As long
                |     Returns or sets the drawing text font overline property.
                |     True if the drawing text is overlined.
                | 
                |     Example:
                |         This example get the parameter Overline on MyText drawing
                |         text.
                | 
                |          oval = MyText.Overline()

        :return: int
        """

        return self.com_object.Overline

    @overline.setter
    def overline(self, value: int):
        """
        :param int value:
        """

        self.com_object.Overline = value

    @property
    def strike_thru(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrikeThru() As long
                |     Returns or sets the drawing text font strikethrough
                |     property.
                |     True if the drawing text font is striked through.
                | 
                |     Example:
                |         This example set the parameter StrikeThru on MyText drawing
                |         text.
                | 
                |          MyText.StrikeThru = 1

        :return: int
        """

        return self.com_object.StrikeThru

    @strike_thru.setter
    def strike_thru(self, value: int):
        """
        :param int value:
        """

        self.com_object.StrikeThru = value

    @property
    def subscript(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Subscript() As long
                |     Returns or sets the drawing text font subscript property.
                |     True if the drawing text font is formatted as subscript.
                | 
                |     Example:
                |         This example set the parameter Subscript on MyText drawing
                |         text.
                | 
                |          MyText.Subscript = 1

        :return: int
        """

        return self.com_object.Subscript

    @subscript.setter
    def subscript(self, value: int):
        """
        :param int value:
        """

        self.com_object.Subscript = value

    @property
    def superscript(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Superscript() As long
                |     Returns or sets the drawing text font superscript
                |     property.
                |     True if the drawing text font is formatted as superscript.
                | 
                |     Example:
                |         This example set the parameter Superscript on MyText drawing
                |         text.
                | 
                |          MyText.Superscript = 1

        :return: int
        """

        return self.com_object.Superscript

    @superscript.setter
    def superscript(self, value: int):
        """
        :param int value:
        """

        self.com_object.Superscript = value

    @property
    def underline(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Underline() As long
                |     Returns or sets the drawing text font underline property.
                |     True if the drawing text is underlined.
                | 
                |     Example:
                |         This example get the parameter bold on MyText drawing
                |         text.
                | 
                |          oval = MyText.Underline

        :return: int
        """

        return self.com_object.Underline

    @underline.setter
    def underline(self, value: int):
        """
        :param int value:
        """

        self.com_object.Underline = value

    def activate_frame(self, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ActivateFrame(CatTextFrameType iType)
                |     Activates the text frame of the drawing text.
                | 
                |     Parameters:
                | 
                |         iType
                |             The text frame type 
                | 
                |     Example:
                |         This example add a rectangle frame to MyText drawing
                |         text.
                | 
                |          CatTextFrameType itype = catRectangle
                |          MyText.ActivateFrame itype
                |          
                | 
                | Example:
                | 
                |      This example remove the frame to MyText drawing text.
                |      
                | 
                |      CatTextFrameType itype = catNone
                |      MyText.ActivateFrame itype

        :param CatTextFrameType i_type:
        :return: None
        """
        return self.com_object.ActivateFrame(i_type)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Update the properties of the drawing text. 
                | Example:
                |     This example update the properties to MyText drawing text.
                | 
                |      MyText.Update

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'DrawingTextProperties()'
