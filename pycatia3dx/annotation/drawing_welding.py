"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.annotation.drawing_leaders import DrawingLeaders
from pycatia3dx.annotation.drawing_text_properties import DrawingTextProperties
from pycatia3dx.annotation.drawing_text_range import DrawingTextRange
from pycatia3dx.system.any_object import AnyObject


class DrawingWelding(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingWelding
                | 
                | Represents a drawing welding in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Angle() As double
                |     Returns or sets the angle of the drawing text. The angle is measured
                |     between the axis system of the drawing view and the local axis system of the
                |     drawing text. The angle is measured in radians and is counted
                |     counterclockwise.
                | 
                |     Example:
                |         This example sets the angle of the MyText drawing Text to 90 degrees
                |         clockwise. You first need to compute the angle in degrees and set the minus
                |         sign to indicate the rotation is clockwise.
                | 
                |          Angle90Clockwise = -90
                |          MyText.Angle = Angle90Clockwise

        :return: float
        """

        return self.com_object.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.Angle = value

    @property
    def identification_line_side(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IdentificationLineSide() As CatWeldingSide
                |     Returns or sets the welding identification line Side of the drawing welding
                |     symbol.
                |     Precondition: This property is only available for ISO
                |     standard.
                | 
                |     Example:
                |         This example sets welding identification line Side to Up
                |         .
                | 
                |          MyWeld.IdentificationLineSide = catWeldingUp

        :return: int
        """

        return self.com_object.IdentificationLineSide

    @identification_line_side.setter
    def identification_line_side(self, value: int):
        """
        :param int value:
        """

        self.com_object.IdentificationLineSide = value

    @property
    def leaders(self) -> DrawingLeaders:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Leaders() As DrawingLeaders (Read Only)
                |     Returns the drawing leader collection of the drawing
                |     welding.
                | 
                |     Example:
                |         This example retrieves in LeaderCollection the collection of leaders of
                |         the MyWelding drawing welding.
                | 
                |          Dim LeaderCollection As DrawingLeaders
                |          Set LeaderCollection = MyWelding.Leaders

        :return: DrawingLeaders
        """

        return DrawingLeaders(self.com_object.Leaders)

    @property
    def text_properties(self) -> DrawingTextProperties:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TextProperties() As DrawingTextProperties (Read Only)
                |     Returns the text properties of the drawing welding.
                | 
                |     Example:
                |         This example retrieves in TextProperties the text properties of the
                |         MyWelding drawing welding..
                | 
                |          Dim TextProperties As DrawingTextProperties
                |          Set TextProperties = MyWelding.TextProperties

        :return: DrawingTextProperties
        """

        return DrawingTextProperties(self.com_object.TextProperties)

    @property
    def welding_side(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WeldingSide() As CatWeldingSide
                |     Returns or sets the welding side of the drawing welding
                |     symbol.
                | 
                |     Example:
                |         This example sets welding side to Up .
                | 
                |          MyWeld.WeldingSide = catWeldingUp

        :return: int
        """

        return self.com_object.WeldingSide

    @welding_side.setter
    def welding_side(self, value: int):
        """
        :param int value:
        """

        self.com_object.WeldingSide = value

    @property
    def welding_tail(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WeldingTail() As CatDftWeldingTail
                |     Returns or sets the welding tail of the drawing welding
                |     symbol.
                | 
                |     Example:
                |         This example displays the welding symbol tail.
                | 
                |          MyWeld.WeldingTail = catDftWeldingTailYES

        :return: int
        """

        return self.com_object.WeldingTail

    @welding_tail.setter
    def welding_tail(self, value: int):
        """
        :param value:
        """

        self.com_object.WeldingTail = value

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property x() As double
                |     Returns or sets the x coordinate of the drawing welding. It is expressed
                |     with respect to the current view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example retrieves in X the x coordinate of the MyWelding drawing
                |         welding.
                | 
                |          X = MyWelding.x

        :return: float
        """

        return self.com_object.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.com_object.x = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property y() As double
                |     Returns or sets the y coordinate of the drawing welding. It is expressed
                |     with respect to the current view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the y coordinate of the MyWelding drawing welding to
                |         5 inches. You need first to convert the 5 inches into
                |         millmeters.
                | 
                |          NewYCoordinate = 5*25.4/1000
                |          MyWelding.y = NewYCoordinate

        :return: float
        """

        return self.com_object.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.com_object.y = value

    def get_additional_symbol(self, i_weld: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetAdditionalSymbol(CatWelding iWeld) As
                | CatWeldAdditionalSymbol
                |     Returns the additional symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iWeld
                |             The xxx
                | 
                |             Example:
                |                 This example sets an concave additinal symbol on the MyWelding
                |                 drawing welding
                | 
                |                  MyWelding.Symbol = DftConcaveSymbol

        :param int i_weld:
        :return: int
        """
        return self.com_object.GetAdditionalSymbol(i_weld)

    def get_finish_symbol(self, i_weld: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetFinishSymbol(CatWelding iWeld) As
                | CatDftWeldFinishSymbol
                |     Returns the finish symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iWeld
                |             The field on which finish symbol is applied.
                | 
                |             Example:
                |                 This example returns the finish symbol on the first symbol of
                |                 the MyWelding drawing welding
                | 
                |                  MyWelding.GetFinishSymbol(catWeldingFieldOne,oFinishSymbol)

        :param int i_weld:
        :return: int
        """
        return self.com_object.GetFinishSymbol(i_weld)

    def get_symbol(self, i_weld: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetSymbol(CatWelding iWeld) As CatWeldingSymbol
                |     Returns the symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iWeld
                |             The field on which the symbol is applied 
                |         oSymbol
                |             The welding symbol
                | 
                |             Example:
                |                 This example gets the symbol on the first field of the
                |                 MyWelding drawing welding
                | 
                |                  MyWelding.GetSymbol(catWeldingFieldOne,oSymbol)

        :param int i_weld:
        :return: int
        """
        return self.com_object.GetSymbol(i_weld)

    def get_text_range(self, i_field: int) -> DrawingTextRange:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetTextRange(CatWeldingField iField) As DrawingTextRange
                |     Returns the field of the drawing welding in a drawing text
                |     range.
                | 
                |     Parameters:
                | 
                |         iField
                |             The drawing welding field 
                | 
                |     Returns:
                |         The drawing text range that corresponds to the drawing welding field
                |         
                | 
                | Example:
                |     This example retrieves the xxx.
                | 
                |      Dim textRange As DrawingTextRange
                |      Set textRange = MyWelding.GetTextRange (catWeldingUp)

        :param int i_field:
        :return: DrawingTextRange
        """
        return DrawingTextRange(self.com_object.GetTextRange(i_field))

    def set_additional_symbol(self, i_symbol: int, iweld: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetAdditionalSymbol(CatWeldAdditionalSymbol iSymbol,CatWelding
                | iweld)
                |     Sets the additional symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iSymbol
                |             The welding additional symbol 
                |         iWeld
                |             The xxx
                | 
                |             Example:
                |                 This example sets an concave additinal symbol on the MyWelding
                |                 drawing welding
                | 
                |                  MyWelding.Symbol = DftConcaveSymbol

        :param int i_symbol:
        :param int iweld:
        :return: None
        """
        return self.com_object.SetAdditionalSymbol(i_symbol, iweld)

    def set_finish_symbol(self, i_finish_symbol: int, i_weld: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetFinishSymbol(CatDftWeldFinishSymbol iFinishSymbol,CatWelding
                | iWeld)
                |     Sets the finish symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iFinishSymbol
                |             The finish welding symbol 
                |         iWeld
                |             The field on which finish symbol will be applied.
                | 
                |             Example:
                |                 This example sets the finish symbol on the first symbol of the
                |                 MyWelding drawing welding
                | 
                |                 
                |                 MyWelding.GetFinishSymbol(catWeldingFieldOne,catDftLetterCWelding)

        :param int i_finish_symbol:
        :param int i_weld:
        :return: None
        """
        return self.com_object.SetFinishSymbol(i_finish_symbol, i_weld)

    def set_symbol(self, i_symbol: int, iweld: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetSymbol(CatWeldingSymbol iSymbol,CatWelding iweld)
                |     Sets the symbol of the drawing welding.
                | 
                |     Parameters:
                | 
                |         iSymbol
                |             The welding symbol 
                |         iWeld
                |             The field on which the symbol is applied
                | 
                |             Example:
                |                 This example sets a symbol on the first field of the MyWelding
                |                 drawing welding
                | 
                |                  MyWelding.SetSymbol(catSquareWelding,catWeldingFieldOne)

        :param CatWeldingSymbol i_symbol:
        :param CatWelding iweld:
        :return: None
        """
        return self.com_object.SetSymbol(i_symbol, iweld)

    def __repr__(self):
        return f'DrawingWelding(name="{ self.name }")'
