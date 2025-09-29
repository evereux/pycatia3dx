"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class DrawingTextRange(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 DrawingTextRange
                | 
                | Represents a drawing text range, or contiguous area, in a drawing
                | text.
                | 
                | A range is a contiguous area in a drawing text defined by the position of a
                | starting and ending character, or by the position of a starting character and a
                | length expressed in number of characters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def length(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Length() As long (Read Only)
                |     Returns the number of characters of the drawing text
                |     range.
                | 
                |     Example:
                |         This example retrieves in NbChar the number of characters of the
                |         MyTextRange drawing text range.
                | 
                |          NbChar = MyTextRange.Length

        :return: int
        """

        return self.com_object.Length

    @property
    def start(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Start() As long (Read Only)
                |     Returns the starting character position of the drawing text
                |     range.
                | 
                |     Example:
                |         This example retrieves in StartCharPosthe starting character position
                |         of the MyTextRange drawing text range.
                | 
                |          StartCharPos = MyTextRange.Start

        :return: int
        """

        return self.com_object.Start

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Text() As CATBSTR
                |     Returns or sets the character string making up the drawing text
                |     range.
                | 
                |     Example:
                |         This example sets in text the character string that makes up the
                |         MyTextRange drawing text range.
                | 
                |          Set textRange = MyWelding.GetTextRange (catWeldingUp)
                |          MyTextRange.Text = text
                |          Set MyTextProperties = MyWelding.TextProperties
                |          MyTextProperties.Update
                |          
                | 
                |     See also:
                |         DrawingTextProperties.Update

        :return: str
        """

        return self.com_object.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.com_object.Text = value

    def get_text_range(self, i_start: int, i_end: int) -> 'DrawingTextRange':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTextRange(long iStart,long iEnd) As DrawingTextRange
                |     Returns a drawing text range within another drawing text range. The text
                |     range is retrieved using its starting and ending character
                |     positions.
                | 
                |     Parameters:
                | 
                |         iStart
                |             The position of the drawing text range starting character
                |             
                |         iEnd
                |             The position of the drawing text range ending character
                |             
                | 
                |     Example:
                |         This example retrieves in extractedTextRange the drawing text range
                |         that begins at the eighth character and end at the fifteenth character of the
                |         MyTextRange drawing text range.
                | 
                |          Dim extractedTextRange As DrawingTextRange
                |          start = 8
                |          end = 15
                |          extractedTextRange = MyTextRange.GetTextRange(start, end)

        :param int i_start:
        :param int i_end:
        :return: DrawingTextRange
        """
        return DrawingTextRange(self.com_object.GetTextRange(i_start, i_end))

    def insert_after(self, i_string: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InsertAfter(CATBSTR iString)
                |     Inserts a character string at the end of the drawing text
                |     range.
                | 
                |     Parameters:
                | 
                |         iString
                |             The character string to be added 
                | 
                |     Example:
                |         This example inserts the String character string at the end of the
                |         MyTextRange drawing text range.
                | 
                |          String = "String to insert after"
                |          Set textRange = MyWelding.GetTextRange (catWeldingUp)
                |          MyTextRange.InsertAfter(String)
                |          Set MyTextProperties = MyWelding.TextProperties
                |          MyTextProperties.Update
                |          
                | 
                | See also:
                |     DrawingTextProperties.Update

        :param str i_string:
        :return: None
        """
        return self.com_object.InsertAfter(i_string)

    def insert_before(self, i_string: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InsertBefore(CATBSTR iString)
                |     Inserts a character string at the beginning of the drawing text
                |     range.
                | 
                |     Parameters:
                | 
                |         iString
                |             The character string to be added 
                | 
                |     Example:
                |         This example inserts the String character string at the beginning of
                |         the MyTextRange drawing text range.
                | 
                |          String = "String to insert before"
                |          Set textRange = MyWelding.GetTextRange (catWeldingUp)
                |          MyTextRange.InsertBefore(String)
                |          Set MyTextProperties = MyWelding.TextProperties
                |          MyTextProperties.Update
                |          
                | 
                | See also:
                |     DrawingTextProperties.Update

        :param str i_string:
        :return: None
        """
        return self.com_object.InsertBefore(i_string)

    def __repr__(self):
        return f'DrawingTextRange()'
