"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_text import DrawingText
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.tps_parallel_on_screen import TPSParallelOnScreen
from pycatia3dx.types.general import CATVariant


class FlagNote(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FlagNote
                | 
                | Interface for the TPS Flag Note object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def flag_note_text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FlagNoteText() As CATBSTR
                |     Retrieves or sets Flag Text.
                | 
                |     Parameters:
                | 
                |         oText
                |             Returned Flag text.

        :return: str
        """

        return self.com_object.FlagNoteText

    @flag_note_text.setter
    def flag_note_text(self, value: str):
        """
        :param str value:
        """

        self.com_object.FlagNoteText = value

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Text() As CATBSTR
                |     Retrieves or sets Flag Text Representation.
                | 
                |     Parameters:
                | 
                |         oText
                |             Returned text for graphical representation.

        :return: str
        """

        return self.com_object.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.com_object.Text = value

    def add_url(self, i_url: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddURL(CATBSTR iUrl)
                |     Sets an URL.
                | 
                |     Parameters:
                | 
                |         iUrl
                |             URL to Set

        :param str i_url:
        :return: None
        """
        return self.com_object.AddURL(i_url)

    def get2d_annot(self) -> DrawingText:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Get2dAnnot() As DrawingText
                |     Retrieves Drafting text.

        :return: DrawingText
        """
        return DrawingText(self.com_object.Get2dAnnot())

    def get_nbr_url2(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbrURL2() As long
                |     Gets the number of URL.
                | 
                |     Parameters:
                | 
                |         oNumberOfURL
                |             returns param oNumberOfURL.

        :return: int
        """
        return self.com_object.GetNbrURL2()

    def modify_url(self, i_url: str, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ModifyURL(CATBSTR iUrl,CATVariant iIndex)
                |     Modifies a URL.
                | 
                |     Parameters:
                | 
                |         iUrl
                |             URL to Set. 
                |         iIndex
                |             index of the URL to modify.

        :param str i_url:
        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.ModifyURL(i_url, i_index)

    def remove_url(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveURL(CATVariant iIndex)
                |     Remove a URL.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             position of the URL to remove.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.RemoveURL(i_index)

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TPSParallelOnScreen() As TPSParallelOnScreen
                |     Gets the annotation on TPSParallelOnScreen interface.

        :return: TPSParallelOnScreen
        """
        return TPSParallelOnScreen(self.com_object.TPSParallelOnScreen())

    def url(self, i_index: CATVariant) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func URL(CATVariant iIndex) As CATBSTR
                |     Retrieves url.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of url. 
                |         oUrl
                |             url 

        :param CATVariant i_index:
        :return: str
        """
        return self.com_object.URL(i_index)

    def __repr__(self):
        return f'FlagNote(name="{ self.name }")'
